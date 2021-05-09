#!/usr/bin/evn python3
# coding=utf-8

import time
import json
import logging
from service.chat import ChatSrv
from handler.base import BaseWebSocketHandler
from util.exception import AppException


class ChatHandler(BaseWebSocketHandler):
    """
    open 聊天功能
    """
    online_count = 0
    clients = set()
    cache = []
    cache_size = 200

    async def open(self):
        try:
            ChatHandler.online_count += 1
            ChatHandler.clients.add(self)
            data = {
                "online": ChatHandler.online_count,
                "msg": {
                    "uid": "管理员",
                    "msg": "新用户进入聊天室",
                    "img": "img/chat/admin.png",
                    "time": time.strftime('%X')
                }
            }
            self.send_updates(data)
        except Exception as e:
            self.logger.error(f"chat_open_error:{e}")

    def on_close(self):
        """
        # 关闭连接的时候,减少在线人数
        :return:
        """
        try:
            self.close(reason="char_close")
            ChatHandler.online_count -= 1
            ChatHandler.clients.remove(self)
        except Exception as e:
            self.logger.error(f"chat_close_error:{e}")

    @classmethod
    def update_cache(cls, message):
        """
        # 更新缓存
        :param message: 消息数据
        """
        cls.cache.append(message)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]

    @classmethod
    def send_updates(cls, message):
        """
        # 发送每个新消息到在线的客户端
        :param message:
        """
        for client in cls.clients:
            try:
                client.write_message(message)
            except AppException as e:
                logging.error(str(e.args), exc_info=True)

    async def on_message(self, message):
        try:
            msg = json.loads(message)
            msg_data = json.dumps({
                "online": ChatHandler.online_count,
                "msg": msg
            })
            ChatHandler.update_cache(msg_data)
            ChatHandler.send_updates(msg_data)
            # 记录聊天记录
            ChatSrv.add_chat(
                ip=self.get_remote_ip(),
                agent=self.get_user_agent(),
                msg=msg["msg"]
            )
        except Exception as e:
            self.logger.error(f"chat_message_error:{e}")


