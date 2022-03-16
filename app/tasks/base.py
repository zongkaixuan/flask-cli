# -*- encoding: utf-8 -*-
from app.queue import task_app
from app.log import log
from app.__init__ import create_app


class BaseTask(task_app.Task):
    _flask_app = None

    def __init__(self):
        self.logger = log.get_logger('BaseTask')

    @property
    def flask_app(self):  # Reuse existing db session in process
        if self._flask_app is None:
            self._flask_app = create_app()
        return self._flask_app

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        self.logger.error("Retry")

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        self.logger.error(einfo)
