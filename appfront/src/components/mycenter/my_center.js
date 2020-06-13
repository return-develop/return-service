import Vue from 'vue'
import MyCenter from './MyCenter'
import viewDesign from 'view-design'
import 'view-design/dist/styles/iview.css'

Vue.use(viewDesign)

/* eslint-disable no-new */
new Vue({
    el: '#mycenter',
    components: { MyCenter }
  })