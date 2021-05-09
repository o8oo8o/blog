<template>
  <div class="content-wrapper">
    <!-- 广告 -->
    <Banner />
    <section class="content">
      <div class="row col-md-10 offset-md-1">
        <div class="col-md-3">
          <div class="card card-primary">
            <div class="card-header">
              <h3 class="card-title">About Me</h3>
              <div class="card-tools">
                <button
                  type="button"
                  class="btn btn-tool"
                  data-card-widget="collapse"
                  data-toggle="tooltip"
                  title="Collapse"
                >
                  <i class="fas fa-minus"></i>
                </button>
                <button
                  type="button"
                  class="btn btn-tool"
                  data-card-widget="remove"
                  data-toggle="tooltip"
                  title="Remove"
                >
                  <i class="fas fa-times"></i>
                </button>
              </div>
            </div>
            <div class="card-body box-profile">
              <div class="text-center">
                <img
                  id="icon_path"
                  class="profile-user-img img-fluid img-circle"
                  :src="this.$store.state.home_data.setting.icon_path"
                  alt="图像"
                />
              </div>
              <h3
                id="icon_text"
                class="profile-username text-center"
                v-text="this.$store.state.home_data.setting.icon_text"
              ></h3>
              <p class="text-muted text-center"></p>
              <ul class="list-group list-group-unbordered mb-3">
                <li id="blog_count" class="list-group-item">
                  <b>文章</b>
                  <a class="float-right" v-text="this.$store.state.home_data.blog_count"></a>
                </li>
                <li id="review_count" class="list-group-item">
                  <b>留言</b>
                  <a class="float-right" v-text="this.$store.state.home_data.review_count"></a>
                </li>
                <li id="user_city" class="list-group-item">
                  <b>城市</b>
                  <a class="float-right" v-text="this.$store.state.home_data.setting.city"></a>
                </li>
                <li id="user_email" class="list-group-item">
                  <b>邮箱</b>
                  <a class="float-right" v-text="this.$store.state.home_data.setting.email"></a>
                </li>
                <li id="user_qq" class="list-group-item">
                  <b>QQ</b>
                  <a class="float-right" v-text="this.$store.state.home_data.setting.qq"></a>
                </li>
                <li id="user_wx"  class="list-group-item">
                  <b>微信</b>
                  <a class="float-right" v-text="this.$store.state.home_data.setting.wx"></a>
                </li>
                <li id="user_wb" class="list-group-item">
                  <b>微博</b>
                  <a
                    v-bind:href="this.$store.state.home_data.setting.weibo_addr"
                    class="float-right"
                  >
                    <span v-text="this.$store.state.home_data.setting.weibo_name"></span>
                  </a>
                </li>
                <li id="user_git"  class="list-group-item">
                  <b>GitHub</b>
                  <a
                    v-bind:href="this.$store.state.home_data.setting.github_addr"
                    class="float-right"
                  >
                    <span v-text="this.$store.state.home_data.setting.github_name"></span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
          <div class="card card-primary">
            <div class="card-header">
              <h3 class="card-title">说明</h3>
              <div class="card-tools">
                <button
                  type="button"
                  class="btn btn-tool"
                  data-card-widget="collapse"
                  data-toggle="tooltip"
                  title="Collapse"
                >
                  <i class="fas fa-minus"></i>
                </button>
                <button
                  type="button"
                  class="btn btn-tool"
                  data-card-widget="remove"
                  data-toggle="tooltip"
                  title="Remove"
                >
                  <i class="fas fa-times"></i>
                </button>
              </div>  
            </div>
            <div class="card-body">
              <div id="note">
                <div class="text-muted" v-html="this.$store.state.home_data.setting.note"></div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-9">
          <div class="card card-primary card-outline">
            <div class="card-header">
              <h3 class="card-title">最近更新</h3>
            </div>
            <div class="card-body">
              <div class="card" v-if="this.$store.state.home_data.setting.info.length > 0">
                <div class="card-body" style="display: block;">
                  <div id="info">
                      <span v-html="this.$store.state.home_data.setting.info"></span>
                  </div>
                </div>
              </div>
              <div
                class="card"
                v-for="(item, index) in this.$store.getters.home_blogs"
                :key="index"
              >
                <div class="card-header">
                  <h3 class="card-title">
                    <router-link :to="{ name:'show', params:{id:item.id} }" v-text="item.title"></router-link>
                  </h3>
                </div>
                <div class="card-body" style="display: block;">
                  创建时间:
                  <span v-text="item.create_time"></span>&nbsp;&nbsp;&nbsp;&nbsp;
                  阅读:
                  <span v-text="item.read_count"></span>&nbsp;&nbsp;&nbsp;&nbsp;
                  留言:
                  <span v-text="item.review_count"></span>&nbsp;&nbsp;&nbsp;&nbsp;
                  分类:
                  <span v-text="item.classify_name"></span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Banner from "@/components/Banner.vue";

export default {
  name: "home",
  props: {
    home_meta_data: {
      type: Object
    }
  },
  components: {
    Banner
  }
};
</script>
