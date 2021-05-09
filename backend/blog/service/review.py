#!/usr/bin/evn python3
# coding=utf-8

import math
from dao.blog import BlogDAO
from dao.review import ReviewDAO
from dao.setting import SettingDAO
from service.base import BaseSrv


class ReviewSrv(BaseSrv):

    @classmethod
    def add_review(cls, blog_id: int, name: str, email: str, text: str) -> None:
        """
        # 新增一条评论
        """
        blog = BlogDAO.select_one_public(blog_id)
        # 博客是否存在
        if blog:
            # 检查博客是否允许评论
            if blog.is_review:
                ReviewDAO.insert_one(blog_id, name, email, text)

    @classmethod
    def get_review_list(cls, page: int = 1, name_or_text_like: str = "") -> tuple:
        """
        # 根据page页码获取评论列表
        :param page: 页码
        :param name_or_text_like: 搜素评论名称或者评论内容
        :return: 最大页码，评论列表
        """
        page_size = SettingDAO.select_setting()["admin_review_pz"]
        reviews = ReviewDAO.select_all(name_or_text_like)
        max_page = math.ceil(len(reviews) / page_size)
        page = max_page if page > max_page else page
        page = 1 if page == 0 else page
        if page == 1:
            start = 0
            end = page_size
        else:
            start = (page-1) * page_size
            end = start + page_size

        reviews_info = [
            {
                "id": item["id"],
                "create_time": item["create_time"].strftime('%Y-%m-%d %H:%M:%S'),
                "email": item["email"],
                "name": item["name"],
                "text": item["text"],
                "blog_title": item["title"]
            } for item in reviews[start:end]
        ]
        return max_page, reviews_info

    @classmethod
    def del_review(cls, review_id: int) -> None:
        """
        # 根据评论ID删除评论
        :param review_id: 评论ID,数据库主键
        """
        ReviewDAO.delete_one(review_id)


