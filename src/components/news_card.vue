<!--
 * @Author: GAO GAO
 * @Date: 2023-11-22 20:51:23
-->
<script setup lang="ts">
import { onMounted, ref } from "vue";

interface newsData {
  type: string;
  data: {
    title: string;
    date: string;
  }[];
}

let data = [
  {
    type: "学院要闻",
    data: [
      { title: "高等职业技术学院2023年“校园杯”排球赛圆满完成", date: "11-17" },
      { title: "高等职业技术学院举办“强国有我·青春有为”爱", date: "11-16" },
      { title: "高等职业技术学院召开2023-2024学年第一学期期", date: "11-08" },
      { title: "高等职业技术学院举行2023年高校国家助学贷款", date: "11-08" },
      { title: "高等职业技术学院开展“总体国家安全观”专题", date: "11-03" },
    ],
  },
  {
    type: "学院公告",
    data: [
      { title: "关于做好2023-2024学年第二学期教学任务安排工作的通知", date: "11-20" },
      { title: "关于2023年度科研项目申报和前期科研项目结项的通知", date: "11-01" },
      { title: "河南科技学院高等职业技术学院关于开展2023年教育教学改革研究项目申报的通知", date: "11-01" },
      { title: "关于开展2022年教改项目结项工作安排的通知", date: "11-01" },
      { title: "关于开展2023～2024学年第一学期期中教学检查工作的通知", date: "10-30" },
    ],
  },
] as newsData[];

//FIXME:未适配移动端，新闻尺寸移动端过大 //已完成
const topImg = ref();
const bottomImg = ref();
let load = ref(false);
let load1 = ref(false);
let news = ref();

onMounted(() => {
  const io = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.target === topImg.value) {
        if (entry.isIntersecting) {
          // 当内容可见
          load.value = true;
          entry.target.classList.add("topImg");
        } else {
          if (load.value) {
            entry.target.classList.remove("topImg");
            load.value = false;
          }
        }
      }
      if (entry.target === bottomImg.value) {
        if (entry.isIntersecting) {
          // 当内容可见
          load1.value = true;
          entry.target.classList.add("bottomImg");
        } else {
          if (load1.value) entry.target.classList.remove("bottomImg");
        }
      }
    });
  });

  //TODO:md尺寸下不运行 //已完成
  //竖屏不执行

  if (window.innerHeight < window.innerWidth) {
    io.observe(topImg.value); // 观察
    io.observe(bottomImg.value); // 观察
  }
});
</script>

<template>
  <div ref="news" class="grid gap-2 place-items-stretch w-full h-full xl:grid-cols-2">
    <div class="w-full relative">
      <div ref="topImg" class="w-2/3 absolute right-1/2 bottom-1/4 cursor-pointer transition-all duration-1000 liner photo">
        <img src="/img/xi.jpg" alt="" class="w-full" />
        <p class="text-sm">高等职业技术学院开展习近平文化思想专题学习</p>
      </div>
    </div>
    <article v-for="i in data" class="overflow-hidden">
      <h3 class="py-1 after:w-1 after:h-1 after:bg-blue-500">
        {{ i.type }}
        <span class="float-right mr-1 underline hover:bg-purple-600 px-2 rounded-md">more</span>
      </h3>
      <div class="list max-sm:text-xs">
        <ul class="w-full">
          <li v-for="item in i.data" class="w-full flex justify-between">
            <router-link :to="{ name: 'article' }" class="block w-[88%] truncate whitespace-nowrap" :title="item.title">{{ item.title }}</router-link>
            <span class="">{{ item.date }} </span>
          </li>
        </ul>
      </div>
    </article>

    <div class="w-full relative">
      <div ref="bottomImg" class="w-4/6 absolute left-1/2 top-1/4 cursor-pointer transition-all duration-1000 liner photo">
        <img src="/img/xin.jpg" alt="" class="w-full" />
        <p class="text-sm">高等职业技术学院开展心理健康宣传月系列活动</p>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
article {
  box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 2px 6px 2px;
  background: #ffffffe8;
}

article:first-child {
  float: left;
}

article:last-child {
  float: right;
}

article > h3 {
  padding-left: 10px;
  background: skyblue;
}

.list {
  padding: 10px;
}

.list li {
  margin: 15px 0 0 0;
  border-bottom: 2px solid #ddd;
}

.list li:hover a {
  color: blue;
}

.list li:hover {
  border-color: red;
}

.list li:first-child {
  margin-top: 10px;
}

.list a {
  color: rgb(0, 0, 0);
}

.topImg {
  @apply right-0 bottom-0;
}

.bottomImg {
  @apply left-0 top-0;
}

.photo {
  @apply hidden xl:block;
}
</style>
