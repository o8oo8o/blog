#!/usr/bin/evn python3
# coding=utf-8

from service.base import BaseSrv
from dao.chat import ChatDAO


class ChatSrv(BaseSrv):

    @classmethod
    def add_chat(cls, ip: str, agent: str, msg: str) -> None:
        """
        # 添加聊天记录
        :param ip: IP地址
        :param agent: 用户agent
        :param msg: 消息内容,把长于65000的消息截取一下
        """
        ChatDAO.insert_one(ip, agent, msg[:65000])


