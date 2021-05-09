#!/usr/bin/evn python3
# coding=utf-8

from service.review import ReviewSrv
from handler.admin.base import BaseAdminHandler


class ReviewHandler(BaseAdminHandler):
    """
    评论处理
    """

    async def get(self):
        """
        # 获取评论列表,没有按照套路出牌,应该是获取单条评论
        """
        page = self.get_argument_int("page", default="1")
        name_or_text_like = self.get_argument_str(
            "name_or_text_like",
            min_len=0,
            max_len=127,
            default=""
        )

        def response(request, max_page, review_list):
            request.send_json({"code": 0, "max_page": max_page, "review_list": review_list})

        if name_or_text_like == "":
            response(self, *ReviewSrv.get_review_list(page))
        else:
            response(self, *ReviewSrv.get_review_list(page, name_or_text_like))

    async def delete(self):
        """
        # 根据评论ID删除评论
        """
        review_id = self.get_argument_int("review_id")
        ReviewSrv.del_review(review_id)
        await self.get()


