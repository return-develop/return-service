<template>
<div class="my-step">
    <Steps :current=current direction="vertical">
        <Step title="完善个人信息" icon="ios-person"></Step>
        <Step title="完善详细信息" icon="ios-person-add"></Step>
        <Step title="求职需求" icon="md-bookmark"></Step>
        <Step title="完成职位筛选" icon="ios-checkmark-circle-outline"></Step>
    </Steps>
</div>
</template>
<script>
    export default {
        props: {
            changeCurrent: {
                type:Number,
                default: 0
            }
        },
        data() {
            return {
                current: 0,

            }
        },
        watch: {
        changeCurrent: function(n) {
            // console.log("收到了" + n)
                this.current = n
            }
        }
        
    }
</script>
<style scoped>
.my-step {
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>