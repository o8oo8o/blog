<template>
  <div>
    <div id="term"></div>
  </div>
</template>

<script>
import { Terminal } from "xterm";
import { AttachAddon } from "xterm-addon-attach";

export default {
  name: "remote",
  beforeRouteLeave(to, from, next) {
    // 导航离开该组件的对应路由时调用
    // 可以访问组件实例 `this`
    this.sock.close();
    this.term.dispose();
    next();
  },
  mounted() {
    var term = new Terminal();
    term.open(document.getElementById("term"));
    var protocol = location.protocol == "http:" ? "ws://" : "wss://";
    var host = location.host;
    var cookie_data = document.cookie.replace(" ", "").replace(";", "&");
    var sock_url = protocol + host + "/api/admin/web_ssh/?" + cookie_data;
    this.sock = new WebSocket(sock_url);
    term.loadAddon(new AttachAddon(this.sock));
    term.resize(
      this.$store.state.setting.ssh_width,
      this.$store.state.setting.ssh_height
    );
    this.term = term;
  },
  beforeDestroy() {
    this.sock.close();
    this.term.dispose();
  },
  data() {
    return {
      term: null,
      sock: null
    };
  }
};
</script>

<style>
/* 上面没有加上scope,是因为放在这里看着方便 */

.xterm {
  font-feature-settings: "liga" 0;
  position: relative;
  user-select: none;
  -ms-user-select: none;
  -webkit-user-select: none;
  margin-top: 20px;
  margin-bottom: 20px;
  margin-left: 10px;
  margin-right: 20px;
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
  color: #fff;
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
