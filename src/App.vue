<!--
 * @Author: GAO GAO
 * @Date: 2023-11-22 00:01:42
-->
<script setup lang="ts">
import Top from "./components/top.vue";
</script>

<template>
  <Suspense>
    <div class="w-full">
      <div class="w-full transition fixed top-0 z-50">
        <Top class="" />
      </div>
      <div class="mt-16 max-sm:mt-10">
        <router-view></router-view>
      </div>
      <footer
        :class="[$router.currentRoute.value.name == 'about_me' ? 'absolute w-full xl:bottom-0' : '']"
        class="bg-teal-700 text-center text-white py-2 flex items-center justify-center gap-2 text-xs"
      >
        <img src="/img/logo1.png" class="h-12 md:h-8 lg:h-10 max-sm:h-6" alt="" />
        Copyright © 2023 计应21xx xx
      </footer>
    </div>
  </Suspense>
</template>

<style scoped lang="scss"></style>
