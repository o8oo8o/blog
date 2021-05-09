import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Blog from "./views/BlogList.vue";
import Show from "./views/BlogShow.vue";
import Resume from "./views/Resume.vue";

Vue.use(Router);

export default new Router({
    routes: [{
            path: "/home",
            name: "home",
            component: Home,
        },
        {
            path: "/resume",
            name: "resume",
            component: Resume,
        },
        {
            path: "/show/:id",
            name: "show",
            component: Show,
        },
        {
            path: "/blog/",
            name: "blog",
            component: Blog,
            children: [{
                    path: "classify/:classify/",
                    name: "classify",
                },
                {
                    path: "year/:year/",
                    name: "year",
                }
            ]
        },
        {
            path: "*",
            name: "tohome",
            redirect: { name: "home" }
        }
    ]
})