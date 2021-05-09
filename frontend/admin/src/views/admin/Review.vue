<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-header p-2">
            <ul class="nav nav-pills">
              <li class="nav-item">
                <a
                  class="nav-link active"
                  href="#review_list"
                  id="nav_review_list"
                  data-toggle="tab"
                >查看</a>
              </li>
              <li class="nav-item">
                <a
                  class="nav-link"
                  href="#review_detail"
                  id="nav_review_detail"
                  data-toggle="tab"
                >详情</a>
              </li>
              &nbsp;&nbsp;
              <li class="nav-item">
                <div class="card-tools">
                  <div class="input-group">
                    <input
                      v-model.trim="name_or_text_like"
                      type="text"
                      name="table_search"
                      class="form-control float-right"
                      placeholder="搜索"
                    />
                    <div class="input-group-append">
                      <button @click="search_review" type="submit" class="btn btn-default">
                        <i class="fas fa-search"></i>
                      </button>
                    </div>
                  </div>
                </div>
              </li>
            </ul>
          </div>
          <div class="card-body">
            <div class="tab-content">
              <div class="tab-pane active" id="review_list">
                <div class="card-body table-responsive p-0" id="card-body_main">
                  <table class="table table-head-fixed table-hover text-nowrap">
                    <thead>
                      <tr>
                        <th>ID</th>
                        <th>创建时间</th>
                        <th>邮箱</th>
                        <th>名字</th>
                        <th>评论文章</th>
                        <th>操作</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr
                        v-for="(item, index) in this.$store.state.review_list"
                        :key="index"
                        @click.stop="detail_mode(item)"
                      >
                        <td v-text="item.id"></td>
                        <td v-text="item.create_time"></td>
                        <td v-text="item.email"></td>
                        <td v-text="item.name"></td>
                        <td v-text="item.blog_title"></td>
                        <td>
                          <div class="btn-group">
                            <button
                              @click="detail_mode(item)"
                              type="button"
                              class="btn btn-default btn-sm"
                            >
                              <i class="fas fa-eye">&nbsp;查看详情</i>
                            </button>
                            <button type="button" class="btn btn-default btn-sm">
                              <i class="fas fa-trash-alt" @click.stop="del_review(item.id)">&nbsp;删除</i>
                            </button>
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="mailbox-controls">
                  <div class="btn-group">
                    <button
                      @click="prev_page($store.state.review_current_page -1)"
                      v-if="this.$store.state.review_current_page > 1"
                      type="button"
                      class="btn btn-default"
                    >
                      <i class="fas fa-chevron-left"></i>&nbsp;上一页
                    </button>
                    <button
                      @click="next_page($store.state.review_current_page +1)"
                      v-if="this.$store.state.review_current_page < this.$store.state.review_max_page"
                      type="button"
                      class="btn btn-default"
                    >
                      下一页&nbsp;&nbsp;
                      <i class="fas fa-chevron-right"></i>
                    </button>
                  </div>
                  <div class="float-right">
                    <div class="input-group">
                      <span class="btn btn-default">
                        共
                        <span v-text="this.$store.state.review_max_page"></span>页/
                        第
                        <span v-text="this.$store.state.review_current_page"></span>页
                      </span>
                      <input
                        type="number"
                        v-model.trim="go_page_number"
                        class="form-control"
                        placeholder="页码"
                        style="width:100px"
                      />
                      <div class="input-group-append">
                        <div @click="go_page" class="btn btn-primary">转到</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <!-- 详细信息 -->
              <div class="tab-pane" id="review_detail">
                <form class="form-horizontal">
                  <div class="form-group">
                    <label class="col-sm-2 control-label">ID</label>
                    <div class="col-sm-12">
                      <input v-model="review_id" type="text" class="form-control" disabled />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-2 control-label">发布时间</label>
                    <div class="col-sm-12">
                      <input v-model="create_time" type="text" class="form-control" />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-2 control-label">邮箱</label>
                    <div class="col-sm-12">
                      <input v-model="email" type="text" class="form-control" />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-2 control-label">名字</label>
                    <div class="col-sm-12">
                      <input v-model="name" type="text" class="form-control" />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-2 control-label">博客标题</label>
                    <div class="col-sm-12">
                      <input v-model="blog_title" type="text" class="form-control" />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-2 control-label">评论内容</label>
                    <div class="col-sm-12">
                      <textarea v-model="text" class="form-control" rows="5"></textarea>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label">删除操作</label>
                    <div class="col-sm-12">
                      <div class="card-footer">
                        <div>
                          <button
                            @click="del_review(review_id)"
                            type="button"
                            class="btn btn-danger"
                          >删除</button>
                        </div>
                      </div>
                    </div>
                  </div>
                </form>
              </div>
            </div>
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
            <h4 class="modal-title" id="succees_modalLabel">操作信息</h4>
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
          </div>
          <div class="modal-body">恭喜你!操作成功</div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "review",
  created() {
    this.$store.dispatch("review_list_get", {
      handle_type: "page",
      page_number: 1
    });
  },
  data() {
    return {
      review_id: 0,
      create_time: "",
      email: "",
      name: "",
      text: "",
      blog_title: "",
      go_page_number: ""
    };
  },
  methods: {
    // 查看评论详细信息
    detail_mode(review) {
      this.diaplay_detail_pane = true;
      this.review_id = review.id;
      this.email = review.email;
      this.name = review.name;
      this.text = review.text;
      this.create_time = review.create_time;
      this.blog_title = review.blog_title;
      setTimeout(function() {
        $("#nav_review_detail").tab("show");
      }, 50);
    },
    // 页码检查
    page_number_check(page_number) {
      var page = 1;
      try {
        page = Number.parseInt(page_number);
        if (!page) {
          return 1;
        }
      } catch (error) {
        return 1;
      }
      if (page <= this.$store.state.review_max_page && page >= 1) {
        return page;
      }
      return 1;
    },
    // 上一页
    prev_page(page_number) {
      let page = this.page_number_check(page_number);
      this.$store.dispatch("review_list_get", {
        handle_type: "page",
        page_number: page
      });
    },
    // 下一页
    next_page(page_number) {
      let page = this.page_number_check(page_number);
      this.$store.dispatch("review_list_get", {
        handle_type: "page",
        page_number: page
      });
    },
    // 跳转到指定页
    go_page() {
      let page = this.page_number_check(this.go_page_number);
      this.$store.dispatch("review_list_get", {
        handle_type: "page",
        page_number: page
      });
    },
    // 删除评论
    del_review(review_id) {
      let obj = {
        oprt_review: "del",
        review_id: review_id
      };
      this.$store.dispatch("review_handler", obj);
    },
    // 搜索评论,(搜索评论名字及评论内容)
    search_review() {
      $("#nav_review_list").tab("show");
      this.$store.dispatch("review_list_get", { handle_type: "find" });
    }
  },
  computed: {
    name_or_text_like: {
      get() {
        return this.$store.state.review_search;
      },
      set(value) {
        this.$store.commit("UpdateReviewSearch", value);
      }
    }
  },
  watch: {
    // 操作成功,弹出成功模态框
    "$store.state.result_status": function(newVal, oldVal) {
      if (newVal) {
        $("#succees_modal").modal("show");
        setTimeout(function() {
          $("#nav_review_list").tab("show");
          $("#succees_modal").modal("hide");
        }, 1000);
      }
    }
  }
};
</script>
