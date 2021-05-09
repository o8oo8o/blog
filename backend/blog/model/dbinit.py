#!/usr/bin/evn python3
# coding=utf-8

import os
import sys

sys.path.append(".")
sys.path.append(os.path.dirname(__file__))

import re
import ssl
import urllib.parse
import urllib.request
import urllib.error
from uuid import uuid4
from random import randint, choice, random
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import BigInteger
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.dialects.mysql import DOUBLE
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy import func
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.query import Query
from util.config import Config

__CONF: Config = Config()


def all_data(self):
    """
    # 猴子补丁,增加Query对象all_data 方法返回字典
    """
    field = tuple([f["name"] for f in self.column_descriptions])
    all_info = self.all()
    result_data = []
    for item in all_info:
        result_data.append(dict(zip(field, item)))
    return result_data


setattr(Query, "all_data", all_data)

# 创建数据库连接引擎
engine = create_engine(__CONF.get_db_url(), echo=__CONF.get_conf("orm")["sql_echo"])
# 自己创建的model需要继承这个类
Base = declarative_base(engine)
# 数据库连接session
session = sessionmaker(engine)()


class Setting(Base):
    """
    用户配置信息表
    """
    __tablename__ = "setting"

    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="ID")
    admin_user = Column(String(127), nullable=False, comment="后台管理账号")
    admin_pwd = Column(String(255), nullable=False, comment="后台管理密码")
    admin_title = Column(String(15), nullable=False, comment="后台浏览器标题")
    admin_name = Column(String(15), nullable=False, comment="后台名字")

    email = Column(String(127), nullable=False, comment="邮箱")
    github_addr = Column(String(255), nullable=False, comment="github地址")
    github_name = Column(String(127), nullable=False, comment="github名字")
    weibo_addr = Column(String(255), nullable=False, comment="微博地址")
    weibo_name = Column(String(127), nullable=False, comment="微博名字")
    qq = Column(String(31), nullable=False, comment="QQ号码")
    wx = Column(String(63), nullable=False, comment="微信号码")
    city = Column(String(15), nullable=False, comment="城市")
    logo_path = Column(String(255), nullable=False, comment="Logo图标路径")
    logo_text = Column(String(5), nullable=False, comment="Logo图标文字")
    icon_path = Column(String(255), nullable=False, comment="用户图像路径")
    icon_text = Column(String(5), nullable=False, comment="用户图像文字")
    web_title = Column(String(15), nullable=False, comment="前台浏览器标题")
    banner = Column(LONGTEXT, nullable=True, comment="广告数据")
    note = Column(Text, nullable=True, comment="说明")
    info = Column(Text, nullable=True, comment="信息")
    footer = Column(Text, nullable=False,  comment="页脚")
    # pz == page size  # 为了简化
    web_last_pz = Column(Integer, nullable=False, comment="前台最近更新分页大小")
    web_blog_pz = Column(Integer, nullable=False, comment="前台博客分页大小")
    admin_blog_pz = Column(Integer, nullable=False, comment="后台博客分页大小")
    admin_review_pz = Column(Integer, nullable=False, comment="后台评论分页大小")
    admin_publish_pz = Column(Integer, nullable=False, comment="后台简历发布分页大小")

    enable_chat = Column(Boolean, nullable=False, default=True, comment="聊天功能")
    enable_music = Column(Boolean, nullable=False, default=True, comment="音乐功能")
    enable_notice = Column(Boolean, nullable=False, default=True, comment="通知功能")
    enable_resume = Column(Boolean, nullable=False, default=True, comment="简历功能")

    ssh_host = Column(String(255), nullable=False, comment="SSH主机")
    ssh_port = Column(Integer, nullable=False, comment="SSH端口")
    ssh_user = Column(String(255), nullable=False, comment="SSH用户名")
    ssh_pwd = Column(String(255), nullable=False,  comment="SSH密码")
    ssh_width = Column(Integer, nullable=False, comment="SSH窗口宽度")
    ssh_height = Column(Integer, nullable=False, comment="SSH窗口高度")

    chart_day = Column(Integer, nullable=False, comment="图表显示天数")
    chart_zero = Column(Boolean, nullable=False, comment="图表Y轴是否从零开始")
    chart_border_width = Column(Integer, nullable=False, comment="图表边框宽度")
    chart_bg_color = Column(String(64), nullable=False, comment="图表背景颜色")
    chart_br_color = Column(String(64), nullable=False, comment="图表边框颜色")

    web_patch_html = Column(LONGTEXT, nullable=True, comment="html")
    web_patch_css = Column(LONGTEXT, nullable=True, comment="css")
    web_patch_js = Column(LONGTEXT, nullable=True, comment="js")

    admin_patch_html = Column(LONGTEXT, nullable=True, comment="html")
    admin_patch_css = Column(LONGTEXT, nullable=True, comment="css")
    admin_patch_js = Column(LONGTEXT, nullable=True, comment="js")

    music_dir = Column(String(127), nullable=False, comment="音乐默认目录,相对网盘根目录")

    mail_smtp = Column(String(127), nullable=False, comment="邮箱SMTP服务器")
    mail_port = Column(Integer, nullable=False, comment="邮箱端口")
    mail_user = Column(String(127), nullable=False, comment="邮箱用户名")
    mail_pwd = Column(String(127), nullable=False, comment="邮箱密码")
    mail_ssl = Column(Boolean, nullable=False, default=True, comment="是否启用ssl")
    mail_recv = Column(String(127), nullable=False, comment="默认收件人")

    create_time = Column(DateTime, nullable=False, default=func.now(), comment='创建时间')
    update_time = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now(), comment='更新时间')

    def __init__(
            self,
            admin_user: str = "admin",
            # 默认密码123456
            admin_pwd: str = "e76fc3683614c5319be298ccf6f606f3513bdc2d3a88a33d49a1e07b4cef454c",
            admin_title: str = "博客后台管理",
            admin_name: str = "博客管理",

            email: str = "a@huangrui.vip",
            github_addr: str = "https://github.com/o8oo8o",
            github_name: str = "o8oo8o",
            weibo_addr: str = "https://weibo.com",
            weibo_name: str = "weibo",
            qq: str = "123456789",
            wx: str = "weixin",
            city: str = "中国",
            logo_path: str = "img/logo.png",
            logo_text: str = "黄",
            icon_path: str = "img/user.png",
            icon_text: str = "黄锐",
            web_title: str = "黄锐博客",
            banner: str = "这里是广告",
            note: str = "这里是说明内容",
            info: str = "这里是信息内容",
            footer: str = "页脚",

            web_last_pz: int = 5,
            web_blog_pz: int = 15,
            admin_blog_pz: int = 15,
            admin_review_pz: int = 15,
            admin_publish_pz: int = 15,

            enable_chat: bool = True,
            enable_music: bool = True,
            enable_notice: bool = True,
            enable_resume: bool = True,

            ssh_host: str = "127.0.0.1",
            ssh_port: int = 22,
            ssh_user: str = "root",
            ssh_pwd: str = "0",
            ssh_width: int = 120,
            ssh_height: int = 30,

            chart_day: int = 15,
            chart_zero: bool = True,
            chart_border_width: int = 1,
            chart_bg_color: str = "rgba(75, 192, 192, 0.2)",
            chart_br_color: str = "rgba(54, 162, 235, 1)",

            web_patch_html: str = "",
            web_patch_css: str = "",
            web_patch_js: str = "",

            admin_patch_html: str = "",
            admin_patch_css: str = "",
            admin_patch_js: str = "",

            music_dir: str = "music",
            mail_smtp: str = "smtp.exmail.qq.com",
            mail_port: int = 465,
            mail_user: str = "send@huangrui.vip",
            mail_pwd: str = "xxxxxxxx",
            mail_ssl: bool = True,
            mail_recv: str = "send@huangrui.vip"


    ) -> None:
        self.admin_user = admin_user
        self.admin_pwd = admin_pwd
        self.admin_title = admin_title
        self.admin_name = admin_name

        self.email = email
        self.github_addr = github_addr
        self.github_name = github_name
        self.weibo_addr = weibo_addr
        self.weibo_name = weibo_name
        self.qq = qq
        self.wx = wx
        self.city = city
        self.logo_path = logo_path
        self.logo_text = logo_text
        self.icon_path = icon_path
        self.icon_text = icon_text
        self.web_title = web_title
        self.banner = banner
        self.note = note
        self.info = info
        self.footer = footer

        self.web_last_pz = web_last_pz
        self.web_blog_pz = web_blog_pz
        self.admin_blog_pz = admin_blog_pz
        self.admin_review_pz = admin_review_pz
        self.admin_publish_pz = admin_publish_pz

        self.enable_chat = enable_chat
        self.enable_music = enable_music
        self.enable_notice = enable_notice
        self.enable_resume = enable_resume

        self.ssh_host = ssh_host
        self.ssh_port = ssh_port
        self.ssh_user = ssh_user
        self.ssh_pwd = ssh_pwd
        self.ssh_width = ssh_width
        self.ssh_height = ssh_height

        self.chart_day = chart_day
        self.chart_zero = chart_zero
        self.chart_border_width = chart_border_width
        self.chart_bg_color = chart_bg_color
        self.chart_br_color = chart_br_color

        self.web_patch_html = web_patch_html
        self.web_patch_css = web_patch_css
        self.web_patch_js = web_patch_js

        self.admin_patch_html = admin_patch_html
        self.admin_patch_css = admin_patch_css
        self.admin_patch_js = admin_patch_js

        self.music_dir = music_dir
        self.mail_smtp = mail_smtp
        self.mail_port = mail_port
        self.mail_user = mail_user
        self.mail_pwd = mail_pwd
        self.mail_ssl = mail_ssl
        self.mail_recv = mail_recv

    def __repr__(self):
        return f"Setting({self.id})"


