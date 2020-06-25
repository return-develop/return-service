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
    import { getCookieValue, deleteCookie } from '../../cookie/useCookie'
    export default {
        data () {
            return {
                modal1: true,
                username: ''
            }
        },
        created() {
            if (getCookieValue('login') == 'yes') {
                if (getCookieValue('username') == '') {
                    this.username = getCookieValue('email')
                } else {
                    this.username = getCookieValue('username')
                }
            }
            
        },
        methods: {
            ok () {
                deleteCookie('login', '/')
                deleteCookie('username', '/')
                if (getCookieValue("remember") !== 'yes') {
                    deleteCookie('remember', '/')
                }
                this.$Message.info('已退出');
                location.href = '/'
            },
            cancel () {
                this.$Message.info('Clicked cancel');
                location.href = '/mycenter'
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
