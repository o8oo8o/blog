#!/usr/bin/evn python3
# coding=utf-8

from dao.resume import ResumeDAO
from service.base import BaseSrv


class ResumeSrv(BaseSrv):
    """
    # 简历增删改查
    """

    @classmethod
    def add_resume(cls, title: str, text: str) -> None:
        """
        # 添加简历
        :param title: 简历标题
        :param text: 简历内容
        """
        return ResumeDAO.insert_one(title, text)

    @classmethod
    def del_resume(cls, resume_id: int) -> None:
        """
        # 删除简历
        :param resume_id: 简历ID,数据库主键
        """
        ResumeDAO.delete_one(resume_id)

    @classmethod
    def put_resume(cls, resume_id: int, **kwargs) -> None:
        """
        # 更新简历
        :param resume_id: 简历ID,数据库主键
        :param kwargs: 简历数据
        """
        ResumeDAO.update_one(resume_id, **kwargs)

    @classmethod
    def get_resume(cls, resume_id: int) -> dict:
        """
        # 根据简历ID获取简历
        :param resume_id: 简历ID
        :return: 简历数据字典
        """
        resume = ResumeDAO.select_one(resume_id)
        if resume:
            resume_data = {
                "id": resume.id,
                "title": resume.title,
                "text": resume.text,
                "create_time": resume.create_time,
                "update_time": resume.update_time
            }
            return resume_data

    @classmethod
    def get_title_exists(cls, title: str) -> bool:
        """
        # 检查该标题的简历是否存在
        :param title: 简历标题
        :return: 布尔值 True-> 存在,  False->不存在
        """
        return ResumeDAO.select_title_exists(title)

    @classmethod
    def get_resume_list(cls) -> list:
        """
        # 获取简历列表
        :return: 简历列表
        """
        resume_list = [
            {
                "id": item.id,
                "title": item.title,
                "publish_count": len(item.publish),
                "create_time": item.create_time,
                "update_time": item.update_time
            } for item in ResumeDAO.select_all()
        ]
        return resume_list


