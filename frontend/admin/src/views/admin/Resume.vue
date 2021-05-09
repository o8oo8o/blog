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
                  href="#resume_list"
                  id="nav_resume_list"
                  data-toggle="tab"
                  @click="change_oper_mode"
                >查看</a>
              </li>
              <li class="nav-item">
                <a
                  class="nav-link"
                  href="#resume_add_or_edit"
                  id="nav_resume_add_or_edit"
                  data-toggle="tab"
                  v-text="oper_mode_txt"
                  @click="change_oper_mode"
                ></a>
              </li>

              <li class="nav-item">
                <a
                  class="nav-link"
                  href="#resume_preview"
                  id="nav_resume_preview"
                  data-toggle="tab"
                >预览</a>
              </li>
            </ul>
            <!-- <div class="card-tools">
              <div class="input-group" style="width: 250px;">
                <input
                  v-model.trim="search_text"
                  type="text"
                  name="table_search"
                  class="form-control float-right"
                  placeholder="搜索"
                />
                <div class="input-group-append">
                  <button @click="search_resume" type="submit" class="btn btn-default">
                    <i class="fas fa-search"></i>
                  </button>
                </div>
              </div>
            </div>-->
          </div>
          <!-- /.card-header -->
          <div class="card-body">
            <div class="tab-content">
              <!-- 列表 -->
              <div class="tab-pane active" id="resume_list">
                <div class="card-body table-responsive p-0" id="card-body_main">
                  <table class="table table-head-fixed table-hover text-nowrap">
                    <thead>
                      <tr>
                        <th>ID</th>
                        <th>标题</th>
                        <th>发布次数</th>
                        <th>创建时间</th>
                        <th>更新时间</th>
                        <th>操作</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr
                        v-for="(item, index) in this.$store.state.resume_list"
                        :key="index"
                        @click.stop="get_resume(item.id)"
                      >
                        <td v-text="item.id"></td>
                        <td v-text="item.title"></td>
                        <td v-text="item.publish_count"></td>
                        <td v-text="item.create_time"></td>
                        <td v-text="item.update_time"></td>

                        <td>
                          <div class="btn-group">
                            <button
                              @click="get_resume(item.id)"
                              type="button"
                              class="btn btn-default btn-sm"
                            >
                              <i class="fas fa-eye">&nbsp;预览</i>
                            </button>
                            <button type="button" class="btn btn-default btn-sm">
                              <i class="fas fa-edit" @click="edit_resume(item.id)">&nbsp;编辑</i>
                            </button>
                            <button
                              v-if="item.publish_count == 0"
                              type="button"
                              class="btn btn-default btn-sm"
                            >
                              <i class="fas fa-trash-alt" @click.stop="del_alert(item)">&nbsp;删除</i>
                            </button>
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <!-- /.card-body -->
              </div>

              <!-- 新增或编辑 -->
              <div class="tab-pane" id="resume_add_or_edit">
                <form class="form-horizontal">
                  <div class="form-group">
                    <label class="col-sm-2 control-label">标题</label>
                    <div class="col-sm-12">
                      <input
                        v-model="title"
                        @blur="title_check"
                        type="text"
                        class="form-control"
                        maxlength="127"
                      />
                      &nbsp;
                      <div v-if="this.$store.state.resume_title_exists" style="color:red">标题已经存在!</div>
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
                  <!-- ======================= -->
                  <div class="form-group">
                    <label class="control-label">更新或保存</label>
                    <div class="col-sm-12">
                      <div class="card-footer">
                        <div v-if="oper_mode == 'put' ">
                          <button
                            type="button"
                            class="btn btn-info float-right"
                            @click="put_resume()"
                          >更新</button>
                        </div>
                        <div v-else>
                          <button
                            type="button"
                            class="btn btn-primary float-left"
                            @click="add_resume()"
                          >保存</button>
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- ======================= -->
                </form>
              </div>

              <!-- 预览 -->
              <div class="tab-pane" id="resume_preview">
                <!-- /.col -->
                <div class="col-md-12">
                  <div class="card card-primary card-outline">
                    <div class="card-header" style="text-align: center">
                      <h5 v-text="this.$store.state.resume.title"></h5>
                    </div>
                    <div class="card-header">
                      发布时间:
                      <span v-text="this.$store.state.resume.create_time"></span>
                      &nbsp;&nbsp;
                      <span class="float-right">
                        更新时间:
                        <span v-text="this.$store.state.resume.update_time"></span> &nbsp;&nbsp;
                      </span>
                    </div>
                    <div class="card-body">
                      <!-- =============================================== -->
                      <div v-html="this.$store.state.resume.text"></div>
                      <!-- =============================================== -->
                    </div>
                  </div>
                  <!-- /.card -->
                </div>
                <!-- /.col -->
              </div>
            </div>
            <!-- /.card-body -->
          </div>
        </div>
      </div>
    </div>
    <!-- =============================== -->
    <!-- ======================删除确认框========================== -->
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
          <div class="modal-body" v-text="delete_resume_title"></div>
          <div class="modal-footer">
            <button @click="del_resume" type="button" class="btn btn-danger">删除</button>
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
          </div>
        </div>
      </div>
    </div>
    <!-- ================================================ -->
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

    <!-- =============================================== -->
    <!-- =============================== -->
  </div>
