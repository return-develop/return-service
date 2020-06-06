import Vue from 'vue'
import MyCenter from './MyCenter'
import iView from 'iview'
import 'iview/dist/styles/iview.css'

Vue.use(iView)

/* eslint-disable no-new */
new Vue({
    el: '#mycenter',
    components: { MyCenter }
  })