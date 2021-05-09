#!/usr/bin/evn python3
# coding=utf-8

from handler.admin.base import BaseAdminHandler
from service.resume import ResumeSrv


class ResumeListHandler(BaseAdminHandler):
    """
    获取简历列表
    """
    async def get(self):
        """
        :return: 返回简历列表
        """
        await self._get_resume_list()

    async def _get_resume_list(self):
        """
        # 获取简历列表
        """
        data = ResumeSrv.get_resume_list()
        self.send_json({"code": 0, "resume_list": data})


class ResumeTitleCheckHandler(BaseAdminHandler):
    """
    检查简历标题是否存在
    """
    async def get(self):
        """
        # 检查简历标题是否存在,前端通过AJAX发送请求检查
        """
        title = self.get_argument_str("title", 0, 127, default="")
        is_exists = ResumeSrv.get_title_exists(title)
        self.send_json({"code": 0, "is_exists": is_exists})


class ResumeHandler(ResumeListHandler):
    """
    简历增删改查
    """
    async def get(self):
        """
        # 获取一个简历
        """
        resume_id = self.get_argument_int("resume_id")
        result_data = {"code": 0, "resume": ResumeSrv.get_resume(resume_id)}
        self.send_json(result_data)

    async def post(self):
        """
        # 增加一个简历
        """
        title = self.get_argument_str("title", max_len=127)
        text = self.get_argument_str("text", max_len=4294967295)
        ResumeSrv.add_resume(title, text)
        await self._get_resume_list()

    async def put(self):
        """
        # 更新一个简历
        """
        resume_id = self.get_argument_int("resume_id")
        title = self.get_argument_str("title", max_len=127)
        text = self.get_argument_str("text", max_len=4294967295)
        ResumeSrv.put_resume(resume_id, title=title, text=text)
        await self._get_resume_list()

    async def delete(self):
        """
        # 删除一个简历
        """
        resume_id = self.get_argument_int("resume_id")
        ResumeSrv.del_resume(resume_id)
        await self._get_resume_list()


