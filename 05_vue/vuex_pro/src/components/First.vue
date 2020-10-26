<template>
    <div>
        第一个组件
        <el-button @click="add">按钮</el-button>
        <el-button type="primary" @click="add" disabled>按钮</el-button>
        <el-button type="success" @click="add">按钮</el-button>
        <el-button type="warning" @click="add" icon="el-icon-edit-outline">修改</el-button>
        <el-button type="danger" @click="add" icon="el-icon-delete-solid"> 删除</el-button>
        <el-button type="info" @click="add">按钮</el-button>
    </div>
</template>

<script>
export default {
    name: "First",
    methods: {
        add() {
            this.$store.commit("add_count")
        },
    }
}
</script>

<style scoped>

</style>
