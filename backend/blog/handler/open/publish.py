#!/usr/bin/evn python3
# coding=utf-8

from datetime import datetime
from handler.open.base import WebBaseHandler
from service.publish import PublishSrv
from service.setting import SettingSrv
from service.loginlog import LoginLogSrv
from util.mail import Mail
from util.blogenum import LoginType
from util.blogenum import ErrorType


class PublishShowHandler(WebBaseHandler):

    def acl_check(self, ip: str, code: str, agent: str) -> bool:
        """
        # 检查IP是否在过滤列表里面
        :param ip: ip 地址
        :param code: 访问码
        :param agent: 访问客户端
        """
        if self.acl.is_permit(ip):
            return True
        # IP 还在过滤列表里面,禁止访问
        self.acl.add_try_count(ip)
        self.send_json({"code": 1, "msg": "try_error_password_many"})
        LoginLogSrv.add_log(
            False, LoginType.resume.value, ErrorType.access_code_acl.value, ip, "resume_acl", code, agent)
        return False

    def enable_resume_check(self, setting: dict, ip: str, code: str, agent: str) -> bool:
        """
        # 检查简历功能是否开启
        :param setting
        :param ip: ip 地址
        :param code: 访问码
        :param agent: 访问客户端
        """
        if setting["enable_resume"]:
            return True
        # 简历功能关闭,禁止访问
        self.acl.add_try_count(ip)
        self.send_json({"code": 2, "msg": "function_is_off"})
        LoginLogSrv.add_log(
            False, LoginType.resume.value, ErrorType.function_off.value, ip, "resume_off", code, agent)
        return False

    def resume_exists_check(self, ip: str, code: str, agent: str, resume_data) -> bool:
        """
        # 根据访问码检查是否简历是否存在
        :param ip: ip 地址
        :param code: 访问码
        :param agent: 访问客户端
        :param resume_data: 简历数据
        """
        if resume_data:
            return True
        # 访问码没有对应的简历数据,禁止访问
        self.acl.add_try_count(ip)
        self.send_json({"code": 1, "msg": "access_code_error"})
        LoginLogSrv.add_log(
            False, LoginType.resume.value, ErrorType.access_code_error.value, ip, "code_error", code, agent)
        return False

    def exp_time_check(self, ip: str, code: str, agent: str, resume_data) -> bool:
        """
        # 检查访问码是否过期
        :param ip: ip 地址
        :param code: 访问码
        :param agent: 访问客户端
        :param resume_data: 简历数据
        """
        if datetime.now() >= resume_data["exp_time"]:
            # 访问码已经过期,禁止访问
            self.acl.add_try_count(ip)
            self.send_json({"code": 1, "msg": "exp_time"})
            LoginLogSrv.add_log(
                False, LoginType.resume.value, ErrorType.access_code_expire.value, ip, "code_expire", code, agent)
            return False
        return True

    async def send_mail(self, setting, read_count, data) -> None:
        """
        # 发送阅读通知邮件
        :param setting: 设置
        :param read_count: 阅读次数
        :param data: 简历数据
        """
        if setting["enable_notice"]:
            # 如果开启通知功能,发送邮件通知
            mail_conf = {
                "smtp": setting["mail_smtp"],
                "port": setting["mail_port"],
                "user": setting["mail_user"],
                "pwd": setting["mail_pwd"],
                "ssl": setting["mail_ssl"]
            }
            mail = Mail(**mail_conf)
            content = f"""
            {data['receiver']},
            上次阅读时间:{data['read_time']},
            第{read_count}次阅读,
            累计阅读{data['read_duration']}秒
            """
            send_data = {
                "subject": "信息阅读提醒",
                "content": content,
                "tolist": [setting["mail_recv"], ]
            }
            mail.ready(**send_data)
            self.guard.register(mail)

    async def post(self):
        """
        # 通过访问码查看简历
        :return: 简历数据 或者 错误数据
        """
        code = self.get_argument_str("access_code", min_len=4, max_len=31)
        ip = self.get_remote_ip()
        agent = self.get_user_agent()
        setting = SettingSrv.get_setting()

        if not self.acl_check(ip, code, agent):
            return

        if not self.enable_resume_check(setting, ip, code, agent):
            return

        resume_data = PublishSrv.get_published_resume(code)
        if not self.resume_exists_check(ip, code, agent, resume_data):
            return

        if not self.exp_time_check(ip, code, agent, resume_data):
            return

        data = {
            "exp_time": resume_data["exp_time"],
            "title": resume_data["title"],
            "text": resume_data["text"],
        }
        self.send_json({"code": 0, "resume": data})
        self.session["resume_access"] = "yes"

        # 更新阅读时间及阅读次数,并记录日志
        read_count = resume_data["read_count"] + 1
        update_data = {"read_count": read_count, "read_time": datetime.now()}
        PublishSrv.put_publish(resume_data["id"], **update_data)
        LoginLogSrv.add_log(
            True, LoginType.resume.value, ErrorType.no_error.value, ip, "resume_ok", code, agent)
        await self.send_mail(setting, read_count, resume_data)

    async def put(self):
        # 更新阅读时长
        code = self.get_argument_str("access_code", min_len=4, max_len=127)
        resume_data = PublishSrv.get_published_resume(code)
        if self.session["resume_access"] == "yes":
            self.send_json({"code": 0})
            # 阅读时长增加2秒钟
            read_duration = resume_data["read_duration"] + 2
            update_data = {"read_duration": read_duration}
            PublishSrv.put_publish(resume_data["id"], **update_data)
        else:
            self.send_json({"code": 432})


