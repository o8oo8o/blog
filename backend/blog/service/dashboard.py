#!/usr/bin/evn python3
# coding=utf-8

from dao.setting import SettingDAO
from dao.blog import BlogDAO
from dao.review import ReviewDAO
from dao.publish import PublishDAO
from dao.accesslog import AccessLogDAO
from dao.loginlog import LoginLogDAO
from service.base import BaseSrv
from util.blogenum import LoginType


class DashboardSrv(BaseSrv):

    @classmethod
    def get_chart_data(cls, chart_day: int = 15) -> dict:
        """
        # 获取仪表板图表数据
        """
        # API调用统计
        api_call = {"date": [], "count": []}
        for item in AccessLogDAO.select_api_call_count(chart_day):
            api_call["date"].append(item["date"])
            api_call["count"].append(item["count"])

        # 用户访问统计
        user_access = {"date": [], "count": []}
        for item in AccessLogDAO.select_user_access_count(chart_day):
            user_access["date"].append(item["date"])
            user_access["count"].append(item["count"])

        # 后台登陆OK统计
        admin_login_ok = {"date": [], "count": []}
        for item in LoginLogDAO.select_login(True, LoginType.admin.value, chart_day):
            admin_login_ok["date"].append(item["date"])
            admin_login_ok["count"].append(item["count"])

        # 简历登陆OK统计
        resume_login_ok = {"date": [], "count": []}
        for item in LoginLogDAO.select_login(True, LoginType.resume.value, chart_day):
            resume_login_ok["date"].append(item["date"])
            resume_login_ok["count"].append(item["count"])

        # 后台登陆失败统计
        admin_login_fail = {"date": [], "count": []}
        for item in LoginLogDAO.select_login(False, LoginType.admin.value, chart_day):
            admin_login_fail["date"].append(item["date"])
            admin_login_fail["count"].append(item["count"])

        # 简历登陆失败统计
        resume_login_fail = {"date": [], "count": []}
        for item in LoginLogDAO.select_login(False, LoginType.resume.value, chart_day):
            resume_login_fail["date"].append(item["date"])
            resume_login_fail["count"].append(item["count"])

        return {
            "chart_api_call": api_call,
            "chart_user_access": user_access,
            "chart_admin_login_ok": admin_login_ok,
            "chart_resume_login_ok": resume_login_ok,
            "chart_admin_login_fail": admin_login_fail,
            "chart_resume_login_fail": resume_login_fail
        }

    @classmethod
    def get_access_data(cls) -> dict:
        """
        # 获取用户访问信息
        """
        # 日志总数
        log_count = AccessLogDAO.select_log_count()

        # 今日API调用次数
        api_call = AccessLogDAO.select_api_call_count(day_offset=0)
        if api_call:
            today_api_call = api_call[0]["count"]
        else:
            today_api_call = 0

        # 今日访问用户数
        user_access = AccessLogDAO.select_user_access_count(day_offset=0)
        if user_access:
            today_user_access = user_access[0]["count"]
        else:
            today_user_access = 0

        # 今日简历阅读数
        today_resume_read = PublishDAO.select_read_count(day_offset=0)
        if today_resume_read:
            today_resume_read = today_resume_read[0]["count"]
        else:
            today_resume_read = 0

        return {
            "log_count": log_count,
            "today_api_call": today_api_call,
            "today_user_access": today_user_access,
            "today_resume_read": today_resume_read
        }

    @classmethod
    def get_today_login_data(cls) -> dict:
        """
        # 获取今日后台及简历访问登陆信息
        """
        login_data = LoginLogDAO.select_today_login()
        today_login_data = {
            "admin_login_ok": 0,
            "admin_login_fail": 0,
            "resume_login_ok": 0,
            "resume_login_fail": 0
        }
        for item in login_data:
            if item["is_success"]:
                if item["login_type"] == LoginType.admin.value:
                    today_login_data["admin_login_ok"] += 1
                else:
                    today_login_data["resume_login_ok"] += 1
            else:
                if item["login_type"] == LoginType.admin.value:
                    today_login_data["admin_login_fail"] += 1
                else:
                    today_login_data["resume_login_fail"] += 1
        return today_login_data

    @classmethod
    def get_dashboard_data(cls) -> dict:
        """
        # 生成后台管理dashboard的展示的数据及图表数据
        """
        setting = SettingDAO.select_setting()
        # 图表展示数据的天数
        chart_day = setting["chart_day"]

        # 今日访问IP排行榜
        ip_top = AccessLogDAO.select_ip_top()

        # 今日慢请求排行榜
        low_top = AccessLogDAO.select_low_top()

        chart_data = cls.get_chart_data(chart_day)
        today_login = cls.get_today_login_data()
        access_data = cls.get_access_data()

        data = {
            "blog_publish_count": len(BlogDAO.select_blog_list()),
            "resume_publish_count": PublishDAO.select_publish_count(),
            "blog_count": BlogDAO.select_blog_count(),
            "review_count": ReviewDAO.select_review_count(),

            "log_count": access_data["log_count"],
            "today_api_call": access_data["today_api_call"],
            "today_user_access": access_data["today_user_access"],
            "today_resume_read": access_data["today_resume_read"],

            "today_admin_login_ok": today_login["admin_login_ok"],
            "today_admin_login_fail": today_login["admin_login_fail"],
            "today_resume_login_ok": today_login["resume_login_ok"],
            "today_resume_login_fail": today_login["resume_login_fail"],

            "chart_api_call": chart_data["chart_api_call"],
            "chart_user_access": chart_data["chart_user_access"],
            "chart_admin_login_ok": chart_data["chart_admin_login_ok"],
            "chart_resume_login_ok": chart_data["chart_resume_login_ok"],
            "chart_admin_login_fail": chart_data["chart_admin_login_fail"],
            "chart_resume_login_fail": chart_data["chart_resume_login_fail"],

            "ip_top": ip_top,
            "low_top": low_top,
            "conf": {
                "chart_zero": setting["chart_zero"],
                "chart_border_width": setting["chart_border_width"],
                "chart_bg_color": setting["chart_bg_color"],
                "chart_br_color": setting["chart_br_color"],
            }
        }

        return data


