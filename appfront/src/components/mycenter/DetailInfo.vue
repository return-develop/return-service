<template>
    <!-- <div class="detail">
        <div class="info-type">用户名</div>
        <div class="my-input"><input placeholder="username" type="text"></div>
        <div class="name-date">
            <div class="name">
                <div class="info-type">姓名</div>
                <div class="my-input"><input  placeholder="name" type="text"></div>
            </div>
            <div class="date">
                <div class="info-type">出生日期</div>
                <div class="date-input">
                    <input  placeholder="birth_year" type="text">
                    <span>年</span>
                    <input  placeholder="birth_month" type="text">
                    <span>月</span>
                    <input  placeholder="birth_day" type="text">
                    <span>日</span>
                </div>
            </div>
        </div>
        <div class="phone-mail">
            <div class="phone">
                <div class="info-type">手机号（推荐填写）</div>
                <div class="pm-input"><input  placeholder="phone" type="text"></div>
            </div>
            <div class="date">
                <div class="info-type">电子邮箱</div>
                <div class="pm-input">
                    <input  placeholder="email" type="text">
                </div>
            </div>
        </div>
        <div class="school">
            <div class="info-type">毕业院校</div>
            <div class="s-input"><input  placeholder="school" type="text"></div>
        </div>
        <div class="professional-education">
            <div class="professional">
                <div class="info-type">专业</div>
                <div class="pe-input"><input  placeholder="professional" type="text"></div>
            </div>
            <div class="education">
                <div class="info-type">最高学历</div>
                <div class="pe-input">
                    <input  placeholder="education" type="text">
                </div>
            </div>
        </div>
        <div class="interest">
            <div class="info-type">兴趣爱好</div>
            <div class="else-input"><textarea  placeholder="interest" type="text"></div>
        </div>
        <div class="award">
            <div class="info-type">获奖情况</div>
            <div class="else-input"><textarea  placeholder="award" type="text"></div>
        </div>
        <div class="certificate">
            <div class="info-type">职业技能证书</div>
            <div class="else-input"><textarea placeholder="certificate" type="text"></div>
        </div>
    </div> -->
    <Form :model="formTop" label-position="top" class="detail" ref="formTop" v-model="formTop" :rules="ruleValidate">
        <FormItem>
            <Row>
                <Col span="11">
                    <FormItem label="用户名" prop="username">
                        <Input v-model="formTop.username" class="myinput">
                    </FormItem>
                </Col>    
                <Col span="11">
                    <FormItem label="性别" prop="gender">
                        <RadioGroup v-model="formTop.gender">
                            <Radio label="男">男</Radio>
                            <Radio label="女">女</Radio>
                        </RadioGroup>
                    </FormItem>
                </Col>
            </Row>
            
        </FormItem>
        <FormItem>
            <Row>
                <Col span="11">
                    <FormItem label="姓名" prop="name">
                        <Input v-model="formTop.name" class="myinput">
                    </FormItem>
                </Col>
                <Col span="11">
                    <FormItem label="出生日期">
                        <DatePicker type="date" v-model="formTop.birth" class="myinput"></DatePicker>
                    </FormItem>
                </Col>
            </Row>
        </FormItem>
        <FormItem>
            <Row>
                <Col span="11">
                    <FormItem label="手机号" prop="phone">
                        <Input v-model="formTop.phone" class="myinput">
                    </FormItem>
                </Col>    
                <Col span="11">
                    <FormItem label="电子邮箱" prop="email">
                        <Input v-model="formTop.email" class="myinput">
                    </FormItem>
                </Col>
            </Row>
        </FormItem>
        <FormItem label="毕业院校" prop="school">
            <Input v-model="formTop.school" class="school">
        </FormItem>
        <FormItem>
            <Row>
                <Col span="11">
                    <FormItem label="专业" prop="professional">
                        <Select v-model="formTop.professional" :placeholder="professional" class="myinput">
                            <Option v-for="item in job" :value="item.name">{{item.name}}</Option>
                        </Select>
                    </FormItem>
                </Col>    
                <Col span="11">
                    <FormItem label="最高学历" prop="education">
                         <Select v-model="formTop.education" :placeholder="education" class="myinput">
                            <Option value="高中">高中</Option>
                            <Option value="本科">本科</Option>
                            <Option value="硕士">硕士</Option>
                            <Option value="博士">博士</Option>
                            <Option value="博士后">博士后</Option>
                        </Select>
                    </FormItem>
                </Col>
            </Row>
        </FormItem>
        <FormItem label="兴趣爱好" >
            <Input v-model="formTop.interest" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder class="school">
        </FormItem>
        <FormItem label="获奖情况" >
            <Input v-model="formTop.award" type="textarea" :autosize="{minRows: 2,maxRows: 5}" class="school">
        </FormItem>
        <FormItem label="职业技能证书" >
            <Input v-model="formTop.certificate" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder class="school">
        </FormItem>
        <FormItem>
            <Button type="primary" @click.native="submit">保存</Button>
            <Button style="margin-left: 16px" @click.native="cancel">取消</Button>
        </FormItem>
