#!/usr/bin/evn python3
# coding=utf-8

import math
from model.model import Blog
from service.base import BaseSrv
from dao.setting import SettingDAO
from dao.blog import BlogDAO


class BaseSrvBlog(BaseSrv):
    """
    # 博客基础类
    """
    @classmethod
    def get_blog_review_list(cls, blog_id: int) -> list:
        """
        # 获取博客的评论列表
        :return: 评论列表
        """
        reviews_list = [
            {
                "id": review.id,
                "name": review.name,
                "text": review.text,
                "create_time": review.create_time,
            } for review in BlogDAO.select_blog_review_list(blog_id)
        ]
        return reviews_list


class BlogSrv(BaseSrvBlog):
    """
    # 前台博客数据获取
    """

    @classmethod
    def get_blog(cls, blog_id: int, is_read=False) -> dict:
        """
        # 根据博客ID查找当前博客数据，及上一篇下一篇元数据
        :return:
        """
        if is_read:
            # 前台web查看的时候,查询已经发布公开的
            blog = BlogDAO.select_one_public(blog_id)
        else:
            # 后台admin查看的时候,直接查询
            blog = BlogDAO.select_one(blog_id)

        if blog:
            blog_data = {
                "id": blog.id,  # 前端使用
                "title": blog.title,  # 前端使用
                "status": blog.status,
                "read_count": blog.read_count,  # 前端使用
                "review_count": BlogDAO.select_blog_review_count(blog_id),  # 前端使用
                "create_time": blog.create_time,  # 前端使用
                "update_time": blog.update_time,
                "is_review": blog.is_review,  # 前端使用
                "is_public": blog.is_public,
                "weight": blog.weight,
                "classify_id": blog.classify_id,
                "classify_name": blog.classify.name,  # 前端使用
                "text": blog.text,  # 前端使用
                "review_list": cls.get_blog_review_list(blog_id),  # 前端使用
            }

            if is_read:
                # 前台web查看的时候,增加阅读计数器
                cls.__put_read_count(blog_id)
                # 前台web查看的时候,需要上一篇及下一篇博客信息方便查看
                prev_blog_info, next_blog_info = cls.__get_prev_and_next_blog_info(blog)
                blog_data["prev_blog"] = prev_blog_info
                blog_data["next_blog"] = next_blog_info
                # 前台web查看的时候,不需要下面五个字段
                blog_data.pop("status")
                blog_data.pop("update_time")
                blog_data.pop("is_public")
                blog_data.pop("weight")
                blog_data.pop("classify_id")
            return blog_data
        else:
            return {}

    @classmethod
    def __put_read_count(cls, blog_id: int) -> None:
        """
        # 更新文章的阅读次数
        """
        blog = BlogDAO.select_one(blog_id)
        if blog:
            BlogDAO.update_one(blog_id, read_count=blog.read_count+1)

    @classmethod
    def __get_prev_and_next_blog_info(cls, blog: Blog) -> tuple:
        """
        # 获取当前博客的数据及上一篇，下一篇信息
        :return:
        """
        blog_id = blog.id
        blog_list = BlogDAO.select_blog_list()
        blog_id_list = [blog["blog_id"] for blog in blog_list]
        # 前一篇文章信息
        prev_blog_info = {"is_exists": False, "id": 0, "title": ""}
        # 后一篇文章信息
        next_blog_info = {"is_exists": False, "id": 0, "title": ""}
        if blog_id in blog_id_list:
            current_blog_index = blog_id_list.index(blog_id)
            if current_blog_index > 0:
                prev_blog = blog_list[current_blog_index - 1]
                prev_blog_info = {
                    "is_exists": True,
                    "id": prev_blog["blog_id"],
                    "title": prev_blog["title"]
                }
            if current_blog_index < len(blog_id_list)-1:
                next_blog = blog_list[current_blog_index + 1]
                next_blog_info = {
                    "is_exists": True,
                    "id": next_blog["blog_id"],
                    "title": next_blog["title"]
                }
        return prev_blog_info, next_blog_info


class BlogAdminSrv(BlogSrv):
    """
    # 后台博客增删改查
    """
    @classmethod
    def add_blog(
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
        # 新增博客
        :param classify_id: 博客分类ID
        :param title: 博客标题
        :param text: 博客内容
        :param weight: 博客权重 10000 - 50000 之间
        :param is_review: 是否允许评论
        :param is_public: 是否公开
        :param status: 状态{0:已发布,1:预览保存}
        """
        BlogDAO.insert_one(classify_id, title, text, weight, is_review, is_public, status)

    @classmethod
    def del_blog(cls, blog_id: int) -> None:
        """
        # 删除博客
        :param blog_id: 博客ID,也是主键ID
        """
        BlogDAO.delete_one(blog_id)

    @classmethod
    def put_blog(
        cls,
        blog_id: int,
        **kwargs
    ) -> None:
        """
        # 根据博客ID更新博客
        :param blog_id: 博客ID
        :param kwargs: 修改内容
        """
        BlogDAO.update_one(blog_id=blog_id, **kwargs)

    @classmethod
    def get_title_exists(cls, title: str) -> bool:
        """
        # 检查该标题的博客是否存在
        :param title: 博客标题
        :return: 布尔值 True-> 存在,  False->不存在
        """
        return BlogDAO.select_title_exists(title)

    @classmethod
    def get_blog_list(cls, page=1, title_like: str = "") -> tuple:
        """
        # 更具页码和搜索文字显示博客
        :param page: 页码
        :param title_like: 搜索博客标题文字
        :return: 最大页码,博客列表
        """
        page_size = SettingDAO.select_setting()["admin_blog_pz"]
        all_blog = BlogDAO.select_admin_blog_list(title_like)
        max_page = math.ceil(len(all_blog) / page_size)
        page = max_page if page > max_page else page
        page = 1 if page == 0 else page
        if page == 1:
            start = 0
            end = page_size
        else:
            start = (page-1) * page_size
            end = start + page_size

        blog_list = [
            {
                "id": item["blog_id"],
                "title": item["title"],
                "status": item["status"],
                "classify_id": item["classify_id"],
                "classify_name": item["classify_name"],
                "read_count": item["read_count"],
                "review_count": item["review_count"] if item["review_count"] else 0,
                "is_public": item["is_public"],
                "is_review":  item["is_review"],
                "create_time": item["create_time"],
                "update_time": item["update_time"]
            } for item in all_blog[start:end]
        ]
        return max_page, blog_list


