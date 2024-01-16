<!--
 * @Author: GAO GAO
 * @Date: 2023-11-25 15:06:32
-->
<script setup lang="ts">
defineProps<{ data: Article }>();
</script>

<template>
  <div class="w-full h-full bg-gray-300 font-['宋体']">
    <div class="xl:w-2/3 p-10 text-base md:w-full max-sm:w-full max-sm:p-1 max-sm:text-xs m-auto">
      <div class="m-2 xl:p-20 lg:p-16 max-md:p-4 md:p-9 min-h-[40rem] rounded-md bg-white shadow-lg">
        <div class="title font-bold text-center mb-7 max-lg:text-3xl max-xl:text-3xl xl:text-4xl text-sky-500">{{ data.title }}</div>
        <div class="time text-center mb-2">{{ data.time }}</div>
        <hr class="border-blue-300 mb-2" />
        <div class="data indent-6" v-for="(i, index) in data.section" :index="index">
          <p>{{ i.content }}</p>
          <br />
        </div>

        <div class="mt-4 text-right pr-4 italic font-bold">
          <div class="" v-if="typeof data.footer !== 'string' && data.footer">
            <div class="footer" v-for="(i, index) in data.footer" :index="index">
              <p>{{ i.content }}</p>
              <br />
            </div>
          </div>
          <div class="" v-else>
            {{ data.footer }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss"></style>
