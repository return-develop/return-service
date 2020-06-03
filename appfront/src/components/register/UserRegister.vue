<template>
  <div id="app">
    <div class="container">
        <div class="ask-login">
          <p>已有账号？<a href="/user_login" class="login-style">请登录</a></p>
          <a @click="trans">ttest</a>
        </div>
        <div class="user-register">
            <h3 class="title">注册 归来</h3>
            <div class="item" >输入邮箱</div>
            <!-- <router-link :to="{ name: 'user_activate', params: { email: 1234 } }"></router-link> -->
            <div class="user-input">
              <Input v-model="formItem.email" placeholder="请输入邮箱" type="text" class="my-input" id="email">
            </div>
            <div class="item">输入密码</div>
            <div class="user-input">
              <Input v-model="formItem.password" placeholder="请输入密码，长度不小于8" type="password" class="my-input">
            </div>
            <div class="item">确认密码</div>
            <div class="user-input">
              <Input v-model="formItem.password2" placeholder="请确认密码" type="password" class="my-input">
            </div>
            <div class="my-button">
              <Button type="primary" @click="submit" class="btn">注册</Button>
            </div>
            <!-- <p class="login">已有账号?<a>点击登录!</a></p> -->
            <p class="clause">点击注册即表示你已阅读并同意归来的<a href="">服务条款</a></p>  
        </div>
    </div>
  </div>
</template>
<script>
  import global_ from '../Const'
  // import Router from 'vue-router'
  // import UserActivate from '@/components/activate/UserActivate'
  // let router = new Router({
  //       routes:[
  //         {
  //           path: '/user_activate',
  //           name: 'UserActivate',
  //           component: UserActivate
  //         }
  //       ]
  //     })
  export default {
    data () {
      return {
        formItem: {
          email: '',
          password: '',
          password2: ''
        }// 注册信息
      }
    },
    methods: {
      fetchBase (url, body) {
        return fetch(url, {
          method: 'post',
          credentials: 'same-origin',
          headers: {
            'X-CSRFToken': this.getCookie('csrftoken'),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(body)
        })
        .then((res) => res.json())
      },
      trans () {
        // 向父组件发送切换到登录界面消息
        // window.location.href = '/user_activate/'
        var email = this.formItem.email
        var myurl="/user_activate"+"?"+"email=" + email
        window.location.assign(encodeURI(myurl)) 
      },
      getCookie (cName) {
        if (document.cookie.length > 0) {
          let cStart = document.cookie.indexOf(cName + '=')
          if (cStart !== -1) {
            cStart = cStart + cName.length + 1
            let cEnd = document.cookie.indexOf(';', cStart)
            if (cEnd === -1) {
              cEnd = document.cookie.length
            }
            return unescape(document.cookie.substring(cStart, cEnd))
          }
        }
        return ''
      },
      checkEmail (email) {
        var ePattern = /^([A-Za-z0-9])+@([A-Za-z0-9])+\.([A-Za-z]{2,4})$/g
        return ePattern.test(email)
      },
      reset () {
        this.formItem.email = ''
        this.formItem.password = ''
        this.formItem.password2 = ''
      },
      trimItem () {
        // 清除两边空格
        this.formItem.email = this.formItem.email.trim()
        this.formItem.password = this.formItem.password.trim()
        this.formItem.password2 = this.formItem.password2.trim()
      },
      async submit () {
        // 检查数据格式，并提交注册信息
        this.trimItem()
        if (this.formItem.email === '' || this.formItem.password === '' || this.formItem.password2 === '' || this.formItem.name === '') {
          this.$Message.warning('不能有选项为空')
          return
        }
        if (this.checkEmail(this.formItem.email.trim()) === false) {
          this.$Message.warning('邮箱格式错误')
          return
        }
        if (this.formItem.password !== this.formItem.password2) {
          this.$Message.warning('两次密码不同')
          return
        }
        if (this.formItem.password.length < 8) {
          this.$Message.warning('密码长度至少为8位')
          return
        }
        let res = await this.fetchBase('/api/user/signup/', {
          'email': this.formItem.email,
          'password': this.formItem.password
        })
        this.reset()
        if (res['flag'] === global_.CONSTGET.EMAIL_REGISTERED) {
          this.$Message.error('此邮箱已被注册!')
        } else if (res['flag'] === global_.CONSTGET.FAIL_SIGN_UP) {
          this.$Message.error('注册失败!')
        } else if (res['flag'] === global_.CONSTGET.SUCCESS) {
          this.$Message.success('注册成功!')
          trans()
        }
      }
    }
  }
</script>
<style scoped>
.my-button >>> .ivu-btn>span {
    vertical-align: initial;
}
#app {
  width: 100%;
}
.ask-login{
  margin-top: 3em;
  text-align: right;
  color: grey;
  font-size: 1em;
}
a.login-style {
    text-decoration: none;
    color: black;
    font-weight: bold;
}
a.login-style:hover {
    color: blue;
    font-weight: bolder;
    text-decoration: none;
}
.user-register{
    height: 26em;
    border: 0.6mm solid #FDF5E6;
    border-radius: 0.5rem;
    margin-top: 0.5em;
}
.title {
  text-align: center;
  margin-bottom: 0.5em;
  margin-top: 1em;
  font-size: 1.5rem;
}
.container {
  display: block;
  width: 35vw;
  margin-left: auto;
  margin-right: auto;
  padding-top: 2vh;
}
.item{
  width: 28vw;
  font-size: 0.9em;
  margin-top: 0;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 0.5em;
}
.user-input {
  width: 28vw;
  height: 2.2em;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 0.5em;
  border-color: blue;
}
.my-button{
  height: 2.2em;
  margin-top: 2em;
}
.btn {
  display: block;
  width: 28vw;
  height: 100%;
  margin-left: auto;
  margin-right: auto;
  background-color: rgb(48, 36, 36);
  font-size: 1.2em;
}
.clause {
  width: 90%;
  height: 4vh;
  font-size: 0.8em;
  margin: 0;
  margin-top: 0.6em;
  padding-left: 9%;
  text-align: center;
}
</style>