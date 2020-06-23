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
      if (this.getCookieValue("remember") == "yes") {
        this.formItem.email = this.getCookieValue("email")
        this.formItem.password = this.getCookieValue("password")
        this.remember = true
      }
      if (navigator.cookieEnabled == false) {
        this.cookieEnable = false
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
      findEmail () {
        this.findback.modal = !this.findback.modal
      },
      async ok () {
        this.trimItem()
        let res = await this.fetchBase('/api/user/findback_password/', {
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
        if (this.getCookieValue("login") == "yes") {
          this.$Message.info("您已登录")
          return 
        }
        if (this.formItem.email === '' || this.formItem.password === '') {
          this.$Message.warning('不能有内容为空')
          return
        }
        let res = await this.fetchBase('/api/user/login/', {
          'email': this.formItem.email,
          'password': this.formItem.password
        })
        // this.reset()
        if (res['flag'] === global_.CONSTGET.SUCCESS) { //success
          this.$Message.success('登录成功!')
          this.addCookie("email", this.formItem.email, 7, "/")
          this.addCookie("password", this.formItem.password, 7, "/")
          this.addCookie("username", res['username'], 7, "/")
          this.addCookie("login", "yes", 1, "/")
          if (this.remember === true) {
            this.addCookie("remember", "yes", 7, "/")
          } else {
            this.addCookie("remember", "", 7, "/")
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
      addCookie(name,value,days,path){  /**添加设置cookie**/
        var name = escape(name);
        var value = escape(value);
        var expires = new Date();
        expires.setTime(expires.getTime() + days * 3600000 * 24);
        //path=/，表示cookie能在整个网站下使用，path=/temp，表示cookie只能在temp目录下使用
        path = path == "" ? "" : ";path=" + path;
        //GMT(Greenwich Mean Time)是格林尼治平时，现在的标准时间，协调世界时是UTC
        //参数days只能是数字型
        var _expires = (typeof days) == "string" ? "" : ";expires=" + expires.toUTCString();
        document.cookie = name + "=" + value + _expires + path;
      },
      getCookieValue(name){ /**获取cookie的值，根据cookie的键获取值**/
        //用处理字符串的方式查找到key对应value
        var name = escape(name);
        //读cookie属性，这将返回文档的所有cookie
        var allcookies = document.cookie;
        //查找名为name的cookie的开始位置
        name += "=";
        var pos = allcookies.indexOf(name);
        //如果找到了具有该名字的cookie，那么提取并使用它的值
        if (pos != -1){                       //如果pos值为-1则说明搜索"version="失败
          var start = pos + name.length;         //cookie值开始的位置
          var end = allcookies.indexOf(";",start);    //从cookie值开始的位置起搜索第一个";"的位置,即cookie值结尾的位置
          if (end == -1) end = allcookies.length;    //如果end值为-1说明cookie列表里只有一个cookie
          var value = allcookies.substring(start,end); //提取cookie的值
          return (value);              //对它解码
        }else{ //搜索失败，返回空字符串
          return "";
        }
      },
      deleteCookie(name,path){  /**根据cookie的键，删除cookie，其实就是设置其失效**/
        var name = escape(name);
        var expires = new Date(0);
        path = path == "" ? "" : ";path=" + path;
        document.cookie = name + "="+ ";expires=" + expires.toUTCString() + path;
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
