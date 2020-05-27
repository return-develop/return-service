import Vue from 'vue'
import Router from 'vue-router'
import UserActivate from '@/components/activate/UserActivate'
import router from '../../router/index.js'
import UserRegister from './UserRegister'
import iView from 'iview'
import 'iview/dist/styles/iview.css'


Vue.use(iView)
Vue.use(Router)

/* eslint-disable no-new */
new Vue({
    el: '#userregister',
    components: { UserRegister },
    router
  })