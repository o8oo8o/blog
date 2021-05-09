#!/usr/bin/evn python3
# coding=utf-8

from service.dashboard import DashboardSrv
from handler.admin.base import BaseAdminHandler


class DashboardHandler(BaseAdminHandler):
    """
    # 后台管理首页仪表盘
    """
    async def get(self):
        """
        # 获取 Dashboard 数据
        """
        dashboard_data = DashboardSrv.get_dashboard_data()
        self.send_json({"code": 0, "data": dashboard_data})


