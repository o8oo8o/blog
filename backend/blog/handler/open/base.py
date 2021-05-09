#!/usr/bin/evn python3
# coding=utf-8

import json
from service.accesslog import AccessLogSrv
from handler.base import BaseHandler


class WebBaseHandler(BaseHandler):

    def write_error(self, status_code: int, **kwargs) -> None:
        """
        # 错误处理
        :param status_code:
        :param kwargs:
        :return:
        """
        self.set_status(432, "error")
        error_info = json.dumps({
            "code": "432",
            "msg": "error",
        })
        self.finish(error_info)

    def on_finish(self) -> None:
        """
        # 请求完成数据提交,记录日志
        """
        AccessLogSrv.add_log(*self.record_request())
        AccessLogSrv.commit()


