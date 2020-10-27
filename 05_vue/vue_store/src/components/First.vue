<template>
  <div>

    {{$store.state.num}}
    <el-button @click="add"> 按钮</el-button>
    <el-button @click="add" type="primary"> 按钮</el-button>
    <el-button @click="add" type="success"> 按钮</el-button>
    <el-button @click="add" type="warning"> 按钮</el-button>
    <el-button @click="add" type="info"> 按钮</el-button>
    <el-button @click="add" type="danger"> 按钮</el-button>
  </div>
</template>

<script>
  export default {
    name: "First",
    methods:{
      add(){
        this.$store.commit('add')
      }
    }
  }
</script>

<style scoped>

</style>
