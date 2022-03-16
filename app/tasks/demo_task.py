# -*- encoding: utf-8 -*-
from app.queue import task_app
from .base import BaseTask


@task_app.task(
    base=BaseTask, default_retry_delay=15 * 60,
    max_retries=2
)
def demo_task():
    with demo_task.flask_app.app_context():
        pass
