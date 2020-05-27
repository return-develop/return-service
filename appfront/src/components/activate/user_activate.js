import Vue from 'vue'
import UserActivate from './UserActivate'
import iView from 'iview'
import 'iview/dist/styles/iview.css'

Vue.use(iView)

/* eslint-disable no-new */
new Vue({
    el: '#useractivate',
    components: { UserActivate }
  })