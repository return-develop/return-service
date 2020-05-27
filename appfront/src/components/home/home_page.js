import Vue from 'vue'
import HomePage from './HomePage'
import iView from 'iview'
import 'iview/dist/styles/iview.css'

Vue.use(iView, {
  i18n: function(path, options) {
    let value = i18n.t(path, options)
    if (value !== null && value !== undefined) {
      return value
    }
    return ''
  }
})

/* eslint-disable no-new */
new Vue({
    el: '#home_page',
    components: { HomePage }
  })