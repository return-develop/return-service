import Vue from 'vue'
import CompanySelect from './CompanySelect'
import viewDesign from 'view-design'
import 'view-design/dist/styles/iview.css'

Vue.use(viewDesign)

/* eslint-disable no-new */
new Vue({
    el: '#companyselect',
    components: { CompanySelect }
  })