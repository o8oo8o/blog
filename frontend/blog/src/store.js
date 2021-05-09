import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        home_data: {
            classify_info: [],
            year_info: [],
            blog_list: [],
            setting: {
                "banner": "",
                "city": "",
                "email": "",
                "enable_chat": false,
                "enable_music": false,
                "enable_resume": false,
                "footer": "",
                "github_addr": "",
                "github_name": "",
                "icon_path": "#",
                "icon_text": "",
                "info": "",
                "logo_path": "#",
                "logo_text": "",
                "note": "",
                "qq": "",
                "web_blog_pz": 15,
                "web_last_pz": 5,
                "web_patch_css": "",
                "web_patch_html": "",
                "web_patch_js": "",
                "web_title": "黄锐",
                "weibo_addr": "",
                "weibo_name": "",
                "wx": ""

            },
            blog_count: 0,
            review_count: 0,
        },
        blog: {
            id: 1,
            title: "",
            read_count: 0,
            review_count: 0,
            create_time: "0",
            is_review: false,
            classify_name: "",
            text: "",
            review_list: [],
            prev_blog: {
                is_exists: false,
                id: 0,
                title: ""
            },
            next_blog: {
                is_exists: false,
                id: 0,
                title: ""
            }
        },
        resume: {
            exp_time: "",
            title: "",
            text: ""
        },
        resume_load_ok: false,
        resume_load_error_msg: "",
        blog_review: {
            review_name: "",
            review_email: "",
            review_text: "",
            verify_code: "",
            verify_code_img: ""
        },
        _xsrf: "",

        verify_code_check_result: false,
        review_is_succees: false,
        blog_list: [],
        current_page: 1,
        current_blog_list: [],
        current_blog_count: 0,
        end_page: 0,
        blog_search_text: "",
        blog_search_list_copy: [],
        sub_search_path: "",
        access_code: "",

    },
    mutations: {
        // 动态增加补丁
        DynamicPatch(state) {
            try {
                var patch = document.getElementById("patch");
                patch.textContent = "";

                var html = document.createElement("div");
                html.id = "patch_html";
                html.innerHTML = state.home_data.setting.web_patch_html;
                patch.appendChild(html);

                var css = document.createElement("style");
                css.id = "patch_css";
                css.innerHTML = state.home_data.setting.web_patch_css;
                patch.appendChild(css);

                var js = document.createElement("script");
                js.id = "patch_js";
                js.innerHTML = `
                    try {
                        ${state.home_data.setting.web_patch_js}
                    }
                    catch(error) {
                        console.log("patch_js error:->"+error.message);
                    }
                `;
                patch.appendChild(js);
            } catch (error) {
                console.log("DynamicPatch_add_error");
            }
        },
        // 主页初始化
        HomeInit(state, data) {
            state.home_data = data;

            let web_blog_pz = data.setting.web_blog_pz;
            state.blog_list = data.blog_list;
            state.current_blog_list = state.blog_list.slice(0, web_blog_pz);
            state.current_blog_count = data.blog_count;
            document.title = data.setting.web_title;

            // 处理一下富文本编辑器内容为空的情况
            if(data.setting.banner === "<p><br></p>"){
                state.home_data.setting.banner = "";
            }

        },
        // 跳转到指定页
        GoPage(state, num) {
            let web_blog_pz = state.home_data.setting.web_blog_pz;
            state.current_page = num;
            let start = state.current_page * web_blog_pz - web_blog_pz;
            state.current_blog_list = state.blog_list.slice(start, start + web_blog_pz);
        },
        // 下一页
        NextPage(state) {
            state.current_page += 1;
            let web_blog_pz = state.home_data.setting.web_blog_pz;
            let start = state.current_page * web_blog_pz - web_blog_pz;
            state.current_blog_list = state.blog_list.slice(start, start + web_blog_pz);
        },
        // 上一页
        PrevPage(state) {
            state.current_page -= 1;
            let web_blog_pz = state.home_data.setting.web_blog_pz
            let start = state.current_page * web_blog_pz - web_blog_pz;
            state.current_blog_list = state.blog_list.slice(start, start + web_blog_pz);
        },
        // 获取博客列表
        GetBlogList(state, obj) {
            state.current_page = 1;
            var filter_a = obj[1];
            var filter_b = obj[2];
            var filter_c = decodeURIComponent(obj[3]);
            let blog_info = JSON.parse(JSON.stringify(state.home_data.blog_list));
            let web_blog_pz = state.home_data.setting.web_blog_pz;
            state.blog_list = blog_info;;
            if (filter_a == "blog" && typeof filter_b == "undefined") {
                state.current_blog_count = blog_info.length;
                state.current_blog_list = blog_info.slice(0, web_blog_pz);
            } else {
                // 根据分类或时间筛选
                let result = blog_info.filter((blog_item) => {
                    if (filter_b == "classify") {
                        return blog_item.classify_name == filter_c;
                    }
                    if (filter_b == "year") {
                        return blog_item.year == filter_c;
                    }
                });
                state.blog_list = result;
                state.current_blog_count = result.length;
                state.current_blog_list = result.slice(0, web_blog_pz);
            }
        },
        // 博客搜索
        BlogSearch(state, obj) {
            let str = obj.blog_search_text;
            let web_blog_pz = state.home_data.setting.web_blog_pz;
            //  先把搜索之前到列表复制一份，等到搜索空文本的时候恢复回去
            if (state.blog_search_list_copy.length == 0 || state.sub_search_path != obj.sub_search_path) {
                state.blog_search_list_copy = JSON.parse(JSON.stringify(state.blog_list));
                state.sub_search_path = obj.sub_search_path;
            }
            if (str == "") {
                state.blog_list = state.blog_search_list_copy;
                state.current_blog_count = state.blog_search_list_copy.length;
                state.current_blog_list = state.blog_list.slice(0, web_blog_pz);
                state.current_page = 1;
                return;
            }
            /** 全部文章列表搜索 */
            // let result = state.home_data.blog_list.filter(function(blog_item) {
            //   return RegExp(str, "i").test(blog_item.title);
            // });
            /** 选中文章列表搜索 */
            let result = state.blog_list.filter(function(blog_item) {
                return RegExp(str, "i").test(blog_item.title);
            });
            state.blog_list = result;
            state.current_blog_count = result.length;
            state.current_blog_list = result.slice(0, web_blog_pz);
            state.current_page = 1;
        },
        UpdateBlog(state, obj) {
            state.blog = obj;
        },
        UpdateReviewName(state, value) {
            state.blog_review.review_name = value
        },
        UpdateReviewEmail(state, value) {
            state.blog_review.review_email = value
        },
        UpdateReviewText(state, value) {
            state.blog_review.review_text = value
        },
        UpdateReviewVerifyCode(state, value) {
            state.blog_review.verify_code = value;
        },
        UpdateReviewVerifyImg(state, value) {
            state.blog_review.verify_code_img = value;
        },
        UpdataVerifyCodeStatus(state, check_result) {
            state.verify_code_check_result = check_result
        },
        UpdateXsrf(state, data) {
            state._xsrf = data._xsrf;
        },
        UpdateReviewIsSuccees(state, review_is_succees) {
            state.review_is_succees = review_is_succees
        },
        UpdateBlogReviewList(state, review_list) {
            state.blog.review_list = review_list
        },
        UpdateResume(state, value) {
            state.resume = value;
        },
        UpdateResumeLoadOk(state, value) {
            state.resume_load_ok = value;
        },
        UpdateResumeLoadErrorMsg(state, value) {
            state.resume_load_error_msg = value;
        },
        UpdateAccessCode(state, value) {
            state.access_code = value;
        }
    },
    actions: {
        // 获取xsrf数据
        get_xsrf(context) {
            axios.get("/api/open/xsrf/")
                .then(function(response) {
                    var data = response.data;
                    if (data.code != 0) {
                        console.log("xsrf获取数据错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateXsrf", data);
                    }
                })
                .catch(function(error) {
                    console.log("xsrf获取数据异常");
                });
        },
        // 获取主页初始化数据
        home_init(context) {
            axios.get("/api/open/home/")
                .then(function(response) {
                    var data = response.data;
                    if (data.code != 0) {
                        console.log("init获取数据错误");
                    }
                    if (data.code == 0) {
                        context.commit("HomeInit", data);
                        context.commit("DynamicPatch");
                    }
                })
                .catch(function(error) {
                    console.log("init获取数据异常");
                });
        },
        // 获取一个博客及博客的评论
        get_blog(context, id) {
            axios
                .get(`/api/open/blog/${id}/`)
                .then(function(response) {
                    var data = response.data;
                    if (data.code != 0) {
                        console.log("获取数据错误/api/show/");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateBlog", data);
                    }
                })
                .catch(function(error) {
                    console.log("获取数据异常/api/show/");
                });
        },
        // 获取验证码图片
        get_verify_code(context) {
            context.commit("UpdataVerifyCodeStatus", false);
            axios
                .get(`/api/open/verify_code/`, {
                    responseType: "arraybuffer"
                })
                .then(function(response) {
                    var verify_code_img = "data:image/png;base64," + btoa(
                        new Uint8Array(response.data).reduce((data, byte) => data + String.fromCharCode(byte), "")
                    );
                    context.commit("UpdateReviewVerifyImg", verify_code_img);
                })
                .catch(function(error) {
                    console.log("获取数据异常/api/verify_code/");
                });
        },
        // 验证码检查
        verify_code_check(context, value) {
            var fm = new FormData();
            fm.append("_xsrf", this.state._xsrf);
            fm.append("verify_code", value);

            axios
                .post(`/api/open/verify_code/`, fm)
                .then(function(response) {

                    var data = response.data;
                    if (data.code != 0) {
                        context.commit("UpdataVerifyCodeStatus", data.status);

                    }
                    if (data.code == 0) {
                        context.commit("UpdataVerifyCodeStatus", data.status);
                    }
                })
                .catch(function(error) {
                    console.log("获取数据异常/api/verify_code/");
                });
        },
        // 添加评论
        post_review(context, blog_id) {
            var fm = new FormData();
            fm.append("_xsrf", this.state._xsrf);
            fm.append("verify_code", this.state.blog_review.verify_code);
            fm.append("blog_id", blog_id);
            fm.append("email", this.state.blog_review.review_email);
            fm.append("name", this.state.blog_review.review_name);
            fm.append("text", this.state.blog_review.review_text);

            axios
                .post(`/api/open/review/`, fm)
                .then(function(response) {
                    var data = response.data;
                    if (data.code != 0) {
                        console.log("/api/open/review/,服务端错误");
                    }
                    if (data.code == 0) {
                        context.commit("UpdateReviewIsSuccees", true);
                        context.commit("UpdateBlogReviewList", data.review_list);
                        setTimeout(function() {
                            context.commit("UpdateReviewIsSuccees", false);
                        }, 2000);
                        context.commit("UpdateReviewEmail", "");
                        context.commit("UpdateReviewName", "");
                        context.commit("UpdateReviewText", "");
                        context.commit("UpdateReviewVerifyCode", "");
                        context.commit("UpdataVerifyCodeStatus", false);
                        context.dispatch("get_verify_code");
                    }
                })
                .catch(function(error) {
                    console.log("/api/open/review/,请求异常");
                });
        },
        // 获取简历
        get_resume(context, access_code) {
            var fm = new FormData();
            fm.append("_xsrf", this.state._xsrf);
            fm.append("access_code", access_code);
            var that = this;
            axios
                .post(`/api/open/resume/`, fm)
                .then(function(response) {
                    var data = response.data;
                    if (data.code == 2) {
                        that.commit("UpdateResumeLoadErrorMsg", "此项功能已经被关闭!");
                    } else if (data.code != 0) {
                        that.commit("UpdateResumeLoadErrorMsg", "访问码错误或过期!");
                    } else if (data.code == 0) {
                        that.commit("UpdateResumeLoadOk", true);
                        that.commit("UpdateResume", data.resume);
                        that.commit("UpdateAccessCode", access_code);
                    }
                })
                .catch(function(error) {
                    console.log("获取数据异常");
                });
        },
        // 更新简历阅读时长
        put_read_duration(context) {
            var fm = new FormData();
            fm.append("_xsrf", this.state._xsrf);
            fm.append("access_code", this.state.access_code);
            var that = this;
            axios
                .put(`/api/open/resume/`, fm)
                .then(function(response) {
                    var data = response.data;
                    if (data.code != 0) {
                        that.commit("UpdateResumeLoadOk", false);
                    }
                    if (data.code == 0) {
                        //console.log("更新阅读时间成功")
                    }
                })
                .catch(function(error) {
                    console.log("更新阅读时间异常");
                });
        },
    },
    getters: {
        // 主页显示博客
        home_blogs(state) {
            let blog_list = state.home_data.blog_list;
            let blogs = blog_list.slice(0, state.home_data.setting.web_last_pz);
            return blogs
        },
        // 最后一页页码
        end_page(state) {
            let blog_count = state.current_blog_count;
            let web_blog_pz = state.home_data.setting.web_blog_pz;
            if (blog_count <= web_blog_pz) {
                return 1;
            } else {
                return Math.ceil(blog_count / web_blog_pz);
            }
        },
        // 上一篇博客链接
        get_prev_link(state) {
            return "#/show/" + state.blog.prev_blog.id;
        },
        // 下一篇博客链接
        get_next_link(state) {
            return "#/show/" + state.blog.next_blog.id;
        }
    }
})