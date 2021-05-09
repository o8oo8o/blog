#!/usr/bin/evn python3
# coding=utf-8

from smtplib import SMTP
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from util.actuator import AbcActuator
from util.logger import AppLog
from util.config import Config


class Mail(AbcActuator):
    """
    邮件发送功能
    """

    def __init__(self, smtp: str, port: int, user: str, pwd: str, ssl: bool = True):
        """
        :param smtp: 服务器地址
        :param port: 端口
        :param user: 用户名
        :param pwd: 密码
        :param ssl: 是否使用ssl,阿里云主机需要使用ssl方式发送,否则会失败
        """
        self.timeout = Config().get_conf("mail")["timeout"]
        self.smtp = smtp
        self.port = port
        self.user = user
        self.pwd = pwd
        self.ssl = ssl
        self.subject = ""
        self.content = ""
        self.tolist = []

    def _data(self, subject, content, tolist, cclist, bcclist, attachment):
        """
        构造邮件数据
        :param subject: 主题
        :param content: 内容
        :param tolist: 收件人列表
        :param cclist: 抄送人列表
        :param bcclist: 秘送人列表
        :param attachment: 附件列表
        :return:(收件人和抄送人列表,邮件内容(包含附件))
        """
        msg = MIMEMultipart()
        msg.set_charset("utf-8")
        msg["subject"] = subject

        msg["from"] = self.user
        msg["to"] = ",".join(tolist)

        addr_list = tolist

        # 抄送
        if cclist:
            msg["cc"] = ",".join(cclist)
            addr_list.extend(cclist)

        # 密送
        if bcclist:
            msg["bcc"] = ",".join(bcclist)
            addr_list.extend(bcclist)

        msg.attach(MIMEText(content, "html", "utf-8"))

        if attachment:
            for i in attachment:
                mimeapp = MIMEApplication(i["body"])
                mimeapp.add_header(
                    "content-disposition",
                    "attachment",
                    filename=i["filename"])
                msg.attach(mimeapp)
        return addr_list, msg

    def send(self,
             subject,
             content,
             tolist,
             cclist=None,
             bcclist=None,
             attachment=None):
        """
        发送邮件
        :param subject: 主题
        :param content: 内容
        :param tolist: 收件人列表
        :param cclist: 抄送人列表
        :param bcclist: 秘送人列表
        :param attachment: 附件列表
        :return: dict 是否发送成功,全部发送成功返回空字典,如果有发送失败的，显示失败信息
        """
        # 调用 构造邮件数据
        addr_list, msg = self._data(
            subject, content, tolist, cclist, bcclist, attachment)

        try:
            if self.ssl:
                smtp = SMTP_SSL(self.smtp, self.port,  timeout=self.timeout)
            else:
                smtp = SMTP(self.smtp, self.port, timeout=self.timeout)
            # smtp.set_debuglevel(1)
            smtp.ehlo()
            smtp.login(self.user, self.pwd)
            smtp.sendmail(self.user, addr_list, msg.as_string())
            smtp.quit()
        except Exception as exp:
            AppLog().logger.error(f"Mail Send Error: {exp}")

    def ready(self, *args, **kwargs) -> None:
        """
        # AbcActuator 的抽象方法，继承以后的具体实现
        :param args:
        :param kwargs:
        """
        self.subject = kwargs["subject"]
        self.content = kwargs["content"]
        self.tolist = kwargs["tolist"]

    def exe(self) -> None:
        """
        # AbcActuator 的抽象方法，继承以后的具体实现
        """
        self.send(self.subject, self.content, self.tolist)


if __name__ == "__main__":
    # 测试
    content = """
    <!DOCTYPE html>
    <head>
      <meta charset="UTF-8">
      <title>备份数据</title>
    </head>
    <body>
      <h1 style="color:red">huangrui</h1>
      <p>数据备份成功,详见附件</p>
    </body>
    </html>
    """
    mail = Mail(**{
        'smtp': 'smtp.exmail.qq.com',
        'port': 465,
        'user': 'send@huangrui.vip',
        'pwd': '12345678',
        'ssl': True
    })
    mail.send(
        "这是主题数据",
        content,
        ["774309635@qq.com"],
        ["b@huangrui.vip", "work@huangrui.vip"],
        ["c@huangrui.vip", "112233@qq.com"],
        [
            {"filename": "附件a.txt", "body": "内容数据".encode("utf-8")},
            {"filename": "附件b.txt", "body": open("blog.py", "rb").read()}
        ]
    )


