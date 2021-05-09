<template>
  <div class="content-wrapper">
    <div v-if="! this.$store.state.resume_load_ok" class="hold-transition">
      <div>
        <br />
        <br />
        <br />
        <br />
        <div class="lockscreen">
          <div class="lockscreen-logo">
            <a href="/">
              <b>简历查看</b>
            </a>
          </div>
          <div class="lockscreen-name">请输入访问码</div>
          <div class="lockscreen-item">
            <div class="lockscreen-image" style="margin-right:100px;">
              <img :src="this.$store.state.home_data.setting.icon_path" alt="img" />
            </div>
            <form class="lockscreen-credentials">
              <div class="input-group">
                <input
                  :type="input_type"
                  v-model="access_code"
                  @input="clear_error_msg"
                  minlength="4"
                  maxlength="30"
                  class="form-control"
                  autofocus
                  required="required"
                  placeholder="password"
                />
                <div class="input-group-append">
                  <button type="button" class="btn" @click="show_pwd">
                    <span v-html="eye"></span>
                  </button>
                  <button type="button" class="btn" @click="get_resume">
                    <i class="fas fa-arrow-right text-muted"></i>
                  </button>
                </div>
              </div>
            </form>
          </div>
          <div id="error">
            <div class="help-block text-center" v-text="input_error_msg"></div>
            <div class="help-block text-center" v-text="resume_load_error_msg"></div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="this.$store.state.resume_load_ok" id="resume">
      <br />
      <section class="content">
        <div class="row col-md-10 offset-md-1">
          <div class="col-md-12">
            <div class="card card-primary card-outline">
              <div class="card-header" style="text-align: center">
                <h5 v-text="this.$store.state.resume.title"></h5>
              </div>
              <div class="card-header">
                <span class="text-danger">
                  访问码过期时间:
                  <span v-text="this.$store.state.resume.exp_time"></span>
                </span>
              </div>
              <div class="card-body">
                <div v-html="this.$store.state.resume.text"></div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: "resume",
  beforeRouteLeave(to, from, next) {
    // 导航离开该组件的对应路由时调用
    // 可以访问组件实例 `this`
    clearInterval(this.crontab);
    next();
  },
  created() {
    this.$store.dispatch("get_xsrf");
    this.$store.dispatch("home_init");
  },
  mounted() {},
  beforeDestroy() {
    clearInterval(this.crontab);
  },
  data() {
    return {
      input_type: "password",
      access_code: "",
      input_error_msg: "",
      eye: '<i class="fas fa-eye-slash text-muted">',
      crontab: ""
    };
  },
  methods: {
    // 显示及隐藏访问码
    show_pwd() {
      this.input_type = this.input_type == "password" ? "text" : "password";
      this.eye =
        this.input_type == "password"
          ? '<i class="fas fa-eye-slash text-muted">'
          : '<i class="fas fa-eye text-muted">';
    },
    // 在输入的时候,清理掉错误信息
    clear_error_msg() {
      this.input_error_msg = "";
      this.$store.commit("UpdateResumeLoadErrorMsg", "");
    },
    // 获取简历数据
    get_resume() {
      if (this.access_code.length < 4) {
        this.input_error_msg = "访问码错误!";
      } else {
        this.$store.dispatch("get_resume", this.access_code);
      }
    }
  },
  watch: {
    "$store.state.resume_load_ok": function(newVal, oldVal) {
      if (newVal) {
        let that = this;
        that.crontab = setInterval(() => {
          that.$store.dispatch("put_read_duration");
        }, 2000);

        document.addEventListener("visibilitychange", function() {
          // 用户离开了当前页面
          if (document.visibilityState === "hidden") {
            // document.title = "页面不可见";
            clearInterval(that.crontab);
          }

          // 用户打开或回到页面
          if (document.visibilityState === "visible") {
            // document.title = "页面可见";
            clearInterval(that.crontab);
            that.crontab = setInterval(() => {
              that.$store.dispatch("put_read_duration");
            }, 2000);
          }
        });
      }
    }
  },
  computed: {
    resume_load_error_msg: {
      get() {
        return this.$store.state.resume_load_error_msg;
      }
    }
  }
};
</script>

<style scope>
#error {
  color: red;
}
</style>
