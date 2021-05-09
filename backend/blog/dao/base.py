#!/usr/bin/evn python3
# coding=utf-8

from datetime import datetime
from datetime import timedelta
from model.base import session
from util.logger import AppLog


class BaseDAO:
    """
    数据操作基类，所有数据操作都需要继承这类
    """
    db_session = session

    @classmethod
    def _day_offset_calculation(cls, day_offset: int = 15) -> tuple:
        """
        # 天数偏移计算,计算时间上限和下限
        :param day_offset:
        """
        date = datetime.now()
        if day_offset == 0:
            # 查询今天的 0:0:0 - 23:59:59
            upper = datetime(date.year, date.month, date.day, 23, 59, 59)
            lower = datetime(date.year, date.month, date.day, 0, 0, 0)
        else:
            upper = datetime(date.year, date.month, date.day)
            lower = upper - timedelta(days=day_offset)
        return lower, upper

    @classmethod
    def commit(cls) -> None:
        """
        # 数据提交请求
        """
        try:
            cls.db_session.commit()
        except Exception as db_exp:
            cls.db_session.rollback()
            AppLog().logger.error(f"数据提交错误:{db_exp}")


