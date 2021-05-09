<template>
  <div>
    <li class="nav-item dropdown">
      <a class="nav-link" data-toggle="dropdown" href="#">
        <i class="fas fa-comments"></i>
      </a>
      <div
        @click.stop
        id="chat_body"
        class="dropdown-menu dropdown-menu-lg dropdown-menu-right"
        style="margin-right: -51px; width: 280px;"
      >
        <div id="chat_box" class="card direct-chat direct-chat-info">
          <div class="card-header">
            <h3 class="card-title">聊天室</h3>
            <div class="card-tools">
              <span data-toggle="tooltip" class="badge badge-info">
                <span v-text="online"></span>人在线
              </span>
            </div>
          </div>
          <div id="card-body">
            <div id="msg_box" class="direct-chat-messages">
              <div v-for="(item, index) in all_msg" :key="index">
                <!-- 左侧 -->
                <div v-if="item.uid != uid" class="direct-chat-msg">
                  <div class="direct-chat-infos clearfix">
                    <span class="direct-chat-name float-left" v-text="item.uid"></span>
                    <span class="direct-chat-timestamp float-right" v-text="item.time"></span>
                  </div>
                  <img class="direct-chat-img" :src="item.img" />
                  <div class="direct-chat-text" v-text="item.msg"></div>
                </div>

                <!-- 右侧 -->
                <div v-if="item.uid == uid" class="direct-chat-msg right">
                  <div class="direct-chat-infos clearfix">
                    <span class="direct-chat-name float-right" v-text="item.uid"></span>
                    <span class="direct-chat-timestamp float-left" v-text="item.time"></span>
                  </div>
                  <img class="direct-chat-img" :src="user_img" />
                  <div class="direct-chat-text" v-text="item.msg"></div>
                </div>
              </div>
            </div>
          </div>
          <div class="card-footer">
            <div class="input-group">
              <input
                v-model.trim="send_msg"
                id="send_text"
                type="text"
                name="message"
                placeholder="消息内容"
                class="form-control"
              />
              <span class="input-group-append">
                <button id="send_button" type="button" class="btn btn-primary" @click="send">发送</button>
              </span>
            </div>
          </div>
        </div>
      </div>
    </li>
  </div>
</template>

<script>
export default {
  name: "chat",
  data() {
    return {
      socket: "",
      send_msg: "",
      uid: "",
      online: 1,
      all_msg: [],
      user_img: ""
    };
  },
  mounted() {
    // 初始化
    let user_id = this.gen_uid();
    this.uid = user_id;
    this.user_img = `img/chat/g${user_id % 17}.ico`;
    this.init();
  },
  methods: {
    time_now: function(fmt) {
      var t = new Date();
      var o = {
        "M+": t.getMonth() + 1, //月份
        "d+": t.getDate(), //日
        "h+": t.getHours(), //小时
        "m+": t.getMinutes(), //分
        "s+": t.getSeconds(), //秒
        "q+": Math.floor((t.getMonth() + 3) / 3), //季度
        S: t.getMilliseconds() //毫秒
      };
      if (/(y+)/.test(fmt)) {
        fmt = fmt.replace(
          RegExp.$1,
          (t.getFullYear() + "").substr(4 - RegExp.$1.length)
        );
      }
      for (var k in o) {
        if (new RegExp("(" + k + ")").test(fmt)) {
          fmt = fmt.replace(
            RegExp.$1,
            RegExp.$1.length == 1
              ? o[k]
              : ("00" + o[k]).substr(("" + o[k]).length)
          );
        }
      }
      return fmt;
    },
    init: function() {
      if (typeof WebSocket === "undefined") {
        console.log("您的浏览器不支持socket");
      } else {
        var protocol = location.protocol == "http:" ? "ws://" : "wss://";
        var host = location.host;
        var sock_url =
          protocol +
          host +
          "/api/open/chat/?" +
          document.cookie.replace(" ", "").replace(";", "&");
        // 实例化socket
        this.socket = new WebSocket(sock_url);
        // 监听socket连接
        this.socket.onopen = this.open;
        // 监听socket错误信息
        this.socket.onerror = this.error;
        // 监听socket消息
        this.socket.onmessage = this.recv;
      }
    },
    gen_uid: function() {
      return Math.floor(Math.random() * 100000000 + 1);
    },
    open: function() {
      //console.log("socket连接成功");
      let t = new Date();
      let data = {
        uid: this.uid,
        msg: "亲,欢迎进入聊天室!",
        img: this.user_img,
        time: this.time_now("hh:mm:ss")
      };
      // {"online": 1, "msg": {"uid": 83388752, "msg": "sdf", "img": "dist/img/img/g8.ico", "time": "19:44:51"}}
      this.send(JSON.stringify(data));
      //this.all_msg.push(data);
    },
    error: function() {
      console.log("socket连接错误");
    },
    recv: function(msg) {
      let recv_data = JSON.parse(msg.data);
      this.online = recv_data.online;
      this.all_msg.push(recv_data.msg);
    },
    send: function(e) {
      if (typeof e == "object") {
        e.stopPropagation();
      }

      if (this.send_msg.length == 0) {
        return;
      }
      let t = new Date();
      let msg_data = {
        uid: this.uid,
        msg: this.send_msg,
        img: this.user_img,
        time: this.time_now("hh:mm:ss")
      };
      this.socket.send(JSON.stringify(msg_data));
      this.send_msg = "";
    },
    close: function() {
      // console.log("socket已经关闭");
    }
  },
  updated() {
    // 更新滚动条对位置
    let msg_box = document.getElementById("msg_box");
    msg_box.scrollTop = 1000000000;
  },
  destroyed() {
    // 销毁监听
    // this.socket.onclose = this.close;
  }
};
</script>



