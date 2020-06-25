<template>
    <div class="app">
        <div class="menu"><navigation></navigation></div>
        <div class="container">
            <div class="content">
                <div class="info">
                    <div class="steps-title">
                        <div class="title">
                            <h2 class="title-h">归来</h2>
                            <p class="title-p">你的归国求职顾问</p>
                        </div>
                        <div class="steps">
                            <FillStep :changeCurrent="changeCurrent"></FillStep>
                        </div>
                    </div>
                    <div class="fill-info"><component :is="currentView" @getForm="getForm" @getCurrent="getCurrent"></component></div>
                    
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import navigation from '../navigation'
import FillStep from './FillStep'
import PersonInfo from './PersonInfo'
import DetailedInfo from './DetailedInfo'
import JobRequire from './JobRequire'
import FillComplete from './FillComplete'
import { addCookie, getCookieValue } from '../../cookie/useCookie'
import { fetchBase } from '../../post/fetchBase'
export default {
    components: {navigation, FillStep, PersonInfo, DetailedInfo, JobRequire, FillComplete},
    data() {
        return {
            changeCurrent: 0,
            currentView: 'PersonInfo',
            tabs:[
                    {
                        type:'填写个人信息',
                        view:'PersonInfo'
                    },
                    {
                        type:'完成详细信息',
                        view:'DetailedInfo'
                    },
                    {
                        type:'求职需求',
                        view:'JobRequire'
                    },
                    {
                        type:'已完成',
                        view:'FillComplete'
                    }
                ],
            formTop: {
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
            },

        }
    },
    // created() {
    //     this.formTop.email = addCookie("email")
    // },
    methods: {
        getForm(res) {
            console.log(res)
            for(var item in res) {
                this.formTop[item] = res[item]
            }
            console.log("这是")
            console.log(this.formTop)
        },
        async getCurrent(res) {
            if (res === 3) {
                this.changeCurrent = res
                this.formTop.email = getCookieValue('email')
                let res = await fetchBase('/user_update_info', {
                    content: this.formTop
                })
                console.log(res)
                if (res['flag'] === global_.CONSTGET.SUCCESS) {
                    
                } else {
                    this.$Message.warning('服务器错误')
                }
                return
            }
            console.log(this.tabs[res].view)
            this.changeCurrent = res
            this.currentView = this.tabs[res].view
        }
    }
}
</script>
<style scoped>
.app {
    width: 100%;
    height: 100%;
    min-height: 100vh;
    background-color: #d8d8d8;
}
.container {
    width: 100%;
    height: 90%;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #d8d8d8;
}
.content {
    width: 80%;
    height: 90%;
    margin-top: 6vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: white;
}
.info {
    width: 80%;
    margin: 4vh auto 6vh;
    height: 90%;
    display: flex;
}
.steps-title {
    width: 25%;
    height: 100%;
    min-height: 66vh;
}
.fill-info {
    width: 75%;
    height: 100%;
}
.title {
    height: 15%;
}
.title-h {
    margin: 0 auto 1vh;
}
.title-p {
    margin: 0 auto;
}
.steps {
    height: 85%;
    margin-top: 18vh;
}
</style>