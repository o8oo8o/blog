#!/usr/bin/evn python3
# coding=utf-8

from dao.setting import SettingDAO
from service.base import BaseSrv


class LoginSrv(BaseSrv):

    @classmethod
    def login_check(cls, user: str, pwd: str) -> bool:
        """
        # 检查用户名密码是否正确
        :return: 布尔值 True-> 检查通过,  False-> 检查不通过
        """
        setting = SettingDAO.select_setting("metadata")
        if user == setting["admin_user"] and pwd == setting["admin_pwd"]:
            return True
        else:
            return False


