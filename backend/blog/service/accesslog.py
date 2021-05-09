#!/usr/bin/evn python3
# coding=utf-8

from service.base import BaseSrv
from dao.accesslog import AccessLogDAO


class AccessLogSrv(BaseSrv):

    @classmethod
    def add_log(
        cls, ip: str,
        method: str,
        status: int,
        qtime: float,
        path: str,
        agent: str,
        query: str
    ) -> None:
        """
        # 添加一条访问日志
        :param ip: IP地址
        :param method: 请求方法
        :param status: 状态码
        :param qtime: 响应时长
        :param path: 请求路径
        :param agent: 客户端
        :param query: 查询字符串
        """
        AccessLogDAO.insert_one(ip, method, status, qtime, path, agent, query)


