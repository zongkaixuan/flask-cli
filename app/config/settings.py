# -*- encoding: utf-8 -*-
import os
import time

basedir = os.path.abspath(os.path.dirname(__file__))


class AppConf:
    APP_NAME = 'demo'


class DBConf:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("APP_SQLALCHEMY_DATABASE_URI", )
    # E.g
    # postgresql://<db-user>:<db-pwd>@<db-host>:<db-port>/<db-name>?client_encoding=utf8


class LogConf:
    LOGPATH = os.environ.get("APP_LOG_PATH", "logs")
    LOGNAME = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    LOGFORMAT = "%(app_name)s - %(asctime)s - %(levelname)s - %(filename)s - %(lineno)s - %(message)s"
    LOGLEVEL = os.environ.get("APP_LOG_LEVEL", "INFO")


class CeleryConf:
    CELERY_TASK_ALWAYS_EAGER = bool(os.environ.get(
        "APP_CELERY_TASK_ALWAYS_EAGER",
        False
    ))
    CELERY_BROKER_URL = os.environ.get(
        "APP_CELERY_BROKER_URL",
        'redis://127.0.0.1:6379/1'
    )
    result_backend = os.environ.get(
        "APP_RESULT_BACKEND",
        'redis://127.0.0.1:6379/2'
    )
    CELERY_TIME_ZONE = os.environ.get(
        "APP_CELERY_TIME_ZONE",
        'Asia/shanghai'
    )

    CELERY_SCHEDULE = {}
    # E.g
    # CELERY_SCHEDULE = {
    #     '<task name>': {
    #         'task': 'app.tasks.<task name>',
    #         'schedule': crontab(hour=10, minute=15)
    #     },
    # }


class Settings(AppConf, DBConf, LogConf, CeleryConf):
    pass
