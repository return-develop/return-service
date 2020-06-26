<template>
    <div id="show-info">
        <div class="introduce" v-if="isShow"> 
            <div class="uname">
                <div class="uuname">
                    <span>{{formTop.username}}</span>
                    <span style="padding:0;font-size:1.6em;">|</span>
                    <span>{{formTop.sex}}</span>
                </div>
                <div class="complete"><Progress :percent="percent" :stroke-width="18" text-inside /></div>
            </div>
            <div class="info">
                <li class="sp"><div>学校：<span>{{formTop.school}}</span></div><div>专业：<span>{{formTop.major}}</span></div><div><Icon type="ios-create-outline" /><a @click="isShow = false">编辑</a></div></li>
                <li class="gg"><div>工作目标：<span>{{goal}}</span></div><div>期待薪资：<span>{{salary}}</span></div></li>
                <li class="dc"><div>期望工作地点：<span>{{city}}</span></div></li>
            </div>
        </div>
        <div v-if="!isShow" class="detail-info"><DetailInfo :sendForm="sendForm" @getChangeName="getChangeName"></DetailInfo></div>
    </div>
</template>
<script>
import DetailInfo from './DetailInfo'
import global_ from '../Const' 
import { getCookieValue } from '../../cookie/useCookie'
import { fetchBase } from '../../post/fetchBase'
export default {
    components:{DetailInfo},
    data () {
        return {
            isShow: true,
            percent: 0,
            sum: 0,
            changeName: '',
            goal: '',
            city: '',
            salary: '',
            formTop: {
                username: '用户名',
                realname:'',
                sex: '待填写',
                school: '待填写',
                major: '待填写',
                education: '待填写',
                goal: [],
                graduate_time: '待填写',
                city: [],
                salary: '',
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
                goal: [],
                graduate_time: '',
                city: [],
                salary: '',
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
        if (getCookieValue("login") === "yes") {
            var email = getCookieValue("email")
            let res = await fetchBase('/user_view_info', {
            'email': email,
            })
            console.log(res)
            if (res['flag'] === global_.CONSTGET.SUCCESS) {
                delete res['flag']
                for (var item in res) {
                    this.sendForm[item] = res[item]
                    if (res[item] != '') {
                        this.formTop[item] = res[item]
                        this.sum += 1
                    }
                }
                for(var item in this.formTop.goal) {
                    if (item == this.formTop.goal.length -1) {
                        this.goal += this.formTop.goal[item]
                    } else {
                        this.goal += this.formTop.goal[item] + '、'
                    }
                }
                for(var item in this.formTop.city) {
                    if (item == this.formTop.city.length -1) {
                        this.city += this.formTop.city[item]
                    } else {
                        this.city += this.formTop.city[item] + '、'
                    }
                }
                this.salary = this.formTop.salary.replace(/[\[\]']/g, '')
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
    display: flex;
}
.uuname {
    width: 36%;
    height: 100%;
    overflow: hidden;
}
.uuname span {
    font-size: 20px;
    font-weight: 700;
    line-height: 70px;
}
.uuname a{
    font-size: 16px;
    line-height: 70px;
    padding-right: 20px;
}
.uuname span {
    padding: 0 12px;
}
.uuname a {
    float: right;
}
.complete {
    float: right;
    width: 64%;
    padding-right: 12px;
    /* position: relative;
    top: 50%;
    transform: translateY(-50%); */
}
.complete >>> .ivu-progress {
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
    font-size: 14px;
    font-weight: 500;
    overflow: hidden;
}
.sp div:last-child {
    width: 30%!important;
    text-align: right;
    padding-right: 12px;
}
</style>