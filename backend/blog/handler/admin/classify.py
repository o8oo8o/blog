#!/usr/bin/evn python3
# coding=utf-8

from service.classify import ClassifySrv
from handler.admin.base import BaseAdminHandler


class ClassifyHandler(BaseAdminHandler):
    """
    博客分类增删改查
    """
    async def get(self):
        """
        # 获取分类列表,没有按照套路来,因为分类数据太简单了
        """
        classify_list = ClassifySrv.get_classify_list()
        self.send_json({"code": 0, "classify_list": classify_list})

    async def put(self):
        """
        # 更新分类
        """
        classify_id = self.get_argument_int("classify_id")
        name = self.get_argument_str("name", max_len=127)
        ClassifySrv.put_classify(classify_id, name)
        await self.get()

    async def post(self):
        """
        # 新增分类
        """
        name = self.get_argument_str("name", max_len=127)
        ClassifySrv.add_classify(name)
        await self.get()

    async def delete(self):
        """
        # 删除分类
        """
        classify_id = self.get_argument_int('classify_id')
        ClassifySrv.del_classify(classify_id)
        await self.get()


