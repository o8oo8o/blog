#!/usr/bin/evn python3
# coding=utf-8

from typing import Union
from sqlalchemy import exists
from model.model import Resume
from model.model import Publish
from dao.base import BaseDAO


class ResumeDAO(BaseDAO):
    """
    对简历表增删改查
    """

    @classmethod
    def insert_one(cls, title: str, text: str) -> None:
        """
        # 增加一条简历
        :param title: 简历标题
        :param text: 简历内容,使用MySQL LongText 存储
        """
        if not cls.select_title_exists(title):
            cls.db_session.add(Resume(title, text))

    @classmethod
    def delete_one(cls, resume_id: int) -> None:
        """
        # 根据ID删除简历,存在才删除,没有发布引用才删除
        :param resume_id: 简历ID
        """
        resume = cls.select_one(resume_id)
        if resume:
            if cls.__select_resume_publish_count(resume_id) == 0:
                cls.db_session.delete(resume)

    @classmethod
    def update_one(cls, resume_id: int, **kwargs) -> None:
        """
        # 根据ID更新简历
        :param resume_id: 简历ID
        :param kwargs: 更新字段例如：update_one(1, title="Python工程师",...)
        """
        resume = cls.select_one(resume_id)
        if resume:
            for key, value in kwargs.items():
                if hasattr(resume, key):
                    setattr(resume, key, value)

    @classmethod
    def select_one(cls, resume_id: int) -> Union[Resume, None]:
        """
        # 根据ID查询简历
        :param resume_id: 简历ID
        :return: Resume对象, 或者None
        """
        return cls.db_session.query(Resume).get(resume_id)

    @classmethod
    def select_title_exists(cls, title: str) -> bool:
        """
        # 查询标题是否存在
        :param title: 简历标题
        :return:  布尔值 True-> 存在,  False->不存在
        """
        is_exists = cls.db_session.query(
            exists().where(Resume.title == title)
        ).scalar()
        return is_exists

    @classmethod
    def __select_resume_publish_count(cls, resume_id: int) -> int:
        """
        # 获取简历发布次数
        :param resume_id: 简历ID
        :return:
        """
        return cls.db_session.query(Publish).\
            filter(Publish.resume_id == resume_id).count()

    @classmethod
    def select_all(cls) -> list:
        """
        # 查询所有简历
        :return: 简历列表
        """
        return cls.db_session.query(Resume).all()


