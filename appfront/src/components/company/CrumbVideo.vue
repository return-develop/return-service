<template>
    <div class="crumb-video">
        <Breadcrumb class="my-crumb" separator=">>">
            <BreadcrumbItem to="/home">
                <Icon type="ios-home-outline"></Icon> 首页
            </BreadcrumbItem>
            <BreadcrumbItem to="/company">
                <Icon type="logo-buffer"></Icon> 所有企业招聘
            </BreadcrumbItem>
            <BreadcrumbItem></BreadcrumbItem>
        </Breadcrumb>
        <Input search v-model="searchContent" placeholder="  关键词搜一搜，如：腾讯" class="my-search" @on-search="myShow"></Input>
        <Button shape="circle" icon="ios-play-outline" size="20" class="v-btn">查看新手教程</Button>
        <!-- <div class="v-btn">
            <Icon type="md-arrow-dropright-circle" size="24" />
            <span>观看新手教程</span>
        </div> -->
    </div>
</template>
<script>
    // import eventBus from '../eventBus.js'
    export default {
        data () {
            return {
                searchContent: ''
            }
        },
        methods: {
            myShow () {
                //向父组件提交用户检索的内容
                this.$emit('getContent', this.searchContent)
            }
        }
    }
</script>
<style scoped>
    .crumb-video {
        width: 100%;
    }
    .my-crumb {
        float: left;
        margin-top: 10px;
        width: 16vw;
    }
    .my-search {
        width: 16vw;
        margin-left: 42vw;
        float: left;
        margin-top: 4px;
    }
    .my-search >>> .ivu-input {
        height: 36px;
        font-size: 14px;
        border: 1px solid #d7d7d7;
        border-radius: 20px;
    }
    .v-btn {
        float: right;
        width: 8vw;
        height: 40px;
        border-radius: 20px;
        background-color: #272727;
        color: white;
        border: 0;
        font-size: 13px;
    }
    .v-btn span {
        padding-left: 5px;
    }
</style>