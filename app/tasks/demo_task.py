# -*- encoding: utf-8 -*-
from app.__init__ import create_app
from app.queue import task_app
from .base import BaseTask


@task_app.task(
    base=BaseTask, default_retry_delay=15 * 60,
    max_retries=2
)
def demo_task():
    app = create_app()
    with app.app_context():
        pass
