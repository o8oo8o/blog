#!/usr/bin/evn python3
# coding=utf-8

import time
from util.config import Config


class Acl:
    """
    # 这是一个单例对象,为啥没用单例装饰器,因为想换一个方法
    # ACL控制用户访问,根据IP地址做访问控制
    # 在两个地方使用:后台登陆,访问码登陆
    """
    __instance = None
    __isFirstInstance = False

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not Acl.__isFirstInstance:
            conf = Config().get_conf("login")
            self.timeout = conf.get("timeout")
            self.max_try_count = conf.get("max_try_count")
            self.acl = {}
            Acl.__isFirstInstance = True

    def add_try_count(self, ip_address: str) -> None:
        """
        # 增加密码错误尝试次数,并且把尝试次数达到上限到加入到acl过滤列表
        :param ip_address:  IP地址(字符串)
        """
        now_time = int(time.time())
        if ip_address in self.acl:
            self.acl[ip_address]["try_count"] += 1
            if self.acl[ip_address]["try_count"] >= self.max_try_count:
                self.acl[ip_address]["timeout"] = now_time + self.timeout
        else:
            self.acl[ip_address] = {
                "try_count": 1,
                "timeout": now_time + self.timeout
            }

    def is_permit(self, ip_address: str) -> bool:
        """
        # 查询IP地址是否允许访问
        :param ip_address: IP地址(字符串)
        :return: 是否允许访问
        """
        expire_list = []
        current_time = int(time.time())
        for key, item in self.acl.items():
            if item["timeout"] < current_time:
                expire_list.append(key)
        [self.acl.pop(item) for item in expire_list]

        if ip_address not in self.acl:
            return True
        if self.acl[ip_address]["try_count"] < self.max_try_count:
            return True
        return False


