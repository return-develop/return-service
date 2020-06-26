import Vue from 'vue'
import JobConsult from './JobConsult'
import viewDesign from 'view-design'
import 'view-design/dist/styles/iview.css'

Vue.use(viewDesign)

/* eslint-disable no-new */
new Vue({
    el: '#job_consult',
    components: { JobConsult }
  })