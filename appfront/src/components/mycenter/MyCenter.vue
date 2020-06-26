<template>
    <div class="app">
        <div class="menu"><navigation :changeName="changeName"></navigation></div>
        <div class="container">
            <div class="items">
                <ul>
                    <li v-for="(tab,index) in tabs" @click="toggle(index,tab.view)" :class="{active:active==index}" class="li-item">
                    <Icon :type="tab.logo" style="padding-right: 10px;" />{{tab.type}}
                    </li>
                </ul>
            </div>
            <!--:is实现多个组件实现同一个挂载点-->
            <div class="item-content">
                <component :is="currentView" @getChangeName0="getChangeName0"></component>
            </div>
        </div>
    </div>
</template>
<script>
    import navigation from '../navigation'
    import MyInfo from './MyInfo'
    import ResetPassword from './ResetPassword'
    import LogOut from './LogOut'
    export default {
        components: {navigation, MyInfo, ResetPassword, LogOut},
        data () {
            return {
                active:0,
                currentView:'MyInfo',
                changeName: '',
                tabs:[
                    {
                        type:'个人信息',
                        view:'MyInfo',
                        logo:'md-person-add'
                    },
                    {
                        type:'修改密码',
                        view:'ResetPassword',
                        logo:'md-create'
                    },
                    {
                        type:'退出登录',
                        view:'LogOut',
                        logo:'md-power'
                    }
                ]
            }
        },
        methods: {
            toggle(i,v) {
                this.active=i;
                this.currentView=v;
            },
            getChangeName0(res) {
                // console.log("祖先" + res)
                this.changeName = res
            }
        }
    }
</script>
<style scoped>
    .container {
        display: flex;
    }
    .items {
        margin-left: 20vw;
        margin-top: 10em;
    }
    .items ul {
        list-style-type: none;
    }
    .items ul li {
        color: #9b9b9b;
        font-size: 16px;
        padding-bottom: 70px;
    }
    .items ul li:first-child {
        padding-bottom: 20px;
    }
    .items ul li.active{
        color: black;
    }
    .item-content {
        width: 40vw;
        margin-left: 3vw;
        margin-top: 10em;
    }
</style>