#!/usr/bin/evn python3
# coding=utf-8

#######################
# 此配置文件用于生产环境 #
#######################


"""
# server 配置
"""
server = {
    # 67108864   64M
    # 134217728  128M
    # 268435456  256M
    # 536870912  512M
    # 1073741824 1G
    "max_buffer_size": 268435456,
    "port": 8899,
}


"""
# App 配置
"""
app = {
    "debug": False,
    "autoreload": True,
    "ui_modules": {},
    # 设置默认的处理函数类，如：404页面等
    "default_handler_class": None,
    "serve_traceback": False,
    "template_path": "template",
    "compiled_template_cache": True,
    "autoescape": None,
    "cookie_secret": "b6fc5e14875abbb980979e5d9ee99891",
    "login_url": "/api/admin/login/",
    "xsrf_cookies": True,
    "xsrf_cookie_version": 2,
    "static_hash_cache": False,
    "static_path": "../static",
    "static_url_prefix": "/static/",
    # 图片上传路径
    "upload_path": "/usr/local/src/web/netdisk/upload/"

}


"""
# redis 配置
"""
redis = {
    "master": {
        "default": {
            "host": "127.0.0.1",
            "port": 6379,
            "db": 0,
            "exp": 86400
        },
    },
}


"""
# orm 配置
"""
orm = {
    "sql_echo": False
}


"""
# mysql 配置
"""
mysql = {
    "master": {
        "default": {
            "username": "root",
            "hostname": "127.0.0.1",
            "port": "3306",
            "database": "mydb",
            "password": "mima",
            "charset": "utf8mb4"
        },
    },
}


"""
# Session 配置
"""
session = {
    # session 名字
    "name": "sid",

    # 域名
    "domain": None,

    # 路径
    "path": "/",

    # 过期时间
    "expires": 3600,

    # 记住密码情况过期时间
    "rem_session_exp": 86400
}


"""
# 网盘配置
"""
net_disk = {
    # 网盘的根目录,对应系统的文件夹,注意:最后一个反斜杠必须存在
    "base_dir": "/usr/local/src/web/netdisk/"
}


"""
# 音乐功能配置
"""
music = {
    # 注意支持成3个字符的后缀
    "type": [".mp3", ".ogg"]
}


"""
# 日志配置
"""
log = {

    # 日志存储路径,注意:最后一个反斜杠必须存在
    "path": "/usr/local/src/web/netdisk/log/",

    # 日志记录格式
    "format": "%(asctime)s - %(levelname)s - %(name)s ==*== %(message)s ==*==",

    # 日志文件名前缀
    "file": "tornado",

    # 是否关闭日志功能
    "disabled": False,

    # 控制台是否输出日志
    "propagate": False,

    #############
    # 日志级别
    #############
    #  CRITICAL 50
    #  ERROR    40
    #  WARNING  30
    #  INFO     20
    #  DEBUG    10
    #  NOTSET   0
    #############
    "level": "INFO",

    #############
    # when 是一个字符串的定义如下,:
    #############
    # "S": 秒
    # "M": 分
    # "H": 时
    # "D": 天
    # "W[0-6]": 周 (0=Monday)
    #############
    "when": "D",

    # 设置日志后缀名称，跟strftime的格式一样,要和when单位保持一致
    # "%Y-%m-%d_%H-%M-%S.log"
    "suffix": "%Y-%m-%d.log",

    # interval 是指等待多少个when单位的时间后，会自动重建日志文件
    "interval": 1,

    # 是保留日志数量
    "backup_count": 10
}


"""
# 登陆密码、访问码配置
"""
login = {
    # 最大尝试次数
    "max_try_count": 5,

    # 多少秒以后可以继续尝试
    "timeout": 1800
}

"""
# 邮箱配置
"""
mail = {
    # 服务器连接超时时间
    "timeout": 15,
}

