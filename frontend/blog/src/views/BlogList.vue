<template>
  <div class="content-wrapper">
    <!-- 广告 -->
    <Banner />
    <section class="content">
      <div class="row col-md-10 offset-md-1">
        <div class="col-md-3">
          <div class="card card-primary">
            <div class="card-header">
              <h3 class="card-title">分类</h3>
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
            <div class="card-body p-0">
              <ul class="nav nav-pills flex-column">
                <li v-for="(item, index) in this.$store.state.home_data.classify_info" :key="index">
                  <router-link
                    class="nav-link"
                    :to="{ name:'classify', params:{classify:item.name} }"
                  >
                    <i class="far text-primary">•</i> &nbsp;
                    <span v-text="item.name"></span>
                    <span class="badge bg-primary float-right" v-text="item.count"></span>
                  </router-link>
                </li>
              </ul>
            </div>
          </div>
          <div class="card card-primary">
            <div class="card-header">
              <h3 class="card-title">年份</h3>
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
            <div class="card-body p-0">
              <ul class="nav nav-pills flex-column">
                <li v-for="(item, index) in this.$store.state.home_data.year_info" :key="index">
                  <router-link class="nav-link" :to="{ name:'year', params:{year:item.name} }">
                    <i class="far text-primary">•</i> &nbsp;
                    <span v-text="item.name"></span>
                    <span class="badge bg-primary float-right" v-text="item.count"></span>
                  </router-link>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="col-md-9">
          <div class="card card-primary card-outline">
            <div class="card-header">
              <h3 class="card-title">文章</h3>
              <div class="card-tools">
                <div class="input-group-sm">
                  <input
                    type="text"
                    class="form-control"
                    placeholder="搜索文章"
                    v-model.trim="blog_search_text"
                    @input="blog_search"
                  />
                </div>
              </div>
            </div>
            <div class="card-body">
              <div class="table-responsive">
                <table class="table text-nowrap">
                  <thead>
                    <tr>
                      <td>
                        <b>标题</b>
                      </td>
                      <td>
                        <b>分类</b>
                      </td>
                      <td>
                        <b>阅读</b>
                      </td>
                      <td>
                        <b>留言</b>
                      </td>
                      <td>
                        <b>发布时间</b>
                      </td>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, index) in this.$store.state.current_blog_list" :key="index">
                      <td class="mailbox-subject">
                        <span v-text="index +1"></span>&nbsp;&nbsp;
                        <router-link :to="{ name:'show', params:{id:item.id} }" v-text="item.title"></router-link>
                      </td>
                      <td class="mailbox-name" v-text="item.classify_name"></td>
                      <td class="mailbox-attachment" v-text="item.read_count"></td>
                      <td class="mailbox-attachment" v-text="item.review_count"></td>
                      <td class="mailbox-date" v-text="item.create_time"></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="card-footer">
              <div>
                <span class="float-right col-12-sm">
                  <div class="card-tools">
                    <div class="input-group">
                      <div class="input-group-prepend">
                        <span
                          class="btn btn-info"
                          @click="prev_page"
                          v-if="this.$store.state.current_page > 1"
                        >
                          <div>&lt;</div>
                        </span>
                        <span class="input-group-text">
                          <span v-text="this.$store.state.current_page"></span>&nbsp;/&nbsp;
                          <span v-text="this.$store.getters.end_page"></span>
                        </span>
                        <span
                          class="btn btn-info"
                          @click="next_page"
                          v-if="this.$store.state.current_page < this.$store.getters.end_page"
                        >
                          <div>&gt;</div>
                        </span>
                      </div>
                      <input
                        v-model.number="page_no"
                        type="number"
                        class="form-control"
                        placeholder="页码"
                        size="5"
                        min="1"
                        max="999"
                        style="width:80px"
                      />
                      <div class="input-group-append">
                        <div class="btn btn-primary">
                          <i @click="go_page">Go</i>
                        </div>
                      </div>
                    </div>
                  </div>
                </span>
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
  name: "blog_list",
  props: {
    home_meta_data: {
      classify: Object
    }
  },
  components: {
    Banner
  },
  data() {
    return {
      blog_search_text: "",
      page_no: ""
    };
  },
  watch: {
    "$route.path": function(newVal, oldVal) {
      let filter_array = String(newVal).split("/");
      this.$store.commit("GetBlogList", filter_array);
    }
  },

  methods: {
    // 跳转到指定页
    go_page() {
      let num = this.page_no;
      if (typeof num != "number") {
        // 输入的不是数字跳转到第一页
        num = 1;
      }
      if (num > this.$store.getters.end_page) {
        // 输入数字大于总页数,直接跳到最后一页
        num = this.$store.getters.end_page;
      }
      this.$store.commit("GoPage", num);
    },
    // 下一页
    next_page() {
      this.$store.commit("NextPage");
    },
    // 上一页
    prev_page() {
      this.$store.commit("PrevPage");
    },
    // 博客搜索
    blog_search() {
      let sub_search_path = String(this.$route.path).trim();
      let search_info = {
        sub_search_path: String(this.$route.path).trim(),
        blog_search_text: this.blog_search_text
      };
      let filter_array = String(this.$route.path).split("/");
      this.$store.commit("GetBlogList", filter_array); // 这一步操作目的，恢复搜索前的内容
      this.$store.commit("BlogSearch", search_info);
    }
  },
  created() {
    let filter_array = ["", "blog"];
    this.$store.commit("GetBlogList", filter_array);
  }
};
</script>
