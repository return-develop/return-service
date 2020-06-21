<template>
    <div id="show-info">
        <div class="introduce" v-if="isShow">
            <div class="uname">
                <span>{{formTop.username}}·</span><span>{{formTop.sex}}</span>
                <a @click="isShow = false">编辑</a>
            </div>
            <div class="info">
                <li class="sp">{{formTop.school}}·{{formTop.major}}</li>
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
                username: '用户（未填）',
                realname:'',
                sex: '性别（未填）',
                school: '学校（未填）',
                major: '专业（未填）',
                education: '学历（未填）',
                goal: '目标（未填）',
                graduate_time: '毕业时间（未填）',
                city: '城市（未填）',
                birth:'',
                phone: '',
                email: '',
                hobby: '',
                prize: '',
                skill: ''
            },
           
        }
    },
    created() {
        this.formTop.email = this.getCookieValue("email")
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
    font-size: 1.1em;
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