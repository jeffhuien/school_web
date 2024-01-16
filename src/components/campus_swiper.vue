<!--
 * @Author: GAO GAO
 * @Date: 2023-11-23 11:42:32
-->

<template>
  <div class="relative">
    <swiper
      :direction="'vertical'"
      :speed="400"
      :loopAdditionalSlides="0"
      :loopPreventsSliding="true"
      :pagination="{
        clickable: true,
      }"
      :modules="modules"
      :mousewheel="{
        invert: false,
        releaseOnEdges: true,
      }"
      :parallax="true"
      class="mySwiper"
    >
      <swiper-slide v-for="(i, index) in ls" :index="index">
        <img :src="name(i)" alt="" class="object-cover" />
        <p
          class="absolute bottom-1/4 left-3 text-4xl text-red-900 w-1/2 bg-pink-100 bg-opacity-80 p-3 rounded-md"
          data-swiper-parallax-opacity="0.5"
          data-swiper-parallax-scale="0.15"
          data-swiper-parallax="-100"
          data-swiper-parallax-duration="600"
        >
          {{ str[Math.floor(Math.random() * str.length)] }}
        </p>
        <p
          style="-webkit-text-stroke: 2px purple"
          class="absolute top-1/4 right-3 text-white text-6xl"
          data-swiper-parallax-opacity="0.5"
          data-swiper-parallax-scale="0.15"
          data-swiper-parallax="300"
          data-swiper-parallax-duration="600"
        >
          美丽校园
        </p>
      </swiper-slide>
    </swiper>

    <span class="absolute bottom-1 text-[4rem] text-red-800 block z-10 left-1/2 animate-bounce">⨈</span>
  </div>
</template>
<script lang="ts" setup>
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/scss";
import "swiper/scss/navigation";
import "swiper/scss/pagination";
// import required modules
import { Autoplay, Pagination, EffectFade, Mousewheel, Parallax } from "swiper/modules";
let modules = [Autoplay, Pagination, EffectFade, Mousewheel, Parallax];

function name(name: string) {
  return new URL("/img/" + name + ".jpg", import.meta.url).href;
}

let ls = [..."oldhouse all hut lane lane1 img(4) img(11) img(2) img(6)".split(" ")];

let str = [
  "别想一下造出大海，必须先由小河川开始。",
  "成功的关键不是努力去拷贝别人的特色方式，而是去学习如何发掘你自己独特的潜质。",
  "做正确的事，再把事情做正确。",
  "本来无望的事，大胆尝试，往往能成功。",
  "智商决定录用；情商决定提升。",
  "你经历的所有的困苦都是有意义的，因为这是你要承担重任的先兆。",
  "人生要成沉淀，要有定力，一个人定力不够会浮躁。",
  "经过海浪的一番磨砺，卵石才变得更加美丽光滑。",
  "成大事不在于力量多少，而在能坚持多久。",
  "不经一番寒彻骨，怎得梅花扑鼻香？",
  "每一个成功者都有一个开始。勇于开始，才能找到成功的路。",
  "你战胜苦难，它就是你的财富；苦难战胜你，它就是你的屈辱。",
  "最重要的就是不要去看远方模糊的，而要做手边清楚的事。",
  "一个人是在对周围生活环境的反抗中创造成功的。",
  "生命不是要超越别人，而是要超越自己。",
  "一个人幸运的前提，其实是他有能力改变自己。",
  "世上最重要的事，不在于我们在何处，而在于我们朝着什么方向走。",
  "自己选择的路，跪着也要把它走完。",
  "不要生气要争气，不要看破要突破，不要嫉妒要欣赏，不要拖延要积极，不要心动要行",
  "人有了信念和追求就能忍受一切艰苦，适应一切环境。",
  "当你再也没有什么可以失去的时候，就是你开始得到的时候。",
  "每一个人都拥有生命，却不是每个人都能读懂生命；每一个人都拥有头脑，却不是每个人",
  "第一个青春是上帝给的；第二个青春是靠自己努力的。",
  "只要功夫深，铁杵磨成针。",
  "如果我们都去做自己能力做得到的事，我们真会叫自己大吃一惊。",
  "经历过；才会明白；有付出才有回报。",
];

console.log(str[Math.random() * str.length]);
</script>

<style scoped lang="scss">
.swiper {
  @apply h-screen;
}
</style>
