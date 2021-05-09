#!/usr/bin/evn python3
# coding=utf-8

from typing import Union
from sqlalchemy import or_
from model.model import Review
from model.model import Blog
from dao.base import BaseDAO
from dao.blog import BlogDAO


class ReviewDAO(BaseDAO):
    """
    对Review表增删改查
    """

    @classmethod
    def insert_one(cls, blog_id: int, name: str, email: str, text: str) -> None:
        """
        # 插入评论
        :param blog_id: 博客ID,是个外键,对应blog表的ID字典
        :param name: 评论人名字
        :param email: 评论人邮箱
        :param text: 评论内容 最多65535个字符
        """
        blog = BlogDAO.select_one_public(blog_id)
        if blog:
            cls.db_session.add(Review(blog_id, name, email, text))

    @classmethod
    def delete_one(cls, review_id: int) -> None:
        """
        # 根据评论ID删除评论
        :param review_id: 评论ID
        """
        review = cls.select_one(review_id)
        if review:
            cls.db_session.delete(review)

    @classmethod
    def update_one(cls, review_id: int, **kwargs) -> None:
        """
        # 根据评论ID更新评论, #目前这个没有使用,预留的
        :param review_id: 评论ID
        :param kwargs: 更新字段例如：update_one(1, name="张三",...)
        """
        review = cls.db_session.query(Review).get(review_id)
        if review:
            for key, value in kwargs.items():
                if hasattr(review, key):
                    setattr(review, key, value)

    @classmethod
    def select_one(cls, review_id: int) -> Union[Review, None]:
        """
        # 根据评论ID查询
        :param review_id: 评论ID
        :return: Review对象, 或者None
        """
        return cls.db_session.query(Review).get(review_id)

    @classmethod
    def select_all(cls, name_or_text_like: str = "") -> list:
        """
        # 查询所有评论,或者根据评论名字或内容搜索
        :param name_or_text_like: 评论名字或内容
        :return: 评论列表
        """
        all_review = cls.db_session.query(
            Review.id,
            Review.create_time,
            Review.email,
            Review.name,
            Review.text,
            Blog.title
        ).join(Blog)
        if name_or_text_like:
            return all_review.filter(
                or_(Review.name.like(
                    f"%{name_or_text_like}%"),
                    Review.text.like(f"%{name_or_text_like}%"))
            ).order_by(Review.id.desc()).all_data()
        return all_review.order_by(Review.id.desc()).all_data()

    @classmethod
    def select_review_count(cls) -> int:
        """
        # 查询一共有多少条评论
        :return: 评论数量
        """
        return cls.db_session.query(Review).count()


