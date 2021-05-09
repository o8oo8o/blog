#!/usr/bin/evn python3
# coding=utf-8

import paramiko
from paramiko import SSHClient
from dao.setting import SettingDAO
from service.base import BaseSrv
from util.exception import AppException


class SSHSrv(BaseSrv):
    """
    # 提供ssh服务
    """

    @classmethod
    def get_ssh_connect(cls) -> tuple:
        """
        # 完成SSH连接
        :return: (SSHClient, SSH连接通道)
        """
        conf = cls.get_ssh_setting()
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(conf["host"], conf["port"], conf["user"], conf["pwd"], timeout=15)
        except paramiko.SSHException as e:
            AppException(str(e))
        else:
            chan = ssh.invoke_shell(
                term="xterm-256color",
                width=conf["width"],
                height=conf["height"]
            )
            chan.setblocking(0)
            return ssh, chan

    @classmethod
    def get_ssh_setting(cls) -> dict:
        """
        # 获取ssh配置信息
        """
        tmp = SettingDAO.select_setting()
        conf = {
            "host": tmp["ssh_host"],
            "port": int(tmp["ssh_port"]),
            "user": tmp["ssh_user"],
            "pwd": tmp["ssh_pwd"],
            "width": int(tmp["ssh_width"]),
            "height": int(tmp["ssh_height"])
        }
        return conf


