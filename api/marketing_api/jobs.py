from logging import getLogger
from typing import Dict

from celery import Celery
from celery.signals import task_prerun

_logger = getLogger(__name__)

queue = Celery('marketing_app.jobs', backend='redis://192.168.99.100/1', broker='redis://192.168.99.100')


class WorkerContext(object):
    def __init__(self):
        self.db = 'XXX'

    def onTaskPrerun(self, kwargs: Dict, *a, **kw):
        kwargs['ctx'] = self


workerCtx = WorkerContext()

task_prerun.connect(workerCtx.onTaskPrerun)


@queue.task(typing=False)
def add(x, y, ctx: WorkerContext):
    _logger.warning('WILL ADD %s + %s :: %s', x, y, ctx)
    return 42


@queue.task(typing=False)
def sendMail(jobId, contactId, template, ctx: WorkerContext) -> None:
    print('SENDING MAIL !!! %s, %s, %s, %s', jobId, contactId, template, ctx)