class Classify(Base):
    """
    博客分类表
    """
    __tablename__ = "classify"
    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="ID")
    name = Column(String(127), nullable=False, unique=True, comment="分类名称")
    create_time = Column(DateTime, nullable=False, default=datetime.now(), comment='创建时间')
    update_time = Column(DateTime, nullable=False, default=datetime.now(), onupdate=func.now(), comment='更新时间')
    blog = relationship("Blog", back_populates="classify", cascade="all, delete", passive_deletes=True)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Classify({self.id} | {self.name})"


class Blog(Base):
    """
    博客表
    """
    __tablename__ = "blog"
    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="ID")
    classify_id = Column(ForeignKey(Classify.id, ondelete="CASCADE"), nullable=False, comment="博客分类ID")
    title = Column(String(128), nullable=False, unique=True, comment="标题")
    text = Column(LONGTEXT, nullable=False, comment="内容")
    is_review = Column(Boolean, default=True, comment="是否允许评论")
    is_public = Column(Boolean, default=True, comment="是否公开")
    status = Column(TINYINT, nullable=False, default=0, comment="状态{0:已发布,1:预览保存}")
    read_count = Column(BigInteger, nullable=False, default=0, comment="阅读数")
    weight = Column(Integer, nullable=False, default=2000, comment="权重")  # 使用范围 1000 - 3000
    create_time = Column(DateTime, nullable=False, default=datetime.now(), comment='创建时间')
    update_time = Column(DateTime, nullable=False, default=datetime.now(), onupdate=func.now(), comment='更新时间')

    classify = relationship("Classify", order_by=Classify.id, back_populates="blog")
    review = relationship("Review", back_populates="blog", cascade="all, delete", passive_deletes=True)

    def __init__(
        self,
        classify_id: int,
        title: str,
        text: str,
        weight: int = 2000,
        is_review: bool = False,
        is_public: bool = False,
        status: int = 0,
        read_count: int = 0,
        create_time=datetime.now()
    ) -> None:
        self.classify_id = classify_id
        self.title = title
        self.text = text
        self.is_review = is_review
        self.is_public = is_public
        self.status = status
        self.read_count = read_count
        self.weight = weight
        self.create_time = create_time

    def __repr__(self):
        return f"Blog({self.id} | {self.title})"


