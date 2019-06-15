import os
from logging import getLogger
from typing import Dict, Optional

from celery import Celery, Task
from celery import signals
from injector import Binder, singleton, Injector, inject

from marketing_api.app import createApp
from marketing_api.db.model import Database
from marketing_api.db.stores import MailingStore, ContactDTO, ServerDTO, TemplateDTO
from marketing_api.sender import MailSender
from marketing_api.template_renderer import TemplateRenderer

_logger = getLogger(__name__)

queue = Celery('marketing_app.jobs', backend='redis://redis/1', broker='redis://redis')


class WorkerContext(object):
    injector: Optional[Injector]

    def __init__(self):
        self.db = None
        self.injector = None

    def onInit(self, *a, **kw):
        """
        Called when task worker is initalizing.

        Connect to database, create DI Container.
        """
        dbHost = os.environ.get('MARKETING_WORKER_DB_HOST', 'db')
        dbPort = int(os.environ.get('MARKETING_WORKER_DB_PORT', 32000))

        app, api, db = createApp(dbHost, dbPort)

        def databaseProvider(binder: Binder):
            binder.bind(Database, to=db, scope=singleton)

        injector = Injector([databaseProvider])

        self.db = db
        self.injector = injector

    def onTaskPrerun(self, kwargs: Dict, *a, **kw):
        """
        Inject this instance into executing' task keyword param
        """

        kwargs['ctx'] = self


workerCtx = WorkerContext()

signals.task_prerun.connect(workerCtx.onTaskPrerun)
signals.worker_init.connect(workerCtx.onInit)


@queue.task(bind=True, typing=False, default_retry_delay=10)
def sendMail(self: Task, jobId: int, serverData: tuple, contactData: tuple, templateData: tuple, ctx: WorkerContext) -> None:
    """
    Thin wrapper for executing task implementation with proper dependency injection.

    If there would be more tasks, then this could be turned in kind of factory wrapping every task the same way.
    """
    try:
        ctx.injector.get(MailSenderTask).execute(jobId, serverData, contactData, templateData)
        ctx.db.session.commit()
    except Exception as exc:
        ctx.db.session.rollback()

        # because we inject custom keyword args, we must reset them while retrying
        raise self.retry(
            args=(jobId, serverData, contactData, templateData),
            kwargs={},
            exc=exc
        )


class MailSenderTask(object):
    @inject
    def __init__(self, mailingStore: MailingStore, renderer: TemplateRenderer, sender: MailSender):
        self.store = mailingStore
        self.renderer = renderer
        self.sender = sender

    def execute(self, jobId: int, serverData: tuple, contactData: tuple, templateData: tuple):

        contact = ContactDTO(*contactData)
        server = ServerDTO(*serverData)
        template = TemplateDTO(*templateData)

        rendered = self.renderer.render(template.content, contact=contact)

        self.sender.send(server, contact, template.subject, rendered)

        self.store.markPartDone(jobId)
