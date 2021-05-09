#!/usr/bin/evn python3
# coding=utf-8

import json
from service.login import LoginSrv
from service.loginlog import LoginLogSrv
from handler.admin.base import BaseAdminHandler
from util.blogenum import LoginType
from util.blogenum import ErrorType


class LoginHandler(BaseAdminHandler):
    """
    # 登陆处理
    """
    def write_error(self, status_code: int, **kwargs) -> None:
        self.set_status(444, "error")
        error_info = json.dumps({
            "code": "444",
            "msg": "error",
        })
        self.finish(error_info)

    async def post(self):
        """
        # 登陆验证检查
        """
        ip = self.get_remote_ip()
        agent = self.get_user_agent()
        user = self.get_argument_str("user", max_len=126)
        pwd = self.get_argument_pwd("pwd", max_len=126)
        rem = self.get_argument_bool("rem")
        if not self.acl.is_permit(ip):
            self.acl.add_try_count(ip)
            self.send_json({"code": 1, "msg": "try_count_many"})
            LoginLogSrv.add_log(
                False, LoginType.admin.value, ErrorType.admin_acl.value, ip, user, pwd, agent)
            return

        result = LoginSrv.login_check(user, pwd)
        if result:
            self.send_json({"code": 0, "msg": "login_ok"})
            self.session["is_login"] = "yes"
            if rem:
                self.session["rem"] = "yes"
            else:
                self.session["rem"] = "no"

            LoginLogSrv.add_log(
                True, LoginType.admin.value, ErrorType.no_error.value, ip,"admin_ok","admin_ok",agent)
        else:
            self.acl.add_try_count(ip)
            self.send_json({"code": 1, "msg": "username_or_password_error"})
            pwd = self.get_argument_str("pwd", max_len=126, default="pwd")
            LoginLogSrv.add_log(
                False, LoginType.admin.value, ErrorType.user_pwd_error.value, ip, user, pwd, agent)


class LogoutHandler(BaseAdminHandler):
    """
    # 退出登陆
    """
    async def get(self):
        """
        # 退出登陆处理
        :return:
        """
        self.session.clean()
        self.send_json({"code": 0, "msg": "logout_ok"})


