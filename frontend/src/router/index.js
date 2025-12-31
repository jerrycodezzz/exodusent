import { createRouter, createWebHistory } from "vue-router";
import VotePage from "../views/VotePage.vue";

const routes = [
  { path: "/vote", component: VotePage },
  { path: "/result", component: () => import("../views/ResultPage.vue") },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});
