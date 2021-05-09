#!/usr/bin/evn python3
# coding=utf-8

import os
import time
import glob
import shutil
from pathlib import Path
from service.base import BaseSrv
from util.config import ConfigMixIn


class NetDiskSrv(BaseSrv, ConfigMixIn):
    """
    # 网盘功能
    """

    @classmethod
    def get_base_dir(cls) -> str:
        """
        # 获得网盘的根目录,如果不是/结尾,加上/
        """
        dir_path = str(cls.conf.get_conf("net_disk")["base_dir"])
        if dir_path.endswith("/"):
            return dir_path
        return dir_path + "/"

    @classmethod
    def __del_startswith(cls, path: str) -> str:
        if path.startswith("/", 0, 1):
            path = path.replace("/", "", 1)
        return os.path.join(cls.get_base_dir(), path)

    @classmethod
    def list_dir(cls, dirname: str = "", search_file: str = "") -> dict:
        """
        # 目录列表获取或文件目录搜索
        :param dirname: 目录名称
        :param search_file: 搜索文件名称
        """
        base_dir = cls.get_base_dir()
        dirname = cls.__del_startswith(dirname)
        data = {"f_count": 0, "d_count": 0, "list": []}
        if not os.path.isdir(dirname):
            return data
        for root, dirs, files in os.walk(dirname):
            for name in files:
                stat = os.stat(os.path.join(root, name))
                file_info = {
                    "name": name,
                    "type": "file",
                    "size": stat.st_size,
                    "mtime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stat.st_mtime)),
                    "path": os.path.join(root, name).replace(base_dir, "", 1),
                }
                if search_file:
                    if search_file in name:
                        data["f_count"] += 1
                        data["list"].append(file_info)
                    continue
                data["f_count"] += 1
                data["list"].append(file_info)
            for name in dirs:
                dir_path = os.path.join(root, name)
                mtime = os.path.getmtime(dir_path)
                dir_info = {
                    "name": name,
                    "type": "dir",
                    "size": len(glob.glob(dir_path+"/*")),
                    "mtime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mtime)),
                    "path": os.path.join(root, name).replace(base_dir, "", 1),
                }
                if search_file:
                    if search_file in name:
                        data["d_count"] += 1
                        data["list"].append(dir_info)
                    continue
                data["d_count"] += 1
                data["list"].append(dir_info)
            if not search_file:
                return data
        return data

    @classmethod
    def remove(cls, path) -> bool:
        """
        # 文件或目录删除
        :param path: 删除的路径
        :return True 删除成功, False 删除失败
        """
        base_dir = cls.get_base_dir()
        path = os.path.join(base_dir, path)
        if not os.path.exists(path):
            return False
        if os.path.isdir(path):
            shutil.rmtree(path)
        if os.path.isfile(path):
            os.remove(path)
        return True

    @classmethod
    def move(cls, src, dst) -> bool:
        """
        # 文件或目录移动
        :param src: 源路径
        :param dst: 目的路径
        :return True 移动成功, False 移动失败
        """
        base_dir = cls.get_base_dir()
        src = Path(base_dir).joinpath(src)
        dst = Path(base_dir).joinpath(dst)
        if str(src.parent) == str(dst):
            return False

        if Path(dst).joinpath(src.name).exists():
            # 目标文件夹存在相同的文件名称
            return False
        if src.exists() and dst.is_dir():
            shutil.move(str(src), str(dst))
            return True
        return False

    @classmethod
    def rename(cls, src, dst) -> bool:
        """
        # 文件或目录重命名
        :param src: 源路径
        :param dst: 目的路径
        :return:  True 重命名成功, False 重命名失败
        """
        base_dir = cls.get_base_dir()
        src = os.path.join(base_dir, src)
        dst = os.path.join(base_dir, dst)
        if src == dst:
            # 源和目标一样直接返回
            return True
        if not os.path.exists(src):
            return False
        if os.path.exists(dst):
            return False
        shutil.move(src, dst)
        return True

    @classmethod
    def copy(cls, src, dst) -> bool:
        """
        # 复制文件或目录
        :param src: 源路径
        :param dst: 目的路径
        :return: True 复制成功, False 复制失败
        """
        base_dir = cls.get_base_dir()
        src = os.path.join(base_dir, src)
        dst = os.path.join(base_dir, dst)
        if not os.path.exists(src):
            # 源名称存在, 直接返回
            return False
        if os.path.exists(dst):
            # 目标名称存在,直接返回
            return False
        if os.path.isfile(src):
            # 复制文件
            shutil.copy(src, dst)
            return True
        shutil.copytree(src, dst)
        return True

    @classmethod
    def copy_link(cls, src, dst) -> bool:
        """
        # 链接方式复制
        :param src: 源路径
        :param dst: 目的路径
        :return: True 链接复制成功, False 链接复制失败
        """
        base_dir: str = cls.get_base_dir()
        src = os.path.join(base_dir, src)
        dst = os.path.join(base_dir, dst)
        if not os.path.exists(src):
            # 源名称存在, 直接返回
            return False
        if os.path.exists(dst):
            # 目标名称存在,直接返回
            return False
        if os.path.isfile(src):
            # 复制文件
            os.link(src, dst)
            return True
        if not os.path.exists(os.path.dirname(dst)):
            os.makedirs(os.path.dirname(dst))
        os.symlink(src, dst)
        return True

    @classmethod
    def dir_tree(cls, path: str = "", web_style: bool = False) -> str:
        """
        # 生成目录树字符串
        :param path:
        :param web_style: html样式,方便前端使用,如果为False,前端可以使用替换字符串方式完成:
        let str = String(data).replace(new RegExp("\n", "gm"), "<br>").\
            replace(new RegExp(" ", "gm"),"&nbsp;&nbsp;")
        :return: 目录树字符串
        """
        path = Path(cls.__del_startswith(path))
        tree_str = ""

        def gen_tree(path_obj, n=0) -> str:
            """
            生成树结构
            :param path_obj: 路径
            :param n: 目录深度,因为下来是递归调用
            """
            nonlocal tree_str
            if path_obj.is_file():
                if web_style:
                    tree_str += "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|" * n + \
                                "----" + str("&nbsp;&nbsp;" + path_obj.name) + '\n'
                else:
                    tree_str += "    |" * n + "----" + str(" " + path_obj.name) + '\n'
            elif path_obj.is_dir():
                if web_style:
                    tree_str += "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|" * n + \
                                "----" + str("&nbsp;&nbsp;" + path_obj.relative_to(path_obj.parent).name)\
                                + '/' + '\n'
                else:
                    tree_str += "    |" * n + "----" + \
                                str(" " + path_obj.relative_to(path_obj.parent).name) + '/' + '\n'
                for item in path_obj.iterdir():
                    gen_tree(item, n + 1)
            return tree_str
        return gen_tree(path)


