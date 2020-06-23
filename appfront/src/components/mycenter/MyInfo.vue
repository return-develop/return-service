<template>
    <div id="show-info">
        <div class="introduce" v-if="isShow"> 
            <div class="uname">
                <span>{{formTop.username}}</span>
                <span style="padding:0;font-size:1.6em;">|</span>
                <span>{{formTop.sex}}</span>
                <div class="complete"><Progress :percent="percent" :stroke-width="18" text-inside /></div>
            </div>
            <div class="info">
                <li class="sp"><div>学校：<span>{{formTop.school}}</span></div><div>专业：<span>{{formTop.major}}</span></div><div><Icon type="ios-create-outline" /><a @click="isShow = false">编辑</a></div></li>
                <li class="gg"><div>工作目标：<span>{{formTop.goal}}</span></div><div>毕业时间：<span>{{formTop.graduate_time}}</span></div></li>
                <li class="dc"><div>期望工作地点：<span>{{formTop.city}}</span></div></li>
            </div>
        </div>
        <div v-if="!isShow" class="detail-info"><DetailInfo :sendForm="sendForm" @getChangeName="getChangeName"></DetailInfo></div>
    </div>
</template>
<script>
import DetailInfo from './DetailInfo'
import global_ from '../Const' 
export default {
    components:{DetailInfo},
    data () {
        return {
            isShow: true,
            percent: 0,
            sum: 0,
            changeName: '',
            formTop: {
                username: '用户名',
                realname:'',
                sex: '待填写',
                school: '待填写',
                major: '待填写',
                education: '待填写',
                goal: '待填写',
                graduate_time: '待填写',
                city: '待填写',
                birthday:'',
                phone: '',
                email: '',
                hobby: '',
                prize: '',
                skill: ''
            },
            sendForm: {
                username: '',
                realname:'',
                sex: '',
                school: '',
                major: '',
                education: '',
                goal: '',
                graduate_time: '',
                city: '',
                birthday:'',
                phone: '',
                email: '',
                hobby: '',
                prize: '',
                skill: ''
            }
        }
    },
    async created() {
        if (this.getCookieValue("login") === "yes") {
            var email = this.getCookieValue("email")
            let res = await this.fetchBase('/user_view_info', {
            'email': email,
            })
            console.log(res)
            if (res['flag'] === global_.CONSTGET.SUCCESS) {
                delete res['flag']
                for (var item in res) {
                    this.sendForm[item] = res[item]
                    if (res[item].trim().length > 0) {
                        this.formTop[item] = res[item]
                        this.sum += 1
                    }
                }
                this.percent = parseInt(parseInt(this.sum) * 100 / parseInt(Object.keys(this.formTop).length))
                console.log("sum:" + this.sum + "percent:" + this.percent)
                this.sum = 0
            } else if (res['flag'] === global_.CONSTGET.FAIL) {
                this.$Message.error("服务器错误，即将为您跳转到首页")
                setTimeout(function () {
                    window.location.href = '/'
                },2000)
            }
        }
    },
    methods: {
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
        getChangeName(res) {
            // console.log("父组件" + res)
            this.$emit('getChangeName0', res)
        }
        // edit () {
        //     this.ishow = !this.ishow;
        // }
    }
}
</script>
<style scoped>
#show-info{
    width:100%;
    height:fit-content;
}
.info-show{
    width:100%;
}
.introduce {
    width: 100%;
    border: 1px solid #dcdee2;
    border-radius: 4px;
}
.detail-info {
    margin-left: 4vw;
}
.uname {
    background-color: #d7d7d7;
    width: 100%;
    height: 70px;
}
.uname span {
    font-size: 20px;
    font-weight: 700;
    line-height: 70px;
}
.uname a{
    font-size: 16px;
    line-height: 70px;
    padding-right: 20px;
}
.uname span {
    padding: 0 12px;
}
.uname a {
    float: right;
}
.complete {
    float: right;
    width: 64%;
    padding-right: 12px;
    position: relative;
    top: 50%;
    transform: translateY(-50%);
}
.info {
    margin-left: 12px;
    list-style-type:none;
    color:black;
    font-size: 1.1em;
    font-weight: 600;
}
.sp {
    padding-bottom: .5em;
    padding-top: .5em;
    display: flex;
}
.gg{
    padding-bottom: 1em;
    display: flex;
}
.dc{
    padding-bottom: .5em;
}
.sp div, .gg div {
    width: 35%;
}
.sp div span, .gg div span, .dc div span {
    font-size: 1em;
    font-weight: 500;
    overflow: hidden;
}
.sp div:last-child {
    width: 30%!important;
    text-align: right;
    padding-right: 12px;
}
</style>