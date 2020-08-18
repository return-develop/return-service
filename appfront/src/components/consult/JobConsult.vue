<template>
    <div class="app">
        <div class="menu"><navigation></navigation></div>
        <div class="container" v-if="isShow">
            <div class="introduce">
                <h1 style="text-align: center">名师1V1咨询</h1>
                <div class="introduce-title">
                    <span class="l-intro-title">【名师简介】</span>
                    <span class="r-intro-title">【学生口碑】</span>
                </div>
                <Divider />
                <div class="introduce-content">
                    <Row>
                        <Col v-for="item in counselor" :key=item.name span='8' class="content-style">
                            <div class="img-style"><img :src=item.url class="my-img-style"></div>
                            <div class="introduce-style">
                                <p style="color:black;font-size:20px;font-weight:bold;padding-bottom: 8px">{{item.name}}</p>
                                <p style="color:black">{{item.description}}</p>
                            </div>
                        </Col>
                    </Row>
                </div>
                <Divider />
            </div>
            <div class="course">
                <Tabs :value="displayTab">
                    <TabPane label="【快速预约】" name="tab1">
                        <div v-for="item in course" :key=item.name class="course-list">
                            <div class="course-item">
                                <div class="course-img"><img :src=item.url class="my-img-style"></div>
                                <div class="course-content">
                                    <div class="title-price">
                                        <div class="consult-title">{{item.title}}</div>
                                        <div class="consult-price">
                                            <p><span style="color:black;font-size:18px">{{item.price}}</span>{{item.unit}}</p>
                                            <p style="text-decoration:line-through">{{item.pre_price}}{{item.unit}}</p>
                                        </div>
                                    </div>
                                    <div class="check-time">
                                        <Button type="primary" style="width:fit-content;float:left" @click="viewOrderTime(item)">查看可约时间</Button>
                                        <Button type="primary" style="width:fit-content;margin-left:20px;float:left" v-if="item.isView" @click="onOrder(item)">{{item.date}}{{item.time}}</Button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </TabPane>
                    <TabPane label="【我的列表】" name="tab2">
                        <div class="my-list">
                            <div class="list-title">
                                <span>{{username}}</span>的预约列表
                            </div>
                            <div v-for="item in orderList" :key=item.phone class="order-list">
                                    <div class="consult-date">
                                        <span style="padding-right:2%">{{item.date}}</span>{{item.time}}
                                    </div>
                                    <div class="consult-operate">
                                        <a style="padding-right: 5%" @click="changeOrder(item)">更改预约</a><a @click="cancelOrder(item)">取消预约</a>
                                    </div>
                            </div>
                            <div v-for="item in orderCompleteList" :key=item.phone class="order-list">
                                    <div class="consult-complete-date">
                                        <span style="padding-right:2%">{{item.date}}</span>{{item.time}}
                                    </div>
                                    <div class="consult-complete-operate">
                                        <a style="padding-right: 5%" @click="viewCompleteOrder(item)">查看预约信息</a><a @click="deleteCompleteOrder(item)">删除</a>
                                    </div>
                            </div>
                            <div class="add-consult"><Icon type="ios-add-circle" size="24" style="padding-right:5px"/>新增预约</div>
                        </div>
                    </TabPane>
                </Tabs>
            </div>
            <Modal
                title="取消预约"
                v-model="modal"
                class-name="vertical-center-modal"
                @on-ok="ok"
                @on-cancel="cancel">
                <p>是否确认<span style="color: red;font-weight:800">取消</span>预约</p>
            </Modal>
        </div>
        <div class="order-consult" v-if="!isShow">
            <Breadcrumb class="my-crumb" separator=">>">
                <BreadcrumbItem to="/home">
                    <Icon type="ios-home-outline"></Icon> 首页
                </BreadcrumbItem>
                <BreadcrumbItem to="/job_consult">
                    <Icon type="logo-buffer"></Icon> 就业咨询
                </BreadcrumbItem>
                <BreadcrumbItem></BreadcrumbItem>
            </Breadcrumb>
            <div class="order-step">
                <div class="order-step-title">
                    预约信息
                </div>
                <div class="order-step-content">
                    <Form :label-width="120" class="order-step-content-form" :rules="ruleValidate" ref="order_info" :model="order_info" v-model="order_info">
                        <FormItem label="课程id（可选）" style="width: 100%;">
                            <Input v-model="order_info.courseId" placeholder="未填写课程id，将为您进行普通预约" :disabled="InputLimit.id" style="margin-left:20px">
                        </FormItem>
                        <FormItem label="上课平台" style="width: 100%;" prop="platform">
                            <RadioGroup v-model="order_info.platform" :disabled="InputLimit.platform" style="margin-left:20px">
                                <!-- <Radio label="wechat"><img src="../../../static/img/wechat.jpg" class="order-step-way"></Radio>
                                <Radio label="tencent"><img src="../../../static/img/tencent_meeting.jpg" class="order-step-way"></Radio>
                                <Radio label="feishu"><img src="../../../static/img/fly_book.jpg" class="order-step-way"></Radio> -->
                                <Radio label="wechat">微信</Radio>
                                <Radio label="feishu">飞书</Radio>
                                <Radio label="tencent">腾讯会议</Radio>
                            </RadioGroup>
                        </FormItem>
                        <FormItem label="所选平台账号" style="width: 100%;" prop="account">
                            <Input v-model="order_info.account" placeholder="为了方便联系您，请填写所选平台账号..." :disabled="InputLimit.account" style="margin-left:20px">
                        </FormItem>
                        <FormItem label="选择时间" style="width: 100%;" prop="date">
                            <DatePicker v-model="order_info.date" type="date" :disabled="InputLimit.date" style="margin-left:20px"></DatePicker>
                        </FormItem>
                        <FormItem label="预约时段" style="width: 100%;" prop="time">
                            <RadioGroup v-model="order_info.time" :disabled="InputLimit.time" style="margin-left:20px">
                                <Radio label="上午" :disabled="InputLimit.time">上午</Radio>
                                <Radio label="下午" :disabled="InputLimit.time">下午</Radio>
                            </RadioGroup>
                        </FormItem>
                        <FormItem style="width: 100%;" v-if="ifDisplayButton">
                            <Button type="primary" @click.native="submitOrder" style="margin-left:20px">{{orderType}}</Button>
                            <Button style="margin-left: 20px" @click.native="cancelSubmit">取消更改</Button>
                        </FormItem>
                    </Form>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import global_ from '../Const'
