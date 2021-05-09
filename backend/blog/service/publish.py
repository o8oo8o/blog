#!/usr/bin/evn python3
# coding=utf-8

import math
from datetime import datetime
from dao.publish import PublishDAO
from dao.setting import SettingDAO
from service.base import BaseSrv


class PublishSrv(BaseSrv):
    """
    # 对简历发布表增删改查
    """

    @classmethod
    def add_publish(
            cls,
            resume_id: int,
            receiver: str,
            access_code: str,
            exp_time: datetime
    ) -> None:
        """
        # 新增一个简历发布
        :param resume_id: 简历ID
        :param receiver: 简历接收者
        :param access_code: 前台简历访问吗
        :param exp_time: 过期时间
        """
        PublishDAO.insert_one(
            resume_id=resume_id,
            receiver=receiver,
            access_code=access_code,
            exp_time=exp_time
        )

    @classmethod
    def del_publish(cls, publish_id: int) -> None:
        """
        # 删除一个简历发布
        :param publish_id: 发布ID
        """
        PublishDAO.delete_one(publish_id)

    @classmethod
    def put_publish(cls, publish_id: int, **kwargs) -> None:
        """
        # 更新一个简历发布
        :param publish_id: 发布ID
        :param kwargs:
            更新字段
            resume_id=resume_id,
            receiver=receiver,
            access_code=access_code,
            exp_time=exp_time
        """
        PublishDAO.update_one(publish_id, **kwargs)

    @classmethod
    def get_publish(cls, publish_id: int) -> dict:
        """
        # 获取一个简历发布
        :param publish_id: 发布ID,数据库中的主键
        """
        publish = PublishDAO.select_one(publish_id)
        if publish:
            publish_data = {
                "id": publish.id,
                "access_code": publish.access_code,
                "resume_id": publish.resume_id,
                "resume_title": publish.resume.title,
                "receiver": publish.receiver,
                "exp_time": publish.exp_time,
                "read_count": publish.read_count,
                "read_time": publish.read_time,
                "read_duration": publish.read_duration,
                "create_time": publish.create_time,
                "update_time": publish.update_time
            }
            return publish_data

    @classmethod
    def get_published_resume(cls, access_code: str) -> dict:
        """
        # 前台通过访问码查看简历
        :param access_code:
        :return: 返回是简历的数据,字典类型
        """
        resume = PublishDAO.select_publish(access_code)
        if resume:
            return resume[0]
        return {}

    @classmethod
    def get_access_code_exists(cls, access_code: str) -> bool:
        """
        # 查询访问码是否存在AJAX请求使用
        :param access_code: 访问码
        """
        return PublishDAO.select_access_code_exists(access_code)

    @classmethod
    def get_publish_list(cls, page=1, receiver_like: str = "") -> tuple:
        """
        # 获取简历发布列表
        :param page: 页码
        :param receiver_like: 简历接收者
        """
        page_size = SettingDAO.select_setting()["admin_publish_pz"]
        all_publish: list = PublishDAO.select_all(receiver_like)
        max_page = math.ceil(len(all_publish) / page_size)
        page = max_page if page > max_page else page
        page = 1 if page == 0 else page
        if page == 1:
            start = 0
            end = page_size
        else:
            start = (page-1) * page_size
            end = start + page_size

        publish_list = [
            {
                "id": item["id"],
                "access_code": item["access_code"],
                "resume_id": item["resume_id"],
                "resume_title":item["title"],
                "receiver": item["receiver"],
                "exp_time": item["exp_time"],
                "read_count": item["read_count"],
                "read_duration":item["read_duration"],
                "read_time":item["read_time"],
                "create_time":item["create_time"],
                "update_time":item["update_time"]
            } for item in all_publish[start:end]
        ]

        return max_page, publish_list


