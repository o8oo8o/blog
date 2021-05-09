#!/usr/bin/evn python3
# coding=utf-8

from typing import Union
from sqlalchemy import func
from sqlalchemy import desc
from sqlalchemy import distinct
from model.model import AccessLog
from dao.base import BaseDAO


class AccessLogDAO(BaseDAO):
    """
    对访问记录表增删查
    """

    @classmethod
    def insert_one(
            cls,
            ip: str,
            method: str,
            status: int,
            qtime: float,
            path: str,
            agent: str,
            query: str
    ) -> None:
        """
        # 插入一条日志
        :param ip: IP地址
        :param method: 请求方法
        :param status: 状态码
        :param qtime: 请求时间
        :param path: 请求路径
        :param agent: 客户端
        :param query: 查询字段
        """
        cls.db_session.add(
            AccessLog(ip, method, status, qtime, path, agent, query)
        )

    @classmethod
    def delete_one(cls, log_id: int) -> None:
        """
        # 删除一条日志
        :param log_id: 主键ID
        """
        cls.db_session.delete(cls.select_one(log_id))

    @classmethod
    def select_one(cls, log_id: int) -> Union[AccessLog, None]:
        """
        # 查询返回一条日志
        :param log_id: 主键ID
        """
        return cls.db_session.query(AccessLog).get(log_id)

    @classmethod
    def select_api_call_count(cls, day_offset: int = 15) -> list:
        """
        # 最近15 天后台AIP调用统计
        :param day_offset: 时间偏移,默认统计15天以前
        """
        lower, upper = cls._day_offset_calculation(day_offset)
        api_count = cls.db_session.query(
            func.date_format(AccessLog.create_time, "%Y-%m-%d").label("date"),
            func.count().label("count")
        ).filter(AccessLog.create_time.between(lower, upper)).\
            group_by("date").all_data()
        return api_count

    @classmethod
    def select_user_access_count(cls, day_offset: int = 15) -> list:
        """
        # 最近15 天用户访问次数
        :param day_offset: 时间偏移,默认统计15天以前
        """
        lower, upper = cls._day_offset_calculation(day_offset)
        access_count = cls.db_session.query(
            func.date_format(AccessLog.create_time, "%Y-%m-%d").label("date"),
            func.count(distinct(AccessLog.ip)).label("count")
        ).filter(AccessLog.create_time.between(lower, upper)).\
            group_by("date").all_data()
        return access_count

    @classmethod
    def select_ip_top(cls, day_offset: int = 0, ret_limit: int = 100) -> list:
        """
        # 今天  访问最多的IP 前100名
        :param day_offset: 时间偏移,默认统计7天以前
        :param ret_limit: 默认返回前100个
        """
        lower, upper = cls._day_offset_calculation(day_offset)
        ip_count = cls.db_session.query(
            AccessLog.ip.label("ip"),
            func.count().label("count")
        ).filter(AccessLog.create_time.between(lower, upper)). \
            group_by("ip").order_by(desc("count")).limit(ret_limit).all_data()
        return ip_count

    @classmethod
    def select_low_top(cls, day_offset: int = 0, ret_limit: int = 100) -> list:
        """
        # 今天 响应时间最长的前100个
        :param day_offset: 时间偏移,默认统计7天以前
        :param ret_limit: 默认返回前100个
        """
        lower, upper = cls._day_offset_calculation(day_offset)
        ip_count = cls.db_session.query(
            AccessLog.id,
            AccessLog.ip,
            AccessLog.qtime.label("qtime"),
        ).filter(AccessLog.create_time.between(lower, upper)). \
            order_by(desc("qtime")).limit(ret_limit).all_data()
        return ip_count

    @classmethod
    def select_log_count(cls) -> int:
        """
        日志总数
        """
        log_count = cls.db_session.query(AccessLog).count()
        return log_count


