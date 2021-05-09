<template>
  <div class="content-wrapper">
    <Banner />
    <section class="content">
      <div class="row col-md-10 offset-md-1">
        <div class="col-md-12">
          <div class="card card-primary card-outline">
            <div class="card-header">
              <h5 v-text="this.$store.state.blog.title"  style="text-align: center" ></h5>
            </div>
            <div class="card-header">
              发布时间:
              <span v-text="this.$store.state.blog.create_time"></span>
              &nbsp;&nbsp;
              <span class="float-right">
                阅读:
                <span v-text="this.$store.state.blog.read_count"></span> &nbsp;&nbsp;
                留言:
                <span v-text="this.$store.state.blog.review_count"></span> &nbsp;&nbsp;
                分类:
                <span v-text="this.$store.state.blog.classify_name"></span>
              </span>
            </div>
            <div class="card-body">
              <!-- 博客正文 -->
              <div id="blog_text">
                <div v-html="this.$store.state.blog.text"></div>
              </div>
            </div>

            <div class="card-footer">
              <h6>
                <span v-if="this.$store.state.blog.prev_blog.is_exists">
                  上一篇:
                  <a
                    v-text="this.$store.state.blog.prev_blog.title"
                    :href="this.$store.getters.get_prev_link"
                  ></a>
                </span>
                <hr />
                <span v-if="this.$store.state.blog.next_blog.is_exists">
                  下一篇:
                  <a
                    v-text="this.$store.state.blog.next_blog.title"
                    :href="this.$store.getters.get_next_link"
                  ></a>
                </span>
              </h6>
              <hr />
            </div>
            <div v-if="this.$store.state.blog.is_review" class="card-body">
              <ul class="nav nav-tabs" id="review-tab" role="tablist">
                <li class="nav-item">
                  <a
                    class="nav-link active"
                    id="review-list-tab"
                    data-toggle="pill"
                    href="#review-list"
                    role="tab"
                    aria-controls="review-list"
                    aria-selected="true"
                  >留言列表</a>
                </li>
                <li class="nav-item">
                  <a
                    class="nav-link"
                    id="review-post-tab"
                    data-toggle="pill"
                    href="#review-post"
                    role="tab"
                    aria-controls="review-post"
                    aria-selected="false"
                  >发布留言</a>
                </li>
              </ul>

              <div class="tab-custom-content">
                <!-- <p class="lead mb-0">Custom Content goes here</p> -->
              </div>

              <div class="tab-content" id="review-tab-content">
                <div
                  class="tab-pane fade active show"
                  id="review-list"
                  role="tabpanel"
                  aria-labelledby="review-list-tab"
                >
                  <div class="card-footer card-comments">
                    <div
                      class="card-comment"
                      v-for="(item, index) in this.$store.state.blog.review_list"
                      :key="index"
                    >
                      <span>
                        <b v-text="index+1"></b>
                        <b>楼:</b>
                      </span>

                      <div class="comment-text">
                        <span class="username">
                          <span v-text="item.name"></span>
                          <span class="text-muted float-right" v-text="item.create_time"></span>
                        </span>
                        <span v-text="item.text"></span>
                        <br />
                      </div>
                    </div>
                  </div>
                </div>
                <div
                  class="tab-pane fade"
                  id="review-post"
                  role="tabpanel"
                  aria-labelledby="blog_review"
                >
                  <div id="review">
                    <form role="form">
                      <input type="hidden" name="_xsrf" v-model="this.$store.state._xsrf" />
                      <div class="form-group">
                        <label>邮箱(保密)</label>
                        <input
                          type="email"
                          v-model.trim="review_email"
                          required="required"
                          id="review_email"
                          name="review_email"
                          maxlength="120"
                          class="form-control"
                          placeholder="请输入你的邮箱"
                        />
                      </div>
                      <div class="form-group">
                        <label>名字(公开)</label>
                        <input
                          type="text"
                          v-model.trim="review_name"
                          required="required"
                          id="review_name"
                          name="review_name"
                          maxlength="120"
                          class="form-control"
                          placeholder="请输入你的名字"
                        />
                      </div>
                      <div class="form-group">
                        <label>内容(公开)</label>
                        <textarea
                          class="form-control"
                          rows="3"
                          v-model.trim="review_text"
                          required="required"
                          id="review_text"
                          name="review_text"
                          maxlength="65000"
                          placeholder="请输入内容"
                        ></textarea>
                      </div>
                      <div class="form-group">
                        <label>
                          验证码(
                          <span style="color:red">点击图片刷新</span>)
                        </label>
                        <i class="fas fa-refresh" style="font-size:24px"></i>
                      </div>
                      <div class="row form-group">
                        <div class="col-lg-2">
                          <div class="input-group">
                            <img
                              :src="this.$store.state.blog_review.verify_code_img"
                              @click="refresh_verify_code"
                              alt="验证码"
                              title="点击换一张"
                              style="margin-top: 1%;"
                            />
                          </div>
                        </div>
                        <div class="col-lg-2">
                          <div class="input-group">
                            <input
                              id="verify_code"
                              v-model.trim="verify_code"
                              type="text"
                              required="required"
                              class="form-control"
                              placeholder="请输入验证码"
                              maxlength="4"
                            />
                          </div>
                        </div>
                        <div class="col-lg-8">
                          <div class="input-group">
                            <span
                              v-if="show_verify_result"
                              id="show_verify_result"
                              class="input-group-text"
                            >
                              <span
                                v-if="this.$store.state.verify_code_check_result"
                                id="verify_ok"
                              >验证码正确</span>
                              <span
                                v-if="! this.$store.state.verify_code_check_result"
                                id="verify_no"
                              >验证码错误</span>
                            </span>
                          </div>
                        </div>
                      </div>
                    </form>
                  </div>
                  <div class="card-footer">
                    <button
                      type="button"
                      @click="post_review"
                      class="btn btn-primary float-right"
                    >提交留言</button>
                  </div>
                  <!-- 信息错误提示模态框 -->
                  <div
                    class="modal fade"
                    id="error_modal"
                    tabindex="-1"
                    role="dialog"
                    aria-labelledby="error_modalLabel"
                    aria-hidden="true"
                  >
                    <div class="modal-dialog">
                      <div class="modal-content bg-warning">
                        <div class="modal-header">
                          <h4 class="modal-title" id="error_modalLabel" v-text="error_title"></h4>
                          <button
                            type="button"
                            class="close"
                            data-dismiss="modal"
                            aria-hidden="true"
                          >&times;</button>
                        </div>
                        <div class="modal-body" v-text="error_msg"></div>
                        <div class="modal-footer">
                          <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- 操作成功模态框 -->
                  <div
                    class="modal fade"
                    id="succees_modal"
                    tabindex="-1"
                    role="dialog"
                    aria-labelledby="succees_modalLabel"
                    aria-hidden="true"
                  >
                    <div class="modal-dialog">
                      <div class="modal-content bg-success">
                        <div class="modal-header">
                          <h4 class="modal-title" id="succees_modalLabel">留言信息</h4>
                          <button
                            type="button"
                            class="close"
                            data-dismiss="modal"
                            aria-hidden="true"
                          >&times;</button>
                        </div>
                        <div class="modal-body">恭喜你!提交成功</div>
                        <div class="modal-footer">
                          <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                        </div>
                      </div>
                    </div>
                  </div>
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
  name: "blog_show",
  props: {
    home_meta_data: {
      type: Object
    }
  },
  components: {
    Banner
  },
  data() {
    return {
      error_title: "",
      error_msg: "",
      show_verify_result: false
    };
  },
  methods: {
    // 获取一个博客
    get_blog(id) {
      let blog_id = Number.parseInt(id);
      this.$store.dispatch("get_blog", blog_id);
      this.$store.dispatch("get_verify_code");
    },
    // 刷新验证码
    refresh_verify_code() {
      this.$store.dispatch("get_verify_code");
    },
    // 提交评论
    post_review() {
      let verify_input = true;
      let email_reg = /^(\w-*\.*)+@(\w-?)+(\.\w{2,})+$/;
      if (!email_reg.test(this.review_email)) {
        this.error_title = "邮箱错误";
        this.error_msg = "请检查邮箱地址";
        $("#error_modal").modal("show");
        verify_input = false;
        return;
      }
      if (this.review_name.length == 0 || this.review_name.length > 120) {
        this.error_title = "名字错误";
        if (this.review_name.length == 0) {
          this.error_msg = "名字不能为空";
          $("#error_modal").modal("show");
          verify_input = false;
          return;
        }
        if (this.review_name.length > 120) {
          this.error_msg = "名字长度不能超过120个字符";
          $("#error_modal").modal("show");
          verify_input = false;
          return;
        }
      }
      if (this.review_text.length == 0 || this.review_text.length > 65000) {
        this.error_title = "评论错误";
        if (this.review_text.length == 0) {
          this.error_msg = "评论内容不能为空";
          $("#error_modal").modal("show");
          verify_input = false;
          return;
        }
        if (this.review_text.length > 120) {
          this.error_msg = "评论内容长度不能超过65000个字符";
          $("#error_modal").modal("show");
          verify_input = false;
          return;
        }
      }
      if (this.verify_code.length < 4) {
        this.error_title = "验证码错误";
        this.error_msg = "验证码输入错误";
        $("#error_modal").modal("show");
        verify_input = false;
        if (!this.$store.state.verify_code_check_result) {
          this.error_msg = "验证码输入错误,点击图片刷新验证码";
          $("#error_modal").modal("show");
          verify_input = false;
          return;
        }
      }
      if (verify_input) {
        this.$store.dispatch("post_review", this.$route.params.id);
      }
    }
  },

  watch: {
    "$route.params.id": function(newVal, oldVal) {
      this.get_blog(newVal);
    },
    // 评论提交成功,弹出模态框提醒,切换到评论列表tab
    "$store.state.review_is_succees": function(newVal, oldVal) {
      if (newVal) {
        this.show_verify_result = false;
        $("#succees_modal").modal("show");
        setTimeout(function() {
          $("#succees_modal").modal("hide");
          $("#review-list-tab").tab("show");
        }, 1200);
      }
    }
  },
  mounted() {
    this.get_blog(this.$route.params.id);
  },
  computed: {
    review_name: {
      get() {
        return this.$store.state.blog_review.review_name;
      },
      set(value) {
        this.$store.commit("UpdateReviewName", value);
      }
    },
    review_email: {
      get() {
        return this.$store.state.blog_review.review_email;
      },
      set(value) {
        this.$store.commit("UpdateReviewEmail", value);
      }
    },
    review_text: {
      get() {
        return this.$store.state.blog_review.review_text;
      },
      set(value) {
        this.$store.commit("UpdateReviewText", value);
      }
    },
    verify_code: {
      get() {
        if (this.$store.state.blog_review.verify_code.length == 1) {
          // 当用户输入一个验证码的时候,就向后端发一个请求,防止403
          this.$store.dispatch("get_xsrf");
        }
        return this.$store.state.blog_review.verify_code;
      },
      set(value) {
        this.$store.commit("UpdateReviewVerifyCode", value);
        if (value.length < 4) {
          this.show_verify_result = false;
        }
        if (value.length == 4) {
          this.$store.dispatch("verify_code_check", value);
          this.show_verify_result = true;
        }
      }
    }
  }
};
</script>

<style scoped>
#verify_ok {
  color: green;
}

#verify_no {
  color: red;
}

#show_verify_result {
  display: inline-block;
  margin-top: 0%;
}
</style>
