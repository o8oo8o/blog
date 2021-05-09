#!/usr/bin/evn python3
# coding=utf-8

import logging
import redis
from typing import Any
from conf import dev_conf as conf
from util import singleton


@singleton
class Config:
    """
    根据指定的配置文件，把conf文件转换成字典
    默认情况下使用 conf 中的配置
    """

    def __init__(self):
        self.config = conf
        self.redis_db = None

    def get_dict(self, exclude: str = "__") -> dict:
        """
        把配置文件的内容转换成字典，默认情况下会忽略配置文件中以 '__xxx' 开头的配置项
        :param exclude:
        :return: dict
        """
        config_data = {}
        for key in dir(self.config):
            if not str(key).startswith(exclude):
                config_data[key] = getattr(self.config, key)
        return config_data

    def get_conf(self, key_name: str) -> Any:
        """
        获取单个配置值
        :param key_name:
        :return:
        """
        all_config = self.get_dict()
        return all_config[key_name]

    def get_db_url(self, db_role="master", db_name="default") -> str:
        """
        # 获取MySQL 连接字符串
        :param db_role:
        :param db_name:
        :return:
        """
        try:
            db_config = self.get_conf("mysql").get(db_role).get(db_name)
        except AttributeError as error_info:
            logging.error(f"Config: {error_info} Key!")
        else:
            tmp = "mysql+pymysql://{username}:{password}@{hostname}:" + \
                  "{port}/{database}?charset={charset}"
            db_url = tmp.format(**db_config)
            return db_url

    def get_redis(self, db_role="master", db_name="default") -> redis.Redis:
        """
        # 获取redis 配置
        :param db_role:
        :param db_name:
        :return:
        """
        if self.redis_db:
            return self.redis_db
        try:
            db_conf = self.get_conf("redis").get(db_role).get(db_name)
            pool = redis.ConnectionPool(
                host=db_conf["host"],
                port=db_conf["port"],
                db=db_conf["db"]
            )
            self.redis_db = redis.Redis(connection_pool=pool)
        except AttributeError as db_exp:
            logging.error(f"get_redis_error:{db_exp}")
        else:
            return self.redis_db


class ConfigMixIn:
    """
    方便其它类混入使用
    """
    conf = Config()


if __name__ == '__main__':
    a = Config()
    b = Config()
    print(id(a))
    print(id(b))

    c = a.get_redis()
    d = b.get_redis()
    print(id(c))
    print(id(d))
    c.set("ka", "va")


