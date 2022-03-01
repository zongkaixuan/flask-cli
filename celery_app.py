# -*- coding:utf-8 -*-
from app import init_celery
from app.config import Settings


app = init_celery()
app.conf.timezone = Settings.CELERY_TIME_ZONE
