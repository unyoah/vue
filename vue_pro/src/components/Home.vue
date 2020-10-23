<template>
    <div>
        <input type="text" v-model="msg">
        <button @click="add_msg">发表留言</button>

        <ul>
            <li v-for="(note,index) in msg_list" :key="index">{{note}}</li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "Home",
        data(){
            return {
                msg:'',
                msg_list:localStorage.msgs ? JSON.parse(localStorage.msgs) : []
            }
        },
        methods:{
            add_msg(){
                if(this.msg){
                    this.msg_list.unshift(this.msg);
                    localStorage.msgs=JSON.stringify(this.msg_list);
                    this.msg=''
                }
            }
        }
    }
</script>

<style scoped>

</style>
