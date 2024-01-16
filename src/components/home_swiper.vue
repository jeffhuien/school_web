<!--
 * @Author: GAO GAO
 * @Date: 2023-11-22 11:05:55
-->
<template>
  <div class="relative">
    <swiper
      :spaceBetween="30"
      :centeredSlides="true"
      :loop="true"
      :speed="400"
      :loopAdditionalSlides="0"
      :loopPreventsSliding="true"
      :pagination="{
        clickable: true,
      }"
      :modules="modules"
      :autoplay="{
        delay: 1500,
        disableOnInteraction: false,
      }"
      class="mySwiper w-full"
    >
      <!-- 
     
     -->
      <swiper-slide v-for="(i, index) in ls" :index="index">
        <img :src="name(i)" alt="" class="object-cover" />
      </swiper-slide>
    </swiper>

    <span class="hidden lg:block absolute bottom-1 text-[4rem] text-red-800 z-10 left-1/2 animate-bounce">⨈</span>
  </div>
</template>
<script lang="ts" setup>
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/scss";
import "swiper/scss/navigation";
import "swiper/scss/pagination";
// import required modules
import { Autoplay, Pagination, EffectFade } from "swiper/modules";
let modules = [Autoplay, Pagination, EffectFade];
function name(name: string) {
  return new URL("/img/" + name, import.meta.url).href;
}
let ls = [
  //
  "stone1.jpg",
  "gate.jpg",
  "oldhouse.jpg",
  "img(1).jpg",
  "img(8).jpg",
  "lane.jpg",
];
</script>

<style>
.swiper {
  @apply lg:h-[94vh] h-[40vh];
}
</style>
