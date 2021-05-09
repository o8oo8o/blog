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
                  href="#type_show"
                  id="nav_type_show"
                  data-toggle="tab"
                  @click="hide_edit_pane"
                >查看</a>
              </li>
              <li class="nav-item">
                <a
                  class="nav-link"
                  href="#type_add"
                  id="nav_type_add"
                  data-toggle="tab"
                  @click="hide_edit_pane"
                >新增</a>
              </li>
              <li class="nav-item" v-if="diaplay_edit_pane">
                <a class="nav-link" href="#type_edit" id="nav_type_edit" data-toggle="tab">编辑</a>
              </li>
            </ul>
          </div>

          <div class="card-body">
            <div class="tab-content">
              <!-- 查看 -->
              <div class="tab-pane active" id="type_show">
                <div class="card-body table-responsive p-0" id="card-body_main">
                  <table class="table table-head-fixed table-hover text-nowrap">
                    <thead>
                      <tr>
                        <th>ID</th>
                        <th>分类名称</th>
                        <th>文章数量</th>
                        <th>创建时间</th>
                        <th>修改时间</th>
                        <th>操作</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(item, index) in this.$store.state.classify_list" :key="index">
                        <td v-text="item.id"></td>
                        <td v-text="item.name"></td>
                        <td v-text="item.blog_count"></td>
                        <td v-text="item.create_time"></td>
                        <td v-text="item.update_time"></td>
                        <td>
                          <div class="btn-group">
                            <button
                              @click="edit_mode(item)"
                              type="button"
                              class="btn btn-default btn-sm"
                            >
                              <i class="fas fa-edit">&nbsp;编辑</i>
                            </button>
                            <button
                              v-if="item.blog_count == 0"
                              type="button"
                              class="btn btn-default btn-sm"
                            >
                              <i class="fas fa-trash-alt" @click="del_classify(item.id)">&nbsp;删除</i>
                            </button>
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>

              <!-- 新增 -->
              <div class="tab-pane" id="type_add">
                <form class="form-horizontal">
                  <div class="form-group">
                    <label for="new_name" class="col-sm-2 control-label">新增分类</label>
                    <div class="col-sm-12">
                      <input v-model="classify_id" type="hidden" />
                      <input
                        v-model.trim="name"
                        type="text"
                        required="required"
                        maxlength="30"
                        class="form-control"
                        id="new_name"
                        placeholder="分类名称"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label">保存</label>
                    <div class="col-sm-12">
                      <div class="card-footer">
                        <div>
                          <button type="submit" class="btn btn-info" @click="add_classify">保存</button>
                        </div>
                      </div>
                    </div>
                  </div>
                </form>
              </div>

              <!-- 编辑 -->
              <div class="tab-pane" id="type_edit">
                <form class="form-horizontal">
                  <div class="form-group">
                    <label for="edit_name" class="col-sm-2 control-label">编辑分类</label>
                    <div class="col-sm-12">
                      <input v-model="classify_id" type="hidden" />
                      <input
                        v-model.trim="name"
                        type="text"
                        required="required"
                        maxlength="30"
                        class="form-control"
                        id="edit_name"
                        placeholder="分类名称"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label">更新</label>
                    <div class="col-sm-12">
                      <div class="card-footer">
                        <div>
                          <button type="submit" class="btn btn-info" @click="put_classify">更新</button>
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
    <!-- 错误提示模态框 -->
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
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
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
            <h4 class="modal-title" id="succees_modalLabel">评论信息</h4>
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
  name: "classify",
  created() {
    let obj = {
      handle_type: "get"
    };
    this.$store.dispatch("classify_handler", obj);
  },
  data() {
    return {
      classify_id: 0,
      name: "",
      diaplay_edit_pane: false,
      error_title: "",
      error_msg: ""
    };
  },
  methods: {
    // 隐藏编辑面板
    hide_edit_pane() {
      this.diaplay_edit_pane = false;
      this.classify_id = 0;
      this.name = "";
    },
    // 进入编辑模式
    edit_mode(classify) {
      this.diaplay_edit_pane = true;
      this.classify_id = classify.id;
      this.name = classify.name;
      setTimeout(function() {
        $("#nav_type_edit").tab("show");
      }, 50);
    },
    // 数据检查
    data_check() {
      if (this.name.length == 0) {
        this.error_title = "填写错误";
        this.error_msg = "数据不能为空";
        $("#error_modal").modal("show");
        return false;
      }
      return true;
    },
    // 添加分类
    add_classify() {
      let obj = {
        handle_type: "add",
        name: this.name
      };
      if (this.data_check()) {
        this.$store.dispatch("classify_handler", obj);
      }
    },
    // 删除分类
    del_classify(classify_id) {
      let obj = {
        handle_type: "del",
        classify_id: classify_id
      };
      this.$store.dispatch("classify_handler", obj);
    },
    // 更新分类
    put_classify() {
      let obj = {
        handle_type: "put",
        classify_id: this.classify_id,
        name: this.name
      };
      if (this.data_check()) {
        this.$store.dispatch("classify_handler", obj);
      }
    }
  },
  watch: {
    // 操作成功,弹出操作成功模态框
    "$store.state.result_status": function(newVal, oldVal) {
      if (newVal) {
        $("#succees_modal").modal("show");
        this.hide_edit_pane();
        setTimeout(function() {
          $("#nav_type_show").tab("show");
        }, 50);
        setTimeout(function() {
          $("#succees_modal").modal("hide");
        }, 1200);
      }
    }
  }
};
</script>
