<template>
    <div>
        <h3>用户列表</h3>
        <!--        <table border="2" cellpadding="0" cellspacing="0">-->
        <!--            <tr>-->
        <!--                <th>Id</th>-->
        <!--                <th>姓名</th>-->
        <!--                <th>生日</th>-->
        <!--                <th>个人信息</th>-->
        <!--                <th>操作</th>-->
        <!--            </tr>-->
        <!--            <tr v-for="user in users" :key="user.id">-->
        <!--                <td>{{user.id}}</td>-->
        <!--                <td>{{user.name}}</td>-->
        <!--                <td>{{user.bir}}</td>-->
        <!--                <td>{{user.content}}</td>-->
        <!--                <td>-->
        <!--                    <button @click="del_user(user.id)"> 删除</button>-->
        <!--                    |-->
        <!--                    <button>-->
        <!--                        <router-link :to="`/detail/${user.id}`" style="text-decoration: none">查看详情信息</router-link>-->
        <!--                    </button>-->
        <!--                </td>-->
        <!--            </tr>-->
        <!--        </table>-->


        <el-table
            :data="users"
            stripe
            style="width: 100%">
            <el-table-column
                prop="id"
                label="ID"
                width="180">
            </el-table-column>
            <el-table-column
                prop="name"
                label="姓名"
                width="180">
            </el-table-column>
            <el-table-column
                prop="bir"
                label="生日"
                width="180">
            </el-table-column>
            <el-table-column
                prop="content"
                label="个人信息"
                width="180">
            </el-table-column>
            <el-table-column
                label="操作">
                <template slot-scope="scope">
                    <el-button class="el-icon-search" @click.native.prevent="to(scope.$index,users)"></el-button>
                    <el-button class="el-icon-delete-solid"  @click.native.prevent="del_row(scope.$index,users)"></el-button>
                </template>
            </el-table-column>
        </el-table>
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
        },
        methods: {
            to(index,users){
                this.$router.push('/detail/'+users[index].id)
            },
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
            del_row(index,rows){
              rows.splice(index,1)
              localStorage.users=JSON.stringify(rows)
          },
            // del_user(id) {
            //     for (let i = 0; i < this.users.length; i++) {
            //         if (this.users[i].id == id) {
            //             this.users.splice(i, 1)
            //         }
            //     }
            //     localStorage.users = JSON.stringify(this.users)
            // },
            del_all() {
                localStorage.users = this.users = []
            }

        }

        // data() {
        //     return {
        //         tableData: [{
        //             date: '2016-05-02',
        //             name: '王小虎',
        //             address: '上海市普陀区金沙江路 1518 弄'
        //         }, {
        //             date: '2016-05-04',
        //             name: '王小虎',
        //             address: '上海市普陀区金沙江路 1517 弄'
        //         }, {
        //             date: '2016-05-01',
        //             name: '王小虎',
        //             address: '上海市普陀区金沙江路 1519 弄'
        //         }, {
        //             date: '2016-05-03',
        //             name: '王小虎',
        //             address: '上海市普陀区金沙江路 1516 弄'
        //         }]
        //     }
        // }

    }
</script>

<style scoped>

</style>
