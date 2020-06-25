import Vue from 'vue'
import Router from 'vue-router'
import router from '../../router/index.js'
import UserInfo from './UserInfo'
import viewDesign from 'view-design'
import 'view-design/dist/styles/iview.css'


Vue.use(viewDesign)
Vue.use(Router)

/* eslint-disable no-new */
new Vue({
    el: '#userinfo',
    components: { UserInfo },
    router
  })