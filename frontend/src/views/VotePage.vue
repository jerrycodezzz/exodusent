<template>
  <div class="vote-container">
    <h1>오늘 점심 뭐 먹을까?</h1>
    <el-radio-group v-model="choice" size="large">
      <el-radio value="짜장면">짜장면</el-radio>
      <el-radio value="짬뽕">짬뽕</el-radio>
    </el-radio-group>
    <el-button type="primary" size="large" @click="vote" :disabled="!choice">
      투표하기
    </el-button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const choice = ref('')

async function vote() {
  await fetch('/api/vote', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ choice: choice.value })
  })
  router.push('/result')
}
</script>

<style scoped>
.vote-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
  padding-top: 100px;
}
</style>

