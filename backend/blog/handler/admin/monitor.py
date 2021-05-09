#!/usr/bin/evn python3
# coding=utf-8

import json
from handler.admin.base import BaseAdminHandler
from util.monitor import Monitor


class MonitorHandler(BaseAdminHandler):
    """
    # 主机监控
    """

    async def get(self):
        """
        获取主机性能数据
        :return:
        """
        # 第一次获取的时候,默认数据
        default_info = {
            "time": "2000-01-01 01:01:01",
            "boot": "2000-01-01 01:01:01",
            "cpu": {
                "user": 0,
                "system": 0,
                "idle": 0
            },
            "mem": {
                "total": 0,
                "used": 0,
                "free": 0,
                "available": 0,
                "percent": 0
            },
            "disk": [],
            "disk_io": {
                "read_count": 0,
                "write_count": 0,
                "read_bytes": 0,
                "write_bytes": 0,
                "read_time": 0,
                "write_time": 0
            },
            "net": {
                "bytes_sent": 0,
                "bytes_revc": 0,
                "packets_sent": 0,
                "packets_recv": 0,
                "errin": 0,
                "errout": 0,
                "dropin": 0,
                "dropout": 0
            }
        }
        # guard 是一个守护进程
        self.guard.register(Monitor())
        db = self.conf.get_redis()
        data = db.get("host_info")
        if data:
            host_info = json.loads(data.decode("utf-8"))
        else:
            host_info = default_info
        result_data = {"code": 0, "data": host_info}
        self.send_json(result_data)


