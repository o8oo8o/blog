#!/usr/bin/evn python3
# coding=utf-8

from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.httpserver import HTTPServer
from util.config import Config
from url import URL
CONF = Config().get_dict()

if __name__ == "__main__":
    app = Application(URL, **CONF["app"])
    http_server = HTTPServer(
        app,
        max_buffer_size=CONF["server"]["max_buffer_size"],
        xheaders=True
    )
    http_server.bind(CONF["server"]["port"])
    http_server.start(1)
    IOLoop.current().start()


