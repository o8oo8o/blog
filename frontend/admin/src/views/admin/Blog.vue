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
                  href="#blog_list"
                  id="nav_blog_list"
                  data-toggle="tab"
                  @click="change_oper_mode"
                >查看</a>
              </li>
              <li class="nav-item">
                <a
                  class="nav-link"
                  href="#blog_add_or_edit"
                  id="nav_blog_add_or_edit"
                  data-toggle="tab"
                  v-text="oper_mode_txt"
                  @click="change_oper_mode"
                ></a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#blog_preview" id="nav_blog_preview" data-toggle="tab">预览</a>
              </li>
              &nbsp;&nbsp;
              <li class="nav-item">
                <div class="card-tools">
                  <div class="input-group">
                    <input
                      v-model.trim="title_like"
                      type="text"
                      name="table_search"
                      class="form-control float-right"
                      placeholder="搜索"
                    />
                    <div class="input-group-append">
                      <button @click="search_blog" type="submit" class="btn btn-default">
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
              <!-- 列表 -->
              <div class="tab-pane active" id="blog_list">
                <div class="card-body table-responsive p-0" id="card-body_main">
                  <table class="table table-head-fixed table-hover text-nowrap">
                    <thead>
                      <tr>
                        <th>ID</th>
                        <th>标题</th>
                        <th>状态</th>
                        <th>分类</th>
                        <th>公开</th>
                        <th>评论</th>
                        <th>创建时间</th>
                        <th>阅读数</th>
                        <th>评论数</th>
                        <th>操作</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr
                        v-for="(item, index) in this.$store.state.blog_list"
                        :key="index"
                        @click.stop="get_blog(item.id)"
                      >
                        <td v-text="item.id"></td>
                        <td v-text="item.title"></td>
                        <td>
                          <span v-if="item.status == 0" style="color:green">已发布</span>
                          <span v-else-if="item.status == 1" style="color:red">已保存</span>
                        </td>
                        <td v-text="item.classify_name"></td>
                        <td>
                          <span v-if="item.is_public" style="color:green">公开</span>
                          <span v-else style="color:red">私有</span>
                        </td>
                        <td>
                          <span v-if="item.is_review" style="color:green">允许</span>
                          <span v-else style="color:red">禁止</span>
                        </td>
                        <td v-text="item.create_time"></td>
                        <td v-text="item.read_count"></td>
                        <td v-text="item.review_count"></td>
                        <td>
                          <div class="btn-group">
                            <button
                              @click="get_blog(item.id)"
                              type="button"
                              class="btn btn-default btn-sm"
                            >
                              <i class="fas fa-eye">&nbsp;预览</i>
                            </button>
                            <button type="button" class="btn btn-default btn-sm">
                              <i class="fas fa-edit" @click="edit_blog(item.id)">&nbsp;编辑</i>
                            </button>
                            <button type="button" class="btn btn-default btn-sm">
                              <i class="fas fa-trash-alt" @click.stop="del_alert(item)">&nbsp;删除</i>
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
                      @click="prev_page($store.state.blog_current_page -1)"
                      v-if="this.$store.state.blog_current_page > 1"
                      type="button"
                      class="btn btn-default"
                    >
                      <i class="fas fa-chevron-left"></i>&nbsp;上一页
                    </button>
                    <button
                      @click="next_page($store.state.blog_current_page +1)"
                      v-if="this.$store.state.blog_current_page < this.$store.state.blog_max_page"
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
                        <span v-text="this.$store.state.blog_max_page"></span>页/
                        第
                        <span
                          v-text="this.$store.state.blog_current_page"
                        ></span>页
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
              <!-- 新增或编辑 -->
              <div class="tab-pane" id="blog_add_or_edit">
                <form class="form-horizontal">
                  <div class="form-group">
                    <label class="col-sm-2 control-label">标题</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="title"
                        @blur="title_check"
                        type="text"
                        class="form-control"
                        maxlength="127"
                      />
                    </div>&nbsp;
                    <div v-if="this.$store.state.blog_title_exists" style="color:red">标题已经存在!</div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-2 control-label">分类</label>
                    <div class="col-sm-12">
                      <select class="form-control" name="classify_id" v-model="classify_id">
                        <option
                          v-for="(item, index) in  this.$store.state.classify_list"
                          :key="index"
                          :value="item.id"
                          v-text="item.name"
                        ></option>
                      </select>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-2 control-label">
                      权重:
                      <span v-text="weight"></span>
                    </label>
                    <div class="col-sm-12">
                      <input
                        v-model="weight"
                        type="range"
                        class="custom-range"
                        min="1000"
                        max="3000"
                        id="weight"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">允许评论</label>
                    <div class="col-sm-8">
                      <div class="form-check form-check-inline">
                        <input
                          v-model="is_review"
                          class="form-check-input"
                          type="radio"
                          name="is_review"
                          id="blog_review_a"
                          value="false"
                        />
                        <label class="form-check-label" for="blog_review_a">禁止</label>
                      </div>
                      <div class="form-check form-check-inline">
                        <input
                          v-model="is_review"
                          class="form-check-input"
                          type="radio"
                          name="is_review"
                          id="blog_review_b"
                          value="true"
                        />
                        <label class="form-check-label" for="blog_review_b">允许</label>
                      </div>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">是否公开</label>
                    <div class="col-sm-8">
                      <div class="form-check form-check-inline">
                        <input
                          v-model="is_public"
                          class="form-check-input"
                          type="radio"
                          name="is_public"
                          id="blog_public_a"
                          value="false"
                        />
                        <label class="form-check-label" for="blog_public_a">保密</label>
                      </div>
                      <div class="form-check form-check-inline">
                        <input
                          v-model="is_public"
                          class="form-check-input"
                          type="radio"
                          name="is_public"
                          id="blog_public_b"
                          value="true"
                        />
                        <label class="form-check-label" for="blog_public_b">公开</label>
                      </div>
                    </div>
                  </div>

                  <div class="form-group">
                    <label class="col-sm-2 control-label">博客内容</label>
                    <div class="col-sm-12">
                      <div id="editor" ref="editor" style="z-index:1;">
                        <!-- 编辑器 -->
                      </div>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label">更新及发布</label>
                    <div class="col-sm-12">
                      <div class="card-footer">
                        <div v-if="oper_mode == 'put' ">
                          <button
                            type="button"
                            class="btn btn-info float-left"
                            @click="put_blog(1)"
                          >更新预览</button>
                          <button
                            type="button"
                            class="btn btn-info float-right"
                            @click="put_blog(0)"
                          >更新发布</button>
                        </div>
                        <div v-else>
                          <button
                            type="button"
                            class="btn btn-primary float-left"
                            @click="add_blog(1)"
                          >保存预览</button>
                          <button
                            type="button"
                            class="btn btn-primary float-right"
                            @click="add_blog(0)"
                          >直接发布</button>
                        </div>
                      </div>
                    </div>
                  </div>
                </form>
              </div>
              <!-- 预览 -->
              <div class="tab-pane" id="blog_preview">
                <div class="col-md-12">
                  <div class="card card-primary card-outline">
                    <div class="card-header" style="text-align: center">
                      <h5 v-text="this.$store.state.blog.title"></h5>
                    </div>
                    <div class="card-header">
                      发布时间:
                      <span v-text="this.$store.state.blog.create_time"></span>
                      &nbsp;&nbsp;
                      <span class="float-right">
                        更新时间:
                        <span v-text="this.$store.state.blog.update_time"></span> &nbsp;&nbsp;
                        阅读:
                        <span
                          v-text="this.$store.state.blog.read_count"
                        ></span> &nbsp;&nbsp;
                        评论:
                        <span
                          v-text="this.$store.state.blog.review_count"
                        ></span> &nbsp;&nbsp;
                        分类:
                        <span v-text="classify_name"></span>
                      </span>
                    </div>
                    <div class="card-body">
                      <!-- 博客正文 -->
                      <div v-html="this.$store.state.blog.text"></div>
                    </div>
                    <div class="card-footer">
                      <!-- 评论信息 -->
                      <div class="card-body">
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
                                  <button
                                    @click="del_review(item.id)"
                                    type="button"
                                    class="btn btn-danger"
                                  >删除</button>
                                  &nbsp;&nbsp;ID:&nbsp;&nbsp;
                                  <b
                                    v-text="item.id"
                                  ></b>
                                </span>
                                <div class="comment-text">
                                  <span class="username">
                                    名字:&nbsp;
                                    <span v-text="item.name"></span>
                                    <span class="text-muted float-right" v-text="item.create_time"></span>
                                  </span>
                                  <span v-text="item.text"></span>
                                  <br />
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
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 删除确认模态框 -->
    <div
      class="modal fade"
      id="delete_modal"
      tabindex="-1"
      role="dialog"
      aria-labelledby="delete_modal_label"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content bg-info">
          <div class="modal-header">
            <h4 class="modal-title" id="delete_modal_label">确认删除</h4>
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
          </div>
          <div class="modal-body" v-text="delete_blog_alert_text"></div>
          <div class="modal-footer">
            <button @click="del_blog" type="button" class="btn btn-danger">删除</button>
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
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
  name: "blog",
  created() {
    let obj = {
      handle_type: "get"
    };
    // 先获取分类数据,方便博客的增加
    this.$store.commit("UpdateBlogTitleExists", false);
    this.$store.dispatch("classify_handler", obj);
    this.$store.dispatch("blog_list_get", {
      handle_type: "page",
      page_number: 1
    });
  },
  mounted() {
    var editor = new Editor(document.getElementById("editor"));
    //var editor = new Editor(this.$refs.editor);
    editor.customConfig.onchange = html => {
      this.text = html;
    };
    // 将图片大小限制为 10M
    editor.customConfig.uploadImgMaxSize = 10 * 1024 * 1024;
    // 限制一次最多上传 50 张图片
    editor.customConfig.uploadImgMaxLength = 50;
    // 自定义编辑器上传图片
    editor.customConfig.customUploadImg = (files, insert) => {
      let obj = {
        handle_type: "edit",
        files: files,
        insert: insert
      };
      this.$store.dispatch("upload_image", obj);
    };
    editor.create();
    this.editor = editor;
  },
  data() {
    return {
      editor: null,
      oper_mode: "add",
      oper_mode_txt: "新增",
      delete_blog_alert_text: "",
      delete_blog_index: 99999,
      delete_blog_id: "",
      go_page_number: ""
    };
  },
  methods: {
    // 改变操作模式
    change_oper_mode() {
      if ((this.oper_mode = "add")) {
        this.oper_mode = "add";
        this.oper_mode_txt = "新增";
        this.editor.txt.clear();
        this.title = "";
        this.status = 1;
        this.text = "";
        this.is_review = false;
        this.is_public = false;
        this.weight = 2000;
        this.classify_id = 1;
        this.$store.commit("UpdateBlogReviewList", []);
        this.$store.commit("UpdateBlogCreateTime", "1970-01-01 00:00:00");
        this.$store.commit("UpdateBlogUpdateTime", "1970-01-01 00:00:00");
        this.$store.commit("UpdateBlogReadCount", 0);
        this.$store.commit("UpdateBlogReviewCount", 0);
      }
    },
    // 检查博客标题是否存在
    title_check() {
      this.$store.dispatch("blog_title_check");
    },
    // 搜索博客,根据博客标题搜索
    search_blog() {
      $("#nav_blog_list").tab("show");
      this.$store.dispatch("blog_list_get", { handle_type: "find" });
    },
    // 获取博客一个博客
    get_blog(blog_id) {
      let obj = {
        handle_type: "get",
        blog_id: blog_id
      };
      this.$store.dispatch("blog_handler", obj);
      if (this.oper_mode != "put") {
        // 如果是编辑操作切换到编辑面板
        $("#nav_blog_preview").tab("show");
      }
    },
    // 删除前弹出模态框
    del_alert(blog) {
      this.delete_blog_id = blog.id;
      this.delete_blog_alert_text = blog.title;
      $("#delete_modal").modal("show");
    },
    // 删除评论,主要是为了操作方便
    del_review(review_id) {
      let obj = {
        oprt_review: "del",
        review_id: review_id
      };
      this.$store.dispatch("review_handler", obj);
    },
    // 删除博客
    del_blog() {
      $("#delete_modal").modal("hide");
      let obj = {
        handle_type: "del",
        blog_id: this.delete_blog_id
      };
      this.$store.dispatch("blog_handler", obj);
      // 删除博客以后跳转到第一页显示
      this.$store.dispatch("blog_list_get", {
        handle_type: "page",
        page_number: 1
      });
    },
    // 新增博客
    add_blog(status) {
      let obj = {
        handle_type: "add"
      };
      this.$store.commit("UpdateBlogStatus", status);
      this.$store.dispatch("blog_handler", obj);
    },
    // 更新博客
    put_blog(status) {
      let obj = {
        handle_type: "put"
      };
      this.$store.commit("UpdateBlogStatus", status);
      this.$store.dispatch("blog_handler", obj);
    },
    // 进入编辑模式
    edit_blog(blog_id) {
      this.oper_mode = "put";
      this.oper_mode_txt = "编辑";
      let obj = {
        handle_type: "get",
        blog_id: blog_id
      };
      this.$store.dispatch("blog_handler", obj);
      $("#nav_blog_add_or_edit").tab("show");
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
      if (page <= this.$store.state.blog_max_page && page >= 1) {
        return page;
      }
      return 1;
    },
    // 上一页
    prev_page(page_number) {
      let page = this.page_number_check(page_number);
      this.$store.dispatch("blog_list_get", {
        handle_type: "page",
        page_number: page
      });
    },
    // 下一页
    next_page(page_number) {
      let page = this.page_number_check(page_number);
      this.$store.dispatch("blog_list_get", {
        handle_type: "page",
        page_number: page
      });
    },
    // 跳转到指定页
    go_page() {
      let page = this.page_number_check(this.go_page_number);
      this.$store.dispatch("blog_list_get", {
        handle_type: "page",
        page_number: page
      });
    }
  },
  computed: {
    title: {
      get() {
        return this.$store.state.blog.title;
      },
      set(value) {
        this.$store.commit("UpdateBlogTitle", value);
      }
    },
    status: {
      get() {
        return this.$store.state.blog.status;
      },
      set(value) {
        this.$store.commit("UpdateBlogStatus", value);
      }
    },
    text: {
      get() {
        return this.$store.state.blog.text;
      },
      set(value) {
        this.$store.commit("UpdateBlogText", value);
      }
    },
    is_review: {
      get() {
        return this.$store.state.blog.is_review;
      },
      set(value) {
        this.$store.commit("UpdateBlogIsReview", value);
      }
    },
    is_public: {
      get() {
        return this.$store.state.blog.is_public;
      },
      set(value) {
        this.$store.commit("UpdateBlogIsPublic", value);
      }
    },
    weight: {
      get() {
        return this.$store.state.blog.weight;
      },
      set(value) {
        this.$store.commit("UpdateBlogWeight", value);
      }
    },
    classify_id: {
      get() {
        return this.$store.state.blog.classify_id;
      },
      set(value) {
        this.$store.commit("UpdateBlogClassifyId", value);
      }
    },
    classify_name: {
      get() {
        return this.$store.state.blog.classify_name;
      }
    },
    title_like: {
      get() {
        return this.$store.state.blog_search;
      },
      set(value) {
        this.$store.commit("UpdateBlogSearch", value);
      }
    }
  },
  watch: {
    // 操作成功,弹出操作成功模态框
    "$store.state.result_status": function(newVal, oldVal) {
      if (newVal) {
        $("#succees_modal").modal("show");
        this.change_oper_mode();
        setTimeout(function() {
          $("#nav_blog_list").tab("show");
          $("#succees_modal").modal("hide");
        }, 1000);
      }
    },
    // 加载完成以后,设置富文本编辑器内容
    "$store.state.load_ok": function(newVal, oldVal) {
      if (newVal) {
        this.editor.txt.html(this.$store.state.blog.text);
      }
    }
  }
};
</script>
