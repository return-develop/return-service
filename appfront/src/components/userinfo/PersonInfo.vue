<template>
<div class="content-info">
    <div class="person-info">
        <div class="job-note">
            我们共计已提供全国：
        </div>
        <div class="job-display">
            <div class="l-display">
                <div class="center-display">
                    <span>{{jobNum}}</span>个<br>
                    <p>岗位信息</p>
                </div>
            </div>
            <div class="r-display">
                <div class="center-display">
                    <span>{{companyNum}}</span>家<br>
                    <p>岗位信息</p>
                </div>
            </div>
        </div>
        <div class="require-note">
            完善你的求职需求，剩下的交给我们
        </div>
        <Divider />
        <Form :model="formTop" label-position="top" class="detail" ref="formTop" v-model="formTop" :rules="ruleValidate">
            <FormItem>
                <Row>
                    <Col span="11">
                        <FormItem label="用户名" prop="username">
                            <Input v-model="formTop.username" maxlength="8" >
                        </FormItem>
                    </Col>   
                    <Col span="11" offset="2">
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
                        <FormItem label="手机号" prop="phone">
                            <Input v-model="formTop.phone" maxlength="11" >
                        </FormItem>
                    </Col>    
                    <Col span="11" offset="2">
                        <FormItem label="出生日期">
                            <DatePicker type="date" v-model="formTop.birthday" style="width:100%;"></DatePicker>
                            
                        </FormItem>
                    </Col>
                </Row>
            </FormItem>
            <FormItem >
                <Row>
                    <Col span="11">
                        <FormItem label="毕业院校" prop="school">
                            <Input v-model="formTop.school" >
                        </FormItem>
                    </Col>
                    <Col span="11" offset="2">
                        <FormItem label="专业" prop="major">
                            <Select v-model="formTop.major" :placeholder="major" >
                                <Option v-for="item in job" :value="item.name">{{item.name}}</Option>
                            </Select>
                        </FormItem>
                    </Col>        
                </Row>   
            </FormItem>
            <FormItem label="最高学历" prop="education">
                <Select v-model="formTop.education" :placeholder="education">
                    <Option value="高中">高中</Option>
                    <Option value="本科">本科</Option>
                    <Option value="硕士">硕士</Option>
                    <Option value="博士">博士</Option>
                    <Option value="博士后">博士后</Option>
                </Select>
            </FormItem>
            <Button type="primary" @click="submit" class="btn">下一步，完善详细信息</Button>
        </Form>
    </div>
    <div class="result-info">
        <div class="result-note">我们需要了解你的基础信息，来为你匹配合适的企业和岗位</div>
    </div>
</div>
</template>
<script>
import { addCookie } from '../../cookie/useCookie'
export default {
    data() {
        return {
            jobNum: 17289,
            companyNum: 468,
            formTop: {
                username: '',
                sex: '',
                school: '',
                major: '',
                education: '',
                birthday:'',
                phone: '',
            },
            ruleValidate: {
                    username: [
                        { required: true, message: '不能为空', trigger: 'blur' }
                    ],
                    sex: [
                        { required: true, message: '不能为空', trigger: 'change' }
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
    methods: {
        submit() { 
            var d = new Date(this.formTop.birthday);
            this.formTop.birthday = d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate()
            // console.log("写改后" + this.formTop.birthday)
            // console.log(this.formTop)
            this.$refs['formTop'].validate((valid) => {
                if (valid) {
                    console.log("填写成功")
                    console.log(this.formTop)
                    addCookie('username', this.formTop.username, 30, '/')
                    this.$emit("getForm", this.formTop)
                    this.$emit("getCurrent", 1)
                } else {
                    this.$Message.warning("请填完必选项哦")
                    return
                }
            })
            document.documentElement.scrollTop = document.body.scrollTop = 0;
        },
    }
}
</script>
<style scoped>
.content-info {
    width: 100%;
    height: 100%;
    display: flex;
}
.person-info {
    width: 70%;
    height: 100%;
}
.result-info {
    width: 30%;
    height: 100%;
    min-height: 60vh;
}
.job-note{
    margin-bottom: 2vh;
    text-align: center;
    font-size: 1em;
    font-weight: 400;
    color: black;
}
.job-display{
    display: flex;
    height: 5em;
    color: white;
}
.l-display, .r-display{
    height: 100%;
    width: 48%;
    display: table;
    text-align: center;
    background-color: #755c5c;
    border-radius: 3px;
}
.r-display{
    margin-left: 4%;
}
.center-display{
    display: table-cell;
    vertical-align: middle;
}
.l-display span, .r-display span{
    font-size: 1.8em;
}
.l-display label, .r-display label{
    font-size: 0.9em;
}
.require-note {
    margin-top: 2vh;
    margin-bottom: 3vh;
    text-align: center;
    font-size: 16px;
    color: grey;
}
.detail >>> .ivu-form-item-label{
    font-size: 15px;
    font-weight: 600;
}
.btn {
    width: 100%;
    text-align: center;
}
.result-info {
    display: flex;
    align-items: center;
    justify-content: center;
}
.result-note {
    color: grey;
    border: 1px dashed #d8d8d8;
    width: 80%;
    margin: auto;
    font-size: 14px;
    padding: 1em;
}
</style>