<template>
    <div class="logout">
        <Modal
            v-model="modal1"
            title="退出登录"
            @on-ok="ok"
            @on-cancel="cancel">
            <p>尊敬的<span>{{username}}</span>用户</p>
            <p>是否确认<b>退出</b>？</p>
        </Modal>
    </div>
</template>
<script>
    export default {
        data () {
            return {
                modal1: true,
                username: '黄德军'
            }
        },
        methods: {
            ok () {
                this.$Message.info('已退出');
                location.href = '/'
            },
            cancel () {
                this.$Message.info('Clicked cancel');
                location.href = '/mycenter'
            }
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
