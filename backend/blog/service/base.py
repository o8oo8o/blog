#!/usr/bin/evn python3
# coding=utf-8

from dao.base import BaseDAO


class BaseSrv:
    """
    服务操作基类，所有服务操作都需要继承这类
    """

    @classmethod
    def commit(cls) -> None:
        """
        # 提交数据
        """
        BaseDAO.commit()


