#!/usr/bin/evn python3
# coding=utf-8

import selectors
import weakref
import tornado.web
import tornado.ioloop
import tornado.websocket
import tornado.web
from util.exception import AppException
from handler.base import BaseWebSocketHandler
from service.ssh import SSHSrv


class SSHWorker(object):

    def __init__(self):
        ssh, chan = SSHSrv.get_ssh_connect()
        self.loop = selectors.DefaultSelector()
        self.ssh = ssh
        self.chan = chan
        self.fd = chan.fileno()
        self.msg = []
        self.handler = None
        self.mode = selectors.EVENT_READ

    def __call__(self, fd, event):
        if event & selectors.EVENT_READ:
            self.on_read()
        if event & selectors.EVENT_WRITE:
            self.on_write()

    def set_handler(self, handler):
        if not self.handler:
            self.handler = handler

    def modify_handler(self, mode):
        if self.mode != mode:
            self.loop.modify(self.fd, mode)
            self.mode = mode
        if mode == selectors.EVENT_WRITE:
            self.on_write()

    def on_read(self):
        try:
            data = self.chan.recv(65535)
        except AppException as e:
            self.close(reason=str(e))
        else:
            self.handler.write_message(data, binary=True)

    def on_write(self):
        try:
            self.chan.send(''.join(self.msg))
            self.msg = []
        except AppException as e:
            self.close(reason=str(e))
        else:
            self.modify_handler(selectors.EVENT_READ)

    def close(self, reason=None):
        self.chan.close()
        self.ssh.close()
        self.handler.close(reason=reason)
        # self.loop.unregister(self.fd)


class WebSSHHandler(BaseWebSocketHandler):
    """
    # 实现网页SSH功能,前后端通过websock通讯
    """

    def initialize(self):
        self.loop = tornado.ioloop.IOLoop.current()
        self.handler_ref = None

    async def open(self):
        """
        # 打开的时候先要做认证检查
        """
        try:
            if self.auth_check():
                handler = SSHWorker()
                self.set_nodelay(True)
                handler.set_handler(self)
                self.handler_ref = weakref.ref(handler)
                if handler.fd not in self.loop.handlers:
                    self.loop.add_handler(handler.fd, handler, selectors.EVENT_READ)
            else:
                await self.write_message(f"web_sock_connect_error".encode("utf-8"), binary=True)
                self.on_close()
        except Exception as e:
            self.logger.error(f"web_sock_open_error:{e}")
            await self.write_message(f"web_sock_open_error:{e}".encode("utf-8"), binary=True)
            self.on_close()

    async def on_message(self, message):
        """
        # 消息处理
        :param message: 消息数据
        """
        try:
            handler = self.handler_ref()
            handler.msg.append(message)
            handler.on_write()
        except Exception as e:
            self.logger.error(f"web_on_message_error:{e}")
            self.on_close()

    def on_close(self):
        try:
            handler = self.handler_ref() if self.handler_ref else None
            if handler:
                handler.close()
        except Exception as e:
            self.logger.error(f"web_on_close_error:{e}")


# 为了方便测试,可以直接运行这个脚步
if __name__ == '__main__':
    url = [
        (r'/api/admin/web_ssh/', WebSSHHandler)
    ]
    loop = tornado.ioloop.IOLoop.current()
    app = tornado.web.Application(url)
    app.listen(8899, "0.0.0.0")
    loop.start()


"""
# 前端 vue 实现

// cnpm install --save xterm 
// cnpm install --save xterm-addon-attach

<template>
  <div>
    <div id="term"></div>
  </div>
</template>

<script>

import { Terminal } from 'xterm';
import { AttachAddon } from 'xterm-addon-attach';


export default {
  name: 'SSH',
  created(){
    var term = new Terminal();
    term.open(document.getElementById('term'));
    term.loadAddon(new AttachAddon(new WebSocket('ws://127.0.0.1:8899/api/admin/web_ssh/')));
    term.resize(120,30);
    this.term = term;
  },
  
  destroyed(){
    this.term.dispose()
  },
  data(){
    return {
      term : null
    }
  }
}
</script>


<style >

.xterm {
    font-feature-settings: "liga" 0;
    position: relative;
    user-select: none;
    -ms-user-select: none;
    -webkit-user-select: none;
}

.xterm.focus,
.xterm:focus {
    outline: none;
}

.xterm .xterm-helpers {
    position: absolute;
    top: 0;
    z-index: 5;
}

.xterm .xterm-helper-textarea {
    position: absolute;
    opacity: 0;
    left: -9999em;
    top: 0;
    width: 0;
    height: 0;
    z-index: -5;
    white-space: nowrap;
    overflow: hidden;
    resize: none;
}

.xterm .composition-view {
    background: #000;
    color: #FFF;
    display: none;
    position: absolute;
    white-space: nowrap;
    z-index: 1;
}

.xterm .composition-view.active {
    display: block;
}

.xterm .xterm-viewport {
    background-color: #000;
    overflow-y: scroll;
    cursor: default;
    position: absolute;
    right: 0;
    left: 0;
    top: 0;
    bottom: 0;
}

.xterm .xterm-screen {
    position: relative;
}

.xterm .xterm-screen canvas {
    position: absolute;
    left: 0;
    top: 0;
}

.xterm .xterm-scroll-area {
    visibility: hidden;
}

.xterm-char-measure-element {
    display: inline-block;
    visibility: hidden;
    position: absolute;
    top: 0;
    left: -9999em;
    line-height: normal;
}

.xterm {
    cursor: text;
}

.xterm.enable-mouse-events {
    cursor: default;
}

.xterm.xterm-cursor-pointer {
    cursor: pointer;
}

.xterm.column-select.focus {
    cursor: crosshair;
}

.xterm .xterm-accessibility,
.xterm .xterm-message {
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    right: 0;
    z-index: 10;
    color: transparent;
}

.xterm .live-region {
    position: absolute;
    left: -9999px;
    width: 1px;
    height: 1px;
    overflow: hidden;
}

.xterm-dim {
    opacity: 0.5;
}

.xterm-underline {
    text-decoration: underline;
}

</style>

"""


