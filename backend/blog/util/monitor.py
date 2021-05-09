#!/usr/bin/evn python3
# coding=utf-8

import json
import time
import datetime
import psutil
from util.actuator import AbcActuator
from util.config import Config
from util.logger import AppLog


class Monitor(AbcActuator):
    """
    主机资源使用监控
    """

    def ready(self, *args, **kwargs) -> None:
        """
        # AbcActuator 的抽象方法，继承以后的具体实现
        """
        pass

    def exe(self) -> None:
        """
        # AbcActuator 的抽象方法，继承以后的具体实现
        """
        try:
            db = Config().get_redis()
            host_info = Monitor.all_info(2)
            db.set("host_info", json.dumps(host_info), ex=3600)
        except Exception as e:
            AppLog().logger.error(f"monitor_exe_error:{e}")

    @classmethod
    def cpu_info(cls, interval=0.5) -> dict:
        cpu = psutil.cpu_times_percent(interval=interval)
        '''
        user : 执行用户进程花费的时间
        system : 执行内核进程的时间
        idle : CPU处于空闲得时间
        '''
        cpu_data = {"user": cpu.user, "system": cpu.system, "idle": cpu.idle}
        return cpu_data

    @classmethod
    def mem_info(cls) -> dict:
        mem = psutil.virtual_memory()
        mem = {
            "total": round(mem.total / 1073741824, 2),
            "used": round(mem.used / 1073741824, 2),
            "free": round(mem.free / 1073741824, 2),
            "available": round(mem.available / 1073741824, 2),
            "percent": mem.percent
        }
        '''
        total:总的物理内存
        available:可用内存
        used:使用的内存
        free:空闲内存数
        percent:空闲百分比
        '''
        return mem

    @classmethod
    def disk_info(cls) -> list:
        disk = []
        for i in psutil.disk_partitions():
            part = psutil.disk_usage(i.mountpoint)
            disk.append({
                "mount": i.mountpoint,
                "total": round(part.total / 1000000000),
                "use": round(part.used / 1000000000),
                "percent": part.percent
            })
        return disk

    @classmethod
    def net_info(cls) -> dict:
        pass

        net = psutil.net_io_counters()
        """
        bytes_sent:发送的字节数
        bytes_recv:收到的字节数
        packets_sent:发送的数据包数量
        packets_recv:收到的数据包数量
        errin：接收时的错误数
        errout:发送时的错误数
        dropin:丢弃的传入数据包总数
        dropout：丢弃的传出数据包总数
        """
        net = {
            "bytes_sent": net.bytes_sent,
            "bytes_revc": net.bytes_recv,
            "packets_sent": net.packets_sent,
            "packets_recv": net.packets_recv,
            "errin": net.errin,
            "errout": net.errout,
            "dropin": net.dropin,
            "dropout": net.dropout
        }
        return net

    @classmethod
    def disk_io_info(cls) -> dict:
        disk = psutil.disk_io_counters(perdisk=False, nowrap=True)
        """
        read_count：读取次数
        write_count：写入次数
        read_bytes：读取的字节数
        write_bytes：写入的字节数
        read_time,
        write_time
        """
        disk = {
            "read_count": disk.read_count,
            "write_count": disk.write_count,
            "read_bytes": disk.read_bytes,
            "write_bytes": disk.write_bytes,
            "read_time": disk.read_time,
            "write_time": disk.write_time
        }
        return disk

    @classmethod
    def boot_info(cls) -> str:
        """
        # 开机时间
        :return:
        """
        boot_time = datetime.datetime.fromtimestamp(
            psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        return boot_time

    @classmethod
    def pids_info(cls) -> list:
        """
        # 进程信息
        :return:
        """
        pss = psutil.pids()
        pss.remove(0 if 0 in pss else 1)
        ps_info = []
        for pid in pss:
            try:
                p = psutil.Process(pid)
                ps_info.append({
                    "pid": pid,
                    "name": p.name(),
                    "exe": p.exe(),
                })
            except Exception as e:
                pass
        return ps_info

    @classmethod
    def all_info(cls, interval=0.5) -> dict:
        """
        # 获取所有信息
        :param interval:
        :return:
        """
        return {
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "boot": cls.boot_info(),
            "cpu": cls.cpu_info(interval=interval),
            "mem": cls.mem_info(),
            "disk": cls.disk_info(),
            "disk_io": cls.disk_io_info(),
            "net": cls.net_info(),
            # "ps": cls.pids_info() # 进程信息
        }


