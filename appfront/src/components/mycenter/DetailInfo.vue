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
                    <FormItem label="性别" prop="sex">
                        <RadioGroup v-model="formTop.sex">
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
                    <FormItem label="姓名" prop="realname">
                        <Input v-model="formTop.realname" class="myinput">
                    </FormItem>
                </Col>
                <Col span="11">
                    <FormItem label="上传头像">
                        <Upload action="../../../static/img">
                            <Button icon="ios-cloud-upload-outline">上传头像</Button>
                        </Upload>
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
                    <FormItem label="出生日期">
                        <DatePicker type="date" v-model="formTop.birth" class="myinput"></DatePicker>
                    </FormItem>
                </Col>
            </Row>
        </FormItem>
        <FormItem >
            <Row>
                <Col span="11">
                    <FormItem label="电子邮箱" prop="email">
                        <Input v-model="formTop.email" readonly="readonly" class="myinput">
                    </FormItem>
                </Col>
                <Col span="11">
                    <FormItem label="毕业院校" prop="school">
                        <Input v-model="formTop.school" class="school">
                    </FormItem>
                </Col>    
            </Row>
            
        </FormItem>
        <FormItem>
            <Row>
                <Col span="11">
                    <FormItem label="专业" prop="major">
                        <Select v-model="formTop.major" :placeholder="major" class="myinput">
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
            <Input v-model="formTop.hobby" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder class="school">
        </FormItem>
        <FormItem label="获奖情况" >
            <Input v-model="formTop.prize" type="textarea" :autosize="{minRows: 2,maxRows: 5}" class="school">
        </FormItem>
        <FormItem label="职业技能证书" >
            <Input v-model="formTop.skill" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder class="school">
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
    props: ["sendForm"],
    data () {
        return{
            infoValid: false,
            formTemp:{
                username: '用户（未填）',
                realname:'',
                sex: '性别（未填）',
                school: '学校（未填）',
                major: '专业（未填）',
                education: '学历（未填）',
                goal: '目标（未填）',
                graduate_time: '毕业时间（未填）',
                city: '城市（未填）',
                birth:'',
                phone: '',
                email: '',
                hobby: '',
                prize: '',
                skill: ''
            },
            formTop: {
                username: '用户（未填）',
                realname:'',
                sex: '性别（未填）',
                school: '学校（未填）',
                major: '专业（未填）',
                education: '学历（未填）',
                goal: '目标（未填）',
                graduate_time: '毕业时间（未填）',
                city: '城市（未填）',
                birth:'',
                phone: '',
                email: '',
                hobby: '',
                prize: '',
                skill: ''
            },
            ruleValidate: {
                    username: [
                        { required: true, message: '不能为空', trigger: 'blur' }
                    ],
                    sex: [
                        { required: true, message: '不能为空', trigger: 'change' }
                    ],
                    realname: [
                        { required: true, message: '不能为空', trigger: 'blur' }
                    ],
                    email: [
                        { required: true, message: '不能为空', trigger: 'blur' },
                        { type: 'email', message: '邮箱格式错误', trigger: 'blur' }
                    ],
                    phone: [
                        { required: true, message: '不能为空', trigger: 'blur' }
                    ],
                    major: [
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
    created() {
        console.log(this.sendForm)
        for (var item in this.sendForm) {
            this.formTop[item] = this.sendForm[item]
        }
    },
    methods: {
        async submit() { 
            this.$refs['formTop'].validate((valid) => {
                if (valid) {
                    this.infoValid = true;
                } else {
                    // this.$Message.error('失败');
                }
            })
            if (this.infoValid == true) {
                let res = await this.fetchBase('/user_update_info', {
                    content: this.formTop
                })
                if (res['flag'] === global_.CONSTGET.SUCCESS) {
                    this.$Message.success('保存成功');
                    console.log("保存成功了");
                    this.infoValid = false
                } else if (res['flag'] === global_.CONSTGET.FAIL) {
                    this.$Message.error('保存失败')
                    this.infoValid = false
                }
            }
        },
        cancel() {
            this.formTop = JSON.parse(JSON.stringify(this.formTemp))
        },
        fetchBase (url, body) {
            return fetch(url, {
            method: 'post',
            credentials: 'same-origin',
            headers: {
                'X-CSRFToken': this.getCookie('csrftoken'),
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
            })
            .then((res) => res.json())
        },
        getCookie (cName) {
            if (document.cookie.length > 0) {
                let cStart = document.cookie.indexOf(cName + '=')
                if (cStart !== -1) {
                    cStart = cStart + cName.length + 1
                    let cEnd = document.cookie.indexOf(';', cStart)
                    if (cEnd === -1) {
                    cEnd = document.cookie.length
                    }
                    return unescape(document.cookie.substring(cStart, cEnd))
                }
            }
            return ''
        },
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
    width:60%
}
</style>