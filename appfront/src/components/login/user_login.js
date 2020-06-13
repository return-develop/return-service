import Vue from 'vue'
import UserLogin from './UserLogin'
import viewDesign from 'view-design'
import 'view-design/dist/styles/iview.css'

Vue.use(viewDesign)

/* eslint-disable no-new */
new Vue({
    el: '#userlogin',
    components: { UserLogin }
  })