<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-header p-2">
            <ul class="nav nav-pills">
              <li class="nav-item">
                <a class="nav-link active" href="#netdisk_list" id="nav_netdisk_list" data-toggle="tab" >查看</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#netdisk_tree" id="nav_netdisk_tree" data-toggle="tab" >目录树</a>
              </li>
              &nbsp;&nbsp;
              <li class="nav-item">
                <div class="card-tools">
                    <div class="input-group" >
                        <input v-model.trim="name_like" type="text" class="form-control float-right" placeholder="搜索" />
                        <div class="input-group-append">
                          <button @click="file_search()" type="submit" class="btn btn-default">
                            <i class="fas fa-search"></i>
                          </button>
                        </div>
                        <input type="file" id="up_file" ref="up_file" accept="*/*" multiple @change="file_upload()" style="filter:alpha(opacity=0);opacity:0;width: 0;height: 0;"/>
                        <input  class="form-control" @input="folder_name_input()" v-model="folder_name" type="text" ref="folder_name" minlength="1" title="新建文件夹的名字"/>
                        <div class="input-group-append">
                          <button @click="new_folder()" class="btn btn-default" title="在当前目录下创建文件夹">
                            <i class="fas fa-plus"></i>
                          </button>
                        </div>
                    </div>
                </div>
              </li>
            </ul>
          </div>
          <div class="input-group ">
            <div class="input-group-append ">
              <button @click="file_select()" class="btn" title="上传文件到服务器">上传</button>
              <button v-if="display_move_button" @click="move()" class="btn bg-gradient-success" title="移动到此">移动到此</button> 
              <button @click="dir_list('/')" class="btn" title="回到根目录文件夹">根目录</button> 
              <button v-for="(item, index) in current_path" :key="index"  v-text="item" @click="dir_list_to(index)" class="btn"></button> 
            </div>
          </div>
          <div class="card-body" style="padding: 0rem;">
            <div class="tab-content" style="padding-top: 0%;">
              <!-- 查看 -->
              <div class="tab-pane active" id="netdisk_list" style="padding-top: 0rem;">
                  <div class="card-body table-responsive p-0" >
                    <table class="table table-head-fixed table-hover text-nowrap">
                      <thead>
                        <tr>
                          <th>名称</th>
                          <th>大小</th>
                          <th>修改时间</th>
                          <th v-if="search_mode">存储路径</th>
                          <th>操作</th>
                        </tr>
                      </thead>
                      <tbody v-for="(item, index) in this.$store.state.netdisk.dir_list.list" :key="index" >
                        <tr v-if="item.type =='file'" class="text-success">
                          <td><i class="nav-icon far fa-file"></i> &nbsp;<span  v-text="item.name"></span></td>
                          <td v-text="item.size"></td>
                          <td v-text="item.mtime"></td>
                          <td v-if="search_mode" v-text="item.path"></td>
                          <td>
                            <div class="btn-group">
                              <button type="button" class="btn btn-default btn-sm" title="下载" @click.stop="file_down(item.path)">
                                <i class="fas fa-download">&nbsp;</i>
                              </button>
                              <button @click.stop="rename_alert(item)" type="button" class="btn btn-default btn-sm" title="重命名">
                                <i class="fas fa-file-signature" >&nbsp;</i>
                              </button>
                              <button @click.stop="del_alert(item)" type="button" class="btn btn-default btn-sm" title="删除">
                                <i class="fas fa-trash-alt" >&nbsp;</i>
                              </button>
                              <button @click.stop="show_move_button(item)" type="button" class="btn btn-default btn-sm" title="移动">
                                <i class="fas fa-arrows-alt" >&nbsp;</i>
                              </button>
                            </div>
                          </td>
                        </tr>
                        <tr v-else class="text-primary" @click="dir_list(item.path)">
                          <td><i class="nav-icon far fa-folder"></i> &nbsp;<span  v-text="item.name"></span></td>
                          <td v-text="item.size"></td>
                          <td v-text="item.mtime"></td>
                          <td v-if="search_mode" v-text="item.path"></td>
                          <td>
                            <div class="btn-group">
                              <button type="button" class="btn btn-default btn-sm" title="目录树" @click.stop="dir_tree(item.path)">
                                <i class="fas fa-sitemap" >&nbsp;</i>
                              </button>
                              <button  @click.stop="rename_alert(item)" type="button" class="btn btn-default btn-sm" title="重命名">
                                <i class="fas fa-file-signature" >&nbsp;</i>
                              </button>
                              <button @click.stop="del_alert(item)" type="button" class="btn btn-default btn-sm" title="删除">
                                <i class="fas fa-trash-alt" >&nbsp;</i>
                              </button>
                              <button @click.stop="show_move_button(item)" type="button" class="btn btn-default btn-sm" title="移动">
                                <i class="fas fa-arrows-alt" >&nbsp;</i>
                              </button>
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <div class="alert alert-secondary">
                      <span>
                        上传<b v-text="upload_index"></b>个,
                        进度:<b v-text="this.$store.state.netdisk.upload_progress"></b>%
                      </span>
                  </div>
              </div>
              <!-- 目录树 -->
              <div class="tab-pane" id="netdisk_tree">
                <div class="col-sm-12">
                  <br>
                    <div v-html="this.$store.state.netdisk.dir_tree"></div>
                  <br>
                </div>
              </div>
            </div>
          </div>
          <br>
        </div>
      </div>
    </div>
    <!-- 删除确认模态框 -->
        <div class="modal fade" id="delete_modal" tabindex="-1" role="dialog" aria-labelledby="delete_modal_label" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content bg-info">
          <div class="modal-header">
            <h4 class="modal-title" id="delete_modal_label">确认删除</h4>
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
          </div>
          <div class="modal-body" v-text="delete_alert_text"></div>
          <div class="modal-footer">
            <button @click="del()" type="button" class="btn btn-danger">删除</button>
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
          </div>
        </div>
      </div>
    </div>
    <!-- 文件、目录重命名模态框 -->
        <div class="modal default" id="rename_modal" tabindex="-1" role="dialog" aria-labelledby="rename_modal_label" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title" id="rename_modal_label">重命名</h4>
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
          </div>
          <div class="modal-body">
            <div class="form-group">
                <label for="old_name">旧名称:</label>
                <input v-model="old_name" type="text" class="form-control" id="old_name" ref="old_name"  disabled/>
            </div>
            <div class="form-group">
                <label for="new_name">新名称:</label>
                <input v-model="new_name" type="text" class="form-control" id="new_name" ref="new_name" />
            </div>
          </div>
          <div class="modal-footer">
            <button @click="rename()" type="button" class="btn btn-info">重命名</button>
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "netdisk",
  created(){
    this.$store.dispatch("netdisk_dir_list_get","");
  },
  data(){
    return {
      current_path:[],
      current_dir:"",
      upload_index:0,
      folder_name:"",
      delete_alert_text:"",
      rename_obj:null,
      old_name:"",
      new_name:"",
      display_move_button:false,
      move_obj:null,
      name_like:"",
      search_mode:false
    }
  },
  methods:{
    //触发 文件选择的click事件
    file_select(){  
      $("#up_file").trigger("click");
    },
    // 文件上传
    file_upload(){
      var files = this.$refs.up_file.files;
      for(let i=0; i<files.length; i++){
        let obj = {
          "dirname": this.current_dir,
          "file": files[i],
        };
        this.upload_index = i + 1;
        this.$store.dispatch("netdisk_file_upload", obj);
      }
    },
    // 文件下载
    file_down(file_link){
      this.$store.dispatch("netdisk_file_down",file_link);
    },
    // 新建文件夹,当有输入的时候,调整一下背景颜色
    folder_name_input(){
      this.$refs.folder_name.style.backgroundColor = "#e9ecef";
    },
    // 新建文件夹
    new_folder(){
        let obj = {
          "method":"new_folder",
          "dirname": this.current_dir,
          "folder_name": this.folder_name,
        };
        if(/^[\u4e00-\u9fa5,a-z,A-Z,0-9,_]{1,255}$/.test(this.folder_name)){
          this.$store.dispatch("netdisk_handler", obj);
          this.folder_name = "";
        }else{
          console.log("new_folder_name_error");
          this.$refs.folder_name.style.backgroundColor = "#f0b598";
        }
    },
    // 删除发布前,弹出确认模态框
    del_alert(item) {
      this.delete_path = item.path;
      this.delete_alert_text = item.name;
      $("#delete_modal").modal("show");
    },
    // 文件或目录删除
    del(){
      $("#delete_modal").modal("hide");
        let obj = {
          "method":"del",
          "path": this.delete_path,
        };
        this.$store.dispatch("netdisk_handler", obj);
    },
    // 删除前弹出警告框
    rename_alert(item) {
      this.rename_obj = item;
      this.old_name = item.name;
      this.new_name = item.name;
      $("#rename_modal").modal("show");
    },
    // 文件或目录重命名
    rename(){
        $("#rename_modal").modal("hide");
        let obj = {
          "method":"rename",
          "old_path": this.rename_obj.path,
          "new_path": this.new_name,
        };
        this.$store.dispatch("netdisk_handler", obj);
    },
    // 显示移动按钮
    show_move_button(item){
      this.display_move_button = true;
      this.move_obj = item;
    },
    // 文件或目录移动
    move(){
      this.display_move_button = false;
      let obj = {
          "method":"move",
          "from_path": this.move_obj.path,
          "to_path": this.current_dir,
        };
        this.$store.dispatch("netdisk_handler", obj);
    },
    // 显示目录下文件及文件夹
    dir_list(dirname){
      this.search_mode = false;
      $("#nav_netdisk_list").tab("show");
      this.current_path = [];
      this.current_dir = dirname;
      let obj = {
        "method": "list",
        "dirname": dirname
      }
      if(dirname == "/" || dirname == ""){
        this.$store.dispatch("netdisk_dir_list_get", obj);
      }else{
        this.current_path = String(dirname).split("/");
        this.$store.dispatch("netdisk_dir_list_get", obj);
      }
    },
    // 文件或目录搜索
    file_search(){
      this.search_mode = true;
      let obj = {
        "method": "search",
        "dirname": this.current_dir,
        "name_like":this.name_like
      }
      this.$store.dispatch("netdisk_dir_list_get", obj);
    },
    // 根据头部路径导航,跳转到指定目录
    dir_list_to(index){
      let obj =  this.current_path.slice(0,index+1);
      this.current_path = obj;
      this.dir_list(obj.join("/"));
    },
    // 显示目录树
    dir_tree(dirname){
      this.$store.dispatch("netdisk_dir_tree_get", dirname);
      $("#nav_netdisk_tree").tab("show");
    },
  },
  watch:{
    "$store.state.result_status":function(newVal,oldVal){
        if(newVal){
          this.dir_list(this.current_dir);
        }
    }
  }
};
</script>


