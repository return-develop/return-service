<template>
    <div class="logout">
        <Modal
            v-model="modal1"
            title="退出登录"
            @on-ok="ok"
            @on-cancel="cancel">
            <p>尊敬的<span style="color:#5cadff;font-weight:600;font-size:14px;">{{username}}</span>用户</p>
            <p>是否确认<b>退出</b>？</p>
        </Modal>
    </div>
</template>
<script>
    export default {
        data () {
            return {
                modal1: true,
                username: ''
            }
        },
        created() {
            if (this.getCookieValue('login') == 'yes') {
                if (this.getCookieValue('username') == '') {
                    this.username = this.getCookieValue('email')
                } else {
                    this.username = this.getCookieValue('username')
                }
            }
            
        },
        methods: {
            ok () {
                this.deleteCookie('login', '/')
                this.deleteCookie('username', '/')
                if (this.getCookieValue("remember") !== 'yes') {
                    this.deleteCookie('remember', '/')
                }
                this.$Message.info('已退出');
                location.href = '/'
            },
            cancel () {
                this.$Message.info('Clicked cancel');
                location.href = '/mycenter'
            },
            deleteCookie(name,path){  /**根据cookie的键，删除cookie，其实就是设置其失效**/
                var name = escape(name);
                var expires = new Date(0);
                path = path == "" ? "" : ";path=" + path;
                document.cookie = name + "="+ ";expires=" + expires.toUTCString() + path;
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
                return unescape(value);              //对它解码
                }else{ //搜索失败，返回空字符串
                return "";
                }
            },
        }
    }
</script>
<style>
    .ivu-modal-header-inner {
        font-size: 16px;
    }
    .ivu-modal-body {
        font-size: 14px;
        text-align: center;
    }
    .ivu-modal-body p span {
        padding:0 3px;
        font-weight: 600;
        font-size: 16px;
        color: black;
    }
    .ivu-modal-body p b {
        color: black;
    }
</style>
