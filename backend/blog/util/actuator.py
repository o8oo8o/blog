#!/usr/bin/evn python3
# coding=utf-8

import abc


class AbcActuator(metaclass=abc.ABCMeta):
    """
    # 执行器抽象类,向 Guard 注册的对象必须实现下面两个方法
    """

    @abc.abstractmethod
    def ready(self, *args, **kwargs) -> None:
        # 准备功能
        ...

    @abc.abstractmethod
    def exe(self) -> None:
        # 执行功能
        ...


