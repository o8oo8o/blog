#!/usr/bin/evn python3
# coding=utf-8

from handler.open.base import WebBaseHandler
from service.setting import SettingSrv
from service.netdisk import NetDiskSrv


class MusicHandler(WebBaseHandler):

    async def get(self):
        """
        # 获取音乐列表
        """

        music_conf = self.conf.get_conf("music")
        setting = SettingSrv.get_setting()
        files = NetDiskSrv.list_dir(setting["music_dir"])
        music_list = []
        for item in files["list"]:
            if str(item["name"])[-4:] in music_conf["type"]:
                music_list.append({
                    "name": str(item["name"])[0:-4],
                    "path": item["path"]
                })
        self.send_json({"code": 0, "count": len(music_list), "music_list": music_list})


