<template>
    <List item-layout="vertical" border>
        <ListItem v-for="item in data.slice(0, 5)" :key="item.title">
            <ListItemMeta :avatar="item.avatar" :title="item.title" />
            <!-- {{ item.content }} -->
            <div class="job-list">
                <div class="jobList1">
                    <li v-for="item in job.slice(0,3)">{{item.name}}</li>
                </div>
                <div class="jobList2">
                    <li v-for="item in job.slice(3,6)">{{item.name}}</li>
                </div>
                <div class="workplace">工作地点：<br><span>深圳，北京，杭州</span></div>
            <div>
            <!-- <template slot="extra">
                <img src="https://dev-file.view-designui.com/5wxHCQMUyrauMCGSVEYVxHR5JmvS7DpH/large" style="width: 280px">
            </template> -->
        </ListItem>
    </List>
</template>
<script>
    export default {
        data () {
            return {
                data: [
                    {
                        title: '腾讯公司',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: '字节跳动',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: '阿里巴巴',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'aaa',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'bbb',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'ccc',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'ddd',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'eee',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'ffff',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'hhhh',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: '字节跳动',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: '阿里巴巴',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: '腾讯公司',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: '字节跳动',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: '阿里巴巴',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    }
                ],
                job: [
                    {name: '前端开发'},
                    {name: '后端开发'},
                    {name: '产品经理'},
                    {name: '销售顾问'},
                    {name: '软件测试工程师'},
                    {name: '游戏工程师'},
                    {name: '哈哈哈哈'}
                ]
            }
        }
    }
</script>
<style>
.ivu-avatar{
    border-radius: 0!important;
}
.ivu-list-item-meta-title{
    margin-top: 0px;
    margin-bottom: 0px;
    /* position: relative; */
    top: 50%; /*偏移*/
    transform: translateY(50%);
}
.ivu-list-item{
    border: 1px solid #dcdee2;
    margin-top: 20px;
    border-radius: 4px;
    padding-left: 0!important;
    padding-right: 0!important;
    padding-top: 0;
    padding-bottom: 12px;
}
.ivu-list-item-meta{
    width: 100%;
    height: 50px;
    background-color: #d7d7d7
}
.ivu-list-item-meta-avatar{
    line-height: 50px;
    margin-left: 12px;
}
.ivu-list-bordered{
    border: 0px;
}
.job-list{
    display: flex;
    margin-left: 62px;
}
.jobList1,.jobList2{
    /* padding-left: 12px; */
    font-size: 0.9em;
    font-weight: 600;
    width: 33%;
}
.workplace{
    padding-left: 62px;
    font-size: 0.9em;
    font-weight: 600;
    width: 33%;
}
.workplace span{
    font-size: 0.8em;
    font-weight: 500;
}
.jobList1 li, .jobList2 li, .workplace li{
    margin-bottom: 3px;
}
</style>
