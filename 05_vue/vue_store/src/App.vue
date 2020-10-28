<template>
  <div id="app">
    <h3>VUE-STORE</h3>

    <router-link to="/first">First</router-link>
    <router-link to="/Second">Second</router-link>
    <hr>
    <router-view/>
  </div>
</template>

<script>
  export default {
    name: 'App'
  }
</script>

<style>

</style>
