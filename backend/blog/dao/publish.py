#!/usr/bin/evn python3
# coding=utf-8

from datetime import datetime
from typing import Union
from sqlalchemy import exists
from sqlalchemy import func
from model.model import Resume
from model.model import Publish
from dao.base import BaseDAO


class PublishDAO(BaseDAO):
    """
    对简历发布表增删改查
    """

    @classmethod
    def insert_one(
            cls,
            access_code: str,
            resume_id: int,
            receiver: str,
            exp_time: datetime,
            read_count: int = 0,
            read_duration: int = 0,
            read_time: datetime = datetime(1970, 1, 1, 0, 0, 0)
    ) -> None:
        """
        # 插入一条简历发布
        # 先检查接收者，和访问码是否存在
        :param resume_id:  简历ID,是个外键,对应resume表的ID字典
        :param receiver: 简历接收者
        :param access_code: 简历访问码,unique 非空约束
        :param exp_time: 简历访问过期时间
        :param read_count: 阅读计数
        :param read_duration: 阅读时长
        :param read_time: 什么时间阅读的
        :return:
        """
        if cls.select_access_code_exists(access_code):
            return None
        cls.db_session.add(
            Publish(
                access_code=access_code,
                resume_id=resume_id,
                receiver=receiver,
                exp_time=exp_time,
                read_count=read_count,
                read_duration=read_duration,
                read_time=read_time
            )
        )

    @classmethod
    def delete_one(cls, publish_id: int) -> None:
        """
        # 根据ID删除简历,存在才删除
        :param publish_id: 发布ID
        :return: 空
        """
        publish = cls.select_one(publish_id)
        if publish:
            cls.db_session.delete(publish)

    @classmethod
    def update_one(cls, publish_id: int, **kwargs) -> None:
        """
        # 根据ID更新简历
        :param publish_id: 发布ID
        :param kwargs: 更新字段例如：update_one(1, access_code="123456")
        :return:
        """
        publish = cls.select_one(publish_id)
        if publish:
            for key, value in kwargs.items():
                if hasattr(publish, key):
                    setattr(publish, key, value)

    @classmethod
    def select_one(cls, publish_id: int) -> Union[Publish, None]:
        """
        # 根据ID查询简历
        :param publish_id:  发布ID
        :return: Publish 对象,或者 None
        """
        return cls.db_session.query(Publish).get(publish_id)

    @classmethod
    def select_access_code_exists(cls, access_code: str) -> bool:
        """
        # 查询接收者是否存在
        :param access_code: 访问码
        :return: 布尔值 True-> 存在,  False->不存在
        """
        is_exists = cls.db_session.query(
            exists().where(Publish.access_code == access_code)
        ).scalar()
        return is_exists

    @classmethod
    def select_all(cls, receiver_like: str = "") -> list:
        """
        # 查询所有简历，或者根据简历接收者搜索
        :rtype:
        :param receiver_like: 搜索简历接收者
        :return:  简历列表
        """

        all_publish = cls.db_session.query(
            Publish.id,
            Publish.access_code,
            Publish.resume_id,
            Resume.title,
            Publish.receiver,
            Publish.exp_time,
            Publish.read_count,
            Publish.read_duration,
            Publish.read_time,
            Publish.create_time,
            Publish.update_time,
        ).join(Resume)
        if receiver_like:
            return all_publish.filter(
                Publish.receiver.like(f"%{receiver_like}%")
            ).order_by(Publish.id.desc()).all_data()
        return all_publish.order_by(Publish.id.desc()).all_data()

    @classmethod
    def select_publish(cls, access_code: str = None) -> list:
        """
        # 前台根据访问码查询简历
        :return: 列表，
        实际上access_code是唯一非空约束，这个列表只有一条记录
        返回list, 为了方便前端
        """
        return cls.db_session.query(
            Publish.id,
            Publish.receiver,
            Publish.access_code,
            Publish.exp_time,
            Publish.read_count,
            Publish.read_time,
            Publish.read_duration,
            Resume.title,
            Resume.text
        ).join(Resume).\
            filter(Publish.access_code == access_code).all_data()

    @classmethod
    def select_read_count(cls, day_offset: int = 15) -> list:
        """
        # 最近15 阅读次数
        :param day_offset: 时间偏移,默认统计15天以前
        """
        lower, upper = cls._day_offset_calculation(day_offset)
        read_count = cls.db_session.query(
            func.date_format(Publish.read_time, "%Y-%m-%d").label("date"),
            func.count().label("count")
        ).filter(Publish.read_time.between(lower, upper)).\
            group_by("date").order_by("date").all_data()
        return read_count

    @classmethod
    def select_publish_count(cls) -> int:
        """
        # 简历发布次数
        :return: 评论数量
        """
        return cls.db_session.query(Publish).count()


