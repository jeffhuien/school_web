<!--
 * @Author: GAO GAO
 * @Date: 2023-11-23 14:07:51
-->
<script setup lang="ts">
let data = [
  {
    key: "北方大学农学院",
    value: [
      { time: "1939年12月", text: "中国共产党早期创建延安自然科学院大学部生物系。" },
      { time: "1947年3月", text: "成为北方大学农学院。" },
      { time: "1948年8月", text: "成为华北大学农学院。" },
      {
        time: "1951年",
        text: "平原省立农业学校、北京农业大学长治分校合 并升格为平原农学院。1951年7月，平原农学院参与多个院校的合并：部分并入河北农学院，发展为现河北农业大学；部分参与合并升格为河南农学院，发展为 现河南农业大学；部分合并升格为北京机械化农业学院，后发展为北京农业机械化学院、北京农业工程大学，现参与合并组建中国农业大学；兽医组参与合并升格为内蒙古畜牧兽医学院，相继发展为现内蒙古农牧学院、内蒙古农业大学；森林系参与合并升格为北京林学院，现发展为北京林业大学。",
      },
      { time: "1953年1月", text: "平原农学院改建为百泉农业学校，郑州林校、洛阳农校、郑州农校、陕州棉校并入百泉农业学校。" },
      { time: "1957年", text: "百泉农业学校 （畜牧/兽医专业）改建为郑州畜牧兽医学校，后发展为郑州畜牧兽医专科学校、郑州牧业工程高等专科学校。" },
      { time: "1958年9月", text: "百泉农业学校升格为百泉农学院。" },
      { time: "1959年", text: "百泉农学院更名为新乡专区农学院，9月，新乡专区农学院改建百泉农业专科学校。" },
      { time: "1962年", text: "郑州水利专科学校（部分）并入百泉农业专科学校。" },
      { time: "1987年2月", text: "百泉农业专科学校升格为河南职业技术师范学院。" },
    ],
  },
  {
    key: "科技学院",
    value: [
      { time: "2004年5月", text: "学院更名为河南科技学院。" },
      { time: "2020年11月", text: "入选河南省特色骨干学科建设高校名单。" },
      { time: "2021年5月15日", text: "成为高等农林院校课程思政联盟理事会员单位。" },
    ],
  },
];
</script>

<template>
  <section>
    <div class="bg-gray-600 text-white">
      <div class="container mx-auto flex flex-col items-start md:flex-row mt-4 lg:p-8 md:p-4">
        <!--  -->
        <div class="flex flex-col w-full sticky md:top-16 lg:w-1/3 mt-2 md:mt-12 px-8 max-sm:p-3 md:p-1">
          <p class="ml-2 text-yellow-300 uppercase tracking-loose">科院历史</p>
          <p class="text-3xl md:text-4xl leading-normal md:leading-relaxed mb-2">河南科技学院的前世今生</p>
          <p class="text-sm md:text-base text-gray-50 mb-4">右方是河南科技学院的历史发展包括了建校、更名、简介等信息。</p>
          <p class="text-sm leading-loose text-justify">
            河南科技学院（Henan Institute of Science and
            Technology）位于河南省新乡市，是国家2011计划协同创新单位、河南省博士学位授予重点立项培育单位。入选国家中西部高校基础能力建设工程、卓越教师培养计划、卓越农林人才教育培养计划、国家级大学生创新创业训练计划、全国重点建设职教师资培训基地、国家高职高专师资培训基地。
            学校始建于1939年，前身为中国共产党早期创建的延安自然科学院大学部生物系，历经北方大学农学院、华北大学农学院、平原农学院、百泉农业专科学校等时期。2004年5月，经教育部批准，更名为河南科技学院。
            截至2023年3月，学校占地面积2021亩，校舍面积近78万平方米，图书馆纸质图书180万册；设有23个二级学院，开设70个本科专业；拥有硕士学位授权一级学科12个，硕士专业学位授权类别13个；有教职工1777人，其中专任教师1515人；全日制普通在校生2.9万余人。
          </p>

          <img src="/img/oldphoto.png" class="mt-8" alt="" />
        </div>
        <div class="ml-0 lg:w-2/3 md:w-full sticky">
          <div class="container mx-auto w-full h-full">
            <div class="relative wrap overflow-hidden p-10 md:p-0 h-full max-sm:p-3">
              <div class="border-yellow-555 absolute h-full border" style="right: 50%; border: 2px solid #ffc100; border-radius: 1%"></div>
              <div class="border-yellow-555 absolute h-full border" style="left: 50%; border: 2px solid #ffc100; border-radius: 1%"></div>

              <template v-for="(category, index) in data" :index="index">
                <div :class="[index % 2 != 0 ? 'R' : 'L']">
                  <div class="order-1 w-5/12"></div>
                  <div class="order-1 w-5/12 px-1 py-4" :class="[index % 2 == 0 ? 'text-right' : 'text-left']">
                    <p class="line_title">{{ category.key }}</p>
                    <template v-for="(item, index1) in category.value" :index="index1">
                      <h4 class="line_time">{{ item.time }}</h4>
                      <p class="line_text" :class="[item.text.length > 50 ? 'text-justify' : '']">
                        {{ item.text }}
                      </p>
                    </template>
                  </div>
                </div>
              </template>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped lang="scss">
.line_title {
  @apply mb-3 text-base text-yellow-300;
}

.line_text {
  @apply text-sm md:text-base leading-snug text-gray-50 text-opacity-100;
}

.line_time {
  @apply mb-3 font-bold text-lg md:text-2xl;
}

.R {
  @apply mb-8 flex justify-between items-center w-full;
}
.L {
  @apply mb-8 w-full ml-8 max-sm:m-3 md:m-3;
}
</style>