import navigation from '../navigation'
import { addCookie, getCookieValue, deleteCookie } from '../../cookie/useCookie'
export default {
    components: {navigation},
    data() {
        return {
            username: '',
            displayTab: "tab1",
            isShow: true,   //咨询页，预约页切换
            modal: false,  //是否显示取消预约询问
            ifDisplayButton: true,  //是否显示按钮（用户查看已完成预约时设置为不显示）
            orderType: '确认预约',
            oldOrderInfo: {},   //用于存储需要更改的预约列表
            // isView: false,  //用户查看预约时间
            InputLimit: {  //是否禁用
                id: true,
                platform: false,
                account: false,
                date: false,
                time: false
            },
            counselor: [
                {
                    url: '../../../static/img/curry.jpg',
                    name: '刘允向',
                    description: '本科毕业于南开大学经济学，硕士毕业于麻省理工学院经济系，曾担任学生会主席，'
                },
                {
                    url: '../../../static/img/logo.jpg',
                    name: '张阿三',
                    description: '本科毕业于南开大学经济学，硕士毕业于麻省理工学院经济系，曾担任学生会主席，'
                },
                {
                    url: '../../../static/img/curry.jpg',
                    name: '王老五',
                    description: '本科毕业于南开大学经济学，硕士毕业于麻省理工学院经济系，曾担任学生会主席，'
                }
            ],
            course: [
                {
                    courseId: '1111',
                    url: '../../../static/img/curry.jpg',
                    title: '体验式免费咨询',
                    price: '0.00',
                    unit: '元/课时',
                    pre_price: '99.99',
                    date: '2020-07-20',
                    time: '上午',
                    isView: false
                },
                {
                    courseId: '2222',
                    url: '../../../static/img/curry.jpg',
                    title: '体验式免费咨询',
                    price: '0.00',
                    unit: '元/课时',
                    pre_price: '99.99',
                    date: '2020-07-20',
                    time: '上午',
                    isView: false
                },
                {
                    courseId: '1234',
                    url: '../../../static/img/curry.jpg',
                    title: '体验式免费咨询',
                    price: '0.00',
                    unit: '元/课时',
                    pre_price: '99.99',
                    date: '2020-07-20',
                    time: '上午',
                    isView: false
                }
            ],
            orderList: [
                {
                    courseId: '',
                    platform: 'feishu',
                    account: "12345679",
                    date: '2020-06-29',
                    time: '上午'
                },
                {
                    courseId: '',
                    platform: 'wechat',
                    account: "12345678",
                    date: '2020-06-30',
                    time: '上午'
                },
                {
                    courseId: '',     
                    platform: 'tencent',
                    account: "12345679",
                    date: '2020-7-1',
                    time: '上午'
                }
            ],
            orderCompleteList: [
                {
                    date: '2020-06-01',
                    time: '上午',
                    way: '飞书',
                    phone: "12345678"
                },
                {
                    date: '2019-06-01',
                    time: '上午',
                    way: '飞书',
                    phone: "12345678"
                }
            ],
            order_info: {
                courseId: '',
                platform: '',
                account: '',
                date: '',
                time: '',
            },
            ruleValidate: {
                    platform: [
                        { required: true, message: '不能为空', trigger: 'change' }
                    ],
                    account: [
                        { required: true, message: '不能为空', trigger: 'blur' }
                    ],
                    date: [
                        { required: true, type: 'date', message: '不能为空', trigger: 'change' }
                    ],
                    time: [
                        { required: true, message: '不能为空', trigger: 'change' }
                    ]
            },
            infoValid: false,
        }
    },
    created() {
        if (getCookieValue('login') ==  'yes') {
            var name = getCookieValue('username')
            if (name != '') {
                this.username = name
            } else {
                this.username = getCookieValue('email')
            }
        } else {
            this.username = '未登录'
            this.$Message.warning("您还未登录，即将为您跳转到登录界面")
            setTimeout(function () {
              window.location.href = '/user_login'
            },2000)
        }
    },
    methods: {
        resetForm(info) {
            for (var item in info) {
                info[item] = ''
            }
        },
        resetInputLimit() {
            this.InputLimit.courseId = true
            this.InputLimit.platform = false
            this.InputLimit.account = false
            this.InputLimit.date = false
            this.InputLimit.time = false
        },
        submitOrder() {
            console.log("这是order")
            console.log(this.order_info)
            // console.log("写改后" + this.formTop.birthday)
            // console.log(this.formTop)
            this.$refs['order_info'].validate((valid) => {
                if (valid) {
                    this.infoValid = true;
                } else {
                    this.$Message.error('填完必选项哦！');
                }
            })
            if(this.infoValid == true) {
                var d = new Date(this.order_info.date);
                this.order_info.date = d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate()
                // email = getCookieValue()
                // let res = await fetchBase('/order_info', {
                //         content: this.order_info
                //     })
                // // console.log(res)
                // if (res['flag'] === global_.CONSTGET.SUCCESS) {
                //     this.$Message.success("预约成功")
                // } else if (res['flag'] === global_.CONSTGET.FAIL) {
                //     this.$Message.error("预约失败")
                // }
                this.$Message.success("预约成功")
                if (this.orderType === '更改预约') { 
                    var isChange = false
                    for (var item in this.order_info) {
                        if (this.oldOrderInfo[item] != this.order_info[item]) {
                            isChange = true
                            break
                        }
                    }
                    if (isChange) {
                        for (var item in this.orderList) {
                            console.log(this.orderList[item])
                            if (JSON.stringify(this.oldOrderInfo) == JSON.stringify(this.orderList[item])) {
                                this.orderList.splice(item, 1)
                            }
                        }
                    }
                    this.orderType = '确认预约'
                }
                setTimeout(function () {  
                }, 1000)
                var newOrderInfo = {}
                for (var item in this.order_info) {
                    newOrderInfo[item] = this.order_info[item]
                }
                this.orderList.push(newOrderInfo)
                this.isShow = true
                this.resetForm(this.order_info)
                this.resetForm(this.oldOrderInfo)
                this.resetInputLimit()
                // this.$refs['order_info'].resetFields()
                console.log(this.order_info)
            }
            
        },
        cancelSubmit() {
            this.resetForm(this.order_info)
            this.resetForm(this.oldOrderInfo)
            this.resetInputLimit()
            this.isShow = true
        },
        viewOrderTime(item) {  
            item.isView = true
        },
        onOrder(item) {
            this.order_info.date = item.date
            this.order_info.time = item.time
            this.order_info.courseId = item.courseId
            if (item.courseId != '') {
                this.InputLimit.date = true
                this.InputLimit.time = true
            }
            this.isShow = false
            this.ifDisplayButton = true
            this.orderType = '确认预约'
            this.displayTab = 'tab2'
        },
        changeOrder(info) {
            for (var item in info) {
                this.order_info[item] = info[item]
                this.oldOrderInfo[item] = info[item]
            }
            if (info.courseId != '') {
                this.InputLimit.date = true
                this.InputLimit.time = true
            }
            console.log(this.order_info)
            this.isShow = false
            this.ifDisplayButton = true
            this.orderType = '更改预约'
            // console.log(this.orderList[0])
            // console.log(this.orderList[1])
            // console.log(this.orderList[2])
            // console.log(JSON.stringify(this.orderList[0]) == JSON.stringify(this.orderList[1]))
            // console.log(JSON.stringify(this.orderList[0]) == JSON.stringify(this.orderList[2]))
        },
        cancelOrder(info) {
            this.modal = true
            for (var item in info) {
                this.oldOrderInfo[item] = info[item]
            }
        },
        ok() {
            for (var item in this.orderList) {
                if (JSON.stringify(this.oldOrderInfo) == JSON.stringify(this.orderList[item])) {
                    this.orderList.splice(item, 1)
                }
            }
            this.resetForm(this.oldOrderInfo)
            this.modal = false
        },
        cancel() {
            this.resetForm(this.oldOrderInfo)
            this.modal = false
        },
        viewCompleteOrder(info) {
            for (var item in info) {
                this.order_info[item] = info[item]
            }
            for (var item in this.InputLimit) {
                this.InputLimit[item] = true
            }
            this.isShow = false
            this.ifDisplayButton = false
        },
        deleteCompleteOrder(info) {
            for (var item in this.orderCompleteList) {
                if (JSON.stringify(info) == JSON.stringify(this.orderCompleteList[item])) {
                    this.orderCompleteList.splice(item, 1)
                }
            }
        }
    }
}
</script>
<style scoped>
.app {
    width: 100%;
    height: 100%;
    min-height: 100vh;
    /* background: url('../../../static/img/bgImg1.jpg');
    background-size: cover;    								
	background-repeat: no-repeat;
    opacity: 0.5; */
    background-color: #d8d8d8;
    /* background-image: linear-gradient(#d8d8d8, #575c5c); */
}
.introduce {
    width: 84vw;
    height: 30%;
    margin: 6vh auto 0;
    /* background-color: yellow; */
}
.course {
    width: 50%;
    height: 70%;
    margin: 0 auto;
    text-align: center;
    /* background-color: green; */
}
.introduce-title {
    width: 100%;
    margin: 2vh 0;
}
.l-intro-title {
    font-size: 18px;
    color: black;
    float: left;
}
.r-intro-title {
    font-size: 18px;
    color: black;
    float: right;
}
.content-style {
    display: flex;
    justify-content: center;
    align-items: center;
    /* min-width: 300px; */
}
.img-style {
    width: 30%;
}
.introduce-style {
    width: 70%;
    padding: 0 1vw;
}
.my-img-style{
    width: 100%;
    height: 100%;
}
.course >>> .ivu-tabs-nav-scroll {
    display: inline-block;
}
.course >>> .ivu-tabs-tab {
    font-size: 18px;
}
.course-list {
    width: 100%;
    height: fit-content;
    margin: 4vh 0;
}
.course-item {
    display: flex;
    width: 100%;
    height: 120px;
    background-color: white;
    padding: 10px;
}
.course-img {
    width: 30%;
    max-width: 120px;
    height: 100%;
}
.course-content {
    width: 100%;
    height: 100%;
    padding: 0 10px;
}
.title-price {
    display: flex;
    width: 100%;
    height: 60%;
}
.consult-title {
    width: 50%;
    height: 100%;
    line-height: 50px;
    font-size: 16px;
    font-weight: 600;
    color: #000;
    text-align: left;
}
.consult-price {
    width: 50%;
    height: 100%;
    text-align: right;
}
.check-time {
    width: 100%;
}
.my-list {
    width: 100%;
    height: fit-content;
    min-height: 400px;
    background-color: white;
    /* border: 1px solid #755c5c; */
}
.list-title {
    width: 100%;
    height: 50px;
    background-color:#755c5c;
    color: white;
    line-height: 50px;
}
.list-title span {
    padding: 0 5px;
    font-size: 18px;
    font-weight: 600;
    color: #2db7f5;
}
.order-list {
    width: 98%;
    height: 40px;
    margin: 1vh auto;
    border-radius: 10px;
    display: flex;
    background-color: #d8d8d8;
}
.consult-date {
    width: 50%;
    height: 100%;
    text-align: left;
    line-height: 40px;
    padding-left: 2%;
    color: black;
}
.consult-operate {
    width: 50%;
    height: 100%;
    text-align: right;
    line-height: 40px;
    padding-right: 2%;
}
.consult-operate a:last-child {
    color: red;
}
.consult-complete-date {
    width: 50%;
    height: 100%;
    text-align: left;
    line-height: 40px;
    padding-left: 2%;
}
.consult-complete-operate {
    width: 50%;
    height: 100%;
    text-align: right;
    line-height: 40px;
    padding-right: 2%;
}
.consult-complete-operate a:last-child {
    color: red;
}
.add-consult {
    margin-top: 5%;
    font-size: 18px;
    color: black;
}
.order-consult {
    width: 84%;
    height: auto;
    margin: 5vh auto 0;
    /* background-color: white; */
}
.order-consult >>> .ivu-breadcrumb a {
    color: black;
}
.order-consult >>> .ivu-breadcrumb-item-separator {
    color: black;
}
.order-step {
    width: 80%;
    height: auto;
    margin: 6vh auto 0;
    background-color: white;
}
.order-step-title {
    width: 100%;
    height: 50px;
    background-color: #575c5c;
    color: white;
    padding-left: 20px;
    font-size: 16px;
    line-height: 50px;
}
.order-step-content {
    width: 80%;
    min-height: 300px;
    height: auto;
    margin: 50px auto 0;
}
.order-step-way {
    width: 30px;
    height: 30px;
    border-radius: 10px;
}
.order-step-content-form {
    width: 70%;
    margin: 0 auto;
    padding-bottom: 30px;
}
.order-consult >>> .ivu-form-item-error-tip {
    margin-left: 20px;
}
.vertical-center-modal {
    /* margin-top: 20vh; */
    display: flex;
    align-items: center;
    justify-content: center;
}
/* .order-step-content >>> .ivu-select-dropdown {
    width: 100%;
}
.order-step-content >>> .ivu-date-picker-cells {
    margin: 10px auto;
}
.order-step-content >>> .ivu-picker-panel-body {
    float: none;
} */
</style>