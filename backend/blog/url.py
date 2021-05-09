#!/usr/bin/evn python3
# coding=utf-8

import handler.open.error
import handler.open.chat
import handler.open.blog
import handler.open.home
import handler.open.xsrf
import handler.open.review
import handler.open.publish
import handler.open.verifycode
import handler.open.music
import handler.admin.login
import handler.admin.dashboard
import handler.admin.classify
import handler.admin.review
import handler.admin.blog
import handler.admin.setting
import handler.admin.upload
import handler.admin.monitor
import handler.admin.resume
import handler.admin.publish
import handler.admin.netdisk
import handler.admin.ssh
from util.config import Config

URL = [
    # 前台功能API(不需要登陆认证)
    (r"/api/open/chat/", handler.open.chat.ChatHandler),
    (r"/api/open/xsrf/", handler.open.xsrf.XsrfHandler),
    (r"/api/open/verify_code/", handler.open.verifycode.VerifyCodeHandler),
    (r"/api/open/home/", handler.open.home.HomeHandler),
    (r"/api/open/blog/(\d+)/", handler.open.blog.BlogHandler),
    (r"/api/open/review/", handler.open.review.ReviewHandler),
    (r"/api/open/resume/", handler.open.publish.PublishShowHandler),
    (r"/api/open/music/", handler.open.music.MusicHandler),
    # 后台管理API(需要登陆认证)
    (Config().get_dict()["app"]["login_url"], handler.admin.login.LoginHandler),
    (r"/api/admin/logout/", handler.admin.login.LogoutHandler),
    (r"/api/admin/dashboard/", handler.admin.dashboard.DashboardHandler),
    (r"/api/admin/classify/", handler.admin.classify.ClassifyHandler),
    (r"/api/admin/review/", handler.admin.review.ReviewHandler),
    (r"/api/admin/blog_list/", handler.admin.blog.BlogListHandler),
    (r"/api/admin/blog/", handler.admin.blog.BlogHandler),
    (r"/api/admin/blog_title_check/", handler.admin.blog.BlogTitleCheckHandler),
    (r"/api/admin/setting/", handler.admin.setting.SettingHandler),
    (r"/api/admin/account/", handler.admin.setting.AccountHandler),
    (r"/api/admin/upload/", handler.admin.upload.UploadHandler),
    (r"/api/admin/resume_list/", handler.admin.resume.ResumeListHandler),
    (r"/api/admin/resume/", handler.admin.resume.ResumeHandler),
    (r"/api/admin/resume_title_check/", handler.admin.resume.ResumeTitleCheckHandler),
    (r"/api/admin/publish_list/", handler.admin.publish.PublishListHandler),
    (r"/api/admin/publish/", handler.admin.publish.PublishHandler),
    (r"/api/admin/publish_access_code_check/", handler.admin.publish.PublishAccessCodeCheckHandler),
    # 主机性能监控API
    (r"/api/admin/monitor/", handler.admin.monitor.MonitorHandler),
    # 网盘API
    (r"/api/admin/dir_list/", handler.admin.netdisk.DirListHandler),
    (r"/api/admin/dir_tree/", handler.admin.netdisk.DirTreeHandler),
    (r"/api/admin/net_disk/", handler.admin.netdisk.NetDiskHandler),
    # SSH远程API
    (r"/api/admin/web_ssh/", handler.admin.ssh.WebSSHHandler),
    # 404 错误
    (r".*", handler.open.error.ErrorHandler),
]


