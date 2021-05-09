#!/usr/bin/evn python3
# coding=utf-8

import sys
import re
import datetime
import json
import hashlib
import hmac
import decimal
from typing import Any
from tornado.escape import utf8
from tornado.web import Application
from tornado.httputil import HTTPServerRequest
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler
from util.acl import Acl
from util.config import ConfigMixIn
from util.session import Backend
from util.session import Session
from util.exception import AppException
from util.exception import AppValueError
from util.logger import AppLog
from util.guard import Guard


class BaseHandler(RequestHandler, ConfigMixIn):
    """
    # Handler 基类,所有的都应该继承这个
    """
    def __init__(
            self,
            application: Application,
            request: HTTPServerRequest,
            **kwargs: Any
    ) -> None:
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.session = Session(request=self, backend=Backend())
        self.acl = Acl()
        self.logger = AppLog().logger
        self.guard = Guard().get_run_guard()

    def set_default_headers(self) -> None:
        """
        # 默认情况下把响应设置成JSON
        """
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.set_header("Server", "httpd24")

    def get_argument_int(
        self,
        name: str,
        min_val: int = -9223372036854775808,
        max_val: int = 18446744073709551615,
        default: str = ""
    ) -> int:
        """
        :param name: 参数名字
        :param default: 默认值
        :param min_val: 最小值
        :param max_val: 最大值
        :return: 整数
        """
        param = self.get_argument(name, default=default, strip=True)
        try:
            param = int(param)
            if param < min_val or param > max_val:
                raise AppValueError("int_number_range_error")
        except AppValueError as value_error:
            self.logger.error("获取整数参数错误", value_error.args)
        else:
            return param

    def get_argument_str(
        self,
        name: str,
        min_len: int = 1,
        max_len: int = 65534,
        default: str = ""
    ) -> str:
        """
        :param name: 参数名字
        :param default: 默认值
        :param min_len: 参数值的最小长度
        :param max_len: 参数值的最大长度
        :return: 字符串
        """
        param = self.get_argument(name, default=default, strip=True)
        try:
            if len(param) < min_len or len(param) > max_len:
                raise AppValueError("param_length_error")
        except AppValueError as value_error:
            self.logger.error("获取参数长度错误", value_error.args)
        else:
            return param

    def get_argument_pwd(
        self, name: str,
        min_len: int = 5,
        max_len: int = 65534
    ) -> str:
        """
        :param name: 参数名字
        :param min_len: 参数值的最小长度
        :param max_len: 参数值的最大长度
        :return: Hash 完成的字符串
        """
        param = self.get_argument_str(name, min_len, max_len)

        def get_pwd_str(pwd_str: str):
            hash_a = hashlib.sha3_256()
            hash_a.update(bytes(pwd_str, encoding='utf-8'))
            hash_b = hashlib.sha3_256()
            hash_b.update(bytes(hash_a.hexdigest(), encoding='utf-8'))
            pwd_str = hash_b.hexdigest()
            return pwd_str
        return get_pwd_str(param)

    def get_argument_bool(self, name: str, default: str = "False") -> bool:
        """
        :param name: 参数名字
        :param default: 默认值
        :return: 布尔值
        """
        param = self.get_argument(name, default=default, strip=True).upper()
        try:
            if param in ("TRUE", "FALSE"):
                param = True if param == "TRUE" else False
            else:
                raise AppValueError("not_bool_param_error")
        except AppValueError as value_error:
            self.logger.error("获取布尔参数错误", value_error.args)
        else:
            return param

    def get_argument_email(
        self,
        name: str,
        min_len: int = 3,
        max_len: int = 254,
        default: str = ""
    ) -> str:
        """
        :param name: 参数名字
        :param default: 默认值
        :param min_len: 参数值的最小长度
        :param max_len: 参数值的最大长度
        :return: 邮箱地址
        """
        param = self.get_argument_str(
            name,
            default=default,
            min_len=min_len,
            max_len=max_len)
        email_regexp = r"^(\w-*\.*)+@(\w-?)+(\.\w{2,})+$"
        try:
            if re.match(email_regexp, param) is None:
                raise AppValueError("email_address_format_error")
        except AppValueError as value_error:
            self.logger.error("获取邮箱参数错误", value_error.args)
        else:
            return param

    def get_argument_datetime(
        self,
        name: str,
        min_len: int = 19,
        max_len: int = 20,
        default: str = ""
    ) -> datetime:
        """
        :param name: 参数名字
        :param default: 默认值
        :param min_len: 参数值的最小长度
        :param max_len: 参数值的最大长度
        :return: 邮箱地址
        """
        param = self.get_argument_str(
            name,
            default=default,
            min_len=min_len,
            max_len=max_len)
        try:
            data = datetime.datetime.strptime(param, "%Y-%m-%d %H:%M:%S")
        except AppValueError as value_error:
            self.logger.error("日期时间参数格式错误", value_error.args)
        else:
            return data

    def send_json(self, obj) -> None:
        """
        # 把任意对象转换成json格式
        :param obj:
        """
        def json_encode(data):
            if isinstance(data, datetime.datetime):
                return data.strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(data, datetime.date):
                return data.strftime("%Y-%m-%d")
            elif isinstance(data, decimal.Decimal):
                return float(data)
            else:
                return str(data)
        json_data = json.dumps(obj, default=json_encode)
        self.write(json_data)
        self.finish()

    def get_remote_ip(self) -> str:
        """
        # 获取客户端的IP地址
        """
        if self.request.headers.get("X-Real-Ip", ""):
            ip = self.request.headers.get("X-Real-Ip", "")
        elif self.request.headers.get("X-Forwarded-For", ""):
            ip = self.request.headers.get("X-Forwarded-For", "")
        else:
            ip = self.request.remote_ip
        return ip

    def get_user_agent(self) -> str:
        """
        # 获取用户agent
        """
        return self.request.headers.get("User-Agent", "other")[:254]

    def record_request(self) -> tuple:
        """
        # 记录request请求,存储到数据库
        """
        ip = self.get_remote_ip()
        method = self.request.method
        status = self.get_status()
        qtime = self.request.request_time()
        path = self.request.path[:254]
        agent = self.get_user_agent()
        query = self.request.query[:254]
        return ip, method, status, qtime, path, agent, query

    def write_error(self, status_code: int, **kwargs) -> None:
        error_info = json.dumps({
            "code": status_code,
            "msg": self._reason,
            "class": str(sys.exc_info()[0]),
            "exp_msg": str(sys.exc_info()[1])
        })
        self.finish(error_info)