class Review(Base):
    """
    评论表
    """
    __tablename__ = "review"
    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="ID")
    blog_id = Column(ForeignKey(Blog.id, ondelete="CASCADE"), nullable=False, comment="博客ID")
    name = Column(String(128), nullable=False, server_default="", comment="账号")
    email = Column(String(128), nullable=False, server_default="", comment="邮箱")
    text = Column(Text, nullable=False, comment="内容")
    create_time = Column(DateTime, nullable=False, default=datetime.now(), comment='创建时间')
    blog = relationship("Blog", order_by=Blog.id, back_populates="review")

    def __init__(self, blog_id: int, name: str, email: str, text: str) -> None:
        self.blog_id = blog_id
        self.name = name
        self.email = email
        self.text = text

    def __repr__(self):
        return f"Review({self.id} | {self.name})"


class Resume(Base):
    """
    简历表
    """
    __tablename__ = "resume"
    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="ID")
    title = Column(String(128), nullable=False, unique=True, default="", server_default="", comment="标题")
    text = Column(LONGTEXT, nullable=False, default="", comment="内容")
    create_time = Column(DateTime, nullable=False, default=datetime.now(), comment='创建时间')
    update_time = Column(DateTime, nullable=False, default=datetime.now(), onupdate=func.now(), comment='更新时间')
    publish = relationship("Publish", back_populates="resume", cascade="all, delete", passive_deletes=True)

    def __init__(self, title: str, text: str):
        self.title = title
        self.text = text

    def __repr__(self):
        return f"Resume({self.id} | {self.title})"


