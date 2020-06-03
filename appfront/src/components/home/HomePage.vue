<template>
    <div class="container">
        <ul class="topmenu">
            <li><a href="/home" class="active">首页</a></li>
            <li class="job-consult"><a href="/consult/">就业咨询</a></li>
            <span>
                <li class="login-register">
                    <button class="dropbtn"><img src="../../../static/img/curry.jpg"></button>
                    <a href="/user_login" class="login-nav">登录</a>/
                    <a href="/user_register" class="register-nav">注册</a>
                    <div class="dropdown-content">
                        <a href="/">个人中心</a>
                        <a href="/">注销退出</a>
			        </div>
                </li>
                <li class="book">
                    <img src="../../../static/img/wechat-1.jpg">
                    <a href="/book" class="book-nav">订阅公众号</a>
                </li>
            </span>
        </ul>
        <div class="header">
            <div class="h-tips">
                <p>成为会员，不错过任何招聘</p>
                <p>已有{{num}}名学子使用</p>
            </div>
            <div class="q-login">
                <input v-model="formItem.email" placeholder="输入邮箱" type="text" class="my-input">
                <input v-model="formItem.password" placeholder="输入密码" type="text" class="my-input">
                <button type="primary" @click="submit" class="btn">登录</button><br>
                <p>{{message}}</p>
            </div>
        </div>
        <div class="content">
            <div class="l-content">
                <div class="consult">
                    <p>不知道如何开始？</p>
                    <a href="/index/">预约名师免费1v1咨询</a>
                </div>
                <div class="select">
                    <a href="/index/" @click="select" class="filter">筛选</a>
                    <a @click="resetList" class="reset">清空</a>
                </div>
                <div class="subject">
                    <p>专业学科</p>
                    <SelectSubject></SelectSubject>
                </div>
                <div class="city">
                    <p>期望就业城市</p>
                    <selectCity></selectCity>
                </div>
                <div class="salary">
                    <p>期望薪资</p>
                    <SelectSalary></SelectSalary>
                </div>
            </div>
            <div class="r-content">
                <div class="video">
                    <CarousalVideo></CarousalVideo>
                </div>
                <div class="job-note">
                    我们为你提供全国：
                </div>
                <div class="job-display">
                    <div class="l-display">
                        <div class="center-display">
                            <span>{{jobNum}}</span>个<br>
                            <p>岗位信息</p>
                        </div>
                    </div>
                    <div class="r-display">
                        <div class="center-display">
                            <span>{{companyNum}}</span>家<br>
                            <p>岗位信息</p>
                        </div>
                    </div>
                </div>
                <div class="company-display">
                    <CompanyDisplay></CompanyDisplay>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import SelectSubject from './SelectSubject'
    import SelectCity from './SelectCity'
    import SelectSalary from './SelectSalary'
    import CarousalVideo from './CarousalVideo'
    import CompanyDisplay from './CompanyDisplay'
    export default {
        components: {SelectSubject, SelectCity, SelectSalary, CarousalVideo, CompanyDisplay},
        data () {
            return{
                num: 9999,
                jobNum: 17182,
                companyNum: 482,
                formItem: {
                    email: '',
                    password: ''
                },
                message: ''
            }
        },
        method: {
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
                this.formItem.email = ''
                this.formItem.password = ''
            },
            trimItem () {
                this.formItem.email = this.formItem.email.trim()
                this.formItem.password = this.formItem.password.trim()
            },
            async submit () {
                // 检查是否为空
                this.trimItem()
                if (this.formItem.email === '' || this.formItem.password === '') {
                this.message = '不能有内容为空!'
                return
                }
                let res = await this.fetchBase('/api/user/login/', {
                'email': this.formItem.email,
                'password': this.formItem.password
                })
                this.reset()
                if (res['flag'] === global_.CONSTGET.SUCCESS) {
                this.$Message.success('登录成功!')
                window.location.href = '/home/'
                } else if (res['flag'] === global_.CONSTGET.ACCOUNT_NOT_ACTIVETED) {
                this.message = '账号未激活!'
                } else if (res['flag'] === global_.CONSTGET.WRONG_PASSWORD) {
                this.message = '密码错误!'
                } else if (res['flag'] === global_.CONSTGET.WRONG_ACCOUNT) {
                this.message = '账号不存在!'
                }
            },
            handleCheck() {

            }
            
        }
    }
