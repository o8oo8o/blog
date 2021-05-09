#!/usr/bin/evn python3
# coding=utf-8

import time
import pickle
import multiprocessing as mp
from multiprocessing import Process
from multiprocessing import Queue
from util import singleton
from util.exception import AppException
from util.actuator import AbcActuator
from util.logger import AppLog


# 在3.7 不需要设置启动方法,但是到3.8 就不行了,官方文档有说明
# https://docs.python.org/zh-cn/3/library/multiprocessing.html
mp.set_start_method("fork")


@singleton
class Guard(Process):
    """
    # 守护进程,根据执行队列注册的对象(AbcActuator)执行
    """

    def __init__(self) -> None:
        super().__init__()
        # 任务队列
        self.__task_queue = Queue(100)
        # 启动次数
        self.__start_count = 0

    def run(self) -> None:
        """
        # 取出队列里面的对象,执行对象的exe方法
        """
        while True:
            try:
                # 从执行队列获取数据
                if not self.__task_queue.empty():
                    data = self.__task_queue.get(timeout=0.25)
                    task = pickle.loads(data)
                    task.exe()
                # 防止CPU利用率100%
                time.sleep(0.25)
            except AppException as exp:
                AppLog().get_logger().error(f"guard_except:{exp}")

    def register(self, task: AbcActuator) -> None:
        """
        # 注册一个对象到任务队列里面
        :param task:
        :return:
        """
        if isinstance(task, AbcActuator):
            self.__task_queue.put(pickle.dumps(task))

    def get_run_guard(self) -> "Guard":
        """
        # 启动进程,并返回自身
        :return:
        """
        if self.__start_count == 0:
            # 只能启动一次,也就是限制进程只能start一次
            self.__start_count += 1
            self.start()
        return self


if __name__ == '__main__':
    # 测试代码
    aa = Guard().get_run_guard()
    bb = Guard().get_run_guard()
    cc = Guard().get_run_guard()
    print(id(aa))
    print(id(bb))
    print(id(cc))