class BaseWebSocketHandler(BaseHandler, WebSocketHandler):
    """
    # WebSocket基类,所有WebSocketHandler都应该继承这个类
    """

    def __init__(
            self,
            application: Application,
            request: HTTPServerRequest,
            **kwargs: Any
    ) -> None:
        super(BaseWebSocketHandler, self).__init__(application, request, **kwargs)

    def check_origin(self, origin):
        """检查同源策略"""
        return True

    def check_xsrf_token(self) -> bool:
        """
        # 检查websock 的 xsrf
        :return:
        """
        token = self.get_argument("_xsrf", None)
        if not token:
            return False
        _, token, _ = self._decode_xsrf_token(token)
        _, expected_token, _ = self._get_raw_xsrf_token()
        if not token:
            return False
        if not hmac.compare_digest(utf8(token), utf8(expected_token)):
            return False
        return True

    def auth_check(self) -> bool:
        """
        # websock 认证检查
        :return: True 认证通过, False 认证失败
        """
        try:
            if not self.check_xsrf_token():
                return False
            session_id = self.get_argument_str("sid", min_len=64, max_len=64)
            is_login = self.session.get_session_data(session_id, "is_login")
            if is_login != "yes":
                return False
        except AppException as e:
            self.logger.error(f"connect_auth_error:{e}")
            return False
        else:
            return True


