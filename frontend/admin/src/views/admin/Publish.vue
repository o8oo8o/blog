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
                  href="#publish_list"
                  id="nav_publish_list"
                  data-toggle="tab"
                  @click="change_oper_mode"
                >查看</a>
              </li>
              <li class="nav-item">
                <a
                  class="nav-link"
                  href="#publish_add_or_edit"
                  id="nav_publish_add_or_edit"
                  data-toggle="tab"
                  v-text="oper_mode_txt"
                  @click="change_oper_mode"
                ></a>
              </li>
              &nbsp;&nbsp;
              <li class="nav-item">
                <div class="card-tools">
                  <div class="input-group">
                    <input
                      v-model.trim="receiver_like"
                      type="text"
                      name="table_search"
                      class="form-control float-right"
                      placeholder="搜索"
                    />
                    <div class="input-group-append">
                      <button @click="search_publish" type="submit" class="btn btn-default">
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
              <div class="tab-pane active" id="publish_list">
                <div class="card-body table-responsive p-0" id="card-body_main">
                  <table class="table table-head-fixed table-hover text-nowrap">
                    <thead>
                      <tr>
                        <th>ID</th>
                        <th>接收人</th>
                        <th>访问码</th>
                        <th>过期时间</th>
                        <th>简历标题</th>
                        <th>阅读次数</th>
                        <th>阅读时长</th>
                        <th>阅读时间</th>
                        <th>操作</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(item, index) in this.$store.state.publish_list" :key="index">
                        <td v-text="item.id"></td>
                        <td v-text="item.receiver"></td>
                        <td v-text="item.access_code"></td>
                        <td v-if="time_compare(item.exp_time)" v-text="item.exp_time"></td>
                        <td v-else v-text="item.exp_time" style="color:red"></td>
                        <td v-text="item.resume_title"></td>
                        <td v-text="item.read_count"></td>
                        <td v-text="item.read_duration"></td>
                        <td v-text="item.read_time"></td>

                        <td>
                          <div class="btn-group">
                            <button type="button" class="btn btn-default btn-sm">
                              <i class="fas fa-edit" @click="edit_publish(item)">&nbsp;编辑</i>
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
                      @click="prev_page($store.state.publish_current_page -1)"
                      v-if="this.$store.state.publish_current_page > 1"
                      type="button"
                      class="btn btn-default"
                    >
                      <i class="fas fa-chevron-left"></i>&nbsp;上一页
                    </button>
                    <button
                      @click="next_page($store.state.publish_current_page +1)"
                      v-if="this.$store.state.publish_current_page < this.$store.state.publish_max_page"
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
                        <span v-text="this.$store.state.publish_max_page"></span>页/
                        第
                        <span
                          v-text="this.$store.state.publish_current_page"
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
              <div class="tab-pane" id="publish_add_or_edit">
                <form class="form-horizontal">
                  <div class="form-group">
                    <label class="col-sm-2 control-label">访问码</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="access_code"
                        @blur="access_code_check"
                        type="text"
                        class="form-control"
                        minlength="4"
                        maxlength="30"
                      />
                      &nbsp;
                      <div
                        v-if="this.$store.state.publish_access_code_exists"
                        style="color:red"
                      >访问码已经存在!</div>
                    </div>
                  </div>

                  <div class="form-group">
                    <label class="col-sm-2 control-label">接收人</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="receiver"
                        type="text"
                        class="form-control"
                        minlength="1"
                        maxlength="127"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-2 control-label">简历</label>
                    <div class="col-sm-12">
                      <select class="form-control" name="resume" v-model="resume_id">
                        <option
                          v-for="(item, index) in  this.$store.state.resume_list"
                          :key="index"
                          :value="item.id"
                          v-text="item.title"
                        ></option>
                      </select>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-2 control-label">过期时间</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="exp_time"
                        type="text"
                        class="form-control"
                        maxlength="20"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label">更新及发布</label>
                    <div class="col-sm-12">
                      <div class="card-footer">
                        <div v-if="oper_mode == 'put' ">
                          <button @click="put_publish()" type="button" class="btn btn-info">更新</button>
                        </div>
                        <div v-else>
                          <button
                            @click="add_publish()"
                            type="button"
                            class="btn btn-primary float-right"
                          >保存</button>
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
          <div class="modal-body" v-text="delete_publish_alert_text"></div>
          <div class="modal-footer">
            <button @click="del_publish" type="button" class="btn btn-danger">删除</button>
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
          </div>
        </div>
      </div>
    </div>
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
  name: "publish",
  created() {
    this.$store.commit("UpdatePublishAccessCodeExists", false);
    this.$store.dispatch("resume_list_get");
    this.$store.dispatch("publish_list_get", {
      handle_type: "page",
      page_number: 1
    });
  },
  data() {
    return {
      editor: null,
      oper_mode: "add",
      oper_mode_txt: "新增",
      delete_publish_alert_text: "",
      delete_publish_index: 99999,
      delete_publish_id: "",
      go_page_number: ""
    };
  },
  methods: {
    // 访问码检查,检查输入的访问码是否已经存在
    access_code_check() {
      this.$store.dispatch("publish_access_code_check");
    },
    // 时间比较功能,让过期的时间显示不同样式
    time_compare(t) {
      let time = Date.parse(t);
      let now = Math.round(new Date());
      return time >= now ? true : false;
    },
    // 时间格式化功能
    dateFormater(formater, t) {
      let date = t ? new Date(t) : new Date(),
        Y = date.getFullYear() + "",
        M = date.getMonth() + 1,
        D = date.getDate(),
        H = date.getHours(),
        m = date.getMinutes(),
        s = date.getSeconds();
      return formater
        .replace(/YYYY|yyyy/g, Y)
        .replace(/YY|yy/g, Y.substr(2, 2))
        .replace(/MM/g, (M < 10 ? "0" : "") + M)
        .replace(/DD/g, (D < 10 ? "0" : "") + D)
        .replace(/HH|hh/g, (H < 10 ? "0" : "") + H)
        .replace(/mm/g, (m < 10 ? "0" : "") + m)
        .replace(/ss/g, (s < 10 ? "0" : "") + s);
    },
    // 改变操作模式
    change_oper_mode() {
      if ((this.oper_mode = "add")) {
        this.oper_mode = "add";
        this.oper_mode_txt = "新增";
        this.receiver = "";
        // 默认过期时间当前时间加7天
        this.exp_time = this.dateFormater(
          "YYYY-MM-DD HH:mm:ss",
          Math.round(new Date()) + 86400000 * 7
        );
        this.access_code = "";
        this.resume_id = 0;
      }
    },
    // 搜索简历发布,根据接收人搜索
    search_publish() {
      this.$store.dispatch("publish_list_get", { handle_type: "find" });
    },
    // 删除发布前,弹出确认模态框
    del_alert(publish) {
      this.delete_publish_id = publish.id;
      this.delete_publish_alert_text = publish.receiver;
      $("#delete_modal").modal("show");
    },
    // 删除发布
    del_publish() {
      $("#delete_modal").modal("hide");
      let obj = {
        handle_type: "del",
        publish_id: this.delete_publish_id
      };
      this.$store.dispatch("publish_handler", obj);
      this.$store.dispatch("publish_list_get", {
        handle_type: "page",
        page_number: 1
      });
    },
    // 添加发布
    add_publish() {
      let obj = {
        handle_type: "add"
      };
      this.$store.dispatch("publish_handler", obj);
    },
    // 更新发布
    put_publish() {
      let obj = {
        handle_type: "put"
      };
      this.$store.dispatch("publish_handler", obj);
    },
    // 编辑发布
    edit_publish(publish) {
      this.oper_mode = "put";
      this.oper_mode_txt = "编辑";
      this.$store.commit("UpdatePublishId", publish.id);
      this.$store.commit("UpdatePublishReceiver", publish.receiver);
      this.$store.commit("UpdatePublishResumeId", publish.resume_id);
      this.$store.commit("UpdatePublishAccessCode", publish.access_code);
      this.$store.commit("UpdatePublishExpTime", publish.exp_time);
      $("#nav_publish_add_or_edit").tab("show");
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
      if (page <= this.$store.state.publish_max_page && page >= 1) {
        return page;
      }
      return 1;
    },
    // 上一页
    prev_page(page_number) {
      let page = this.page_number_check(page_number);
      this.$store.dispatch("publish_list_get", {
        handle_type: "page",
        page_number: page
      });
    },
    // 下一页
    next_page(page_number) {
      let page = this.page_number_check(page_number);
      this.$store.dispatch("publish_list_get", {
        handle_type: "page",
        page_number: page
      });
    },
    // 跳转到指定页
    go_page() {
      let page = this.page_number_check(this.go_page_number);
      this.$store.dispatch("publish_list_get", {
        handle_type: "page",
        page_number: page
      });
    }
  },
  computed: {
    receiver: {
      get() {
        return this.$store.state.publish.receiver;
      },
      set(value) {
        this.$store.commit("UpdatePublishReceiver", value);
      }
    },
    resume_id: {
      get() {
        return this.$store.state.publish.resume_id;
      },
      set(value) {
        this.$store.commit("UpdatePublishResumeId", value);
      }
    },
    access_code: {
      get() {
        return this.$store.state.publish.access_code;
      },
      set(value) {
        this.$store.commit("UpdatePublishAccessCode", value);
      }
    },
    exp_time: {
      get() {
        return this.$store.state.publish.exp_time;
      },
      set(value) {
        this.$store.commit("UpdatePublishExpTime", value);
      }
    },
    receiver_like: {
      get() {
        return this.$store.state.publish_search;
      },
      set(value) {
        this.$store.commit("UpdatePublishSearch", value);
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
          $("#nav_publish_list").tab("show");
          $("#succees_modal").modal("hide");
        }, 1000);
      }
    }
  }
};
</script>

