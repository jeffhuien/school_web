/*
 * @Author: GAO GAO
 * @Date: 2023-11-22 00:01:42
 */
import { createRouter, createWebHistory } from "vue-router";
import home from "@/views/home.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: home,
    },
    {
      path: "/campus_style",
      name: "campus_style",
      component: () => import("@/views/style.vue"),
    },
    {
      path: "/about_me",
      name: "about_me",
      component: () => import("@/views/about_me.vue"),
    },
    {
      path: "/campus_history",
      name: "campus_history",
      component: () => import("@/views/history.vue"),
    },

    {
      path: "/article",
      name: "article",
      component: () => import("@/views/article.vue"),
    },
  ],
});

export default router;