class Publish(Base):
    """
    简历发布表
    """
    __tablename__ = "publish"
    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="ID")
    access_code = Column(String(128), nullable=False, unique=True, comment="访问码")
    resume_id = Column(ForeignKey(Resume.id, ondelete="CASCADE"), nullable=False, comment="简历ID")
    receiver = Column(String(128), nullable=False, comment="接收者")
    exp_time = Column(DateTime, nullable=False, default=datetime.now(), comment='过期时间')
    read_count = Column(BigInteger, nullable=False, default=0, comment="阅读数")
    read_duration = Column(BigInteger, nullable=False, default=0, comment="阅读时长")
    read_time = Column(DateTime, index=True, nullable=False, default=datetime.now(), comment='阅读时间')
    create_time = Column(DateTime, nullable=False, default=datetime.now(), comment='创建时间')
    update_time = Column(DateTime, nullable=False, default=datetime.now(), onupdate=func.now(), comment='更新时间')
    resume = relationship("Resume", order_by=Resume.id, back_populates="publish")

    def __init__(
        self,
        access_code: str,
        resume_id: int,
        receiver: str,
        exp_time: datetime,
        read_count: int = 0,
        read_duration: int = 0,
        read_time: datetime = datetime.now()
    ) -> None:
        self.resume_id = resume_id
        self.receiver = receiver
        self.access_code = access_code
        self.exp_time = exp_time
        self.read_count = read_count
        self.read_duration = read_duration
        self.read_time = read_time

    def __repr__(self):
        return f"Publish({self.id} | {self.receiver})"


class AccessLog(Base):
    """
    访问日志
    """
    __tablename__ = "access_log"
    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="ID")
    ip = Column(String(40), index=True, nullable=False, comment="IP地址")
    method = Column(String(15), nullable=False, comment="请求方法")
    status = Column(SMALLINT, nullable=False, comment="状态码")
    qtime = Column(DOUBLE, index=True, nullable=False, comment="请求时间")
    path = Column(String(256), nullable=False, comment="访问路径")
    agent = Column(String(256), nullable=False, comment="客户端")
    query = Column(String(256), nullable=True, comment="查询字段")
    create_time = Column(DateTime, index=True, nullable=False, default=datetime.now(), comment='创建时间')

    def __init__(self, ip: str, method: str, status: int, qtime: float, path: str, agent: str, query: str,
             creata_time = datetime.now()
    ) -> None:
        self.ip = ip
        self.method = method
        self.status = status
        self.qtime = qtime
        self.path = path
        self.agent = agent
        self.query = query
        self.create_time = creata_time

    def __repr__(self):
        return f"AccessLog({self.id})"