</Form>
</template>
<script>
import global_ from '../Const'
export default {
    data () {
        return{
            formTemp:{
                username: '黄德军',
                name:'黄德军',
                gender: '',
                school: '南开大学',
                professional: '软件工程',
                education: '硕士',
                goal: '寻找实习',
                graduate_time: '2022年6月毕业',
                city: '北京',
                birth:'1995-10-21',
                phone: "18722492209",
                email: "2120190512@mail.nankai.edu.cn",
                interest: '唱歌，跳舞，打球',
                award: '2019年软件学院软件之星称号',
                certificate: "cet4"
            },
            formTop: {
                username: '黄德军',
                name:'黄德军',
                gender: '',
                school: '南开大学',
                professional: '软件工程',
                education: '硕士',
                goal: '寻找实习',
                graduate_time: '2022年6月毕业',
                city: '北京',
                birth:'1995-10-21',
                phone: "18722492209",
                email: "2120190512@mail.nankai.edu.cn",
                interest: '唱歌，跳舞，打球',
                award: '2019年软件学院软件之星称号',
                certificate: "cet4"
            },
            ruleValidate: {
                    username: [
                        { required: true, message: '不能为空', trigger: 'blur' }
                    ],
                    gender: [
                        { required: true, message: '不能为空', trigger: 'change' }
                    ],
                    name: [
                        { required: true, message: '不能为空', trigger: 'blur' }
                    ],
                    email: [
                        { required: true, message: '不能为空', trigger: 'blur' },
                        { type: 'email', message: '邮箱格式错误', trigger: 'blur' }
                    ],
                    phone: [
                        { required: true, message: '不能为空', trigger: 'blur' }
                    ],
                    professional: [
                        { required: true, message: '不能为空', trigger: 'change' }
                    ],
                    education: [
                        { required: true, message: '不能为空', trigger: 'change' }
                    ],
                    school: [
                        { required: true, message: '不能为空', trigger: 'change' }
                    ]
                },
            job: [
                    {name: '哲学'},
                    {name: '经济学'},
                    {name: '法学'},
                    {name: '教育学'},
                    {name: '文学'},
                    {name: '历史学'},
                    {name: '数学'},
                    {name: '物理学'},
                    {name: '声学'},
                    {name: '光学'},
                    {name: '化学'},
                    {name: '天文学'},
                    {name: '地理学'},
                    {name: '气象学'},
                    {name: '海洋科学'},
                    {name: '地质学 '},
                    {name: '生物学'},
                    {name: '机械工程'},
                    {name: '车辆工程'},
                    {name: '材料科学与工程'},
                    {name: '冶金工程'},
                    {name: '电气工程'},
                    {name: '信息与通信工程'},
                    {name: '计算机科学'},
                    {name: '软件工程'},
                    {name: '物联网工程'},
                    {name: '控制科学与工程'},
                    {name: '林业工程'},
                    {name: '环境科学与工程'},
                    {name: '生物医学工程'},
                    {name: '食品科学与工程'},
                    {name: '农学'},
                    {name: '林学'},
                    {name: '基础医学'},
                    {name: '临床医学'},
                    {name: '工商管理'},
                    {name: '会计学'},
                    {name: '旅游管理'},
                    {name: '行政管理'},
                    {name: '社会学'}
                ]
        }
    },
    methods: {
        submit() { 
            this.$refs['formTop'].validate((valid) => {
                if (valid) {
                    this.$Message.success('保存成功');
                    console.log('2222')
                    // let res = this.fetchBase('/api/user/signup/', {
                    // content: this.formTop//有可能出错
                    // })
                    // this.reset()
                    // if (res['flag'] === global_.CONSTGET.SUCCESS) {
                    // this.$Message.success('保存成功');
                    // } else if (res['flag'] === global_.CONSTGET.FAILED) {
                    // this.$Message.error('保存失败')
                    // }
                } else {
                    // this.$Message.error('失败');
                }
            })
        },
        cancel() {
            this.formTop = JSON.parse(JSON.stringify(this.formTemp))
        },
        // fetchBase (url, body) {
        //     return fetch(url, {
        //     method: 'post',
        //     credentials: 'same-origin',
        //     headers: {
        //         'X-CSRFToken': this.getCookie('csrftoken'),
        //         'Accept': 'application/json',
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify(body)
        //     })
        //     .then((res) => res.json())
        // },
        // getCookie (cName) {
        //     if (document.cookie.length > 0) {
        //         let cStart = document.cookie.indexOf(cName + '=')
        //         if (cStart !== -1) {
        //             cStart = cStart + cName.length + 1
        //             let cEnd = document.cookie.indexOf(';', cStart)
        //             if (cEnd === -1) {
        //             cEnd = document.cookie.length
        //             }
        //             return unescape(document.cookie.substring(cStart, cEnd))
        //         }
        //     }
        //     return ''
        // },
    }
}
</script>
<style scoped>
.detail >>> .ivu-form-item-label{
    font-size: 15px;
    font-weight: 600;
}
.myinput {
    width:60%;
}
.school{
    width:74%
}
</style>