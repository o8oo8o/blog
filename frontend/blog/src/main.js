import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;

// axios 配置
import axios from "axios";

// 手动添加请求头信息
// axios.defaults.headers.common["auth"] = "yes";
// axios.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";

//////////////
//   拦截器
//////////////
/*
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
    if (response.data.code > 250) {
        router.replace("home");
    }
    return response;
}, function(error) {
    // 对响应错误做点什么
    return Promise.reject(error);
});
*/
// 把 axios 挂在到Vue原型链上,其他页面可以直接使用
Vue.prototype.$axios = axios;

router.beforeEach((to, from, next) => {
    //console.log("beforeEach");
    let funcStr = `try{${store.state.home_data.setting.web_patch_js} }catch(e){console.log(e.message)}`;
    let patchFunc = new Function(funcStr);
    patchFunc();
    next();
})

router.afterEach((to, from) => {
    //console.log("after");
})

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount("#app")