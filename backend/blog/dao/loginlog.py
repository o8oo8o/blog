#!/usr/bin/evn python3
# coding=utf-8

from typing import Union
from sqlalchemy import func
from model.model import LoginLog
from dao.base import BaseDAO
from util.blogenum import LoginType


class LoginLogDAO(BaseDAO):
    """
    对登陆表增删查
    """

    @classmethod
    def insert_one(
            cls,
            is_success: bool,
            login_type: int,
            error_type: int,
            ip: str,
            user: str,
            pwd: str,
            agent: str
            
    ) -> None:
        """
        # 插入一条日志
        :param is_success: 是否成功
        :param login_type: 登陆类型
        :param error_type: 错误类型
        :param ip: IP地址
        :param user: 用户名
        :param pwd: 密码
        :param agent: 登陆agent
        """
        cls.db_session.add(LoginLog(is_success, login_type, error_type, ip, user, pwd, agent))

    @classmethod
    def delete_one(cls, log_id: int) -> None:
        """
        # 删除一条日志
        :param log_id: 主键ID
        :return:
        """
        cls.db_session.delete(cls.select_one(log_id))

    @classmethod
    def select_one(cls, log_id: int) -> Union[LoginLog, None]:
        """
        # 查询返回一条日志
        :param log_id: 主键ID
        """
        return cls.db_session.query(LoginLog).get(log_id)

    @classmethod
    def select_login(
            cls,
            is_success: bool,
            login_type: int,
            day_offset: int = 15,
    ) -> list:
        """
        # 最近 15 天后台登陆调用统计
        :param is_success 是否登陆成功
        :param login_type 登陆类型
        :param day_offset: 时间偏移,默认统计15天以前
        """
        lower, upper = cls._day_offset_calculation(day_offset)
        login_data = cls.db_session.query(
            func.date_format(LoginLog.create_time, "%Y-%m-%d").label("date"),
            func.count().label("count")
        ).filter(LoginLog.is_success == is_success). \
            filter(LoginLog.login_type == login_type).\
            filter(LoginLog.create_time.between(lower, upper)). \
            group_by("date").order_by("date").all_data()
        return login_data

    @classmethod
    def select_today_login(cls, day_offset: int = 0) -> list:
        """
        # today 天登陆调用统计
        """
        lower, upper = cls._day_offset_calculation(day_offset)
        login_data = cls.db_session.query(
            func.date_format(LoginLog.create_time, "%Y-%m-%d").label("date"),
            LoginLog.is_success.label("is_success"),
            LoginLog.login_type.label("login_type")
        ).filter(LoginLog.create_time.between(lower, upper)).all_data()
        return login_data


