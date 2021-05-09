#!/usr/bin/evn python3
# coding=utf-8

from service.base import BaseSrv
from dao.classify import ClassifyDAO


class ClassifySrv(BaseSrv):
    """
    # 博客分类增删改查
    """

    @classmethod
    def add_classify(cls, name: str) -> None:
        """
        # 新增博客分类
        :param name: 分类名称
        """
        ClassifyDAO.insert_one(name)

    @classmethod
    def del_classify(cls, classify_id: int) -> None:
        """
        # 删除分类
        :param classify_id: 分类ID
        """
        ClassifyDAO.delete_one(classify_id)

    @classmethod
    def put_classify(cls, classify_id: int, name: str) -> None:
        """
        # 更新博客分类
        :param classify_id: 分类ID
        :param name: 分类名称
        """
        if not cls.get_name_exists(name):
            ClassifyDAO.update_one(classify_id, name=name)

    @classmethod
    def get_classify_list(cls) -> list:
        """
        # 获取分类列表
        :return: 分类列表
        """
        blog_type_data = [
            {
                "id": item["id"],
                "name": item["name"],
                "blog_count": item["blog_count"] if item["blog_count"] else 0,
                "create_time":item["create_time"].strftime('%Y-%m-%d %H:%M:%S'),
                "update_time": item["update_time"].strftime('%Y-%m-%d %H:%M:%S')
            } for item in ClassifyDAO.select_classify_list()
        ]
        return blog_type_data

    @classmethod
    def get_classify_blog_count(cls, classify_id: int) -> int:
        """
        # 查询该分类博客数量
        :param classify_id: 分类ID
        """
        return ClassifyDAO.select_classify_blog_count(classify_id)

    @classmethod
    def get_name_exists(cls, name: str) -> bool:
        """
        # 根据分类名称查询该分类是否存在
        :param name: 分类名称
        """
        return ClassifyDAO.select_name_exists(name)


