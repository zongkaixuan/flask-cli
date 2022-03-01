# -*- coding: utf-8 -*-
import logging
import os
from pythonjsonlogger import jsonlogger
from app.config import Settings


class Log:
    '''
    from flask import current_app
    current_app.logger.info('yyyy')
    '''
    def __init__(self):
        # Create log folder
        self.extra = {'app_name': Settings.APP_NAME}
        log_path = Settings.LOGPATH
        log_name = Settings.LOGNAME + '.log'
        log_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)) + os.sep + log_path
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        # Full dir for log file
        log_file = log_path + os.sep + log_name
        handler = logging.FileHandler(log_file, encoding='UTF-8')
        stream_handler = logging.StreamHandler()
        logging_format = logging.Formatter(Settings.LOGFORMAT)
        logging_format = jsonlogger.JsonFormatter(fmt=Settings.LOGFORMAT)
        handler.setFormatter(logging_format)
        stream_handler.setFormatter(logging_format)
        self.handler = handler
        self.stream_handler = stream_handler

    def init_app(self, app):
        app.logger.setLevel(Settings.LOGLEVEL)
        app.logger.addHandler(self.handler)
        app.logger.propagate = False  # Make sure do not write the duplicate log in file
        app.logger.addHandler(self.stream_handler)
        app.logger = logging.LoggerAdapter(app.logger, extra=self.extra)

    def get_logger(self, name):
        logger = logging.getLogger(name)
        logger.propagate = False  # Make sure do not write the duplicate log in file
        logger.setLevel(Settings.LOGLEVEL)
        logger.addHandler(self.handler)
        logger.addHandler(self.stream_handler)
        logger = logging.LoggerAdapter(logger, extra=self.extra)
        return logger


log = Log()
