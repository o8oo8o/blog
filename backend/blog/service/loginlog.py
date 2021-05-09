#!/usr/bin/evn python3
# coding=utf-8

from service.base import BaseSrv
from dao.loginlog import LoginLogDAO


class LoginLogSrv(BaseSrv):

    @classmethod
    def add_log(
            cls,
            is_success: bool,
            login_type: int,
            error_type: int,
            ip: str,
            user: str,
            pwd: str,
            agent: str,
    ) -> None:
        """
        # 记录登陆日志及访问码登陆信息
        :param is_success: 是否登陆成功
        :param login_type: 登陆类型
        :param error_type: 错误类型
        :param ip: IP地址
        :param user: 用户名
        :param pwd: 密码
        :param agent: 客户端
        """
        LoginLogDAO.insert_one(is_success, login_type, error_type, ip, user, pwd, agent)


