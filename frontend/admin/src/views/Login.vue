<template>
  <div>
    <div class="container">
      <form class="form-signin">
        <h2 class="text-center">欢迎登陆</h2>
        <br />
        <div class="input-group mb-3">
          <div class="input-group-prepend">
            <span class="input-group-text" id="user">账号</span>
          </div>
          <input
            name="user"
            v-model="user"
            type="text"
            class="form-control"
            placeholder="账号"
            aria-label="name"
            aria-describedby="name"
            required
            autofocus
          />
        </div>

        <div class="input-group mb-3">
          <div class="input-group-prepend">
            <span class="input-group-text" id="pwd">密码</span>
          </div>
          <input
            name="pwd"
            v-model="pwd"
            type="password"
            class="form-control"
            placeholder="密码"
            aria-label="pwd"
            aria-describedby="pwd"
            required
          />
        </div>
        <div class="checkbox">
          <label>
            <input type="checkbox" v-model="rem" name="rem" />记住密码
          </label>
        </div>
        <button class="btn btn-lg btn-primary btn-block" type="button" @click="login">登陆</button>
      </form>
    </div>
    <div
      class="modal fade"
      id="loginModal"
      tabindex="-1"
      role="dialog"
      aria-labelledby="loginModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title" id="loginModalLabel">用户名或密码错误</h4>
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
          </div>
          <div class="modal-body">请检查用户名或者密码</div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "login",
  created() {
    this.$store.dispatch("get_xsrf");
    this.$store.commit("UpdateAuth", false);
    localStorage.clear();
  },
  data() {
    return {
      user: "",
      pwd: "",
      rem: false
    };
  },
  methods: {
    login() {
      let user_reg = /^[A-Za-z0-9_]{2,63}$/;
      if (!user_reg.test(this.user)) {
        $("#loginModal").modal("show");
        return;
      }
      let pwg_reg = /^[A-Za-z0-9_]{5,63}$/;
      if (!pwg_reg.test(this.pwd)) {
        $("#loginModal").modal("show");
        return;
      }
      var fm = new FormData();
      fm.append("user", this.user);
      fm.append("pwd", this.pwd);
      fm.append("rem", this.rem);
      fm.append("_xsrf", this.$store.state._xsrf);
      axios.defaults.headers.common["X-Xsrftoken"] = this.$store.state._xsrf;
      var that = this;
      axios
        .post("/api/admin/login/", fm, {
          headers: { "Content-Type": "application/x-www-form-urlencoded" }
        })
        .then(function(response) {
          let data = response.data;
          if (data.code == 1) {
            $("#loginModal").modal("show");
          }

          if (data.code == 0) {
            localStorage.setItem("auth", "yes");
            that.$store.commit("UpdateAuth", true);
            that.$router.replace({ name: "home" });
          }
        })
        .catch(function(error) {
          console.log("login_error");
        });
    }
  }
};
</script>


<style scope>
body {
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #eee;
}

.form-signin {
  max-width: 330px;
  padding: 15px;
  margin: 0 auto;
}
.form-signin .form-signin-heading,
.form-signin .checkbox {
  margin-bottom: 10px;
}
.form-signin .checkbox {
  font-weight: normal;
}
.form-signin .form-control {
  position: relative;
  height: auto;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  padding: 10px;
  font-size: 16px;
}
.form-signin .form-control:focus {
  z-index: 2;
}
</style>
