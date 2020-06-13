<template>
<div>
    <div class="result-sum">
        <div class="l-result-sum">为你找到<span class="select-sum">{{dataCount}}</span>条结果</div>
        <div class="r-result-sum">
            <Dropdown>
                <Icon type="ios-list-box-outline" size="24"/><span>{{getSum}}/16</span>
                <DropdownMenu slot="list">
                    <DropdownItem><a href='/' style="color:#272727">去定制企业清单</a></DropdownItem>
                    <DropdownItem><a href='/' style="color:#272727">去定制企业清单</a></DropdownItem>
                </DropdownMenu>
            </Dropdown>
        </div>
    </div>
    <List item-layout="vertical" border>
        <ListItem v-for="item in historyData" :key="item.title">
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
        <Page
          :total="dataCount"
          :page-size="pageSize"
          show-total
          @on-change="changepage"
          show-elevator
          class="page"
          v-if="!showFail"
        ></Page>
    </List> 
    <div class="fail-search" v-if="showFail">
        <Icon type="ios-outlet-outline" size="24"/>
        <span>很遗憾，没有找到!</span>
    </div>
</div>
</template>
<script>
    
    export default {
        props: {
            saveSum: {
            type: Number,
            default: 0
            },
            letter: {
                type:String,
                default: ''
            }
        },
        data () {
            return {
                ajaxHistoryData: [],
                exportdata: [],
                // 初始化信息总条数
                dataCount: 0,
                getSum: 0,
                searchCompany: '',
                // 每页显示多少条
                pageSize: 10,
                historyData: [],
                selectData: [],
                showFail: false,
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
                        title: 'jjj',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'kkk',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'lll',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'mmm',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'nnn',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: '腾讯-公司',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: '字节-跳动',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: '阿里-巴巴',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'aa-a',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'bb-b',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'cc-c',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'dd-d',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'ee-e',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'fff-f',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'hhh-h',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'jjj-',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'kk-k',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'll-l',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'mm-m',
                        description: 'This is description, this is description, this is description.',
                        avatar: '../../../static/img/curry.jpg',
                        content: 'This is the content, this is the content, this is the content, this is the content.'
                    },
                    {
                        title: 'nn-n',
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
                ],
                tempData: [],
                tempDict: {}
            }
        },
        created () {
            this.selectData = this.data
            this.exportdata = this.data
            this.getSum = this.saveSum;
            this.showList(this.selectData)
            // this.$emit('showTotal', this.dataCount)
        },
        watch: {
            // letter(cur) {
            //     console.log("子组件"+cur)
            //     let content = cur
            //     if (content.trim() == ''){
            //         this.showList(this.data)
            //     }
            //     else{
            //         this.showList(this.selectData.splice(0, 15))
            //     }
            // },
            letter: function(n) {//箭头函数  不然会发生this改变
                console.log("子组件"+ n)
                let content = n
                if (content.trim() == ''){
                    console.log("子组件"+ '111')
                    this.showList(this.data)
                } else {
                    this.tempData = []
                    for (var item in this.data){
                        console.log('1777'+ this.data[item])
                        if(this.data[item].title){
                            if (this.data[item].title.search(n) != -1) {
                                this.tempDict['title'] = this.data[item].title
                                this.tempDict['avatar'] = this.data[item].avatar
                                this.tempData.push(this.tempDict)
                                this.tempDict = {}
                            }
                        }
                    }
                    if (this.tempData.length == 0) {
                        this.showFail = true;
                    } else {
                        this.showFail = false;
                    }
                    this.showList(this.tempData)
                    this.tempData = []
                }
            }
        },
        methods: {
            changepage(index) {
                var _start = (index - 1) * this.pageSize;
                var _end = index * this.pageSize;
                this.historyData = this.ajaxHistoryData.slice(_start, _end);
                document.documentElement.scrollTop = document.body.scrollTop = 0;
            },
            showList(data) {
                this.ajaxHistoryData = data;
                this.exportdata = data;
                this.dataCount = data.length; //this.ajaxHistoryData.length;//vm.ajaxHistoryData;
                // 初始化显示，小于每页显示条数，全显，大于每页显示条数，取前每页条数显示
                if (this.dataCount < this.pageSize) {
                    this.historyData = this.ajaxHistoryData;
                } else {
                    this.historyData = this.ajaxHistoryData.slice(0, this.pageSize);
                }
                console.log(this.historyData)
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
.page {
    margin: 20px auto;
}
.result-sum{
        width: 100%;
        height: 50px;
        background-color: #755c5c;
        color: white;
}
.l-result-sum {
    float: left;
    padding-left: 12px;
    height: 50px;
    line-height: 50px;
}
.r-result-sum {
    float: right;
    padding-right: 12px;
    height: 50px;
    line-height: 50px;
}
.select-sum {
    color: red;
}  
.result-sum span {
    padding: 0 5px;
}
.fail-search{
    font-size: 18px;
    text-align: center;
    margin-top: 16vh;
}
</style>