import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/components/Dashboard'
import Login from '@/components/Login'
import Settings from '@/components/Settings'
import RecorderInput from '@/components/RecorderInput'
import List from '@/components/List'
import Collect from '@/components/Collect'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/settings',
      name: 'Settings',
      component: Settings
    },
    {
      path: '/recorderinput',
      name: 'recorderinput',
      component: RecorderInput
    },
    {
      path: '/list',
      name: 'list',
      component: List
    },
    {
      path: '/collect',
      name: 'collect',
      component: Collect
    }
  ]
})
