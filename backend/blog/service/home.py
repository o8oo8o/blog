#!/usr/bin/evn python3
# coding=utf-8

from dao.blog import BlogDAO
from dao.setting import SettingDAO
from dao.review import ReviewDAO
from service.base import BaseSrv


class HomeSrv(BaseSrv):

    @staticmethod
    def get_home_init_data() -> dict:
        """
        # 获取主页初始化需要的数据
        """
        # 博客分类数据
        classify_info = [
            {
                "name": item["name"],
                "count": item["blog_count"]
            } for item in BlogDAO.select_classify_count()
        ]
        # 博客按年数据
        year_info = [
            {
                "name": item["year"],
                "count": item["blog_count"]
            } for item in BlogDAO.select_year_count()
        ]
        # 博客数据
        blog_list = [
            {
                "id": item["blog_id"],
                "title": item["title"],
                "classify_name": item["classify_name"],
                "create_time": item["create_time"].strftime('%Y-%m-%d %H:%M:%S'),
                "read_count": item["read_count"],
                "review_count": item["review_count"] if item["review_count"] else 0,
                "year": item["create_time"].year
            } for item in BlogDAO.select_blog_list()
        ]
        # 设置数据,注意下面的排除字段,因为有密码字段
        setting = SettingDAO.select_setting(
            "id",
            "metadata",
            "admin_user",
            "admin_pwd",
            "admin_title",
            "admin_name",
            "admin_blog_pz",
            "admin_review_pz",
            "admin_publish_pz",
            "ssh_height",
            "ssh_width",
            "ssh_host",
            "ssh_port",
            "ssh_pwd",
            "ssh_user",
            "chart_day",
            "chart_zero",
            "chart_border_width",
            "chart_bg_color",
            "chart_br_color",
            "admin_patch_html",
            "admin_patch_css",
            "admin_patch_js",
            "enable_resume",
            "music_dir",
            "mail_smtp",
            "mail_port",
            "mail_user",
            "mail_pwd",
            "mail_ssl",
            "mail_recv",
            "update_time",
            "create_time",
        )
        # 主页初始化数据,由上面的数据组成
        home_init_data = {
            "code": 0,
            "classify_info": classify_info,
            "year_info": year_info,
            "blog_list": blog_list,
            "setting": setting,
            "blog_count": len(blog_list),
            "review_count": ReviewDAO.select_review_count(),
        }

        return home_init_data


