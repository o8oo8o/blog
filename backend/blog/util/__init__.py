#!/usr/bin/evn python3
# coding=utf-8


def singleton(cls):
    """
    # class单例装饰器
    """
    instance = {}

    def func(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return func


