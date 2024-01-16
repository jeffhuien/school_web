<!--
 * @Author: GAO GAO
 * @Date: 2023-11-22 00:41:07
-->
<script setup lang="ts"></script>

<template>
  <div class="top">
    <img src="/img/logo1_new.png" alt="" class="h-3/4" />
    <div class="links">
      <router-link :to="{ name: 'home' }"> 首页 </router-link>
      <router-link :to="{ name: 'campus_style' }"> 校园风貌 </router-link>
      <router-link :to="{ name: 'campus_history' }"> 校园历史 </router-link>
      <router-link :to="{ name: 'about_me' }"> 关于我 </router-link>
    </div>

    <!-- TODO:适配移动端 -->
    <img src="/img/con-font.png" alt="" class="h-0 xl:h-8 animate-bounce" />
  </div>
</template>

<style scoped lang="scss">
.top {
  @apply py-1 h-16 w-full flex gap-12 bg-purple-400 items-center xl:justify-center;
  @apply max-sm:h-10;

  .links {
    @apply max-md:-translate-x-36;
    @apply shrink-0 flex items-center md:translate-x-[-9rem]  max-sm:-translate-x-24 xl:translate-x-0;
    a {
      @apply px-3  w-20 py-1 mr-3 h-full flex items-center justify-center transition rounded-md hover:bg-white hover:text-purple-600;
      @apply xl:whitespace-nowrap;
      @apply max-sm:block  max-sm:px-1 max-sm:w-auto max-sm:mr-1  max-md:m-0 px-0  max-lg:text-xs;
    }
  }

  .router-link-active,
  .router-link-exact-active {
    @apply bg-white text-purple-600;
  }
}
</style>
