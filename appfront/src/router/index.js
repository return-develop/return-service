import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import UserActivate from '@/components/activate/UserActivate'
import UserRegister from '@/components/register/UserRegister'

Vue.use(Router)
const VueRouterPush = Router.prototype.push 
Router.prototype.push = function push (to) {
    return VueRouterPush.call(this, to).catch(err => err)
}
export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/user_activate/',
      name: 'UserActivate',
      component: UserActivate
    }
  ]
})
