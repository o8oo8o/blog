#!/usr/bin/evn python3
# coding=utf-8

import os
import uuid
from service.setting import SettingSrv
from handler.admin.base import BaseAdminHandler


class UploadHandler(BaseAdminHandler):
    """
    # 头像、Logo、编辑器图片、上传处理
    """

    async def post(self):
        """
        # 上传头像或logo
        :return: 图片线上可访问地址
        """
        upload_path = self.application.settings.get("upload_path")
        files = self.request.files.get('files', None)
        user_id = self.get_argument_int("id", default="0")
        handle_type = self.get_argument_str("handle_type")
        if not files:
            self.send_json({"code": 1})
            return

        filename = files[0]["filename"]

        new_filename = str(uuid.uuid4()).replace("-", "_") + os.path.splitext(filename)[1]

        file_path = os.path.join(upload_path, new_filename)

        with open(file_path, "wb+") as up:
            up.write(files[0]['body'])

        data = "img/upload/" + new_filename

        if handle_type == "logo":
            update = {"logo_path": data}
            SettingSrv.put_setting(user_id, data=update)
        if handle_type == "icon":
            update = {"icon_path": data}
            SettingSrv.put_setting(user_id, data=update)
        self.send_json({"code": 0, "data": data})