class LoginLog(Base):
    """
    # 登陆记录
    """
    __tablename__ = "login_log"
    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="ID")
    is_success = Column(Boolean, index=True, nullable=False, comment="是否登陆成功")
    login_type = Column(Integer, index=True, nullable=False, comment="登陆类型")
    error_type = Column(Integer, index=True, nullable=False, comment="错误类型")
    ip = Column(String(40), index=True, nullable=False, comment="IP地址")
    user = Column(String(127), nullable=False, comment="账号")
    pwd = Column(String(255), nullable=False, comment="密码")
    agent = Column(String(256), nullable=False, comment="客户端")
    create_time = Column(DateTime, index=True, nullable=False, default=func.now(), comment='创建时间')

    def __init__(
            self,
            is_success: bool,
            login_type: int,
            error_type: int,
            ip: str,
            user: str,
            pwd: str,
            agent: str,
            create_time
    ) -> None:
        self.is_success = is_success
        self.login_type = login_type
        self.error_type = error_type
        self.ip = ip
        self.user = user
        self.pwd = pwd
        self.agent = agent
        self.create_time = create_time


    def __repr__(self):
        return f"LoginLog({self.id})"



class Chat(Base):
    """
    # 聊天记录
    """
    __tablename__ = "chat"
    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="ID")
    ip = Column(String(40), index=True, nullable=False, comment="IP地址")
    agent = Column(String(256), nullable=False, comment="客户端")
    msg = Column(Text, nullable=True, comment="消息")
    create_time = Column(DateTime, index=True, nullable=False, default=datetime.now(), comment='创建时间')

    def __init__(self, ip: str, agent: str, msg: str) -> None:
        self.ip = ip
        self.agent = agent
        self.msg = msg

    def __repr__(self):
        return f"Chat({self.id})"


ssl._create_default_https_context = ssl._create_unverified_context

"""
# 添加模拟数据
"""


def add_setting() -> None:
    """
    # 添加配置数据
    """
    user = Setting()
    session.add(user)
    session.commit()


def add_classify() -> None:
    """
    # 添加分类数据
    """
    ta = Classify("Python")
    tb = Classify("Java")
    tc = Classify("PHP")
    td = Classify("Node")
    te = Classify("GoLang")
    tf = Classify("MySQL")
    tg = Classify("Oracle")
    th = Classify("读书笔记")
    ti = Classify("科技新闻")
    session.add_all([ta, tb, tc, td, te, tf, tg, th, ti])
    session.commit()


def add_blog():
    """
    # 添加博客
    """

    def get_html():
        for num in range(1000, 1203):
            try:
                url = f"https://so.gushiwen.org/guwen/bookv_{num}.aspx"
                html = urllib.request.urlopen(url).read().decode("utf-8")
            except Exception as e:
                continue
            yield html

    next_blog = get_html()

    def get_data():
        blog = str(next(next_blog))
        blog_title = str(re.findall(r'<title>(.*)</title>', blog, re.S | re.M)[0])
        blog_text = str(re.findall(r'<div class="contson">(.*?)</div>', blog, re.S | re.M)[0])
        blog_title = blog_title[:-5]
        blog_title = blog_title[6:]
        return blog_title, blog_text

    blog_list = []
    for i in range(1, 101):
        title, text = get_data()
        blog_list.append(Blog(
            classify_id=randint(1, 9),
            title=f"{str(title) + str(i) if title else str('title_none' + str(i))}",
            text=f"{text if text else str('text_none' + str(i))}",
            weight=randint(1001, 2999),
            is_review=bool(choice([0, 1])),
            is_public=bool(1),
            status=choice([0, 1]),
            create_time=datetime(
                randint(2018, 2021),
                randint(1, 12),
                randint(1, 28),
                randint(1, 23),
                randint(1, 59),
                randint(1, 59))
        ))

    session.add_all(blog_list)
    session.commit()


