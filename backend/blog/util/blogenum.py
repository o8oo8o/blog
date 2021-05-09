#!/usr/bin/evn python3
# coding=utf-8

# 博客用到的枚举类型都这个文件里定义

from enum import Enum


class LoginType(Enum):
    """
    # 登陆类型有两种
    """
    admin: int = 1  # 后台管理登陆
    resume: int = 2  # 简历访问登陆


class ErrorType(Enum):
    """
    # 登陆错误类型
    """
    no_error: int = 0  # 没有发生错误，写在这主要是为了统一管理
    user_pwd_error: int = 1  # 用户密码错误
    admin_acl: int = 2  # 用户被ACL过滤
    function_off: int = 3  # 功能关闭
    access_code_acl: int = 4  # 访问码被ACL过滤
    access_code_error: int = 5  # 访问码错误
    access_code_expire: int = 6  # 访问码过期



