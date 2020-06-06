<template>
    <ul class="topmenu">
        <li><a href="/home" class="active">首页</a></li>
        <li><a href="/consult">就业咨询</a></li>
        <span>
            <li class="login-register">
                <button class="dropbtn"><img src="../../static/img/profile.jpg"></button>
                <a href="/user_login" class="login-nav">登录</a>
                <a href="/user_register" class="register-nav">注册</a>
                <div class="dropdown-content" v-if="isShow">
                    <a href="/" >个人中心</a>
                    <a href="/" >注销退出</a>
                </div>
            <li class="book">
                <img src="../../static/img/wechat-1.jpg">
                <a href="/book" class="book-nav">订阅公众号</a>
            </li>
        </span>
    </ul>
</template>
<script>
    export default {
        data () {
            return{
                isShow: false
            }
        },
        method: {
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
.topmenu li {
    float: left;
    line-height: 36px;
}
.topmenu li a {
    display: inline-block;
    color: white;
    font-size: 14px;
    text-align: center;
    padding: 0 16px;
    text-decoration: none;
}
.topmenu li a:hover {
    background-color: #222;
    color: white;
    font-weight: bold;
}
.topmenu li:first-child {
    color: white;
    padding-left: 7vw;
    /* background-color: rgb(91, 76, 175); */
}

.topmenu span{
    float: right;
    font-size: 0.9em;
}

.topmenu li:last-child{
    padding-right: 7vw;
}

ul span a.login-nav{
    padding-left: 2px!important;
    padding-right: 2px;
}

ul span a.register-nav{
    padding-left: 0px!important;
}

ul span a.book-nav{
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
</style>