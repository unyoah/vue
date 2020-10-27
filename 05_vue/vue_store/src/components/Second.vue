<template>
    <div>
        <el-container>
            <el-header>后台管理系统</el-header>
            <el-main>
                <el-table :data="tableData" border style="width: 100%">
                    <el-table-column prop="date" label="日期" width="180"></el-table-column>
                    <el-table-column prop="name" label="姓名" width="180"></el-table-column>
                    <el-table-column prop="address" label="地址"></el-table-column>
                    <el-table-column fixed="right" label="操作">
                        <template slot-scope="scope">
                          <el-button type="warning" class="el-icon-edit"> 修改</el-button>
                          <el-button type="danger" class="el-icon-delete" @click="delUser(scope.row)" slot="reference"> 删除
                            </el-button>

                        </template>
                    </el-table-column>
                </el-table>
            </el-main>
            <el-footer>本网站已在公安局备案: </el-footer>
        </el-container>
    </div>
</template>

<script>
export default {
    name: "Second",
    methods: {
        delUser(index) {
            console.log(index);
            this.$message({
                message: '恭喜你，这是一条删除成功',
                type: 'warning',
                showClose: true,
                duration: 1000,
            });
        },
    },
    data() {
        return {
            tableData: [{
                date: '2016-05-02',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1518 弄'
            }, {
                date: '2016-05-04',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1517 弄'
            }, {
                date: '2016-05-01',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1519 弄'
            }, {
                date: '2016-05-03',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1516 弄'
            }]
        }
    }
}
</script>

<style scoped>

.el-header, .el-footer {
    background-color: #fec0cb;
    color: #333;
    text-align: center;
    line-height: 60px;
}


body > .el-container {
    margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
    line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
    line-height: 320px;
}
</style>
