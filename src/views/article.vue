<!--
 * @Author: GAO GAO
 * @Date: 2023-11-25 15:14:51
-->
<script setup lang="ts">
import Article from "@/components/article.vue";

let data1 = `高等职业技术学院第五十七期党的基本知识培训班成绩合格人员名单公示
2023年11月20日 18:17  点击：[21]
高等职业技术学院第五十七期党的基本知识培训班结业考试成绩合格人员为53名，现将名单公示如下：

职能科室第一党支部：

   郑宇敏

职能科室第二党支部：

   万  克

生命科学技术系党支部：

   朱参参 张莹莹 何俊奇 李梦婷

电子信息系党支部：

   李  玮 张二领 张艺佳 张冰欣 吕文蕾

   苗  帅 南储岭 宋佳晶 高  炎

经济与管理系党支部：

   杨  静 程潆纳 赵  杨 赵俊平

   宋佳慧 马熠卓 张  佳 郭梦慧 徐爱梨

艺术系党支部：

   马俊丽 张大千 胡家赫 许艺山 张馨艺  孙箴言

   王怡佳 李新雅 程金耀 印金玉 石心雨  贺闪星

财经金融系党支部：

   杜路路 魏雪晗 朱丽丽 刘凯迪 朱延涛

   常  硕 马梦雅

机电与汽车工程系党支部：

   樊梦心 王文杰 王坤鹏 何  静

   李双强 温宇杰 张滢滢 杨忠贤 王宏福 侯翔云

   公示时间5天，如有异议，请在公示期内将意见反馈至学院党政办公室。电话：0373-6203026。

   中共河南科技学院高等职业技术学院委员会

2023年11月20日

（初审/李孝彦 复审/杨大光 终审/孙敬坤）`.split("\n");

let title = data1[0],
  time = data1[1],
  section = [],
  footer = [
    ...data1
      .slice(-5, data1.length)
      .map(i => {
        //去除空白行
        return { content: i };
      })
      .filter(i => i && i.content.trim()),
  ];

for (let i of data1.slice(2, -5)) {
  section.push({
    content: i,
  });
}
section = section.filter(i => i && i.content.trim());
let article1 = {
  title,
  time,
  section,
  footer,
} as Article;

console.log(article1);
</script>

<template>
  <Article :data="article1"></Article>
</template>

<style scoped lang="scss"></style>
