import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
Vue.config.productionTip = false;

// 导航守卫 配置
// 使用 router.beforeEach 注册一个全局前置守卫，判断用户是否登陆

router.beforeEach((to, from, next) => {
    if (to.path === "/login") {
        next();
    } else {
        let vuex_auth = store.state.auth;
        var local_auth = localStorage.getItem("auth");
        if (local_auth === "yes" || vuex_auth === true) {
            next();
        } else {
            next("/login");
        }
    }
});

// axios 配置
// 手动添加请求头信息
// axios.defaults.headers.common["rtime"] = String(Number.parseInt(new Date().getTime() / 1000));
// axios.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";

//////////////
//   拦截器
//////////////

//在请求或响应被 then 或 catch 处理前拦截它们。
// 添加请求拦截器
axios.interceptors.request.use(function(config) {
    // 在发送请求之前做些什么
    config.headers.sessionobj = "huangrui";
    return config;
}, function(error) {
    // 对请求错误做些什么
    return Promise.reject(error);
});

// 添加响应拦截器
axios.interceptors.response.use(function(response) {
    // 对响应数据做点什么
    if (response.data.code === 444) {
        router.replace("login");
    }
    return response;
}, function(error) {
    // 对响应错误做点什么
    return Promise.reject(error);
});

// 把 axios 挂在到Vue原型链上,其他页面可以直接使用
// Vue.prototype.$axios = axios;

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount("#app")