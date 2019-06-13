from logging import getLogger
from typing import Dict, Optional

from celery import Celery
from celery import signals
from injector import Binder, singleton, Injector, inject

from marketing_api.app import createApp
from marketing_api.db.model import Database
from marketing_api.db.stores import MailingStore, ContactDTO
from marketing_api.template_renderer import TemplateRenderer

_logger = getLogger(__name__)

queue = Celery('marketing_app.jobs', backend='redis://192.168.99.100/1', broker='redis://192.168.99.100')


class WorkerContext(object):
    injector: Optional[Injector]

    def __init__(self):
        self.db = None
        self.injector = None

    def onInit(self, *a, **kw):
        app, api, db = createApp('192.168.99.100', 32000)

        def databaseProvider(binder: Binder):
            binder.bind(Database, to=db, scope=singleton)

        injector = Injector([databaseProvider])

        self.db = db
        self.injector = injector

    def onTaskPrerun(self, kwargs: Dict, *a, **kw):
        kwargs['ctx'] = self


workerCtx = WorkerContext()

signals.task_prerun.connect(workerCtx.onTaskPrerun)
signals.worker_init.connect(workerCtx.onInit)


@queue.task(typing=False)
def sendMail(*a, ctx: WorkerContext, **kw) -> None:

    try:
        ctx.injector.get(MailSenderTask).execute(*a, **kw)
        ctx.db.session.commit()
    except:
        ctx.db.session.rollback()
        raise


class MailSenderTask(object):
    @inject
    def __init__(self, mailingStore: MailingStore, renderer: TemplateRenderer):
        self.store = mailingStore
        self.renderer = renderer

    def execute(self, jobId: int, contactData: tuple, template: str):

        contact = ContactDTO(*contactData)
        rendered = self.renderer.render(template, contact=contact)

        _logger.info('Sending mail to %s :: %s', contact, rendered)

        self.store.markPartDone(jobId)
