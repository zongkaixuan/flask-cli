# -*- encoding: utf-8 -*-
from app.queue import task_app
from flask import Flask
from app.api import api
from app.log import log
from flask_cors import CORS
from app.models import db
from app.marshalling import ma
from werkzeug.middleware.proxy_fix import ProxyFix
from app.config.settings import CeleryConf


cors = CORS()


def init_celery(app=None):
    app = app or create_app()
    task_app.conf.broker_url = app.config["CELERY_BROKER_URL"]
    # Flask only support load config variable with uppercase, but celery suggest that use lowercase instead
    task_app.conf.result_backend = CeleryConf.result_backend
    task_app.conf.beat_schedule = app.config["CELERY_SCHEDULE"]
    task_app.conf.update(app.config)

    class ContextTask(task_app.Task):
        abstract = True
        """Make celery tasks work with Flask app context"""

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    task_app.Task = ContextTask
    return task_app


def register_plugin(app):
    cors.init_app(app)
    api.init_app(app)
    log.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    init_celery(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    # Try to fix the issue while access the swagger ui through https
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)
    app.config.from_object('app.config.Settings')
    register_plugin(app)
    return app
