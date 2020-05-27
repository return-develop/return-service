<template>
    <div class="app">
        <h3 class="title">还差一步，激活账号</h3>
        <div class="item">
          输入邮箱中获得的激活码
          <span value="点击获取激活码" @click="settime">{{content}}</span>
        </div>
        <div class="user-input">
          <Input v-model="formItem.active_code" placeholder="激活码" type="text" class="customer-input">
        </div>
        <div class="my-button">
            <Button type="primary" @click="submit" class="btn1">激活账号</Button>
            <Button type="primary" @click="goToEmailLogin(formItem.email)" class="btn2">前往邮箱</Button>
        </div>
    </div>
</template>
<script>
export default {
    data () {
      return {
        formItem: {
          email: '',
          active_code: ''
        },
        countdown: 180,
        content: '点击获取'
      }
    },
    created() {
      var url=location.href 
      var tmp1 = url.split("?")[1]
      var tmp2 = tmp1.split("&")[0]
      var tmp3 = tmp2.split("=")[1]
      this.formItem.email = tmp3
      console.log(this.formItem.email)
    },
    watch:{
      'countdown':{
        deep:true,
        handler: function(newV, oldV) {
          if(newV == 170){
            this.$Message.warning('111111')
          }
        }
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
        this.formItem.active_code = ''
      },
      settime() {
        let timeInt = setInterval(() => {
          this.content = "重新发送(" + this.countdown + ")"
          this.countdown--;
          if (this.countdown <= 0) {
            this.content = "点击获取"
            this.countdown = 180
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
        let res = await this.fetchBase('/api/user/activate/', {
          'email': this.formItem.email,
          'active_code': this.formItem.active_code
        })
        this.reset()
        if (res['flag'] === global_.CONSTGET.INVALID) {
          this.$Message.error(global_CONSTSHOW.INVALID)
        } else if (res['flag'] === global_.CONSTGET.EXPIRED) {
          this.$Message.error(global_CONSTSHOW.EXPIRED)
        } else if (res['flag'] === global_.CONSTGET.SUCCESS) {
          this.$Message.success('激活成功!')
          window.location.href = '/user_login/'
        }
      },
      goToEmailLogin (email) {
        var hash = {
            'qq.com': 'http://mail.qq.com',
            'gmail.com': 'http://mail.google.com',
            'sina.com': 'http://mail.sina.com.cn',
            '163.com': 'http://mail.163.com',
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
        var _email = email.split('@')[1];    //获取邮箱域
        if(hash.hasOwnProperty(_email)){
            location.href=hash[_email];
        }else{
            this.$Message.warning("抱歉!未找到对应的邮箱登录地址，请自己登录邮箱查看邮件！");
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
        height: 2.2em;
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
