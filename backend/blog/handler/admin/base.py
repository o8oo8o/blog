#!/usr/bin/evn python3
# coding=utf-8

from service.base import BaseSrv
from handler.base import BaseHandler


class BaseAdminHandler(BaseHandler):
    """
    # 后台管理基类,所有/api/admin/开头的handler都要继承这个类
    """
    def prepare(self) -> None:
        """
        # 检查是否登陆
        """
        path = self.request.path
        if path != self.application.settings.get("login_url"):
            if self.session["is_login"] != "yes":
                self.send_json({"code": 444})
                self.finish()

    def on_finish(self) -> None:
        """
        # 请求完成数据提交
        """
        BaseSrv.commit()


