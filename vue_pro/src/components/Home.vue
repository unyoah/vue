<template>
    <div>
        <input type="text" v-model="msg">
        <button @click="add_msg">发表留言</button>
        <button @click="del(0,msg_list.length)">删除所有留言</button>

        <ul>
            <li v-for="(note,index) in msg_list" :key="index">{{note}}
                <button @click="del(index)">删除</button>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "Home",
        data() {
            return {
                msg: '',
                msg_list: localStorage.msgs ? JSON.parse(localStorage.msgs) : []
            }
        },
        methods: {
            add_msg() {
                if (this.msg) {
                    this.msg_list.unshift(this.msg);
                    localStorage.msgs = JSON.stringify(this.msg_list);
                    this.msg = ''
                }
            },
            del(i, l = 1) {
                this.msg_list.splice(i, l)
                localStorage.msgs = JSON.stringify(this.msg_list)
            }
        }
    }
</script>

<style scoped>

</style>
