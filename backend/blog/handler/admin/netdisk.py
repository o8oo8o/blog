#!/usr/bin/evn python3
# coding=utf-8

"""
# 网盘功能
"""

import os
import uuid
import pathlib
from urllib.parse import quote
from service.netdisk import NetDiskSrv
from handler.admin.base import BaseAdminHandler


class DirListHandler(BaseAdminHandler):
    """
    获取文件列表
    """
    async def get(self):
        dirname = self.get_argument_str("dirname", min_len=0, max_len=255, default="")
        search_file = self.get_argument_str("search_file", min_len=0, max_len=255, default="")
        if search_file:
            # 搜索文件
            data = NetDiskSrv.list_dir(dirname, search_file)
            self.send_json({"code": 0, **data})
        else:
            # 获取文件列表
            data = NetDiskSrv.list_dir(dirname)
            self.send_json({"code": 0, **data})


class DirTreeHandler(BaseAdminHandler):
    """
    # 树形展示目录结构
    """
    async def get(self):
        dirname = self.get_argument_str("dirname", min_len=0, max_len=255, default="")
        self.send_json({"code": 0, "data": NetDiskSrv.dir_tree(dirname, web_style=False)})


class NetDiskHandler(BaseAdminHandler):
    """
    网盘文件增删改查
    """

    async def send_file(self, path, filename: str):
        """
        # 发送文件到web客户端
        :param path: 文件路径
        :param filename: 文件名
        """
        self.set_header("Content-Type", "application/octet-stream")
        self.set_header("Content-Disposition", "attachment; filename="+quote(filename))
        # 不缓存
        self.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.set_header("Pragma", "no-cache")
        self.set_header("Expires", "0")
        self.set_header("Server", "httpd24")
        with open(path, 'rb') as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                self.write(data)
        await self.finish()

    async def download(self):
        """
        # 文件下载
        """
        file = self.get_argument_str("file", max_len=255)
        filename = str(os.path.basename(file))
        path = NetDiskSrv.get_base_dir() + file
        if os.path.isfile(path):
            await self.send_file(path, filename)

    async def file_write(self, dirname: str, file_metas):
        """
        # 文件写入磁盘
        :param dirname: 目录名称
        :param file_metas: 文件元数据
        """
        base_dir = NetDiskSrv.get_base_dir()
        for file in file_metas:
            filename = str(file["filename"])
            if dirname == "/":
                file_path = pathlib.Path(base_dir).joinpath(filename)
            else:
                file_path = pathlib.Path(base_dir).joinpath(dirname).joinpath(filename)
            if file_path.exists():
                # 如果文件存在,在源文件名称后面加上uuid
                tmp = file_path.stem + "__" + str(uuid.uuid4()).replace("-", "_") + file_path.suffix
                file_path = pathlib.Path(file_path.parent).joinpath(tmp)
            with open(str(file_path), "wb") as f:
                f.write(file["body"])
        self.send_json({"code": 0})

    async def upload(self):
        """
        # 文件上传
        """
        dirname = self.get_argument_str("dirname", min_len=0, max_len=255, default="/")
        file_metas = self.request.files.get('file', None)
        if file_metas:
            await self.file_write(dirname, file_metas)
        else:
            self.send_json({"code": 1})

    async def new_folder(self):
        """
        # 新建文件夹
        """
        base_dir = NetDiskSrv.get_base_dir()
        dirname = self.get_argument_str("dirname", min_len=0, max_len=255, default="/")
        folder_name = self.get_argument_str("folder_name", min_len=1, max_len=255)
        if dirname == "/":
            folder_path = pathlib.Path(base_dir).joinpath(folder_name)
        else:
            folder_path = pathlib.Path(base_dir).joinpath(dirname).joinpath(folder_name)

        if folder_path.exists():
            tmp = folder_path.stem + "__" + str(uuid.uuid4()).replace("-", "_") + folder_path.suffix
            folder_path = pathlib.Path(folder_path.parent).joinpath(tmp)
        folder_path.mkdir()
        self.send_json({"code": 0})

    async def delete_(self):
        """
        # 文件或目录删除
        """
        path = self.get_argument_str("path", min_len=1, max_len=255)
        if NetDiskSrv.remove(path):
            self.send_json({"code": 0})
            return
        self.send_json({"code": 1})

    async def rename(self):
        """
        # 文件或目录重命名
        """
        old_path = self.get_argument_str("old_path", min_len=1, max_len=255)
        new_path = self.get_argument_str("new_path", min_len=1, max_len=255)
        new_name = pathlib.Path(pathlib.Path(old_path).parent).joinpath(new_path)
        if NetDiskSrv.rename(old_path, new_name):
            self.send_json({"code": 0})
            return
        self.send_json({"code": 1})

    async def move(self):
        """
        # 文件或目录移动
        """
        from_path = self.get_argument_str("from_path", min_len=1, max_len=255)
        to_path = self.get_argument_str("to_path", min_len=1, max_len=255)
        if NetDiskSrv.move(from_path, to_path):
            self.send_json({"code": 0})
            return
        self.send_json({"code": 1})

    async def post(self):
        """
        # 这相当于是一个分发器,根据method字段调用对应的方法
        """
        method = self.get_argument_str("method", max_len=255)
        if hasattr(self, method):
            await getattr(self, method)()


