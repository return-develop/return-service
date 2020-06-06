<template>
    <div id="show-info">
        <div class="introduce" v-if="isShow">
            <div class="uname">
                <span>{{formTop.username}}·</span><span>{{formTop.sex}}</span>
                <a @click="isShow = false">编辑</a>
            </div>
            <div class="info">
                <li class="sp">{{formTop.school}}·{{formTop.professional}}</li>
                <li class="gg">{{formTop.goal}}·{{formTop.graduate_time}}</li>
                <li class="dc">期望工作地点：{{formTop.city}}</li>
            </div>
        </div>
        <div v-if="!isShow" class="detail-info"><DetailInfo></DetailInfo></div>
    </div>
</template>
<script>
import DetailInfo from './DetailInfo'
export default {
    components:{DetailInfo},
    data () {
        return {
            isShow: true,
            formTop: {
                username: '黄德军',
                name:'黄德军',
                gender: '',
                school: '南开大学',
                professional: '软件工程',
                education: '硕士',
                goal: '寻找实习',
                graduate_time: '2022年6月毕业',
                city: '北京',
                birth:'1995-10-21',
                phone: "18722492209",
                email: "2120190512@mail.nankai.edu.cn",
                interest: '唱歌，跳舞，打球',
                award: '2019年软件学院软件之星称号',
                certificate: "cet4"
            },
           
        }
    },
    methods: {
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
.uname span:first-child {
    padding-left: 12px;
}
.uname a {
    float: right;
}
.info {
    margin-left: 12px;
    list-style-type:none;
    color:black;
    font-size: 1.2em;
    font-weight: 600;
}
.sp {
    padding-bottom: .5em;
    padding-top: .5em;
}
.gg{
    padding-bottom: 1em;
}
.dc{
    padding-bottom: .5em;
}
</style>