#!/usr/bin/evn python3
# coding=utf-8

from handler.open.base import WebBaseHandler
from service.blog import BlogSrv


class BlogHandler(WebBaseHandler):

    async def get(self, blog_id):
        """
        # 根据博客ID获取一个博客
        :param blog_id: 博客ID
        """
        blog = BlogSrv.get_blog(int(blog_id), is_read=True)
        if blog:
            self.send_json({"code": 0, **blog})
        else:
            self.send_json({"code": 1})