</script>
<style>
    .dropbtn {
       background-color: #272727;
       border: none;
    }
    .dropdown-content {
        display: none;
        position: absolute;
        background-color: white;
        min-width: 90px;
        border-radius: 5px;
        z-index: 999;
        /* box-shadow:  0px 8px 16px 0px rgba(0,0,0,0.2); */
    }
    .dropdown-content a {
        color: #000000!important;
        padding: 5px!important;
        text-decoration: none;
        display: block;
    }
    .dropdown-content a:hover {
        background-color: #f1f1f1!important;
        border-radius: 5px;
    }
    .login-register:hover .dropdown-content {
        display: flex;
        flex-direction: column;
    }   
    .header{
        width: 100%;
        height: 5em;
        background-color: #d8d8d8;
        display: flex;
    }
    .h-tips{
        width: 25vw;
        margin-left: 10vw;
        margin-top: auto;
        margin-bottom: auto;
    }
    .h-tips p:first{
        font-size: 1.1em;
    }
    .h-tips p:last-child{
        font-size: 0.8em;
    }
    .q-login{
        position:absolute;
        right: 8vw;
    }
    .my-input{
        margin-left: 4px;
        padding-left: 8px;
        border-radius: 3px;
        border: 1px solid white;
        height: 1.8em;
        width: 14em;
        margin-top: 1.6em;
        float: left;

    }
    .btn{
        width: 4em;
        height: 2.2em;
        text-align: center;
        border-radius: 3px;
        border: 1.2px solid #989696;
        background-color: #d8d8d8;
        margin-top: 1.4em;
        font-weight: 600;
        margin-left: 8px;
    }
    .q-login p{
        font-size: 0.8em;
        color: red;
        margin-left: 4px;
    }
    .content{
        width: 100%;
        display:flex;
        flex-direction: row;
    }
    .l-content{
        width: 16vw;
        margin-top: 2vh;
        margin-left: 8vw;
        margin-right: 8vw;
        display: flex;
        flex-direction: column;
    }
    .r-content{
        width: 54vw;
        margin-top: 2vh;
        margin-left: 6vw;
        margin-right: 8vw;
    }
    .consult{
        width: 15em;
        height: 5em;
        text-align: center;
        background-color: #d8d8d8;
        position: relative;
        display: table-cell;
        vertical-align: middle;
    }
    .consult p{
        font-size:1em;
        padding-top: 0.8em;
    }
    .consult a{
        font-size: 1.2em;
        color: black;
        font-weight: 600;
        text-decoration: none;
    }
    .filter-content{
        width: 100%;
    }
    ul span{
        color:black;
        display: initial;
        float: none;
    }
    label {
        display: initial;
        float: right;
    }
    .select{
        width: 100%;
        margin-top: 2vh;
        color: black;
    }
    .filter{
        float: left;
        text-decoration: none;
        font-weight: 600;
        color: rgb(48, 36, 36);
    }
    .reset{
        float: right;
        text-decoration: none;
        color:  rgb(48, 36, 36);
    }
    .subject .city .salary p{
        font-size: 1em;
        color: #464c5b;
    }
    .subject .city .salary{
        margin-top: 2vh;
    }
    .video{
        width: 100%;
        height: 16em;
    }
    .job-note{
        margin-top: 4vh;
        margin-bottom: 4vh;
        text-align: center;
        font-size: 1em;
        font-weight: 400;
        color: black;
    }
    .job-display{
        display: flex;
        height: 6em;
        color: white;
    }
    .l-display, .r-display{
        height: 100%;
        width: 48%;
        display: table;
        text-align: center;
        background-color: #755c5c;
        border-radius: 3px;
    }
    .r-display{
        margin-left: 4%;
        
    }
    .center-display{
        display: table-cell;
        vertical-align: middle;
    }
    .l-display span, .r-display span{
        font-size: 1.8em;
    }
    .l-display label, .r-display label{
        font-size: 0.9em;
    }
    .company-display{
        width: 100%;
        height: fit-content;
        margin-top: 4vh;
    }
</style>