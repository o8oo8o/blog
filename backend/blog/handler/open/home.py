#!/usr/bin/evn python3
# coding=utf-8

from handler.open.base import WebBaseHandler
from service.home import HomeSrv


class HomeHandler(WebBaseHandler):

    async def get(self):
        """
        获取主页加载数据
        """
        home_init_data = HomeSrv.get_home_init_data()
        self.send_json(home_init_data)


