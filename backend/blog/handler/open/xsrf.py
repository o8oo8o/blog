#!/usr/bin/evn python3
# coding=utf-8

from handler.open.base import WebBaseHandler


class XsrfHandler(WebBaseHandler):
    """
    Xsrf 处理
    """
    async def get(self):
        """返回xsrf 数据"""
        data = {"code": 0, "_xsrf": self.xsrf_token.decode("utf-8")}
        self.send_json(data)


