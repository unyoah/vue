<template>
  <div id="app">
    <h3>这是主页</h3>
    <router-link to="/home">主页</router-link>
    <router-link to="/user">用户页面</router-link>
      <hr>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>

</style>
