#!/usr/bin/evn python3
# coding=utf-8

from typing import Union
from sqlalchemy import exists
from sqlalchemy import func
from model.model import Classify
from model.model import Blog
from dao.base import BaseDAO
from dao.blog import BlogDAO


class ClassifyDAO(BaseDAO):
    """
    对博客分类表增删改查
    """

    @classmethod
    def insert_one(cls, name: str) -> None:
        """
        # 插入一个博客分类,当分类名称不存在的时候可以插入
        :param name: 分类名称
        """
        if not cls.select_name_exists(name):
            cls.db_session.add(Classify(name))

    @classmethod
    def delete_one(cls, classify_id: int) -> None:
        """
        # 根据分类ID删除,分类存在的时候删除
        :param classify_id: 分类ID
        """
        classify = cls.select_one(classify_id)
        if classify:
            # 该分类下博客数量为零才删除
            if cls.select_classify_blog_count(classify_id) == 0:
                cls.db_session.delete(classify)

    @classmethod
    def update_one(cls, classify_id: int, **kwargs) -> None:
        """
        # 根据分类ID更新,分类存在的时候更新
        :param classify_id: 分类ID
        :param kwargs: 更新字段例如：update_one(1, name="Python")
        """
        classify = cls.select_one(classify_id)
        if classify:
            for key, value in kwargs.items():
                if hasattr(classify, key):
                    setattr(classify, key, value)

    @classmethod
    def select_one(cls, classify_id: int) -> Union[Classify, None]:
        """
        # 根据分类ID查询
        :param classify_id: 分类ID
        :return: Classify 对象,或者None
        """
        return cls.db_session.query(Classify).get(classify_id)

    @classmethod
    def select_name_exists(cls, name: str) -> bool:
        """
        # 根据分类名称，查询分类是否存在
        :param name: 分类名称
        :return: 布尔值 True-> 存在,  False->不存在
        """
        it_exists = cls.db_session.query(
            exists().where(Classify.name == name)
        ).scalar()
        return it_exists

    @classmethod
    def select_classify_blog_count(cls, classify_id: int) -> int:
        """
        # 根据分类下面博客的数量
        :param classify_id: 博客ID
        :return: 分类下面博客的数量
        """
        return cls.db_session.query(Blog).\
            filter(Blog.classify_id == classify_id).count()

    @classmethod
    def select_classify_list(cls) -> list:
        """
        # 获取分类列表
        :return: 分类列表
        """
        classify_group = BlogDAO.db_session.query(
            Blog.classify_id.label("classify_id"),
            func.count(Blog.classify_id).label("blog_count")
        ).group_by(Blog.classify_id).subquery()

        classify_list = cls.db_session.query(
            Classify.id,
            Classify.name,
            classify_group.c.blog_count,
            Classify.create_time,
            Classify.update_time
            ).outerjoin(classify_group).order_by(Classify.id).all_data()
        return classify_list


