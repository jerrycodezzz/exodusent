<template>
  <div class="result-container">
    <h1>투표 결과</h1>
    <div class="result-item">짜장면 : {{ votes.짜장면 }}표</div>
    <div class="result-item">짬뽕 : {{ votes.짬뽕 }}표</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const votes = ref({ 짜장면: 0, 짬뽕: 0 });

onMounted(async () => {
  const res = await fetch("/api/votes");
  votes.value = await res.json();
});
</script>

<style scoped>
.result-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  padding-top: 100px;
}
.result-item {
  font-size: 24px;
}
</style>
