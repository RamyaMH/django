import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import EmployeeList from '@/components/EmployeeList'
import UserAuth from '@/components/UserAuth'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/list',
      name: 'EmployeeList',
      component: EmployeeList
    },
    {
      path: '/auth',
      name: 'UserAuth',
      component: UserAuth
    }
  ]
})
