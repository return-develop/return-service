import Vue from 'vue'
import UserLogin from './UserLogin'
import iView from 'iview'
import 'iview/dist/styles/iview.css'

Vue.use(iView)

/* eslint-disable no-new */
new Vue({
    el: '#userlogin',
    components: { UserLogin }
  })