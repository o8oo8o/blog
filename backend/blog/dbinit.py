#!/usr/bin/evn python3
# coding=utf-8

"""
# 第一次部署的时候需要对数据库初始化,执行此脚步
"""


import os
import sys

sys.path.append(".")
sys.path.append(os.path.dirname(__file__))


def db_init() -> None:
    """
    # 执行数据库初始化
    """
    from model.base import Base
    from model.base import session
    from model.model import Setting

    Base.metadata.drop_all()
    Base.metadata.create_all()
    session.add(Setting())
    session.commit()


if __name__ == '__main__':
    db_init()


