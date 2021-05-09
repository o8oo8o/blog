<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-header p-2">
            <ul class="nav nav-pills">
              <li class="nav-item">
                <a class="nav-link active" href="#config" id="nav_config" data-toggle="tab">配置</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#mail" id="nav_mail" data-toggle="tab">邮箱</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#chart" id="nav_chart" data-toggle="tab">图表</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#image" id="nav_image" data-toggle="tab">图像</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#account" id="nav_account" data-toggle="tab">账号</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#remote" id="nav_remote" data-toggle="tab">远程</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#frontend" id="nav_frontend" data-toggle="tab">前台</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#backend" id="nav_backend" data-toggle="tab">后台</a>
              </li>
            </ul>
          </div>
          <div class="card-body">
            <div class="tab-content">
              <div class="tab-pane active" id="config">
                <div class="form-horizontal">
                  <div class="form-group">
                    <label class="col-sm-4 control-label">后台标题</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="admin_title"
                        name="admin_title"
                        type="text"
                        required="required"
                        maxlength="15"
                        class="form-control"
                        placeholder="后台标题"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">后台名称</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="admin_name"
                        name="admin_name"
                        type="text"
                        required="required"
                        maxlength="15"
                        class="form-control"
                        placeholder="后台名称"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">邮箱</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="email"
                        name="email"
                        type="email"
                        required="required"
                        maxlength="126"
                        class="form-control"
                        placeholder="邮箱"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">GitHub链接</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="github_addr"
                        name="github_addr"
                        type="text"
                        required="required"
                        maxlength="254"
                        class="form-control"
                        placeholder="GitHub链接"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">GitHub名字</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="github_name"
                        name="github_name"
                        type="text"
                        required="required"
                        maxlength="127"
                        class="form-control"
                        placeholder="GitHub名字"
                      />
                    </div>
                  </div>

                  <div class="form-group">
                    <label class="col-sm-4 control-label">微博链接</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="weibo_addr"
                        name="weibo_addr"
                        type="text"
                        required="required"
                        maxlength="254"
                        class="form-control"
                        placeholder="微博链接"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">微博名字</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="weibo_name"
                        name="weibo_name"
                        type="text"
                        required="required"
                        maxlength="127"
                        class="form-control"
                        placeholder="微博名字"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">QQ号</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="qq"
                        name="qq"
                        type="text"
                        required="required"
                        maxlength="15"
                        class="form-control"
                        placeholder="QQ号"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">微信</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="wx"
                        name="wx"
                        type="text"
                        required="required"
                        maxlength="127"
                        class="form-control"
                        placeholder="微信"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">城市</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="city"
                        name="city"
                        type="text"
                        required="required"
                        maxlength="14"
                        class="form-control"
                        placeholder="城市"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">Logo文字</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="logo_text"
                        name="logo_text"
                        type="text"
                        required="required"
                        maxlength="4"
                        class="form-control"
                        placeholder="Logo文字"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">图像文字</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="icon_text"
                        name="icon_text"
                        type="text"
                        required="required"
                        maxlength="4"
                        class="form-control"
                        placeholder="Logo文字"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">前台标题</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="web_title"
                        name="web_title"
                        type="text"
                        required="required"
                        maxlength="15"
                        class="form-control"
                        placeholder="前台标题"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">音乐默认存储目录</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="music_dir"
                        name="music_dir"
                        type="text"
                        required="required"
                        minlength="1"
                        maxlength="127"
                        class="form-control"
                        placeholder="音乐默认存储目录,相对网盘根目录"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">说明(可以HTML)</label>
                    <div class="col-sm-12">
                      <textarea
                        v-model.trim="note"
                        name="note"
                        rows="3"
                        required="required"
                        class="form-control"
                        placeholder="说明(note可以HTML)"
                      ></textarea>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">信息(可以HTML)</label>
                    <div class="col-sm-12">
                      <textarea
                        v-model.trim="info"
                        name="note"
                        rows="3"
                        required="required"
                        class="form-control"
                        placeholder="信息(info可以HTML)"
                      ></textarea>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">页脚(可以HTML)</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="footer"
                        name="footer"
                        type="text"
                        required="required"
                        class="form-control"
                        placeholder="页脚(HTML)"
                      />
                    </div>
                  </div>

                  <div class="form-group">
                    <label class="col-sm-4 control-label">前台最近更新分页大小</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="web_last_pz"
                        name="web_last_pz"
                        type="number"
                        required="required"
                        min="2"
                        max="15"
                        class="form-control"
                        placeholder="前台最近更新分页大小"
                      />
                    </div>
                  </div>

                  <div class="form-group">
                    <label class="col-sm-4 control-label">前台博客分页大小</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="web_blog_pz"
                        name="web_blog_pz"
                        type="number"
                        required="required"
                        min="2"
                        max="100"
                        class="form-control"
                        placeholder="前台博客分页大小"
                      />
                    </div>
                  </div>

                  <div class="form-group">
                    <label class="col-sm-4 control-label">后台博客分页大小</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="admin_blog_pz"
                        name="admin_blog_pz"
                        type="number"
                        required="required"
                        min="2"
                        max="100"
                        class="form-control"
                        placeholder="后台博客分页大小"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">后台评论分页大小</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="admin_review_pz"
                        name="admin_review_pz"
                        type="number"
                        required="required"
                        min="2"
                        max="100"
                        class="form-control"
                        placeholder="后台评论分页大小"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">后台简历发布分页大小</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="admin_publish_pz"
                        name="admin_publish_pz"
                        type="number"
                        required="required"
                        min="2"
                        max="100"
                        class="form-control"
                        placeholder="后台简历发布分页大小"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">聊天功能</label>
                    <div class="col-sm-8">
                      <div class="form-check form-check-inline">
                        <input
                          v-model="enable_chat"
                          class="form-check-input"
                          type="radio"
                          required="required"
                          name="enable_chat"
                          id="enable_chat_a"
                          value="false"
                        />
                        <label class="form-check-label" for="enable_chat_a">关闭</label>
                      </div>
                      <div class="form-check form-check-inline">
                        <input
                          v-model="enable_chat"
                          class="form-check-input"
                          type="radio"
                          required="required"
                          name="enable_chat"
                          id="enable_chat_b"
                          value="true"
                        />
                        <label class="form-check-label" for="enable_chat_b">打开</label>
                      </div>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">音乐功能</label>
                    <div class="col-sm-8">
                      <div class="form-check form-check-inline">
                        <input
                          v-model="enable_music"
                          class="form-check-input"
                          type="radio"
                          required="required"
                          name="enable_music"
                          id="enable_music_a"
                          value="false"
                        />
                        <label class="form-check-label" for="enable_music_a">关闭</label>
                      </div>
                      <div class="form-check form-check-inline">
                        <input
                          v-model="enable_music"
                          class="form-check-input"
                          type="radio"
                          required="required"
                          name="enable_music"
                          id="enable_music_b"
                          value="true"
                        />
                        <label class="form-check-label" for="enable_music_b">打开</label>
                      </div>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">通知功能</label>
                    <div class="col-sm-8">
                      <div class="form-check form-check-inline">
                        <input
                          v-model="enable_notice"
                          class="form-check-input"
                          type="radio"
                          required="required"
                          name="enable_notice"
                          id="enable_notice_a"
                          value="false"
                        />
                        <label class="form-check-label" for="enable_notice_a">关闭</label>
                      </div>
                      <div class="form-check form-check-inline">
                        <input
                          v-model="enable_notice"
                          class="form-check-input"
                          type="radio"
                          required="required"
                          name="enable_notice"
                          id="enable_notice_b"
                          value="true"
                        />
                        <label class="form-check-label" for="enable_notice_b">打开</label>
                      </div>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">简历功能</label>
                    <div class="col-sm-8">
                      <div class="form-check form-check-inline">
                        <input
                          v-model="enable_resume"
                          class="form-check-input"
                          type="radio"
                          required="required"
                          name="enable_resume"
                          id="enable_resume_a"
                          value="false"
                        />
                        <label class="form-check-label" for="enable_resume_a">关闭</label>
                      </div>
                      <div class="form-check form-check-inline">
                        <input
                          v-model="enable_resume"
                          class="form-check-input"
                          type="radio"
                          required="required"
                          name="enable_resume"
                          id="enable_resume_b"
                          value="true"
                        />
                        <label class="form-check-label" for="enable_resume_b">打开</label>
                      </div>
                    </div>
                  </div>

                  <div class="form-group">
                    <label class="col-sm-4 control-label">广告</label>
                    <div class="col-sm-12">
                      <div id="editor" ref="editor" style="z-index:1;"></div>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label">保存</label>
                    <div class="col-sm-12">
                      <div class="card-footer">
                        <div>
                          <button @click="put_setting" type="button" class="btn btn-primary">保存</button>
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- ======================= -->
                </div>
              </div>
              <div class="tab-pane" id="mail">
                <div class="form-horizontal">
                  <div class="form-group">
                    <label class="col-sm-4 control-label">SMTP服务器</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="mail_smtp"
                        name="mail_smtp"
                        type="text"
                        required="required"
                        minlength="1"
                        maxlength="127"
                        class="form-control"
                        placeholder="SMTP服务器"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">SMTP端口</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="mail_port"
                        name="mail_port"
                        type="number"
                        required="required"
                        min="1"
                        max="65535"
                        class="form-control"
                        placeholder="SMTP端口"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">邮箱账号</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="mail_user"
                        name="mail_user"
                        type="mail"
                        required="required"
                        minlength="1"
                        maxlength="127"
                        class="form-control"
                        placeholder="邮箱账号"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">邮箱密码</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="mail_pwd"
                        name="mail_pwd"
                        type="password"
                        required="required"
                        minlength="1"
                        maxlength="127"
                        class="form-control"
                        placeholder="邮箱密码"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">开启SSL</label>
                    <div class="col-sm-8">
                      <div class="form-check form-check-inline">
                        <input
                          v-model="mail_ssl"
                          class="form-check-input"
                          type="radio"
                          required="required"
                          name="mail_ssl"
                          id="mail_ssl_a"
                          value="false"
                        />
                        <label class="form-check-label" for="mail_ssl_a">否</label>
                      </div>
                      <div class="form-check form-check-inline">
                        <input
                          v-model="mail_ssl"
                          class="form-check-input"
                          type="radio"
                          required="required"
                          name="mail_ssl"
                          id="mail_ssl_b"
                          value="true"
                        />
                        <label class="form-check-label" for="mail_ssl_b">是</label>
                      </div>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">接收通知邮箱</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="mail_recv"
                        name="mail_recv"
                        type="mail"
                        required="required"
                        minlength="1"
                        maxlength="127"
                        class="form-control"
                        placeholder="接收通知邮箱"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label">保存</label>
                    <div class="col-sm-12">
                      <div class="card-footer">
                        <div>
                          <button @click="put_setting" type="button" class="btn btn-primary">保存</button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane" id="chart">
                <div class="form-horizontal">
                  <div class="form-group">
                    <label class="col-sm-4 control-label">图表显示天数</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="chart_day"
                        name="chart_day"
                        type="number"
                        required="required"
                        min="3"
                        max="90"
                        class="form-control"
                        placeholder="图表显示天数"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">Y轴是否从零显示</label>
                    <div class="col-sm-8">
                      <div class="form-check form-check-inline">
                        <input
                          v-model="chart_zero"
                          class="form-check-input"
                          type="radio"
                          required="required"
                          name="chart_zero"
                          id="chart_zero_a"
                          value="false"
                        />
                        <label class="form-check-label" for="chart_zero_a">否</label>
                      </div>
                      <div class="form-check form-check-inline">
                        <input
                          v-model="chart_zero"
                          class="form-check-input"
                          type="radio"
                          required="required"
                          name="chart_zero"
                          id="chart_zero_b"
                          value="true"
                        />
                        <label class="form-check-label" for="chart_zero_b">是</label>
                      </div>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">图表边框宽度</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="chart_border_width"
                        name="chart_border_width"
                        type="number"
                        required="required"
                        min="1"
                        max="10"
                        class="form-control"
                        placeholder="图表边框宽度"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">图表背景颜色</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="chart_bg_color"
                        name="chart_bg_color"
                        type="text"
                        required="required"
                        minlength="1"
                        maxlength="63"
                        class="form-control"
                        placeholder="图表背景颜色"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">图表边框颜色</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="chart_br_color"
                        name="chart_br_color"
                        type="text"
                        required="required"
                        minlength="1"
                        maxlength="63"
                        class="form-control"
                        placeholder="图表边框颜色"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label">保存</label>
                    <div class="col-sm-12">
                      <div class="card-footer">
                        <div>
                          <button @click="put_setting" type="button" class="btn btn-primary">保存</button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane" id="image">
                <div class="form-horizontal">
                  <div class="form-group form-inline">
                    <label class="control-label">Logo(点击图片更换)</label>
                    <span class="col-sm-4">
                      <img
                        :src="this.$store.state.setting.logo_path"
                        @click="file_select"
                        id="logo"
                        ref="logo"
                        class="img-circle elevation-3"
                        style="border: 1px solid #ccc; width: 128px; height: 128px; background-size: contain; background-repeat: no-repeat; background-position: center center;"
                      />
                    </span>
                  </div>
                  <div class="form-group form-inline">
                    <label class="control-label">图像(点击图片更换)</label>
                    <span class="col-sm-4">
                      <img
                        :src="this.$store.state.setting.icon_path"
                        @click="file_select"
                        id="icon"
                        ref="icon"
                        class="img-circle elevation-3"
                        style="border: 1px solid #ccc; width: 128px; height: 128px; background-size: contain; background-repeat: no-repeat; background-position: center center;"
                      />
                    </span>
                  </div>
                  <span class="display:none">
                    <!-- 文件输入框 -->
                    <input
                      @change="update_img"
                      type="file"
                      name="imgs"
                      class="custom-file-input"
                      id="img_file"
                      ref="img_file"
                      accept="image/*"
                    />
                  </span>
                </div>
              </div>
              <div class="tab-pane" id="account">
                <div class="form-horizontal">
                  <div class="form-group">
                    <label class="col-sm-4 control-label">用户名</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="admin_user"
                        name="admin_user"
                        type="text"
                        required="required"
                        maxlength="126"
                        class="form-control"
                        placeholder="后台管理账号"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">密码</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="pwd"
                        @input="input_change"
                        name="pwd"
                        type="password"
                        required="required"
                        maxlength="126"
                        class="form-control"
                        placeholder="密码"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">确认密码</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="pwd2"
                        @input="input_change"
                        name="pwd2"
                        type="password"
                        required="required"
                        maxlength="126"
                        class="form-control"
                        placeholder="密码"
                      />
                    </div>
                  </div>

                  <div class="form-group">
                    <div class="col-sm-12">
                      <span v-text="error_msg" style="color:red"></span>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label">保存</label>
                    <div class="col-sm-12">
                      <div class="card-footer">
                        <div>
                          <button @click="put_pwd" type="button" class="btn btn-primary">保存</button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane" id="remote">
                <div class="form-horizontal">
                  <div class="form-group">
                    <label class="col-sm-4 control-label">SSH主机</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="ssh_host"
                        name="ssh_host"
                        type="text"
                        required="required"
                        maxlength="126"
                        class="form-control"
                        placeholder="SSH主机"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">SSH端口</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="ssh_port"
                        name="ssh_port"
                        type="number"
                        required="required"
                        min="1"
                        max="65535"
                        class="form-control"
                        placeholder="SSH端口"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">SSH用户</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="ssh_user"
                        name="ssh_user"
                        type="text"
                        required="required"
                        maxlength="126"
                        class="form-control"
                        placeholder="SSH用户"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">SSH密码</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="ssh_pwd"
                        name="ssh_pwd"
                        type="password"
                        required="required"
                        maxlength="126"
                        class="form-control"
                        placeholder="SSH密码"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">SSH窗口宽度</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="ssh_width"
                        name="ssh_width"
                        type="number"
                        required="required"
                        min="30"
                        max="600"
                        class="form-control"
                        placeholder="SSH窗口宽度"
                      />
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-sm-4 control-label">SSH窗口高度</label>
                    <div class="col-sm-12">
                      <input
                        v-model.trim="ssh_height"
                        name="ssh_height"
                        type="number"
                        required="required"
                        min="10"
                        max="300"
                        class="form-control"
                        placeholder="SSH窗口高度"
                      />
                    </div>
                  </div>

                  <div class="form-group">
                    <div class="col-sm-12">
                      <span v-text="error_msg" style="color:red"></span>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label">保存</label>
                    <div class="col-sm-12">
                      <div class="card-footer">
                        <div>
                          <button @click="put_setting" type="button" class="btn btn-primary">保存</button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane" id="frontend">
                <div class="form-horizontal">
                  <div class="form-group">
                    <textarea
                      v-model.trim="web_patch_html"
                      class="form-control"
                      rows="11"
                      placeholder="HTML"
                      wrap="off"
                    ></textarea>
                    <textarea
                      v-model.trim="web_patch_css"
                      class="form-control"
                      rows="11"
                      placeholder="CSS"
                      wrap="off"
                    ></textarea>
                    <textarea
                      v-model.trim="web_patch_js"
                      class="form-control"
                      rows="11"
                      placeholder="JavaScript"
                      wrap="off"
                    ></textarea>
                  </div>

                  <div class="form-group">
                    <div class="col-sm-12">
                      <span v-text="error_msg" style="color:red"></span>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label">保存</label>
                    <div class="col-sm-12">
                      <div class="card-footer">
                        <div>
                          <button @click="put_setting" type="button" class="btn btn-primary">保存</button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane" id="backend">
                <div class="form-horizontal">
                  <div class="form-group">
                    <textarea
                      v-model.trim="admin_patch_html"
                      class="form-control"
                      rows="11"
                      placeholder="HTML"
                      wrap="off"
                    ></textarea>
                    <textarea
                      v-model.trim="admin_patch_css"
                      class="form-control"
                      rows="11"
                      placeholder="CSS"
                      wrap="off"
                    ></textarea>
                    <textarea
                      v-model.trim="admin_patch_js"
                      class="form-control"
                      rows="11"
                      placeholder="JavaScript"
                      wrap="off"
                    ></textarea>
                  </div>

                  <div class="form-group">
                    <div class="col-sm-12">
                      <span v-text="error_msg" style="color:red"></span>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="control-label">保存</label>
                    <div class="col-sm-12">
                      <div class="card-footer">
                        <div>
                          <button @click="put_setting" type="button" class="btn btn-primary">保存</button>
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
            <h4 class="modal-title" id="succees_modalLabel">控制面板</h4>
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
  name: "setting",
  created() {
    let obj = {
      handle_type: "get"
    };
    this.$store.dispatch("setting_handler", obj);
  },
  mounted() {
    // 富文本编辑器
    var editor = new window.Editor(document.getElementById("editor"));
    //this.editor = editor;
    //var editor = new window.Editor(this.$refs.editor);
    editor.customConfig.onchange = html => {
      this.banner = html;
    };
    // 将图片大小限制为 10M
    editor.customConfig.uploadImgMaxSize = 10 * 1024 * 1024;

    // 限制一次最多上传 5 张图片
    editor.customConfig.uploadImgMaxLength = 50;

    // 上传图片到服务器
    editor.customConfig.uploadImgServer = "/api/admin/upload/";
    // 自定义上传方法
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
      pwd: "",
      pwd2: "",
      error_msg: "",
      editor: "",
      imgage: ""
    };
  },
  methods: {
    // 更新设置
    put_setting() {
      let obj = {
        handle_type: "put"
      };
      this.$store.dispatch("setting_handler", obj);
    },
    // 触发 文件选择的click事件
    file_select(e) {
      document.getElementById("img_file").click();
      this.imgage = String(e.target.id);
    },
    // 更新图像或者logo
    update_img() {
      let obj = {
        handle_type: this.imgage,
        files: this.$refs.img_file.files
      };
      this.$store.dispatch("upload_image", obj);
    },
    // 输入事件,输入的时候清理掉错误消息
    input_change() {
      this.error_msg = "";
    },
    // 更新密码
    put_pwd() {
      if (this.$store.state.setting.admin_user.length == 0) {
        this.error_msg = "用户名不能为空";
        return;
      }
      if (this.pwd.length < 6) {
        this.error_msg = "密码太短了,至少6位.";
        return;
      }
      if (this.pwd != this.pwd2) {
        this.error_msg = "两次密码输入不一致!";
        return;
      }
      this.$store.dispatch("account_handler", this.pwd);
    }
  },
  computed: {
    admin_user: {
      get() {
        return this.$store.state.setting.admin_user;
      },
      set(value) {
        this.$store.commit("UpdateSettingAdminUser", value);
      }
    },
    admin_pwd: {
      get() {
        return this.$store.state.setting.admin_pwd;
      },
      set(value) {
        this.$store.commit("UpdateSettingAdminPwd", value);
      }
    },
    admin_title: {
      get() {
        return this.$store.state.setting.admin_title;
      },
      set(value) {
        this.$store.commit("UpdateSettingAdminTitle", value);
      }
    },
    admin_name: {
      get() {
        return this.$store.state.setting.admin_name;
      },
      set(value) {
        this.$store.commit("UpdateSettingAdminName", value);
      }
    },
    //=========================
    email: {
      get() {
        return this.$store.state.setting.email;
      },
      set(value) {
        this.$store.commit("UpdateSettingEmail", value);
      }
    },
    github_addr: {
      get() {
        return this.$store.state.setting.github_addr;
      },
      set(value) {
        this.$store.commit("UpdateSettingGithubAddr", value);
      }
    },
    github_name: {
      get() {
        return this.$store.state.setting.github_name;
      },
      set(value) {
        this.$store.commit("UpdateSettingGithubName", value);
      }
    },
    weibo_addr: {
      get() {
        return this.$store.state.setting.weibo_addr;
      },
      set(value) {
        this.$store.commit("UpdateSettingWeiboAddr", value);
      }
    },
    weibo_name: {
      get() {
        return this.$store.state.setting.weibo_name;
      },
      set(value) {
        this.$store.commit("UpdateSettingWeiboName", value);
      }
    },
    qq: {
      get() {
        return this.$store.state.setting.qq;
      },
      set(value) {
        this.$store.commit("UpdateSettingQQ", value);
      }
    },
    wx: {
      get() {
        return this.$store.state.setting.wx;
      },
      set(value) {
        this.$store.commit("UpdateSettingWX", value);
      }
    },
    city: {
      get() {
        return this.$store.state.setting.city;
      },
      set(value) {
        this.$store.commit("UpdateSettingCity", value);
      }
    },
    logo_path: {
      get() {
        return this.$store.state.setting.logo_path;
      },
      set(value) {
        this.$store.commit("UpdateSettingLogoPath", value);
      }
    },
    logo_text: {
      get() {
        return this.$store.state.setting.logo_text;
      },
      set(value) {
        this.$store.commit("UpdateSettingLogoText", value);
      }
    },
    icon_path: {
      get() {
        return this.$store.state.setting.icon_path;
      },
      set(value) {
        this.$store.commit("UpdateSettingIconPath", value);
      }
    },
    icon_text: {
      get() {
        return this.$store.state.setting.icon_text;
      },
      set(value) {
        this.$store.commit("UpdateSettingIconText", value);
      }
    },
    web_title: {
      get() {
        return this.$store.state.setting.web_title;
      },
      set(value) {
        this.$store.commit("UpdateSettingWebTitle", value);
      }
    },
    banner: {
      get() {
        return this.$store.state.setting.banner;
      },
      set(value) {
        this.$store.commit("UpdateSettingBanner", value);
      }
    },
    note: {
      get() {
        return this.$store.state.setting.note;
      },
      set(value) {
        this.$store.commit("UpdateSettingNote", value);
      }
    },
    info: {
      get() {
        return this.$store.state.setting.info;
      },
      set(value) {
        this.$store.commit("UpdateSettingInfo", value);
      }
    },
    footer: {
      get() {
        return this.$store.state.setting.footer;
      },
      set(value) {
        this.$store.commit("UpdateSettingFooter", value);
      }
    },
    //=========================
    web_last_pz: {
      get() {
        return this.$store.state.setting.web_last_pz;
      },
      set(value) {
        this.$store.commit("UpdateSettingWebLastPz", value);
      }
    },
    web_blog_pz: {
      get() {
        return this.$store.state.setting.web_blog_pz;
      },
      set(value) {
        this.$store.commit("UpdateSettingWebBlogPz", value);
      }
    },
    admin_blog_pz: {
      get() {
        return this.$store.state.setting.admin_blog_pz;
      },
      set(value) {
        this.$store.commit("UpdateSettingAdminBlogPz", value);
      }
    },
    admin_review_pz: {
      get() {
        return this.$store.state.setting.admin_review_pz;
      },
      set(value) {
        this.$store.commit("UpdateSettingAdminReviewPz", value);
      }
    },
    admin_publish_pz: {
      get() {
        return this.$store.state.setting.admin_publish_pz;
      },
      set(value) {
        this.$store.commit("UpdateSettingAdminPublishPz", value);
      }
    },
    //=========================
    enable_chat: {
      get() {
        return this.$store.state.setting.enable_chat;
      },
      set(value) {
        this.$store.commit("UpdateSettingEnableChat", value);
      }
    },
    enable_music: {
      get() {
        return this.$store.state.setting.enable_music;
      },
      set(value) {
        this.$store.commit("UpdateSettingEnableMusic", value);
      }
    },
    enable_notice: {
      get() {
        return this.$store.state.setting.enable_notice;
      },
      set(value) {
        this.$store.commit("UpdateSettingEnableNotice", value);
      }
    },
    enable_resume: {
      get() {
        return this.$store.state.setting.enable_resume;
      },
      set(value) {
        this.$store.commit("UpdateSettingEnableResume", value);
      }
    },
    //=========================
    ssh_host: {
      get() {
        return this.$store.state.setting.ssh_host;
      },
      set(value) {
        this.$store.commit("UpdateSettingSshHost", value);
      }
    },
    ssh_port: {
      get() {
        return this.$store.state.setting.ssh_port;
      },
      set(value) {
        this.$store.commit("UpdateSettingSshPort", value);
      }
    },
    ssh_user: {
      get() {
        return this.$store.state.setting.ssh_user;
      },
      set(value) {
        this.$store.commit("UpdateSettingSshUser", value);
      }
    },
    ssh_pwd: {
      get() {
        return this.$store.state.setting.ssh_pwd;
      },
      set(value) {
        this.$store.commit("UpdateSettingSshPwd", value);
      }
    },
    ssh_width: {
      get() {
        return this.$store.state.setting.ssh_width;
      },
      set(value) {
        this.$store.commit("UpdateSettingSshWidth", value);
      }
    },
    ssh_height: {
      get() {
        return this.$store.state.setting.ssh_height;
      },
      set(value) {
        this.$store.commit("UpdateSettingSshHeight", value);
      }
    },
    //=========================
    chart_day: {
      get() {
        return this.$store.state.setting.chart_day;
      },
      set(value) {
        this.$store.commit("UpdateSettingChartDay", value);
      }
    },
    chart_zero: {
      get() {
        return this.$store.state.setting.chart_zero;
      },
      set(value) {
        this.$store.commit("UpdateSettingChartZero", value);
      }
    },
    chart_border_width: {
      get() {
        return this.$store.state.setting.chart_border_width;
      },
      set(value) {
        this.$store.commit("UpdateSettingChartBorderWidth", value);
      }
    },
    chart_bg_color: {
      get() {
        return this.$store.state.setting.chart_bg_color;
      },
      set(value) {
        this.$store.commit("UpdateSettingChartBgColor", value);
      }
    },
    chart_br_color: {
      get() {
        return this.$store.state.setting.chart_br_color;
      },
      set(value) {
        this.$store.commit("UpdateSettingChartBrColor", value);
      }
    },
    //=========================
    web_patch_html: {
      get() {
        return this.$store.state.setting.web_patch_html;
      },
      set(value) {
        this.$store.commit("UpdateSettingWebPatchHtml", value);
      }
    },
    web_patch_css: {
      get() {
        return this.$store.state.setting.web_patch_css;
      },
      set(value) {
        this.$store.commit("UpdateSettingWebPatchCss", value);
      }
    },
    web_patch_js: {
      get() {
        return this.$store.state.setting.web_patch_js;
      },
      set(value) {
        this.$store.commit("UpdateSettingWebPatchJs", value);
      }
    },
    admin_patch_html: {
      get() {
        return this.$store.state.setting.admin_patch_html;
      },
      set(value) {
        this.$store.commit("UpdateSettingAdminPatchHtml", value);
      }
    },
    admin_patch_css: {
      get() {
        return this.$store.state.setting.admin_patch_css;
      },
      set(value) {
        this.$store.commit("UpdateSettingAdminPatchCss", value);
      }
    },
    admin_patch_js: {
      get() {
        return this.$store.state.setting.admin_patch_js;
      },
      set(value) {
        this.$store.commit("UpdateSettingAdminPatchJs", value);
      }
    },
    //=========================
    music_dir: {
      get() {
        return this.$store.state.setting.music_dir;
      },
      set(value) {
        this.$store.commit("UpdateSettingMusicDir", value);
      }
    },
    mail_smtp: {
      get() {
        return this.$store.state.setting.mail_smtp;
      },
      set(value) {
        this.$store.commit("UpdateSettingMailSmtp", value);
      }
    },
    mail_port: {
      get() {
        return this.$store.state.setting.mail_port;
      },
      set(value) {
        this.$store.commit("UpdateSettingMailPort", value);
      }
    },
    mail_user: {
      get() {
        return this.$store.state.setting.mail_user;
      },
      set(value) {
        this.$store.commit("UpdateSettingMailUser", value);
      }
    },
    mail_pwd: {
      get() {
        return this.$store.state.setting.mail_pwd;
      },
      set(value) {
        this.$store.commit("UpdateSettingMailPwd", value);
      }
    },
    mail_ssl: {
      get() {
        return this.$store.state.setting.mail_ssl;
      },
      set(value) {
        this.$store.commit("UpdateSettingMailSsl", value);
      }
    },
    mail_recv: {
      get() {
        return this.$store.state.setting.mail_recv;
      },
      set(value) {
        this.$store.commit("UpdateSettingMailRecv", value);
      }
    }
  },
  watch: {
    // 操作成功,弹出操作成功模态框
    "$store.state.result_status": function(newVal, oldVal) {
      if (newVal) {
        $("#succees_modal").modal("show");
        setTimeout(function() {
          $("#succees_modal").modal("hide");
        }, 1000);
      }
    },
    // 加载完成以后,设置富文本编辑器内容
    "$store.state.load_ok": function(newVal, oldVal) {
      if (newVal) {
        this.editor.txt.html(this.$store.state.setting.banner);
      }
    }
  }
};
</script>
