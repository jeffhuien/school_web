/*
 * @Author: GAO GAO
 * @Date: 2023-11-22 00:01:42
 */
import "./assets/main.scss";

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

const app = createApp(App);

app.use(router);

app.mount("#app");
