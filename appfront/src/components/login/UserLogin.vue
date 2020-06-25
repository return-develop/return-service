<template>
  <div class="app">
    <div class="menu"><navigation></navigation></div>
    <div class="wrap">
      <div class="ask_register">
         <p>没有账号？<a href="/user_register" class="register-style">请注册</a></p>
      </div>
      <div class="user_login">
        <h3 class="title">登录 归来</h3>
        <div class="item">电子邮箱</div>
        <div class="user-input">
          <Input v-model="formItem.email" placeholder="邮箱" type="text" class="customer-input">
        </div>
        <div class="item">密码<a @click="findEmail">找回密码？</a></div>
        <div class="user-input">
          <Input v-model="formItem.password" placeholder="密码" type="password" class="customer-input" @on-enter="submit">
        </div>
        <div class="my-button">
          <Button type="primary" @click="submit" class="btn">登录</Button>
          <Checkbox v-model="remember" class="remember-me">记住我</Checkbox>
          <!-- <input type="checkbox" name="remember" value="yes"  class="remember"/>
          <span class="remember-me">记住我</span> -->
        </div>
        <p class="signup"><a></a></p>
        <Modal
          v-model="findback.modal"
          title="找回密码"
          @on-ok="ok"
          @on-cancel="cancel">
          <p>请输入邮箱</p>
          <Input v-model="formItem.email">
        </Modal>
      </div>
    </div>
  </div>
</template>
<script>
  import global_ from '../Const' 
  import navigation from '../navigation'
  import { addCookie, getCookieValue, deleteCookie } from '../../cookie/useCookie'
  import { fetchBase } from '../../post/fetchBase'
  export default {
    components: {navigation},
    data () {
      return {
        formItem: {
          email: '',
          password: ''
        },
        findback: {
          modal: false,
          email: ''
        },
        remember: false,
        cookieEnable: true
      }
    },
    created() {
      if (getCookieValue("remember") == "yes") {
        this.formItem.email = getCookieValue("email")
        this.formItem.password = getCookieValue("password")
        this.remember = true
      }
      if (navigator.cookieEnabled == false) {
        this.cookieEnable = false
      }
    },
    methods: {
      findEmail () {
        this.findback.modal = !this.findback.modal
      },
      async ok () {
        this.trimItem()
        let res = await fetchBase('/api/user/findback_password/', {
          'email': this.formItem.email
        })
        console.log(res)
        if (res['flag'] === global_.CONSTGET.SUCCESS) {
          this.$Message.warning('已发送一封邮件给您，请注意查看')
        } else {
          this.$Message.warning('发生错误')
        }
      },
      cancel () {},
      reset () {
        this.formItem.email = ''
        this.formItem.password = ''
      },
      trimItem () {
        this.formItem.email = this.formItem.email.trim()
        this.formItem.password = this.formItem.password.trim()
        this.findback.email = this.findback.email.trim()
      },
      async submit () {
        if(this.cookieEnable == false){
          this.$Message.warning("请开启cookie设置")
          return
        }
        // 检查是否为空
        this.trimItem()
        if (getCookieValue("login") == "yes") {
          this.$Message.info("您已登录")
          return 
        }
        if (this.formItem.email === '' || this.formItem.password === '') {
          this.$Message.warning('不能有内容为空')
          return
        }
        let res = await fetchBase('/api/user/login/', {
          'email': this.formItem.email,
          'password': this.formItem.password
        })
        // this.reset()
        if (res['flag'] === global_.CONSTGET.SUCCESS) { //success
          this.$Message.success('登录成功!')
          addCookie("email", this.formItem.email, 7, "/")
          addCookie("password", this.formItem.password, 7, "/")
          addCookie("username", res['username'], 7, "/")
          addCookie("login", "yes", 1, "/")
          if (this.remember === true) {
            addCookie("remember", "yes", 7, "/")
          } else {
            addCookie("remember", "", 7, "/")
          }
          console.log(document.cookie)
          setTimeout(function () {
              window.location.href = '/home/'
            },1000)
        // } else if (res['flag'] === global_.CONSTGET.ACCOUNT_LOGGED_IN) { //account has been logged in
        //   this.$Message.info('账号已登录!')
        //   setTimeout(function () {
        //       window.location.href = '/main_return/'
        //     },2000)
        } else if (res['flag'] === global_.CONSTGET.WRONG_ACCOUNT) { //wrong account
          this.$Message.error('账号不存在!')
        } else if (res['flag'] === global_.CONSTGET.ACCOUNT_NOT_ACTIVETED) { //account not be activated
          this.$Message.warning('账号未激活,即将前往激活')
          var that = this
          setTimeout(function () {
            window.location.assign(encodeURI("/user_activate"+"?"+"email=" + that.formItem.email)) 
          },2000)
        } else if (res['flag'] === global_.CONSTGET.WRONG_PASSWORD) { //wrong password
          this.$Message.error('密码错误!')
          this.formItem.password = ''
        } 
      },
    }
  }
</script>
<style scoped>
.my-button >>> .ivu-btn>span {
    vertical-align: initial;
}
input{
  height: 36px!important;
}
.app {
  width: 100%;
}
.wrap {
  width: 35vw;
  margin-left: auto;
  margin-right: auto;
  padding-top: 2vh;
}
.ask_register{
  margin-top: 3em;
  text-align: right;
  color: grey;
  font-size: 1em;
}
a.register-style {
    text-decoration: none;
    color: black;
    font-weight: bold;
}
a.register-style:hover {
    color: blue;
    font-weight: bolder;
    text-decoration: none;
}
.user_login{
  height: 20em;
  border: 0.6mm solid #FDF5E6;
  border-radius: 0.5rem;
  margin-top: 0.5em;
}
.title {
  margin-left: 9%;
  margin-bottom: 0.8em;
  margin-top: 0.8em;
  font-size: 1.5em;
}
.user-input {
  width: 28vw;
  height: 2.2em;
  margin-left: auto;
  margin-right: auto;
  border-color: blue;
}
.btn {
  width: 14vw;
  height: 2em;
  margin-left: auto;
  margin-right: auto;
  background-color: rgb(48, 36, 36);
  font-size: 1.2em;
  text-align: center;
}
.signup {
  display: inline-block;
  width: 50%;
  font-size: 1.2em;
  margin: 0;
  margin-bottom: 2vh;
  padding-left: 9%;
}
.item{
  width: 28vw;
  font-size: 0.9em;
  margin-top: 1em;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 0.5em;
}
.item a{
  float:right;
  text-decoration: none;
  text-align: right;
  color:#515a6e;
}
.item a:hover{
  color: blue;
  text-decoration: none;
}
.my-button{
  display: block;
  width: 28vw;
  height: 2.2em;
  margin-top: 2em;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 2vh;
}
.remember-me {
  margin-left: 1vw;
}
</style>
