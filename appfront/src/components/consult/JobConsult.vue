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
                <Tabs value="name1">
                    <TabPane label="【快速预约】" name="name1">
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
                                        <Button type="primary" style="width:fit-content;float:left">查看可约时间</Button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </TabPane>
                    <TabPane label="【我的列表】" name="name2">
                        <div class="my-list">
                            <div class="list-title">
                                <span>{{username}}</span>的预约列表
                            </div>
                            <div v-for="item in orderList" :key=item.phone class="order-list">
                                    <div class="consult-date">
                                        <span style="padding-right:2%">{{item.date}}</span>{{item.time}}
                                    </div>
                                    <div class="consult-operate">
                                        <a style="padding-right: 5%">更改预约</a><a>取消预约</a>
                                    </div>
                            </div>
                            <div v-for="item in orderCompleteList" :key=item.phone class="order-list">
                                    <div class="consult-complete-date">
                                        <span style="padding-right:2%">{{item.date}}</span>{{item.time}}
                                    </div>
                                    <div class="consult-complete-operate">
                                        <a style="padding-right: 5%">查看预约信息</a><a>删除</a>
                                    </div>
                            </div>
                            <div class="add-consult"><Icon type="ios-add-circle" size="24" style="padding-right:5px"/>新增预约</div>
                        </div>
                    </TabPane>
                </Tabs>
            </div>
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
                    <Form :label-width="100" class="order-step-content-form">
                        <FormItem label="上课平台" style="width: 100%;">
                            <RadioGroup v-model="order_info.radio" style="margin-left:20px">
                                <!-- <Radio label="wechat"><img src="../../../static/img/wechat.jpg" class="order-step-way"></Radio>
                                <Radio label="tencent"><img src="../../../static/img/tencent_meeting.jpg" class="order-step-way"></Radio>
                                <Radio label="feishu"><img src="../../../static/img/fly_book.jpg" class="order-step-way"></Radio> -->
                                <Radio label="wechat">微信</Radio>
                                <Radio label="tencent">飞书</Radio>
                                <Radio label="feishu">腾讯会议</Radio>
                            </RadioGroup>
                        </FormItem>
                        <FormItem label="所选平台账号" style="width: 100%;">
                            <Input v-model="order_info.account" placeholder="为了方便联系您，请填写所选平台账号..." style="margin-left:20px">
                        </FormItem>
                        <FormItem label="选择时间" style="width: 100%;">
                            <DatePicker v-model="order_info.date" type="date" style="margin-left:20px"></DatePicker>
                        </FormItem>
                        <FormItem label="预约时段" style="width: 100%;">
                            <RadioGroup v-model="order_info.time" style="margin-left:20px">
                                <Radio label="上午">上午</Radio>
                                <Radio label="下午">下午</Radio>
                            </RadioGroup>
                        </FormItem>
                        <FormItem style="width: 100%;">
                            <Button type="primary" @click.native="submitOrder" style="margin-left:20px">确认预约</Button>
                            <Button style="margin-left: 20px" @click.native="cancelOrder">取消预约</Button>
                        </FormItem>
                    </Form>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import navigation from '../navigation'
import { addCookie, getCookieValue, deleteCookie } from '../../cookie/useCookie'
export default {
    components: {navigation},
    data() {
        return {
            username: '',
            isShow: false,
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
                    url: '../../../static/img/curry.jpg',
                    title: '体验式免费咨询',
                    price: '0.00',
                    unit: '元/课时',
                    pre_price: '99.99'
                },
                {
                    url: '../../../static/img/curry.jpg',
                    title: '体验式免费咨询',
                    price: '0.00',
                    unit: '元/课时',
                    pre_price: '99.99'
                },
                {
                    url: '../../../static/img/curry.jpg',
                    title: '体验式免费咨询',
                    price: '0.00',
                    unit: '元/课时',
                    pre_price: '99.99'
                }
            ],
            orderList: [
                {
                    date: '2020-06-28',
                    time: '上午',
                    way: '飞书',
                    phone: "12345678"
                },
                 {
                    date: '2020-06-28',
                    time: '上午',
                    way: '飞书',
                    phone: "12345678"
                },
                 {
                    date: '2020-06-28',
                    time: '上午',
                    way: '飞书',
                    phone: "12345678"
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
                radio: 'wechat',
                account: '',
                date: "",
                time: '',
            }
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
        submitOrder() {

        },
        cancelOrder() {
            
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
    border: 1px solid #755c5c;
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
    margin-left: 20px;
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