</template>

<script>
// var editor = new window.Editor( document.getElementById('editor') );
// editor.create();

export default {
  name: "resume",
  created() {
    this.$store.commit("UpdateResumeTitleExists", false);
    this.$store.dispatch("resume_list_get");
  },
  mounted() {
    //var editor = new window.Editor( document.getElementById('editor') );
    var editor = new window.Editor(this.$refs.editor);
    editor.customConfig.onchange = html => {
      this.text = html;
    };
    // 将图片大小限制为 3M
    editor.customConfig.uploadImgMaxSize = 3 * 1024 * 1024;

    // 限制一次最多上传 5 张图片
    editor.customConfig.uploadImgMaxLength = 5;

    // 上传图片到服务器
    editor.customConfig.uploadImgServer = "/api/admin/upload/";

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
      delete_resume_title: "",
      delete_resume_index: 99999,
      delete_resume_id: "",
      search_text: ""
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
        this.text = "";
      }
    },
    // 简历标题检查,检查简历标题是否存在
    title_check() {
      this.$store.dispatch("resume_title_check");
    },
    // 获取一个简历
    get_resume(resume_id) {
      let obj = {
        handle_type: "get",
        resume_id: resume_id
      };
      this.$store.dispatch("resume_handler", obj);
      if (this.oper_mode != "put") {
        $("#nav_resume_preview").tab("show");
      }
    },
    // 删除前,弹出模态框
    del_alert(resume) {
      this.delete_resume_id = resume.id;
      this.delete_resume_title = resume.title;
      $("#delete_modal").modal("show");
    },
    // 删除简历
    del_resume() {
      $("#delete_modal").modal("hide");
      let obj = {
        handle_type: "del",
        resume_id: this.delete_resume_id
      };
      this.$store.dispatch("resume_handler", obj);
      this.$store.dispatch("resume_list_get");
    },
    // 添加简历
    add_resume() {
      let obj = {
        handle_type: "add"
      };
      this.$store.dispatch("resume_handler", obj);
    },
    // 更新简历
    put_resume() {
      let obj = {
        handle_type: "put"
      };
      this.$store.dispatch("resume_handler", obj);
    },
    // 编辑简历
    edit_resume(resume_id) {
      this.oper_mode = "put";
      this.oper_mode_txt = "编辑";
      let obj = {
        handle_type: "get",
        resume_id: resume_id
      };
      this.$store.dispatch("resume_handler", obj);
      $("#nav_resume_add_or_edit").tab("show");
    }
  },
  computed: {
    title: {
      get() {
        return this.$store.state.resume.title;
      },
      set(value) {
        this.$store.commit("UpdateResumeTitle", value);
      }
    },
    text: {
      get() {
        return this.$store.state.resume.text;
      },
      set(value) {
        this.$store.commit("UpdateResumeText", value);
      }
    }
  },
  watch: {
    // 操作成功,弹出成功模态框
    "$store.state.result_status": function(newVal, oldVal) {
      if (newVal) {
        $("#succees_modal").modal("show");
        this.change_oper_mode();
        setTimeout(function() {
          $("#nav_resume_list").tab("show");
          $("#succees_modal").modal("hide");
        }, 1000);
      }
    },
    // 加载完成以后,设置富文本编辑器内容
    "$store.state.load_ok": function(newVal, oldVal) {
      if (newVal) {
        this.editor.txt.html(this.$store.state.resume.text);
      }
    }
  }
};
</script>

