<template>
  <div>
      <div class="menu"><navigation></navigation></div>
      <div class="app">
          <h3 class="title">还差一步，激活账号</h3>
          <div class="item">
            输入邮箱中获得的激活码
            <span value="点击获取激活码" @click="settime" v-if="isShow">{{content}}</span>
            <span value="重新发送时间" v-if="!isShow">重新发送({{countdown}})</span>
          </div>
          <div class="user-input">
            <Input v-model="formItem.active_code" placeholder="激活码" type="text" class="customer-input">
          </div>
          <div class="my-button">
              <Button type="primary" @click="submit" class="btn1">激活账号</Button>
              <Button type="primary" @click="goToEmailLogin(formItem.email)" class="btn2">前往邮箱</Button>
          </div>
      </div>
  </div>
</template>
<script>
import navigation from '../navigation'
import global_ from '../Const'
import { fetchBase } from '../../post/fetchBase'
export default {
    components:{navigation},
    data () {
      return {
        formItem: {
          email: '',
          active_code: ''
        },
        activate_code: '',  //服务器返回的激活码
        countdown: 180, //发送倒计时
        content: '点击获取',
        isShow: true  //显示
      }
    },
    //解析url
    created() {
      var url=location.href 
      var tmp1 = url.split("?")[1]
      var tmp2 = tmp1.split("&")[0]
      var tmp3 = tmp2.split("=")[1]
      this.formItem.email = tmp3
//       console.log(this.formItem.email)
    },
    watch:{
      'countdown':{
        deep:true,
        handler: function(newV, oldV) {
          if(newV == 0) {
          }
          if(newV == 170){
          }
        }
      }
    },
    methods: {
      reset () {
        this.formItem.active_code = ''
      },
      async settime() {
        this.isShow = false
        let res = await fetchBase('/api/user/activate/', {
          'email': this.formItem.email.trim(),
          'message': 'user activate'
        })
        console.log(res)
        if (res['flag'] === global_.CONSTGET.SUCCESS) {
          this.activate_code = res['activate_code']
        } else if (res['flag'] === global_.CONSTGET.EMAIL_ACTIVATED) {
          this.$Message.error("您的邮箱已激活")
          this.isShow = true
          return
        } else if (res['flag'] === global_.CONSTGET.FAIL) {
          this.$Message.error("获取激活码失败，可能是您的邮箱不存在！")
          this.isShow = true
          return
        }
        let timeInt = setInterval(() => {
          this.countdown--;
          if (this.countdown <= 0) {
            this.countdown = 180
            this.isShow = true
            window.clearInterval(timeInt)
          }
        }, 1000)
      },
      async submit () {
        // 检查数据格式，并提交注册信息
        if (this.formItem.active_code === '' ) {
          this.$Message.warning("不能为空！")
          return
        }
        if (this.countdown === 180) {
          this.$Message.warning("验证码无效，请重新获取！")
          this.activate_code = ''
          return
        }
        if (this.formItem.active_code === this.activate_code) {
          console.log("激活码正确")
          let res = await fetchBase('/api/user/check_activate/', {
          'email': this.formItem.email,
          'isactivate': "true"
          })
          if (res['flag'] === global_.CONSTGET.SUCCESS) {
            this.$Message.success("激活成功！即将为您跳转到登录界面")
            setTimeout(function () {
              window.location.href = '/user_login/'
            },2000)
          } else if (res['flag'] === global_.CONSTGET.FAIL) {
            this.$Message.error("服务器错误")
            return
          }
        } else {
          this.$Message.error("验证码错误，重新输入")
          this.reset()
          return
        }
      },
      goToEmailLogin (email) {
        var hash = {
            'qq.com': 'http://mail.qq.com',
            'gmail.com': 'http://mail.google.com',
            'sina.com': 'http://mail.sina.com.cn',
            '163.com': 'http://mail.163.com',
            '162.com': 'http://mail.162.com',
            '126.com': 'http://mail.126.com',
            'yeah.net': 'http://www.yeah.net/',
            'sohu.com': 'http://mail.sohu.com/',
            'tom.com': 'http://mail.tom.com/',
            'sogou.com': 'http://mail.sogou.com/',
            '139.com': 'http://mail.10086.cn/',
            'hotmail.com': 'http://www.hotmail.com',
            'live.com': 'http://login.live.com/',
            'live.cn': 'http://login.live.cn/',
            'live.com.cn': 'http://login.live.com.cn',
            '189.com': 'http://webmail16.189.cn/webmail/',
            'yahoo.com.cn': 'http://mail.cn.yahoo.com/',
            'yahoo.cn': 'http://mail.cn.yahoo.com/',
            'eyou.com': 'http://www.eyou.com/',
            '21cn.com': 'http://mail.21cn.com/',
            '188.com': 'http://www.188.com/',
            'foxmail.com': 'http://www.foxmail.com',
            'outlook.com': 'http://www.outlook.com'
        }
        if (this.isShow == true) {
          this.$Message.warning("请点击获取验证码！")
          return
        }
        var _email = email.split('@')[1];    //获取邮箱域
        if(hash.hasOwnProperty(_email)){
            window.open(hash[_email]);
        }else{
            this.$Message.warning("未匹配到邮箱地址，请自行登录查看！");
        }
      }
    }
}
</script>
<style scoped >
    .app {
        width: 35vw;
        height: 19em;
        margin-top: 20vh;
        margin-left: auto;
        margin-right: auto;
        border: 0.6mm solid #FDF5E6;
    }
    .title {
        text-align: center;
        margin-top: 1.5em;
    }
    .item{
        width: 28vw;
        font-size: 0.9em;
        font-weight: 600;
        margin-top: 3em;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 1vh;
    }
    .user-input {
        width: 28vw;
        height: 2.2em;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 2vh;
        border-color: blue;
    }
    .my-button{
        height: 5.9em;
        margin-top: 1.5em;
    }
    .btn1, .btn2 {
        display: block;
        width: 28vw;
        height: 2.5em;
        margin-left: auto;
        margin-right: auto;
        font-size: 1em;
        border: 1px solid #dcdee2;
    }
    .btn1 {
      background-color: rgb(48, 36, 36);
    }
    .btn2 {
      background-color: white;
      color: rgb(48, 36, 36);
      margin-top: 0.5em;
    }
    .item span {
     float: right;
     font-weight: 500;
    }
</style>
