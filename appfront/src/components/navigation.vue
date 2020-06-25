<template>
    <ul class="topmenu">
        <li class="menu-item1"><a href="/home" class="active">首页</a></li>
        <li class="menu-item2"><a href="/">就业咨询</a></li>
        <li class="menu-item3"><a href="/">定制企业清单</a></li>
        <span class="else-item">
            <li class="login-register menu-item1">
                    <button class="dropbtn"><img src="../../static/img/profile.jpg"></button>
                    <a href="/user_login" class="login-nav" v-if="!isShow">登录</a>
                    <Divider type="vertical" v-if="!isShow"/>
                    <a href="/user_register" class="register-nav" v-if="!isShow">注册</a>
                    <span style="padding: 0 10px;color:white;line-height:36px;max-length:100px;overflow:hidden;" v-if="isShow">你好，<span style="color:#5cadff;font-weight:600;">{{username}}</span></span>
                    <div class="dropdown-content" v-if="dropShow">
                        <a href="/mycenter" >个人中心</a>
                        <a @click="logout">退出登录</a>
                    </div>
                    <!-- <Dropdown v-if="isShow">
                        <a style="padding: 0 10px;font-size: 12px" >你好，{{username}}</a>
                        <DropdownMenu slot="list">
                            <DropdownItem><span style="color:#272727;line-height: 36px;padding: 5px" @click="toCenter">个人中心</span></DropdownItem>
                            <DropdownItem><span style="color:#272727;line-height: 36px" @click="toLogout">退出登录</span></DropdownItem>
                        </DropdownMenu>
                    </Dropdown> -->
            <li class="book menu-item1">
                <img src="../../static/img/wechat-1.jpg">
                <a href="/book" class="book-nav">订阅公众号</a>
            </li>
        </span>
    </ul>
</template>
<script>
    import { addCookie, getCookieValue, deleteCookie } from '../cookie/useCookie'
    export default {
        props: {
            changeName: {
                type:String,
                default: ''
            }
        },
        data () {
            return{
                isShow: false,
                dropShow: false,
                username: '用户'
            }
        },
        created() {
            var url = window.location.href.split('/').filter(function (s) { return s && s.trim()})[2]
            console.log(document.cookie)
            var isLogin = getCookieValue("login")
            if (isLogin == "yes" && url == 'mycenter'){
                this.isShow = true;
                this.dropShow = false;
                if (getCookieValue("username") == ""){
                    this.username = getCookieValue("email")
                } else {
                    this.username = getCookieValue("username")
                }
            } else if (isLogin == "" && url == 'mycenter') {
                this.$Message.warning("未登录，即将跳转到登录界面")
                setTimeout(function () {
                    window.location.href = '/user_login/'
                    },2000)
            } else if (isLogin == "") {
                this.isShow = false
                this.dropShow = false
            }
            else if (getCookieValue("login") == "yes") {
                this.isShow = true;
                this.dropShow = true;
                if (getCookieValue("username").trim().length == 0){
                    this.username = getCookieValue("email")
                } else {
                    this.username = getCookieValue("username")
                }
            }
        },
        watch: {
            changeName: function(n) {
                // console.log("收到了" + n)
                if (n != this.username) {
                    this.username = n
                }
            }
        },
        methods: {
            logout() {
                deleteCookie('login', '/')
                deleteCookie('username', '/')
                if (getCookieValue("remember") == '') {
                    deleteCookie('remember', '/')
                }
                this.$Message.info('已退出')
                location.href = '/'
            }
        }
    }
</script>
<style scoped>
/* body{
    margin: 0;
    padding: 0;
    font-size:15px!important;
} */
.topmenu {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    height: 36px;
    background-color:#272727;
}
.menu-item1, .menu-item2, .menu-item3 {
    float: left;
    line-height: 36px;
}
.menu-item1 a, .menu-item2 a, .menu-item3 a {
    display: inline-block;
    color: white;
    font-size: 14px;
    text-align: center;
    padding: 0 16px;
    text-decoration: none;
}
.menu-item1 a:hover, .menu-item2 a:hover, .menu-item3 a:hover{
    background-color: rgb(63, 60, 60);
    color: white;
    font-weight: bold;
}
.topmenu li:first-child {
    color: white;
    padding-left: 7vw;
    /* background-color: rgb(91, 76, 175); */
}

.else-item{
    float: right;
    font-size: 14px;
}

.topmenu li:last-child{
    padding-right: 7vw;
}

ul span a.login-nav{
    padding-left: 2px!important;
    padding-right: 2px;
}

.register-nav, .book-nav{
    padding-left: 0px!important;
}
ul span li img{
    vertical-align: middle;
    border-radius: 50%;
    width: 20px;
    height: 20px;
}
.dropbtn {
    background-color: #272727;
    border: none;
}
.dropdown-content {
    display: none;
    position: absolute;
    background-color:white;
    width: 150px;
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
</style>