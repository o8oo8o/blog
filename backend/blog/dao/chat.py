#!/usr/bin/evn python3
# coding=utf-8

from model.model import Chat
from dao.base import BaseDAO


class ChatDAO(BaseDAO):

    @classmethod
    def insert_one(cls, ip: str, agent: str, msg: str) -> None:
        """
        # 插入聊天记录
        :param ip: IP地址
        :param agent: 用户agent
        :param msg: 消息内容
        """
        cls.db_session.add(Chat(ip, agent, msg))


