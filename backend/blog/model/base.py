#!/usr/bin/evn python3
# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.query import Query
from util.config import Config

__CONF = Config()


def all_data(self):
    """
    # 猴子补丁,增加Query对象all_data 方法返回字典
    """
    field = tuple([f["name"] for f in self.column_descriptions])
    all_info = self.all()
    result_data = []
    for item in all_info:
        result_data.append(dict(zip(field, item)))
    return result_data


setattr(Query, "all_data", all_data)

# 创建数据库连接引擎
engine = create_engine(
    __CONF.get_db_url(),
    echo=__CONF.get_conf("orm")["sql_echo"],
    pool_pre_ping=True
)
# 自己创建的model需要继承这个类
Base = declarative_base(engine)
# 数据库连接session
session = sessionmaker(engine)()