def add_review():
    """
    # 添加评论数据
    """
    session.add_all([
        Review(
            blog_id=randint(1, 90),
            email=f"{randint(100000, 999999)}@{choice(['qq', '126', '163'])}.com",
            name=f"review_name_{uuid4()}",
            text=f"{uuid4()}__review_text___{uuid4()}",
        ) for i in range(101)
    ])
    session.commit()


def add_access_log() -> None:
    """
    # 数据填充,添加访问日志
    """
    session.add_all([
        AccessLog(
            ip=f"192.168.1.{randint(1, 200)}",
            method=choice(["GET", "HEAD", "POST", "DELETE", "PATCH", "PUT", "OPTIONS"]),
            status=randint(100, 505),
            qtime=random(),
            path=choice(["/aa", "/bb", "/cc", "/dd", "/ee", "/ff", "/gg", "/xx", "yy"]),
            agent=choice(["Macintosh", "Windows", "IPadOS", "Linux", "Android", "IOS"]),
            query=f"{uuid4()}={uuid4()}",
            creata_time=datetime(
                randint(2018, 2021),
                randint(1, 12),
                randint(1, 28),
                randint(1, 23),
                randint(1, 59),
                randint(1, 59))
        ) for i in range(30000)
    ])
    session.commit()


def add_login_log() -> None:
    """
    # 添加登陆日志
    """
    session.add_all([
        LoginLog(
            is_success=choice([False, True]),
            login_type=choice([1, 2]),
            error_type=choice([0,1,2,3,4,5,6]),
            ip=f"192.168.1.{randint(1, 200)}",
            user=choice(["uaera", "uaerb", "uaerc", "userd", "userd"]),
            pwd=randint(1000000, 5000000),
            agent=choice(["Macintosh", "Windows", "IPadOS", "Linux", "Android", "IOS"]),
            create_time=datetime(
                randint(2018, 2021),
                randint(1, 12),
                randint(1, 28),
                randint(1, 23),
                randint(1, 59),
                randint(1, 59))
        ) for i in range(30000)
    ])
    session.commit()


def add_resume():
    """
    # 添加简历数据
    """
    session.add(Resume("运维工程师", "运维工程师yes_这是内容"))
    session.add(Resume("python工程师", "python工程师yes_这是内容"))
    session.add(Resume("后端工程师", "后端工程师yes_这是内容"))
    session.add(Resume("js工程师", "js工程师yes_这是内容"))
    session.commit()


def add_publish():
    """
    # 添加简历发布数据
    """
    session.add_all([
            Publish(
                access_code=f"{i}",
                resume_id=choice([1, 2, 3]),
                receiver=f"{choice(['百度', '阿里', '腾讯', '网易', '京东', '搜狐'])}_{i}",
                exp_time=datetime(
                    randint(2018, 2021),
                    randint(1, 12),
                    randint(1, 28),
                    randint(1, 23),
                    randint(1, 59),
                    randint(1, 59)),
                read_count=randint(1, 59),
                read_duration=randint(1, 1000),
                read_time=datetime(
                    randint(2018, 2021),
                    randint(1, 12),
                    randint(1, 28),
                    randint(1, 23),
                    randint(1, 59),
                    randint(1, 59)),
            ) for i in range(600000, 603000)
        ])
    session.commit()


def main():
    add_setting()
    add_classify()
    add_blog()
    add_review()
    add_resume()
    add_publish()
    add_access_log()
    add_login_log()


if __name__ == '__main__':
    Base.metadata.drop_all()
    Base.metadata.create_all()
    main()



