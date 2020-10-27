<template>


    <div><h3>用户信息</h3>
        ID：{{id}}
        <hr>
        姓名：{{user.name}}
        <hr>
        生日 ：{{user.bir }}
        <br>
        <hr>
        个人信息：{{user.content}}

    </div>

</template>

<script>
    export default {
        name: "Detail",
        data() {
            return {
                user: '',
                id: this.$route.params.id
            }
        },
        created() {

            let users = JSON.parse(localStorage.users)
            let id = parseInt(this.$route.params.id)
            for (let i = 0; i < users.length; i++) {
                if (id === users[i].id) {
                    this.user = users[i]
                }
            }
        }
    }


</script>

<style scoped>

</style>
