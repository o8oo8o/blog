#!/usr/bin/evn python3
# coding=utf-8

import time
import logging
import logging.handlers
from util.config import ConfigMixIn
from util import singleton


@singleton
class AppLog(ConfigMixIn):
    """
    # 日志记录功能
    #############
    # 日志支持的级别
    #############
    #  CRITICAL 50
    #  ERROR    40
    #  WARNING  30
    #  INFO     20
    #  DEBUG    10
    #  NOTSET   0
    #############
    """

    def __init__(self):
        log_conf = self.conf.get_conf("log")
        # 名字需要写 tornado.access
        logger = logging.getLogger("tornado.access")
        # 是否关闭日志功能
        logger.disabled = log_conf["disabled"]
        # 控制台是否输出日志
        logger.propagate = log_conf["propagate"]

        handler = logging.handlers.TimedRotatingFileHandler(
            filename=log_conf["path"] + time.strftime(log_conf["file"]),
            when=log_conf["when"],
            interval=log_conf["interval"],
            backupCount=log_conf["backup_count"]
        )
        handler.suffix = log_conf["suffix"]

        level = log_conf["level"]
        if level == "NOTSET":
            logger.setLevel(logging.NOTSET)
        if level == "DEBUG":
            logger.setLevel(logging.DEBUG)
        if level == "INFO":
            logger.setLevel(logging.INFO)
        if level == "WARNING":
            logger.setLevel(logging.WARNING)
        if level == "ERROR":
            logger.setLevel(logging.ERROR)
        if level == "CRITICAL":
            logger.setLevel(logging.CRITICAL)
        formatter = logging.Formatter(log_conf["format"])
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        self.logger = logger


