<template>
    <div class="footer">
        <div class="foot-top">
            <div class="top-left">
                <span>归来，您的私人求职管家，为海外学子倾心打造</span>
            </div>
            <div class="top-right">
                <a href="/home">首页</a>|
                <a href="/home">就业咨询</a>|
                <a href="/home">定制企业清单</a>|
                <a href="/home">关于我们</a>|
                <a href="/home">服务条款</a>|
                <a href="/home">帮助中心</a>
            </div>
        </div>
        <div class="foot-bottom">
            <div class="bottom-left">
                <ul>
                    <li>邮箱：{{email}}</li>
                    <li>电话：{{phone}}</li>
                    <li>地址：{{address}}</li>
                </ul>
            </div>
            <div class="bottom-right">
                <ul>
                    <li>未经Guilai.com同意，不得转载本网站所有招聘信息（版权号）</li>
                    <li>归来信息技术有限公司（备案号）</li>
                </ul>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data () {
        return {
            email: "Guilai@163.com",
            phone: "12345678",
            address: "天津市津南区同砚路38号"
        }
    }
}
</script>
<style scoped>
.footer {
    width: 100%;
    height: 120px;
    background-color: #272727;
}
.foot-top {
    height: 30%;
    margin: 0 8vw;
    display: flex;
}
.foot-bottom {
    height: 70%;
    margin: 0 8vw;
    display: flex;
}
.top-left, .top-right, .bottom-left, .bottom-right {
    width: 50%;
    height: 100%;
    display: flex;
    align-items: center;
}
.top-left span {
    color: white;
    font-size: 17px;
    line-height: 36px;
}
.top-right {
    font-size: 14px;
}
.top-right a {
    padding: 0 10px;
}
.bottom-left ul {
    margin-left: 20px;
}
.bottom-left ul li {
    list-style-type: none;
    font-size: 13px;
    color: white;
}
.bottom-right ul li{
    color: white;
    font-size: 13px;
    margin-left: 20px;
    list-style-type: none;
}
</style>