#!/usr/bin/evn python3
# coding=utf-8
import logging


class AppException(Exception):
    def __init__(self, *args, **kwargs):
        logger = logging.getLogger("tornado.access")
        # 控制台是否输出日志
        logger.propagate = False
        logger.error(f"AppException:{args}")


class AppValueError(AppException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AppAttributeError(AppException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


