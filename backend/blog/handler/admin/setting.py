#!/usr/bin/evn python3
# coding=utf-8

from service.setting import SettingSrv
from handler.admin.base import BaseAdminHandler


class SettingHandler(BaseAdminHandler):

    async def get(self):
        """
        # 获取用户设置
        """
        result_data = SettingSrv.get_setting()
        result_data["code"] = 0
        self.send_json(result_data)

    async def put(self):
        """
        # 更新用户设置
        """
        user_id = self.get_argument_int("id")
        admin_title = self.get_argument_str("admin_title", max_len=15)
        admin_name = self.get_argument_str("admin_name", max_len=15)
        email = self.get_argument_email("email", max_len=126)
        github_name = self.get_argument_str("github_name", max_len=126)
        github_addr = self.get_argument_str("github_addr", max_len=254)
        weibo_addr = self.get_argument_str("weibo_addr", max_len=254)
        weibo_name = self.get_argument_str("weibo_name", max_len=126)
        qq = self.get_argument_str("qq", max_len=15)
        wx = self.get_argument_str("wx", max_len=126)
        city = self.get_argument_str("city", max_len=14)

        logo_text = self.get_argument_str("logo_text", max_len=4)
        icon_text = self.get_argument_str("icon_text", max_len=4)
        web_title = self.get_argument_str("web_title", max_len=15)

        banner = self.get_argument_str("banner", min_len=0, max_len=4294967295)
        note = self.get_argument_str("note", min_len=0, max_len=6000)
        info = self.get_argument_str("info", min_len=0, max_len=6000)
        footer = self.get_argument_str("footer", max_len=60000)

        web_last_pz = self.get_argument_int("web_last_pz", min_val=1, max_val=10)
        web_blog_pz = self.get_argument_int("web_blog_pz", min_val=2, max_val=100)
        admin_blog_pz = self.get_argument_int("admin_blog_pz", min_val=2, max_val=100)
        admin_review_pz = self.get_argument_int("admin_review_pz", min_val=2, max_val=100)
        admin_publish_pz = self.get_argument_int("admin_publish_pz", min_val=2, max_val=100)

        enable_chat = self.get_argument_bool("enable_chat")
        enable_music = self.get_argument_bool("enable_music")
        enable_notice = self.get_argument_bool("enable_notice")
        enable_resume = self.get_argument_bool("enable_resume")

        ssh_host = self.get_argument_str("ssh_host", max_len=255)
        ssh_port = self.get_argument_int("ssh_port", min_val=1, max_val=65535)
        ssh_user = self.get_argument_str("ssh_user", max_len=255)
        ssh_pwd = self.get_argument_str("ssh_pwd", max_len=255)
        ssh_width = self.get_argument_int("ssh_width", min_val=29, max_val=601)
        ssh_height = self.get_argument_int("ssh_height", min_val=9, max_val=301)

        chart_day = self.get_argument_int("chart_day", min_val=3, max_val=90)
        chart_zero = self.get_argument_bool("chart_zero")
        chart_border_width = self.get_argument_int("chart_border_width", min_val=1, max_val=10)
        chart_bg_color = self.get_argument_str("chart_bg_color", max_len=63)
        chart_br_color = self.get_argument_str("chart_br_color", max_len=63)

        web_patch_html = self.get_argument_str("web_patch_html", min_len=0, max_len=4294967295)
        web_patch_css = self.get_argument_str("web_patch_css", min_len=0, max_len=4294967295)
        web_patch_js = self.get_argument_str("web_patch_js", min_len=0, max_len=4294967295)

        admin_patch_html = self.get_argument_str("admin_patch_html", min_len=0, max_len=4294967295)
        admin_patch_css = self.get_argument_str("admin_patch_css", min_len=0, max_len=4294967295)
        admin_patch_js = self.get_argument_str("admin_patch_js", min_len=0, max_len=4294967295)

        music_dir = self.get_argument_str("music_dir", max_len=127)
        mail_smtp = self.get_argument_str("mail_smtp", max_len=127)
        mail_port = self.get_argument_int("mail_port", min_val=1, max_val=65535)
        mail_user = self.get_argument_str("mail_user", max_len=127)
        mail_pwd = self.get_argument_str("mail_pwd", max_len=127)
        mail_ssl = self.get_argument_bool("mail_ssl")
        mail_recv = self.get_argument_str("mail_recv", max_len=127)

        profile_data = locals()
        profile_data.pop("self")
        profile_data.pop("user_id")
        SettingSrv.put_setting(user_id, profile_data)
        SettingSrv.commit()
        await self.get()


class AccountHandler(SettingHandler):
    """
    # 修改账号信息
    """

    async def put(self):
        """
        # 修改用户名及密码
        """
        user_id = self.get_argument_int("id")
        admin_user = self.get_argument_str("admin_user", max_len=126)
        admin_pwd = self.get_argument_pwd("admin_pwd", max_len=126)
        data = {"admin_user": admin_user, "admin_pwd": admin_pwd}
        SettingSrv.put_setting(user_id, data)
        self.send_json({"code": 0})


