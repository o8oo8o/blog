#!/usr/bin/evn python3
# coding=utf-8

from typing import Union
from sqlalchemy import exists
from sqlalchemy import func
from model.model import Blog
from model.model import Classify
from model.model import Review
from dao.base import BaseDAO


class BlogDAO(BaseDAO):
    """
    对blog表增删改查
    """
    @classmethod
    def insert_one(
            cls,
            classify_id: int,
            title: str,
            text: str,
            weight: int = 20000,
            is_review: bool = False,
            is_public: bool = False,
            status: int = 0
    ) -> None:
        """
        # 插入单条博客
        :param classify_id: 博客分类ID,是个外键,对应classify表的ID字典
        :param title: 博客标题
        :param text: 博客内容
        :param weight: 权重 范围 10000 - 50000 之间
        :param is_review: 是否允许评论
        :param is_public: 是否公开
        :param status: 状态:状态{0:已发布,1:预览保存}
        :return: 空
        """
        if not cls.select_title_exists(title):
            blog = Blog(classify_id, title, text, weight, is_review, is_public, status)
            cls.db_session.add(blog)

    @classmethod
    def delete_one(cls, blog_id: int) -> None:
        """
        # 根据ID删除博客,存在才能删除
        :param blog_id: 博客ID
        :return:
        """
        blog = cls.select_one(blog_id)
        if blog:
            cls.db_session.delete(blog)

    @classmethod
    def update_one(cls, blog_id: int, **kwargs) -> None:
        """
        # 根据ID更新博客
        :param blog_id: 博客ID
        :param kwargs: 更新字段例如：update_one(1, title="blog_tile",text="this text",...)
        :return: 空
        """
        blog = cls.select_one(blog_id)
        if blog:
            for key, value in kwargs.items():
                if hasattr(blog, key):
                    setattr(blog, key, value)

    @classmethod
    def select_one(cls, blog_id: int) -> Union[Blog, None]:
        """
        # 根据ID查询博客
        :param blog_id: 博客ID
        :return: Blog
        """
        return cls.db_session.query(Blog).get(blog_id)

    @classmethod
    def select_title_exists(cls, title: str) -> bool:
        """
        # 查询标题是否存在
        :param title: 博客标题
        :return: 布尔值 True-> 存在,  False->不存在
        """
        is_exists = cls.db_session.query(
            exists().where(Blog.title == title)
        ).scalar()
        return is_exists

    @classmethod
    def select_one_public(cls, blog_id: int) -> Union[Blog, None]:
        """
        # 返回一个已公开发布的博客
        :param blog_id: 博客ID
        :return: 一个Blog对象，或者None
        """
        blog = cls.db_session.query(Blog).\
            filter(Blog.id == blog_id).\
            filter(Blog.is_public). \
            filter(Blog.status == 0).first()
        return blog

    @classmethod
    def select_blog_review_list(cls, blog_id: int) -> list:
        """
        # 根据博客ID,查询博客的评论
        :param blog_id: 博客ID
        :return: 评论列表
        """
        return cls.db_session.query(Review).filter(Review.blog_id == blog_id).all()

    @classmethod
    def select_year_count(cls) -> list:
        """
        # 查询已发布的博客，按照年统计数量
        :return:
        例如:
        [{'year': '2016', 'blog_count': 3}, {'year': '2017', 'blog_count': 6}, ...]
        """
        year_count = cls.db_session.query(
            func.date_format(Blog.create_time, '%Y').label('year'),
            func.count(Blog.id).label('blog_count')
        ).filter(Blog.is_public).\
            filter(Blog.status == 0).\
            group_by('year').\
            order_by("year").all_data()
        return year_count

    @classmethod
    def select_classify_count(cls) -> list:
        """
        # 查询已发布的博客，按照分类统计数量
        :return: 例如:
        [
            {'name': 'Python', 'blog_count': 9, 'classify_id': 1},
            {'name': 'Java', 'blog_count': 5, 'classify_id': 2}
        ]
        """
        classify_group = cls.db_session.query(
            Blog.classify_id.label("classify_id"),
            func.count(Blog.classify_id).label("blog_count")
        ).filter(Blog.is_public).\
            filter(Blog.status == 0).\
            group_by(Blog.classify_id).subquery()

        classify_count = cls.db_session.query(
            Classify.name,
            classify_group.c.blog_count,
            classify_group.c.classify_id,
        ).join(Classify).\
            filter(classify_group.c.blog_count > 0).\
            order_by(Classify.id).all_data()
        return classify_count

    @classmethod
    def select_blog_review_count(cls, blog_id: int) -> int:
        """
        # 根据博客ID查找博客的评论数量
        :param blog_id: 博客ID
        :return: 博客评论的数量
        """
        return cls.db_session.query(Review).filter(Review.blog_id == blog_id).count()

    @classmethod
    def __select_blog_review_group_by_count(cls):
        """
        # 查询博客评论数量
        """
        return cls.db_session.query(
            Review.blog_id.label("blog_id"),
            func.count(Review.blog_id).label("review_count")
        ).group_by(Review.blog_id).subquery()

    @classmethod
    def select_blog_list(cls, is_public: bool = True) -> list:
        """
        # 默认查询已发布的博客列表
        :return: 已发布博客列表
        """
        blog_review_count = cls.__select_blog_review_group_by_count()
        blog = cls.db_session.query(
            Blog.id.label("blog_id"),
            Blog.weight.label("weight"),
            Blog.title.label("title"),
            Classify.name.label("classify_name"),
            Blog.create_time.label("create_time"),
            Blog.read_count.label("read_count"),
        ).outerjoin(Classify). \
            filter(Blog.is_public == is_public). \
            filter(Blog.status == 0).subquery()

        blog_list = cls.db_session.query(
            blog.c.blog_id,
            blog.c.title,
            blog.c.classify_name,
            blog.c.create_time,
            blog.c.read_count,
            blog_review_count.c.review_count
        ).outerjoin(blog_review_count). \
            order_by(blog.c.weight.desc()). \
            order_by(blog.c.create_time.desc()).all_data()
        return blog_list

    @classmethod
    def select_admin_blog_list(cls, title_like="") -> list:
        """
        # 查询所有博客列表,或者按照博客标题(title)搜索
        :param title_like: 搜索文字
        :return: 所有博客列表
        """
        blog_review_count = cls.__select_blog_review_group_by_count()
        blog = cls.db_session.query(
            Blog.id.label("blog_id"),
            Blog.weight.label("weight"),
            Blog.title.label("title"),
            Blog.status.label("status"),
            Blog.classify_id.label("classify_id"),
            Classify.name.label("classify_name"),
            Blog.read_count.label("read_count"),
            Blog.is_public.label("is_public"),
            Blog.is_review.label("is_review"),
            Blog.create_time.label("create_time"),
            Blog.update_time.label("update_time"),
        ).outerjoin(Classify). \
            filter(Blog.title.like(f"%{title_like}%")).subquery()

        """
        # 相当于执行下面的SQL:
        """
        blog_list = cls.db_session.query(
            blog.c.blog_id,
            blog.c.title,
            blog.c.status,
            blog.c.classify_id,
            blog.c.classify_name,
            blog.c.read_count,
            blog_review_count.c.review_count,
            blog.c.is_public,
            blog.c.is_review,
            blog.c.create_time,
            blog.c.update_time
        ).outerjoin(blog_review_count).\
            order_by(blog.c.weight.desc()). \
            order_by(blog.c.create_time.desc()).all_data()
        return blog_list

    @classmethod
    def select_blog_count(cls) -> int:
        """
        # 查询一共有博客
        :return: 评论数量
        """
        return cls.db_session.query(Blog).count()


