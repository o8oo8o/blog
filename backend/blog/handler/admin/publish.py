#!/usr/bin/evn python3
# coding=utf-8

from handler.admin.base import BaseAdminHandler
from service.publish import PublishSrv


class PublishListHandler(BaseAdminHandler):
    async def get(self):
        """
        # 根据分页查询blog
        :return: 返回 blog 列表
        """
        await self._get_publish_list()

    async def _get_publish_list(self):
        """
        # 根据分页和搜索内容显示博客列表
        :return:
        """
        page = self.get_argument_int("page", default="1")
        receiver_like = self.get_argument_str(
            "receiver_like", min_len=0, max_len=127, default=""
        )

        def response(request, max_page, publish_list):
            request.send_json({
                "code": 0, "max_page": max_page, "publish_list": publish_list
            })

        if receiver_like == "":
            response(self, *PublishSrv.get_publish_list(page))
        else:
            response(self, *PublishSrv.get_publish_list(page, receiver_like))


class PublishAccessCodeCheckHandler(BaseAdminHandler):
    """
    # 检查访问码否存在
    """
    async def get(self):
        """
        # 检查blog标题是否存在,前端通过AJAX发送请求检查
        :return:
        """
        access_code = self.get_argument_str("access_code", 0, 127, default="")
        is_exists = PublishSrv.get_access_code_exists(access_code)
        self.send_json({"code": 0, "is_exists": is_exists})


class PublishHandler(PublishListHandler):
    """
    # 简历发布增删改查
    """

    async def get(self):
        """
        # 获取一个发布
        """
        publish_id = self.get_argument_int("publish_id")
        self.send_json({"code": 0, **PublishSrv.get_publish(publish_id)})

    async def post(self):
        """
        # 增加一个发布
        """
        resume_id = self.get_argument_int("resume_id")
        receiver = self.get_argument_str("receiver", max_len=127)
        access_code = self.get_argument_str("access_code", min_len=4, max_len=127)
        exp_time = self.get_argument_datetime("exp_time")
        PublishSrv.add_publish(resume_id, receiver, access_code, exp_time)
        await self._get_publish_list()

    async def put(self):
        """
        # 更新一个发布
        """
        publish_id = self.get_argument_int("publish_id")
        resume_id = self.get_argument_int("resume_id")
        receiver = self.get_argument_str("receiver", max_len=127)
        access_code = self.get_argument_str("access_code", max_len=127)
        exp_time = self.get_argument_datetime("exp_time")
        PublishSrv.put_publish(
            publish_id=publish_id,
            resume_id=resume_id,
            receiver=receiver,
            access_code=access_code,
            exp_time=exp_time
        )
        await self._get_publish_list()

    async def delete(self):
        """
        # 删除一个发布
        """
        publish_id = self.get_argument_int("publish_id")
        PublishSrv.del_publish(publish_id)
        await self._get_publish_list()


