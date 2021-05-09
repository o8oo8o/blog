#!/usr/bin/evn python3
# coding=utf-8

from service.blog import BlogAdminSrv
from handler.admin.base import BaseAdminHandler


class BlogTitleCheckHandler(BaseAdminHandler):
    """
    # 检查blog标题是否存在
    """
    async def get(self):
        """
        # 检查blog标题是否存在,前端通过AJAX发送请求检查
        :return:
        """
        title = self.get_argument_str("title", 0, 127, default="")
        is_exists = BlogAdminSrv.get_title_exists(title)
        self.send_json({"code": 0, "is_exists": is_exists})


class BlogListHandler(BaseAdminHandler):
    """
    # 获取博客列表,根据博客标题搜索
    """
    async def get(self):
        """
        根据分页查询blog
        :return: 返回 blog 列表
        """
        await self._get_blog_list()

    async def _get_blog_list(self):
        """
        # 根据分页和搜索内容显示博客列表
        :return:
        """
        page = self.get_argument_int("page", default="1")
        title_like = self.get_argument_str(
            "title_like",
            min_len=0,
            max_len=127,
            default=""
        )

        def response(request, max_page, blog_data):
            return_data = {
                "code": 0,
                "max_page": max_page,
                "blog_list": blog_data
            }
            request.send_json(return_data)

        if title_like == "":
            response(self, *BlogAdminSrv.get_blog_list(page))
        else:
            response(self, *BlogAdminSrv.get_blog_list(page, title_like))


class BlogHandler(BlogListHandler):
    """
    # 博客增删改查
    """
    async def _get_param(self):
        title = self.get_argument_str("title", 1, 127)
        status = self.get_argument_int("status", 0, 1)
        text = self.get_argument_str("text", 1, 4294967295)
        is_review = self.get_argument_bool("is_review")
        is_public = self.get_argument_bool("is_public")
        weight = self.get_argument_int("weight", 1000, 3000)
        classify_id = self.get_argument_int("classify_id")
        params = {
            "title": title,
            "status": status,
            "text": text,
            "is_review": is_review,
            "is_public": is_public,
            "weight": weight,
            "classify_id": classify_id
        }
        return params

    async def get(self):
        """
        # 获取一个blog
        """
        blog_id = self.get_argument_int("blog_id")
        result_data = {"code": 0, **BlogAdminSrv.get_blog(blog_id)}
        self.send_json(result_data)

    async def post(self):
        """
        # 增加一个blog
        """
        data = await self._get_param()
        BlogAdminSrv.add_blog(**data)
        await self._get_blog_list()

    async def put(self):
        """
        # 更新一个blog
        """
        data = await self._get_param()
        blog_id = self.get_argument_int("blog_id")
        BlogAdminSrv.put_blog(blog_id, **data)
        await self._get_blog_list()

    async def delete(self):
        """
        # 删除一个blog
        """
        blog_id = self.get_argument_int("blog_id")
        BlogAdminSrv.del_blog(blog_id)
        await self._get_blog_list()


