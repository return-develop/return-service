<template>
    <div class="reset-pwd">
        <Form ref="form" :model="form" :rules="ruleInline" class="myform">
            <FormItem label="当前密码" prop="password">
                <Input type="text" v-model="form.password" >
            </FormItem>
            <FormItem label="新密码" prop="password1">
                <Input type="password" v-model="form.password1" >
            </FormItem>
            <FormItem label="确认密码" prop="password2">
                <Input type="password" v-model="form.password2" >
            </FormItem>
            <FormItem>
                <Row type="flex" justify="end">
                    <Col span="4">
                        <FormItem>
                            <Button type="primary" @click="submit">确认</Button>
                        </FormItem>
                    </Col>    
                    <Col span="3">
                        <FormItem>
                            <Button @click="cancel">取消</Button>
                        </FormItem>
                    </Col>
                </Row>
            </FormItem>
        </Form>
    </div>
</template>
<script>
import global_ from '../Const' 
import { addCookie, getCookieValue } from '../../cookie/useCookie'
export default {
    data () {
        return {
            infoValid: false,
            form: {
                password: '',
                password1: '',
                password2: ''
            },
            ruleInline: {
                password: [
                    { required: true, message: '不能为空', trigger: 'blur' },
                    { type: 'string', min: 8, message: '不能少于8位', trigger: 'blur' }
                ],
                password1: [
                    { required: true, message: '不能为空', trigger: 'blur' },
                    { type: 'string', min: 8, message: '不能少于8位', trigger: 'blur' }
                ],
                password2: [
                    { required: true, message: '不能为空', trigger: 'blur' },
                    { type: 'string', min: 8, message: '不能少于8位', trigger: 'blur' }
                ]
            }
        }
    },
    methods: {
        async submit() {
            if ( this.form.password1 !== this.form.password2) {
                this.$Message.warning("两次密码不同")
                return
            }
            this.$refs['form'].validate((valid) => {
                if (valid) {
                    this.infoValid = true;
                } else {
                    this.$Message.error('修改失败');
                }
            })
            if (this.infoValid == true) {
                let res = await this.fetchBase('/user_update_password', {
                    "email": getCookieValue("email"),
                    "oldPwd": this.form.password,
                    "newPwd": this.form.password1
                })
                // console.log(res)
                if (res['flag'] === global_.CONSTGET.SUCCESS) {
                    this.$Message.success('修改成功');
                    addCookie("password", this.form.password1, 7, '/')
                    this.reset()
                } else if (res['flag'] === "password wrong") {
                    this.$Message.error("原密码错误")
                } else if (res['flag'] === global_.CONSTGET.FAIL) {
                    this.$Message.error("修改失败")
                }
                this.infoValid = false
            }
        },
        cancel() {
            this.reset()
            this.$Message.success('已取消');
        },
        reset() {
            this.form.password = ''
            this.form.password1 = ''
            this.form.password2 = ''
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
.reset-pwd >>> .ivu-form-item-label{
    font-size: 14px;
    font-weight: 600;
}
.reset-pwd {
    width:100%;
    border: 1px solid #FDF5E6;
    border-radius: 0.5rem;
}
.myform{
    width:80%;
    margin-top:2em;
    margin-left: auto;
    margin-right: auto;
}
.mybtn {
    display: right;
}
</style>  