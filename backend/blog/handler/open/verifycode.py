#!/usr/bin/evn python3
# coding=utf-8

from functools import wraps
from handler.open.base import WebBaseHandler
from util.verifycode import ValidCodeImg


def check_verify_code(func):
    """
    # 验证码检查装饰器
    :param func: 被装饰的函数
    :return: 函数
    """
    @wraps(func)
    async def check(request, *args, **kwargs):
        receive_verify_code = request.get_argument_str("verify_code", min_len=4, max_len=4)
        verify_code = str(request.session["verify_code"])
        if (not receive_verify_code) or (receive_verify_code.upper() != verify_code.upper()):
            request.send_json({"code": 1, "status": False, "msg": "验证码错误"})
            return
        await func(request, *args, **kwargs)
    return check


class VerifyCodeHandler(WebBaseHandler):
    """验证码获取及检查处理类"""
    async def get(self):
        """
        # 获取验证码
        :return: 验证码图片
        """
        img = ValidCodeImg()
        data, valid_str, base64_str = img.getValidCodeImg()
        self.session["verify_code"] = valid_str
        self.set_header("Content-Type", "image/png")
        self.write(data)

    @check_verify_code
    async def post(self):
        """
        # 检查验证码
        :return:
        """
        self.send_json({"code": 0,  "status": True, "msg": "验证码正确"})


