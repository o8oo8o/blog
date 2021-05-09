#!/usr/bin/evn python3
# coding=utf-8

import time
import uuid
import hashlib
from util.config import Config
from util import singleton


@singleton
class Backend:
    """
    # session后端存储redis实现
    """

    def __init__(self):
        self.db = Config().get_redis()

    def getitem(self, name: str, key: str) -> str:
        """
        # 根据指定的字典名字和key获取字典的值
        :param name: 字典的名字
        :param key: 字典的字段
        :return: 字典指定字段的字符串值
        """
        data = self.db.hgetall(name)
        result = {}
        for key_name, item in data.items():
            result.setdefault(key_name.decode("utf-8"), item.decode("utf-8"))
        return result.get(key, "")

    def setitem(self, name: str, key: str, value: str, expires: int = None) -> None:
        """
        # 根据 设置字典字段的值
        :param name: 字典名字
        :param key: 字典字段
        :param value: 设置的值
        :param expires: 过期时间
        """
        self.db.hset(name, key, str(value))
        if expires:
            self.db.expire(name, expires)
        else:
            self.db.expire(name, 3600)

    def delete(self, name: str, key: str) -> None:
        """
        # 删除字典指定的字段
        :param name: 字典名字
        :param key: 字典字段
        """
        self.db.hdel(name, key)

    def clean(self, key: str) -> None:
        """
        # 删除指定的字典
        :param key: 字典名
        """
        self.db.delete(key)

    def expires(self, name: str, expires: int) -> None:
        """
        # 设置字典的过期
        :param name: 字典名
        :param expires: 过期时间(秒)
        """
        self.db.expire(name, expires)


class Session(dict):
    """
    会话对象
    """

    def __init__(self, request, backend, **kwargs) -> None:
        super().__init__()
        # 获取session 的相关配置
        cnf = Config().get_conf("session")
        self._request = request
        self._backend = backend
        self._name = cnf["name"]
        self._domain = cnf["domain"]
        self._path = cnf["path"]
        self._expires = cnf["expires"]

        self._session_id = request.get_cookie(cnf["name"], None)
        if not self._session_id:
            self._session_id = self.gen_session_id()

        rem = backend.getitem(self._session_id, "rem")
        if rem == "yes":
            # 用户勾选记住我的时候
            self._expires = cnf["rem_session_exp"]
        self.set_expires(self._expires)

    def __getitem__(self, key: str) -> str:
        """
        # 获取session的值
        :param key:
        """
        return self._backend.getitem(self._session_id, key)

    def __delitem__(self, key) -> None:
        """
        # 删除session
        :param key:
        :return:
        """
        self._backend.delete(self._session_id, key)

    def __setitem__(self, key, value) -> None:
        """
        # 设置session指定字段的值
        :param key: 字段
        :param value: 值
        """
        self._backend.setitem(self._session_id, key, value, self._expires)

    def clean(self) -> None:
        """
        # 删除session
        """
        self._backend.clean(self._session_id)

    def set_expires(self, expires: int) -> None:
        """
        # 设置session 过期时间
        """
        self._request.set_cookie(
            name=self._name,
            value=self._session_id,
            domain=self._domain,
            path=self._path,
            expires=int(time.time()) + expires
        )
        self._backend.expires(self._session_id, expires)

    @staticmethod
    def gen_session_id() -> str:
        """
        # 生成一个session id
        :return: 字符串
        """
        tmp = f"{time.time()}{uuid.uuid4()}".encode("utf-8")
        hash_obj = hashlib.sha256()
        hash_obj.update(tmp)
        return hash_obj.hexdigest()

    def get_session_data(self, session_id, key) -> str:
        """
        # 获取指定session的key, 这个方法在websock 认证的时候使用
        :param session_id:  会话ID
        :param key: 查询的key
        :return: key 对应的值
        """
        return self._backend.getitem(session_id, key)


