import Vue from "vue";
import Router from "vue-router";

import Login from "./views/Login.vue";
import Home from "./views/Home.vue";
import Dashboard from "./views/admin/Dashboard.vue";
import Classify from "./views/admin/Classify.vue";
import Blog from "./views/admin/Blog.vue";
import Review from "./views/admin/Review.vue";
import Setting from "./views/admin/Setting.vue";
import Resume from "./views/admin/Resume.vue";
import Publish from "./views/admin/Publish.vue";
import Netdisk from "./views/admin/Netdisk.vue";
import Monitor from "./views/admin/Monitor.vue";
import Remote from "./views/admin/Remote.vue";

Vue.use(Router);

export default new Router({
    routes: [{
            path: "/login",
            name: "login",
            component: Login
        },
        {
            path: "/home",
            name: "home",
            component: Home,
            redirect: { name: "dashboard" },
            children: [{
                    path: "dashboard",
                    name: "dashboard",
                    component: Dashboard
                },
                {
                    path: "classify",
                    name: "classify",
                    component: Classify
                },
                {
                    path: "blog",
                    name: "blog",
                    component: Blog
                },
                {
                    path: "review",
                    name: "review",
                    component: Review
                },
                {
                    path: "resume",
                    name: "resume",
                    component: Resume
                },
                {
                    path: "publish",
                    name: "publish",
                    component: Publish
                },
                {
                    path: "setting",
                    name: "setting",
                    component: Setting
                },
                {
                    path: "netdisk",
                    name: "netdisk",
                    component: Netdisk
                },
                {
                    path: "monitor",
                    name: "monitor",
                    component: Monitor
                },
                {
                    path: "remote",
                    name: "remote",
                    component: Remote
                },
            ]
        },
        {
            path: "*",
            name: "tologin",
            redirect: { name: "login" }
        }
    ]
})