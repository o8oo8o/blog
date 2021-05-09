<template>
  <div class="wrapper">
    <nav class="main-header navbar navbar-expand navbar-white navbar-light">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" data-widget="pushmenu" href="#">
            <i class="fas fa-bars"></i>
          </a>
        </li>
        <li class="nav-item d-none d-sm-inline-block">
          <router-link :to="{name:'home'}" class="nav-link">主页</router-link>
        </li>
        <li class="nav-item">
          <a>
            <router-link :to="{name:'login'}" class="nav-link">
              <span @click="logout" style="color:red">
                退出&nbsp;&nbsp;
                <i class="fas fa-times"></i>
              </span>
            </router-link>
          </a>
        </li>
      </ul>

      <ul class="navbar-nav ml-auto">
        <!-- 聊天组件 -->
        <Chat></Chat>
        <!-- 聊天组件 -->

        <!-- 音乐播放组件 -->
        <Music></Music>
        <!-- 音乐播放组件 -->
      </ul>
    </nav>

    <aside class="main-sidebar sidebar-dark-primary elevation-4">
      <router-link :to="{name:'home'}" class="brand-link">
        <img
          :src="this.$store.state.setting.logo_path"
          alt="img"
          class="brand-image img-circle elevation-3"
          style="opacity: .8"
        />
        <span class="brand-text font-weight-light" v-text="this.$store.state.setting.admin_name"></span>
      </router-link>
      <div class="sidebar">
        <nav class="mt-2">
          <ul
            class="nav nav-pills nav-sidebar flex-column"
            data-widget="treeview"
            role="menu"
            data-accordion="false"
          >
            <li class="nav-item has-treeview menu-open">
              <router-link :to="{name:'home'}" class="nav-link active">
                <i class="nav-icon fas fa-tachometer-alt"></i>
                <p>
                  菜单
                  <i class="right fas fa-angle-left"></i>
                </p>
              </router-link>
              <ul class="nav nav-treeview">
                <li class="nav-item">
                  <router-link :to="{name:'classify'}" class="nav-link">
                    <i class="far fa-circle nav-icon"></i>
                    <p>分类管理</p>
                  </router-link>
                </li>
                <li class="nav-item">
                  <router-link :to="{name:'blog'}" class="nav-link">
                    <i class="far fa-circle nav-icon"></i>
                    <p>博客管理</p>
                  </router-link>
                </li>
                <li class="nav-item">
                  <router-link :to="{name:'review'}" class="nav-link">
                    <i class="far fa-circle nav-icon"></i>
                    <p>评论管理</p>
                  </router-link>
                </li>
                <li class="nav-item">
                  <router-link :to="{name:'resume'}" class="nav-link">
                    <i class="far fa-circle nav-icon"></i>
                    <p>个人信息</p>
                  </router-link>
                </li>
                <li class="nav-item">
                  <router-link :to="{name:'publish'}" class="nav-link">
                    <i class="far fa-circle nav-icon"></i>
                    <p>信息发布</p>
                  </router-link>
                </li>
                <li class="nav-item">
                  <router-link :to="{name:'setting'}" class="nav-link">
                    <i class="far fa-circle nav-icon"></i>
                    <p>控制面板</p>
                  </router-link>
                </li>
                <li class="nav-item">
                  <router-link :to="{name:'netdisk'}" class="nav-link">
                    <i class="far fa-circle nav-icon"></i>
                    <p>网络磁盘</p>
                  </router-link>
                </li>
                <li class="nav-item">
                  <router-link :to="{name:'monitor'}" class="nav-link">
                    <i class="far fa-circle nav-icon"></i>
                    <p>主机监控</p>
                  </router-link>
                </li>
                <li class="nav-item">
                  <router-link :to="{name:'remote'}" class="nav-link">
                    <i class="far fa-circle nav-icon"></i>
                    <p>远程管理</p>
                  </router-link>
                </li>
              </ul>
            </li>
          </ul>
        </nav>
      </div>
    </aside>

    <div class="content-wrapper" style="margin-top: 20px;margin-bottom: 0px;">
      <section class="content">
        <!-- 路由视图 -->
        <router-view></router-view>
      </section>
    </div>
    <!-- 页脚 -->
    <footer class="main-footer">
      <div class="float-center d-none d-sm-inline-block">
        <div v-html="this.$store.state.setting.footer"></div>
      </div>
    </footer>
  </div>
</template>

<script>
// @ is an alias to /src
import Music from "@/components/Music.vue";
import Chat from "@/components/Chat.vue";

export default {
  name: "home",
  components: {
    Music,
    Chat
  },
  created() {
    this.$store.dispatch("get_xsrf");
    let obj = {
      handle_type: "get"
    };
    this.$store.dispatch("setting_handler", obj);
  },
  methods: {
    logout() {
      this.$store.dispatch("logout");
    }
  },
  watch: {
    "$store.state.setting.admin_title": function(newVal, oldVal) {
      document.title = newVal;
    }
  }
};
</script>

