import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        classify_list: [],

        review_list: [],
        review_max_page: 0,
        review_current_page: 1,
        review_search: "",

        blog_list: [],
        blog_max_page: 0,
        blog_current_page: 1,
        blog_title_exists: false,
        blog_search: "",

        resume_list: [],
        resume_title_exists: false,
        resume: {
            id: 0,
            title: "",
            text: "",
            create_time: "",
            update_time: ""
        },
        publish_list: [],
        publish_max_page: 0,
        publish_current_page: 1,
        publish_search: "",
        publish_access_code_exists: false,
        publish: {
            id: 0,
            access_code: "",
            resume_id: 1,
            resume_title: "",
            receiver: "",
            exp_time: "",
            read_count: 0,
            read_time: "",
            read_duration: 0,
            create_time: "",
            update_time: ""
        },
        netdisk: {
            dir_list: {
                f_count: 0,
                d_count: 0,
                list: []
            },
            dir_tree: "",
            upload_progress: 0,
            down_progress: "",
        },
        setting: {
            id: 0,
            admin_user: "",
            admin_pwd: "",
            admin_title: "博客后台管理",
            admin_name: "博客管理",

            email: "",
            github_addr: "",
            github_name: "",
            weibo_addr: "",
            weibo_name: "",
            qq: "",
            wx: "",
            city: "",
            logo_path: "img/logo.png",
            logo_text: "",
            icon_path: "img/user.png",
            icon_text: "",
            web_title: "",
            banner: "",
            note: "",
            info: "",
            footer: "",
            // pz  = page size 为了方便,简写了
            web_last_pz: 5,
            web_blog_pz: 15,
            admin_blog_pz: 15,
            admin_review_pz: 15,
            admin_publish_pz: 15,

            enable_chat: false,
            enable_music: false,
            enable_notice: true,
            enable_resume: false,

            ssh_host: "",
            ssh_port: 22,
            ssh_user: "",
            ssh_pwd: "",
            ssh_width: 120,
            ssh_height: 30,

            chart_day: 15,
            chart_zero: "",
            chart_border_width: 1,
            chart_bg_color: "",
            chart_br_color: "",

            web_patch_html: "",
            web_patch_css: "",
            web_patch_js: "",

            admin_patch_html: "",
            admin_patch_css: "",
            admin_patch_js: "",

            music_dir: "",
            mail_smtp: "",
            mail_port: "",
            mail_user: "",
            mail_pwd: "",
            mail_ssl: "",
            mail_recv: "",
        },

        blog: {
            id: 1,
            title: "",
            status: 1,
            read_count: 0,
            review_count: 0,
            create_time: "",
            update_time: "",
            is_review: false,
            is_public: false,
            weight: 2000,
            classify_id: 1,
            classify_name: "",
            text: "",
            review_list: []
        },
        monitor: {
            time: "0000-00-00 00:00:00",
            boot: "0000-00-00 00:00:00",
            cpu: {
                user: 0,
                system: 0,
                idle: 0
            },
            mem: {
                total: 0,
                used: 0,
                free: 0,
                available: 0,
                percent: 0
            },
            disk: [],
            disk_io: {
                read_count: 0,
                write_count: 0,
                read_bytes: 0,
                write_bytes: 0,
                read_time: 0,
                write_time: 0
            },
            net: {
                bytes_sent: 0,
                bytes_revc: 0,
                packets_sent: 0,
                packets_recv: 0,
                errin: 0,
                errout: 0,
                dropin: 0,
                dropout: 0
            }
        },
        _xsrf: "",
        result_status: false,
        load_ok: false,
        auth: false
    },
    mutations: {
        // 更新设置编辑或新增数据
        UpdateSetting(state, value) { state.setting = value },
        UpdateSettingAdminUser(state, value) { state.setting.admin_user = value },
        UpdateSettingAdminPwd(state, value) { state.setting.admin_pwd = value },
        UpdateSettingAdminTitle(state, value) { state.setting.admin_title = value },
        UpdateSettingAdminName(state, value) { state.setting.admin_name = value },

        UpdateSettingEmail(state, value) { state.setting.email = value },
        UpdateSettingGithubAddr(state, value) { state.setting.github_addr = value },
        UpdateSettingGithubName(state, value) { state.setting.github_name = value },
        UpdateSettingWeiboAddr(state, value) { state.setting.weibo_addr = value },
        UpdateSettingWeiboName(state, value) { state.setting.weibo_name = value },
        UpdateSettingQQ(state, value) { state.setting.qq = value },
        UpdateSettingWX(state, value) { state.setting.wx = value },
        UpdateSettingCity(state, value) { state.setting.city = value },
        UpdateSettingLogoPath(state, value) { state.setting.logo_path = value },
        UpdateSettingLogoText(state, value) { state.setting.logo_text = value },
        UpdateSettingIconPath(state, value) { state.setting.icon_path = value },
        UpdateSettingIconText(state, value) { state.setting.icon_text = value },
        UpdateSettingWebTitle(state, value) { state.setting.web_title = value },
        UpdateSettingBanner(state, value) { state.setting.banner = value },
        UpdateSettingNote(state, value) { state.setting.note = value },
        UpdateSettingInfo(state, value) { state.setting.info = value },
        UpdateSettingFooter(state, value) { state.setting.footer = value },
        // Pz = page size 为了简写
        UpdateSettingWebLastPz(state, value) { state.setting.web_last_pz = value },
        UpdateSettingWebBlogPz(state, value) { state.setting.web_blog_pz = value },
        UpdateSettingAdminBlogPz(state, value) { state.setting.admin_blog_pz = value },
        UpdateSettingAdminReviewPz(state, value) { state.setting.admin_review_pz = value },
        UpdateSettingAdminPublishPz(state, value) { state.setting.admin_publish_pz = value },

        UpdateSettingEnableChat(state, value) { state.setting.enable_chat = value },
        UpdateSettingEnableMusic(state, value) { state.setting.enable_music = value },
        UpdateSettingEnableNotice(state, value) { state.setting.enable_notice = value },
        UpdateSettingEnableResume(state, value) { state.setting.enable_resume = value },

        UpdateSettingSshHost(state, value) { state.setting.ssh_host = value },
        UpdateSettingSshPort(state, value) { state.setting.ssh_port = value },
        UpdateSettingSshUser(state, value) { state.setting.ssh_user = value },
        UpdateSettingSshPwd(state, value) { state.setting.ssh_pwd = value },
        UpdateSettingSshWidth(state, value) { state.setting.ssh_width = value },
        UpdateSettingSshHeight(state, value) { state.setting.ssh_height = value },

        UpdateSettingChartDay(state, value) { state.setting.chart_day = value },
        UpdateSettingChartZero(state, value) { state.setting.chart_zero = value },
        UpdateSettingChartBorderWidth(state, value) { state.setting.chart_border_width = value },
        UpdateSettingChartBgColor(state, value) { state.setting.chart_bg_color = value },
        UpdateSettingChartBrColor(state, value) { state.setting.chart_br_color = value },

        UpdateSettingWebPatchHtml(state, value) { state.setting.web_patch_html = value },
        UpdateSettingWebPatchCss(state, value) { state.setting.web_patch_css = value },
        UpdateSettingWebPatchJs(state, value) { state.setting.web_patch_js = value },

        UpdateSettingAdminPatchHtml(state, value) { state.setting.admin_patch_html = value },
        UpdateSettingAdminPatchCss(state, value) { state.setting.admin_patch_css = value },
        UpdateSettingAdminPatchJs(state, value) { state.setting.admin_patch_js = value },

        UpdateSettingMusicDir(state, value) { state.setting.music_dir = value },
        UpdateSettingMailSmtp(state, value) { state.setting.mail_smtp = value },
        UpdateSettingMailPort(state, value) { state.setting.mail_port = value },
        UpdateSettingMailUser(state, value) { state.setting.mail_user = value },
        UpdateSettingMailPwd(state, value) { state.setting.mail_pwd = value },
        UpdateSettingMailSsl(state, value) { state.setting.mail_ssl = value },
        UpdateSettingMailRecv(state, value) { state.setting.mail_recv = value },

        UpdateXsrf(state, value) { state._xsrf = value; },
        UpdateAuth(state, value) { state.auth = value; },
        UpdateResultStatus(state, value) { state.result_status = value },
        UpdateLoadOk(state, value) { state.load_ok = value; },

        // 更新博客分类列表
        UpdateClassifyList(state, value) { state.classify_list = value },

        // 更新博客列表
        UpdateBlogList(state, data) {
            state.blog_list = data.blog_list;
            state.blog_max_page = data.max_page;
        },
        // 更新整个博客、搜索标题、标题是否存在、当前页码
        UpdateBlog(state, value) { state.blog = value; },
        UpdateBlogSearch(state, value) { state.blog_search = value; },
        UpdateBlogTitleExists(state, value) { state.blog_title_exists = value; },
        UpdateBlogCurrentPage(state, value) { state.blog_current_page = value; },
        //更新编辑或新增数据
        UpdateBlogTitle(state, value) { state.blog.title = value; },
        UpdateBlogStatus(state, value) { state.blog.status = value; },
        UpdateBlogText(state, value) { state.blog.text = value; },
        UpdateBlogIsReview(state, value) { state.blog.is_review = value; },
        UpdateBlogIsPublic(state, value) { state.blog.is_public = value; },
        UpdateBlogWeight(state, value) { state.blog.weight = value; },
        UpdateBlogClassifyId(state, value) { state.blog.classify_id = value; },
        UpdateBlogReviewList(state, value) { state.blog.review_list = value; },
        UpdateBlogCreateTime(state, value) { state.blog.create_time = value; },
        UpdateBlogUpdateTime(state, value) { state.blog.update_time = value; },
        UpdateBlogReadCount(state, value) { state.blog.read_count = value; },
        UpdateBlogReviewCount(state, value) { state.blog.review_count = value; },

        // 更新评论列表
        UpdateReviewList(state, data) {
            state.review_list = data.review_list;
            state.review_max_page = data.max_page;
        },
        UpdateReviewSearch(state, value) { state.review_search = value; },
        UpdateReviewCurrentPage(state, page_number) { state.review_current_page = page_number; },

        // 更新简历列表及编辑
        UpdateResumeList(state, value) { state.resume_list = value },
        UpdateResumeTitle(state, value) { state.resume.title = value },
        UpdateResumeText(state, value) { state.resume.text = value },
        UpdateResume(state, value) { state.resume = value },
        UpdateResumeTitleExists(state, value) { state.resume_title_exists = value },

        // 更新发布列表及编辑
        UpdatePublishList(state, data) {
            state.publish_list = data.publish_list;
            state.publish_max_page = data.max_page;
        },
        UpdatePublishCurrentPage(state, value) { state.publish_current_page = value },
        UpdatePublish(state, value) { state.publish = value },
        UpdatePublishAccessCodeExists(state, value) { state.publish_access_code_exists = value },
        UpdatePublishSearch(state, value) { state.publish_search = value; },
        UpdatePublishId(state, value) { state.publish.id = value },
        UpdatePublishReceiver(state, value) { state.publish.receiver = value },
        UpdatePublishAccessCode(state, value) { state.publish.access_code = value },
        UpdatePublishExpTime(state, value) { state.publish.exp_time = value },
        UpdatePublishResumeId(state, value) { state.publish.resume_id = value },

        // 更新设置编辑或新增数据
        UpdateNetDiskDirTree(state, value) {
            // 这种替换需要考虑性能
            //let str = String(value.data).replace(new RegExp("\n", "gm"), "<br>").replace(new RegExp(" ", "gm"),"&nbsp;&nbsp;");
            let str = String(value.data).replace(/\n/gm, "<br>").replace(/ /gm, "&nbsp;&nbsp;");
            state.netdisk.dir_tree = str;
        },
        UpdateNetDiskDirList(state, value) {
            state.netdisk.dir_list = value;
        },
        // 上传下载进度
        UpdateNetDiskUploadProgress(state, value) { state.netdisk.upload_progress = value },
        UpdateNetDiskDownProgress(state, value) { state.netdisk.down_progress = value },

        // 更新主机监控数据
        UpdateMonitor(state, value) { state.monitor = value },

        // 动态增加补丁
        DynamicPatch(state) {
            try {
                var patch = document.getElementById("patch");
                patch.textContent = "";

                var html = document.createElement("div");
                html.id = "patch_html";
                html.innerHTML = state.setting.admin_patch_html;
                patch.appendChild(html);

                var css = document.createElement("style");
                css.id = "patch_css";
                css.innerHTML = state.setting.admin_patch_css;
                patch.appendChild(css);

                var js = document.createElement("script");
                js.id = "patch_js";
                js.innerHTML = `
                    try {
                        ${state.setting.admin_patch_js}
                    }
                    catch(error) {
                        console.log("patch_js error:->"+error.message);
                    }
                `;
                patch.appendChild(js);
            } catch (error) {
                console.log("DynamicPatch_add_error");
            }
        }
    },
    actions: {
        // 获取xsrf
        get_xsrf(context) {
            axios.get("/api/open/xsrf/")
                .then(function(response) {
                    var data = response.data;
                    if (data.code != 0) {
                        console.log("/api/open/xsrf/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateXsrf", data._xsrf);
                    }
                })
                .catch(function(error) {
                    console.log("/api/open/xsrf/,请求异常");
                });
        },
        // 退出登陆
        logout() {
            localStorage.clear()
            var that = this;
            axios.get("/api/admin/logout/?").then(function(response) {
                console.log("logout_finish");
            }).catch(function(error) {
                console.log("/api/admin/logout/,请求异常");
            });
        },
        // 图像,Logo,编辑器的图片上传
        upload_image(context, obj) {
            for (var i = 0; i < obj.files.length; i++) {
                var fm = new FormData();
                fm.append("_xsrf", this.state._xsrf);
                fm.append("id", this.state.setting.id);
                fm.append("handle_type", obj.handle_type);
                fm.append("files", obj.files[i]);
                axios.post(`/api/admin/upload/`, fm)
                    .then(function(response) {
                        var data = response.data;
                        if (data.code != 0) {
                            console.log("/api/admin/upload/,服务端错误");
                        }
                        if (data.code == 0) {
                            if (obj.handle_type == "logo") {
                                context.commit("UpdateSettingLogoPath", data.data);
                            }
                            if (obj.handle_type == "icon") {
                                context.commit("UpdateSettingIconPath", data.data);
                            }
                            if (obj.handle_type == "edit") {
                                // insert 是编辑器带的方法
                                obj.insert(data.data);
                            }
                        }
                    })
                    .catch(function(error) {
                        console.log("/api/admin/upload/,请求异常");
                    });
            }
        },
        // 博客分类处理
        classify_handler(context, obj) {
            context.commit("UpdateResultStatus", false);
            axios.defaults.headers.common["X-Xsrftoken"] = this.state._xsrf;
            var param = "";
            var ajax = null;
            var fm = new FormData();
            fm.append("_xsrf", this.state._xsrf);
            if (obj.handle_type == "get") {
                // 获取操作,实际上返回的是一个列表,因为类型数据比较简单,所有偷懒了，没有按照套路出牌
                ajax = axios.get
            }
            if (obj.handle_type == "add") {
                // 增加操作
                fm.append("name", obj.name);
                ajax = axios.post
            }
            if (obj.handle_type == "del") {
                // 删除操作
                param = "?classify_id=" + String(obj.classify_id);
                ajax = axios.delete
            }
            if (obj.handle_type == "put") {
                // 更新操作
                fm.append("classify_id", obj.classify_id);
                fm.append("name", obj.name);
                ajax = axios.put
            }

            ajax(`/api/admin/classify/${param}`, fm)
                .then(function(response) {
                    var data = response.data;

                    if (data.code != 0) {
                        console.log("/api/admin/classify/,服务端错误");
                    }
                    if (data.code == 0) {
                        if (obj.handle_type != "get") {
                            context.commit("UpdateResultStatus", true);
                        }
                        context.commit("UpdateClassifyList", data.classify_list);
                    }
                })
                .catch(function(error) {
                    console.log("/api/admin/classify/,请求异常");
                });
            context.commit("UpdateResultStatus", false);
        },
        // 博客列表获取及搜索 
        blog_list_get(context, obj) {
            var param = null;
            var page = 1;
            if (obj.handle_type == "page") {
                // 分页查找
                page = obj.page_number;
                param = "?page=" + String(obj.page_number) + "&title_like=" + String(this.state.blog_search);
            }
            if (obj.handle_type == "find") {
                // 搜索操作
                param = "?page=1&title_like=" + String(this.state.blog_search);
            }
            axios.get(`/api/admin/blog_list/${param}`)
                .then(function(response) {
                    var data = response.data;
                    if (data.code != 0) {
                        console.log("/api/admin/blog_list/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateBlogList", data);
                        context.commit("UpdateBlogCurrentPage", page);
                    }
                })
                .catch(function(error) {
                    console.log("/api/admin/blog_list/,请求异常");
                });
        },
        // 博客标题检查 
        blog_title_check(context) {
            axios.get(`/api/admin/blog_title_check/?title=${this.state.blog.title}`)
                .then(function(response) {
                    var data = response.data;
                    if (data.code != 0) {
                        console.log("/api/admin/blog_title_check/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateBlogTitleExists", data.is_exists);
                    }
                })
                .catch(function(error) {
                    console.log("/api/admin/blog_title_check/,请求异常");
                });
        },
        // 博客处理
        blog_handler(context, obj) {
            context.commit("UpdateResultStatus", false);
            context.commit("UpdateLoadOk", false);
            axios.defaults.headers.common["X-Xsrftoken"] = this.state._xsrf;
            var param = "";
            var ajax = null;
            var fm = new FormData();
            fm.append("_xsrf", this.state._xsrf);
            fm.append("title", this.state.blog.title);
            fm.append("status", this.state.blog.status);
            fm.append("text", this.state.blog.text);
            fm.append("is_review", this.state.blog.is_review);
            fm.append("is_public", this.state.blog.is_public);
            fm.append("weight", this.state.blog.weight);
            fm.append("classify_id", this.state.blog.classify_id);
            if (obj.handle_type == "get") {
                // 获取操作
                param = "?blog_id=" + String(obj.blog_id);
                ajax = axios.get;
            }
            if (obj.handle_type == "add") {
                // 增加操作
                ajax = axios.post;
            }
            if (obj.handle_type == "del") {
                // 删除操作
                param = "?blog_id=" + String(obj.blog_id);
                ajax = axios.delete;
            }
            if (obj.handle_type == "put") {
                // 更新操作
                fm.append("blog_id", this.state.blog.id);
                ajax = axios.put;
            }
            ajax(`/api/admin/blog/${param}`, fm)
                .then(function(response) {
                    var data = response.data;

                    if (data.code != 0) {
                        console.log("/api/admin/blog/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateLoadOk", true);
                        if (obj.handle_type == "get") {
                            context.commit("UpdateBlog", data);
                        } else {
                            context.commit("UpdateResultStatus", true);
                            context.commit("UpdateBlogList", data);
                        }
                    }
                })
                .catch(function(error) {
                    console.log("/api/admin/blog/,请求异常");
                });
            context.commit("UpdateResultStatus", false);
            context.commit("UpdateLoadOk", false);
        },
        // 评论列表获取及搜索
        review_list_get(context, obj) {
            var param = null;
            var page = 1;
            if (obj.handle_type == "page") {
                // 分页查找
                page = obj.page_number;
                param = "?page=" + String(obj.page_number) + "&name_or_text_like=" + String(this.state.review_search);
            }
            if (obj.handle_type == "find") {
                // 搜索操作
                param = "?page=1&name_or_text_like=" + String(this.state.review_search);
            }
            axios.get(`/api/admin/review/${param}`)
                .then(function(response) {
                    var data = response.data;
                    if (data.code != 0) {
                        console.log("/api/admin/review/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateReviewList", data);
                        context.commit("UpdateReviewCurrentPage", page)
                    }
                })
                .catch(function(error) {
                    console.log("/api/admin/review/,请求异常");
                });
        },
        // 评论处理
        review_handler(context, obj) {
            context.commit("UpdateResultStatus", false);
            axios.defaults.headers.common["X-Xsrftoken"] = this.state._xsrf;
            axios.delete(`/api/admin/review/?review_id=${obj.review_id}`)
                .then(function(response) {
                    var data = response.data;
                    if (data.code != 0) {
                        console.log("/api/admin/review/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateResultStatus", true);
                        context.commit("UpdateReviewList", data);
                    }
                })
                .catch(function(error) {
                    console.log("/api/admin/review/,请求异常");
                });
            context.commit("UpdateResultStatus", false);
        },
        // 简历列表获取
        resume_list_get(context) {
            axios.get(`/api/admin/resume_list/?`)
                .then(function(response) {
                    var data = response.data;

                    if (data.code != 0) {
                        console.log("/api/admin/resume_list/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateResumeList", data.resume_list);
                    }
                })
                .catch(function(error) {
                    console.log("/api/admin/resume_list/,请求异常");
                });
        },
        // 简历标题检查
        resume_title_check(context) {
            axios.get(`/api/admin/resume_title_check/?title=${this.state.resume.title}`)
                .then(function(response) {
                    var data = response.data;
                    if (data.code != 0) {
                        console.log("/api/admin/resume_title_check/,服务器错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateResumeTitleExists", data.is_exists);
                    }
                })
                .catch(function(error) {
                    console.log("/api/admin/resume_title_check/,请求异常");
                });
        },
        // 简历处理
        resume_handler(context, obj) {
            context.commit("UpdateResultStatus", false);
            context.commit("UpdateLoadOk", false);
            axios.defaults.headers.common["X-Xsrftoken"] = this.state._xsrf;
            var param = "";
            var ajax = null;
            var fm = new FormData();
            fm.append("_xsrf", this.state._xsrf);
            fm.append("title", this.state.resume.title);
            fm.append("text", this.state.resume.text);

            if (obj.handle_type == "get") {
                // 获取操作
                param = "?resume_id=" + String(obj.resume_id);
                ajax = axios.get;
            }
            if (obj.handle_type == "add") {
                // 增加操作
                ajax = axios.post;
            }
            if (obj.handle_type == "del") {
                // 删除操作
                param = "?resume_id=" + String(obj.resume_id);
                ajax = axios.delete;
            }
            if (obj.handle_type == "put") {
                // 更新操作
                fm.append("resume_id", this.state.resume.id);
                ajax = axios.put;
            }
            ajax(`/api/admin/resume/${param}`, fm)
                .then(function(response) {
                    var data = response.data;

                    if (data.code != 0) {
                        console.log("/api/admin/resume/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateLoadOk", true);
                        if (obj.handle_type == "get") {
                            context.commit("UpdateResume", data.resume);
                        } else {
                            context.commit("UpdateLoadOk", true);
                            context.commit("UpdateResultStatus", true);
                            context.commit("UpdateResumeList", data.resume_list);
                        }
                    }
                })
                .catch(function(error) {
                    console.log("/api/admin/resume/,请求异常");
                });
            context.commit("UpdateResultStatus", false);
            context.commit("UpdateLoadOk", false);
        },
        // 发布列表获取及搜索
        publish_list_get(context, obj) {
            var param = null;
            var page = 1;
            if (obj.handle_type == "page") {
                // 分页查找
                page = obj.page_number;
                param = "?page=" + String(obj.page_number) + "&receiver_like=" + String(this.state.publish_search);
            }
            if (obj.handle_type == "find") {
                // 搜索操作
                param = "?page=1&receiver_like=" + String(this.state.publish_search);
            }
            axios.get(`/api/admin/publish_list/${param}`)
                .then(function(response) {
                    var data = response.data;
                    if (data.code != 0) {
                        console.log("/api/admin/publish_list/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdatePublishList", data);
                        context.commit("UpdatePublishCurrentPage", page);
                    }
                })
                .catch(function(error) {
                    console.log("/api/admin/publish_list/,请求异常");
                });
        },
        // 发布访问码检查
        publish_access_code_check(context) {
            axios.get(`/api/admin/publish_access_code_check/?access_code=${this.state.publish.access_code}`)
                .then(function(response) {
                    var data = response.data;
                    if (data.code != 0) {
                        console.log("/api/admin/publish_access_code_check/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdatePublishAccessCodeExists", data.is_exists);
                    }
                })
                .catch(function(error) {
                    console.log("/api/admin/publish_access_code_check/,请求错误");
                });
        },
        // 发布简历
        publish_handler(context, obj) {
            context.commit("UpdateResultStatus", false);
            axios.defaults.headers.common["X-Xsrftoken"] = this.state._xsrf;
            var param = "";
            var ajax = null;
            var fm = new FormData();
            fm.append("_xsrf", this.state._xsrf);
            fm.append("resume_id", this.state.publish.resume_id);
            fm.append("receiver", this.state.publish.receiver);
            fm.append("access_code", this.state.publish.access_code);
            fm.append("exp_time", this.state.publish.exp_time);
            if (obj.handle_type == "add") {
                // 增加操作
                ajax = axios.post;
            }
            if (obj.handle_type == "del") {
                // 删除操作
                param = "?publish_id=" + String(obj.publish_id);
                ajax = axios.delete;
            }
            if (obj.handle_type == "put") {
                // 更新操作
                fm.append("publish_id", this.state.publish.id);
                ajax = axios.put;
            }
            ajax(`/api/admin/publish/${param}`, fm)
                .then(function(response) {
                    var data = response.data;

                    if (data.code != 0) {
                        console.log("/api/admin/publish/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateResultStatus", true);
                        context.commit("UpdatePublishList", data);
                    }
                })
                .catch(function(error) {
                    console.log("/api/admin/publish/,请求异常");
                });
            context.commit("UpdateResultStatus", false);
            context.commit("UpdateLoadOk", false);
        },
        // 获取文件列表,或搜索文件
        netdisk_dir_list_get(context, obj) {
            var param = "";
            if (obj.method == "search") {
                // 搜索文件
                param = "?dirname=" + String(obj.dirname) + "&search_file=" + String(obj.name_like);
            }
            if (obj.method == "list") {
                // 获取文件列表
                param = "?dirname=" + String(obj.dirname);
            }
            axios.get(`/api/admin/dir_list/${param}`)
                .then(function(response) {
                    var data = response.data;
                    if (data.code != 0) {
                        console.log("/api/admin/dir_list/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateNetDiskDirList", data);
                    }
                }).catch(function(error) {
                    console.log("/api/admin/dir_list/,请求异常");
                })
        },
        // 获取目录树
        netdisk_dir_tree_get(context, dirname) {
            axios.get(`/api/admin/dir_tree/?dirname=${dirname}`)
                .then(function(response) {
                    var data = response.data;
                    if (data.code != 0) {
                        console.log("/api/admin/dir_tree/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateNetDiskDirTree", data);
                    }
                }).catch(function(error) {
                    console.log("/api/admin/dir_tree/,请求异常");
                })
        },
        // 文件下载
        netdisk_file_down(context, file_link) {
            let filename = file_link.split("/").pop();
            var fm = new FormData();
            fm.append("method", "download");
            fm.append("_xsrf", this.state._xsrf);
            fm.append("file", file_link);
            axios.post(`/api/admin/net_disk/?`, fm, { responseType: "blob" })
                .then(function(response) {
                    let data = response.data;
                    if (!data) {
                        return;
                    }
                    let url = window.URL.createObjectURL(new Blob([data]));
                    let link = document.createElement("a");
                    link.style.display = "none";
                    link.href = url;
                    link.setAttribute("download", filename);
                    document.body.appendChild(link);
                    link.click();
                    // 对象释放
                    window.URL.revokeObjectURL(url);
                    document.body.removeChild(link);
                }).catch(function(error) {
                    console.log("/api/admin/net_disk/,请求异常");
                })
        },
        // 文件上传
        netdisk_file_upload(context, obj) {
            context.commit("UpdateResultStatus", false);
            var fm = new FormData();
            fm.append("method", "upload");
            fm.append("_xsrf", this.state._xsrf);
            fm.append("dirname", obj.dirname);
            fm.append("file", obj.file);
            axios.post(`/api/admin/net_disk/?`, fm, {
                onUploadProgress: function(e) { //原生获取上传进度的事件
                    if (e.lengthComputable) {
                        //属性lengthComputable主要表明总共需要完成的工作量和已经完成的工作是否可以被测量
                        //如果lengthComputable为false，就获取不到e.total和e.loaded
                        let upload_progress = Math.round(Number.parseInt(e.loaded / e.total * 100));
                        context.commit("UpdateNetDiskUploadProgress", upload_progress);
                    } else {
                        context.commit("UpdateNetDiskUploadProgress", 100);
                    }
                },
            }).then(function(response) {
                var data = response.data;
                if (data.code != 0) {
                    console.log("/api/admin/net_disk/,服务端错误");
                }
                if (data.code == 0) {
                    context.commit("UpdateResultStatus", true);
                    context.commit("UpdateNetDiskUploadProgress", 0);
                }
            }).catch(function(error) {
                console.log("/api/admin/net_disk/,请求异常");
            })
            context.commit("UpdateResultStatus", false);
        },
        // 新建文件夹
        netdisk_handler(context, obj) {
            context.commit("UpdateResultStatus", false);
            var fm = new FormData();
            fm.append("_xsrf", this.state._xsrf);
            if (obj.method == "new_folder") {
                fm.append("method", "new_folder");
                fm.append("dirname", obj.dirname);
                fm.append("folder_name", obj.folder_name);
            } else if (obj.method == "del") {
                fm.append("method", "delete_");
                fm.append("path", obj.path);
            } else if (obj.method == "rename") {
                fm.append("method", "rename");
                fm.append("old_path", obj.old_path);
                fm.append("new_path", obj.new_path);
            } else if (obj.method == "move") {
                fm.append("method", "move");
                fm.append("from_path", obj.from_path);
                fm.append("to_path", obj.to_path);
            }
            axios.post(`/api/admin/net_disk/?`, fm)
                .then(function(response) {
                    var data = response.data;
                    if (data.code != 0) {
                        console.log("/api/admin/net_disk/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateResultStatus", true);
                    }
                }).catch(function(error) {
                    console.log("/api/admin/net_disk/,请求异常");
                })
            context.commit("UpdateResultStatus", false);
        },
        // 设置操作
        setting_handler(context, obj) {
            context.commit("UpdateLoadOk", false);
            context.commit("UpdateResultStatus", false);
            axios.defaults.headers.common["X-Xsrftoken"] = this.state._xsrf;
            var ajax = null;
            var fm = new FormData();
            fm.append("_xsrf", this.state._xsrf);

            if (obj.handle_type == "get") {
                // 获取操作
                ajax = axios.get;
            }
            if (obj.handle_type == "put") {
                // 更新操作
                fm.append("id", this.state.setting.id);
                fm.append("admin_title", this.state.setting.admin_title);
                fm.append("admin_name", this.state.setting.admin_name);

                fm.append("email", this.state.setting.email);
                fm.append("github_addr", this.state.setting.github_addr);
                fm.append("github_name", this.state.setting.github_name);
                fm.append("weibo_addr", this.state.setting.weibo_addr);
                fm.append("weibo_name", this.state.setting.weibo_name);
                fm.append("qq", this.state.setting.qq);
                fm.append("wx", this.state.setting.wx);
                fm.append("city", this.state.setting.city);
                fm.append("logo_text", this.state.setting.logo_text);
                fm.append("icon_text", this.state.setting.icon_text);
                fm.append("web_title", this.state.setting.web_title);
                fm.append("banner", this.state.setting.banner);
                fm.append("note", this.state.setting.note);
                fm.append("info", this.state.setting.info);
                fm.append("footer", this.state.setting.footer);

                fm.append("web_last_pz", this.state.setting.web_last_pz);
                fm.append("web_blog_pz", this.state.setting.web_blog_pz);
                fm.append("admin_blog_pz", this.state.setting.admin_blog_pz);
                fm.append("admin_review_pz", this.state.setting.admin_review_pz);
                fm.append("admin_publish_pz", this.state.setting.admin_publish_pz);

                fm.append("enable_chat", this.state.setting.enable_chat);
                fm.append("enable_music", this.state.setting.enable_music);
                fm.append("enable_notice", this.state.setting.enable_notice);
                fm.append("enable_resume", this.state.setting.enable_resume);

                fm.append("ssh_host", this.state.setting.ssh_host);
                fm.append("ssh_port", this.state.setting.ssh_port);
                fm.append("ssh_user", this.state.setting.ssh_user);
                fm.append("ssh_pwd", this.state.setting.ssh_pwd);
                fm.append("ssh_width", this.state.setting.ssh_width);
                fm.append("ssh_height", this.state.setting.ssh_height);

                fm.append("chart_day", this.state.setting.chart_day);
                fm.append("chart_zero", this.state.setting.chart_zero);
                fm.append("chart_border_width", this.state.setting.chart_border_width);
                fm.append("chart_bg_color", this.state.setting.chart_bg_color);
                fm.append("chart_br_color", this.state.setting.chart_br_color);

                fm.append("web_patch_html", this.state.setting.web_patch_html);
                fm.append("web_patch_css", this.state.setting.web_patch_css);
                fm.append("web_patch_js", this.state.setting.web_patch_js);

                fm.append("admin_patch_html", this.state.setting.admin_patch_html);
                fm.append("admin_patch_css", this.state.setting.admin_patch_css);
                fm.append("admin_patch_js", this.state.setting.admin_patch_js);

                fm.append("music_dir", this.state.setting.music_dir);
                fm.append("mail_smtp", this.state.setting.mail_smtp);
                fm.append("mail_port", this.state.setting.mail_port);
                fm.append("mail_user", this.state.setting.mail_user);
                fm.append("mail_pwd", this.state.setting.mail_pwd);
                fm.append("mail_ssl", this.state.setting.mail_ssl);
                fm.append("mail_recv", this.state.setting.mail_recv);
                ajax = axios.put;
            }
            ajax(`/api/admin/setting/`, fm)
                .then(function(response) {
                    var data = response.data;

                    if (data.code != 0) {
                        console.log("/api/admin/setting/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateLoadOk", true);
                        if (obj.handle_type == "put") {
                            context.commit("UpdateResultStatus", true);
                        }
                        context.commit("UpdateSetting", data);
                        context.commit("DynamicPatch");
                    }
                })
                .catch(function(error) {
                    console.log("/api/admin/setting/,请求异常");
                });
            context.commit("UpdateResultStatus", false);
            context.commit("UpdateLoadOk", false);
        },
        // 修改账号密码
        account_handler(context, pwd) {
            context.commit("UpdateResultStatus", false);
            var fm = new FormData();
            fm.append("_xsrf", this.state._xsrf);
            fm.append("id", this.state.setting.id);
            fm.append("admin_user", this.state.setting.admin_user);
            fm.append("admin_pwd", pwd);

            axios.put(`/api/admin/account/?`, fm)
                .then(function(response) {
                    var data = response.data;

                    if (data.code != 0) {
                        console.log("/api/admin/account/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateResultStatus", true);
                    }
                })
                .catch(function(error) {
                    console.log("/api/admin/account/,请求异常");
                });
            context.commit("UpdateResultStatus", false);
        },
        // 获取监控数据
        monitor_handler(context) {
            axios.defaults.headers.common["X-Xsrftoken"] = this.state._xsrf;
            axios.get(`/api/admin/monitor/?`)
                .then(function(response) {
                    var data = response.data;

                    if (data.code != 0) {
                        console.log("/api/admin/monitor/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateMonitor", data.data);
                    }
                })
                .catch(function(error) {
                    console.log("/api/admin/monitor/,请求异常");
                });
        },
    },
    getters: {}
})