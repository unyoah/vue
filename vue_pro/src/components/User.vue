<template>
    <div>
        <h3>用户列表</h3>
        <table border="2" cellpadding="0" cellspacing="0">
            <tr>
                <th>Id</th>
                <th>姓名</th>
                <th>生日</th>
                <th>个人信息</th>
                <th>操作</th>
            </tr>
            <tr v-for="user in users" :key="user.id">
                <td>{{user.id}}</td>
                <td>{{user.name}}</td>
                <td>{{user.bir}}</td>
                <td>{{user.content}}</td>
                <td>
                    <button @click="del_user(user.id)"> 删除</button>
                    |
                    <button>
                        <router-link :to="`/detail/${user.id}`" style="text-decoration: none">查看详情信息</router-link>
                    </button>
                </td>
            </tr>
        </table>
        <hr>
        姓名：<input type="text" v-model="name" placeholder="请在此输入您的姓名"><br>
        生日：<input type="date" v-model="bir"><br>
        个人信息：<input type="text" v-model="content" placeholder="请在此输入您的个人信息"><br>
        <button @click="add_user">添加用户</button>
        <button @click="del_all">删除所有用户</button>

    </div>
</template>

<script>
    export default {
        name: "User",
        data() {
            return {
                name: '',
                bir: '',
                content: '',
                users: localStorage.users ? JSON.parse(localStorage.users) : [],
                count: localStorage.count ? JSON.parse(localStorage.count) : 1,
            }
        }, methods: {
            add_user() {
                this.count += 1;
                localStorage.count = JSON.stringify(this.count)
                if (this.name) {
                    let user = {'id': this.count, 'name': this.name, 'bir': this.bir, 'content': this.content}
                    this.users.push(user);
                    localStorage.users = JSON.stringify(this.users)
                    this.name = '';
                    this.bir = '';
                    this.content = '';
                }
            },
            del_user(id) {
                for (let i = 0; i < this.users.length; i++) {
                    if (this.users[i].id == id) {
                        this.users.splice(i, 1)
                    }
                }
                localStorage.users = JSON.stringify(this.users)
            },
            del_all() {
                localStorage.users = this.users = []

            }

        }
    }
</script>

<style scoped>

</style>
