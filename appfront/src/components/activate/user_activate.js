import Vue from 'vue'
import UserActivate from './UserActivate'
import viewDesign from 'view-design'
import 'view-design/dist/styles/iview.css'

Vue.use(viewDesign)

/* eslint-disable no-new */
new Vue({
    el: '#useractivate',
    components: { UserActivate }
  })