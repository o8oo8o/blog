<template>
  <div id="app">
    <nav class="main-header navbar navbar-expand navbar-light navbar-white border-bottom">
      <div class="container">
        <a href="/" class="navbar-brand">
          <img
            :src="this.$store.state.home_data.setting.logo_path"
            alt="logo"
            class="brand-image img-circle elevation-3"
            style="opacity: .8"
          />
          <span
            class="brand-text font-weight-light"
            v-text="this.$store.state.home_data.setting.logo_text"
          ></span>
        </a>
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link class="nav-link" to="/home">主页</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/blog">文章</router-link>
          </li>
        </ul>

        <ul class="navbar-nav ml-auto">
          <!-- 聊天-->
          <Chat v-if="this.$store.state.home_data.setting.enable_chat"></Chat>

          <!-- 音乐 -->
          <Music v-if="this.$store.state.home_data.setting.enable_music"></Music>
        </ul>
      </div>
    </nav>
    <!-- 路由视图 -->
    <router-view />
    <footer class="main-footer text-sm" style="text-align: center">
      <span v-html="this.$store.state.home_data.setting.footer"></span>
    </footer>
  </div>
</template>

<script>
import Chat from "@/components/Chat.vue";
import Music from "@/components/Music.vue";

export default {
  name: "App",
  components: {
    Chat,
    Music
  },
  data() {
    return {
      home_data: this.$store.state.home_data
    };
  },

  created() {
    this.$store.dispatch("home_init");
  },
  methods: {}
};
</script>

<style>
a.router-link-exact-active {
  color: peru !important;
}

.content-wrapper {
  background: #e9ecef;
}
</style>
