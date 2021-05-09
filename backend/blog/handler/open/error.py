#!/usr/bin/evn python3
# coding=utf-8

from handler.open.base import WebBaseHandler


class ErrorHandler(WebBaseHandler):
    async def get(self):
        """
        # 发送404错误数据
        """
        self.send_json({"code": 404, "msg": "NotFound"})


