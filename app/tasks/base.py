# -*- encoding: utf-8 -*-
from app.queue import task_app
from app.log import log


class BaseTask(task_app.Task):
    def __init__(self):
        self.logger = log.get_logger('BaseTask')

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        self.logger.error("Retry")

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        self.logger.error(einfo)
