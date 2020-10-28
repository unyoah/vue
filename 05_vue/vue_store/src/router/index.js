import Vue from 'vue'
import Router from 'vue-router'
import First from "../components/First";
import Second from "../components/Second";


Vue.use(Router)

export default new Router({
  routes: [
    {path:'/first',component:First},
    {path:'/second',component:Second},
    {path:'/',redirect:'/first'},

  ]
})
