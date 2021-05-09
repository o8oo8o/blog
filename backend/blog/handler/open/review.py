#!/usr/bin/evn python3
# coding=utf-8

from handler.open.base import WebBaseHandler
from service.blog import BlogSrv
from service.review import ReviewSrv
from handler.open.verifycode import check_verify_code


class ReviewHandler(WebBaseHandler):
    """
    # 新增评论
    """

    # 检查验证码装饰器
    @check_verify_code
    async def post(self):
        """
        # 新增评论
        :return: success_data 或者 error_data
        """
        blog_id = self.get_argument_int("blog_id")
        email = self.get_argument_email("email")
        name = self.get_argument_str("name", max_len=127)
        text = self.get_argument_str("text")
        ReviewSrv.add_review(blog_id, name, email,  text)
        self.send_json({
            "code": 0,
            "review_list": BlogSrv.get_blog_review_list(blog_id)
        })


