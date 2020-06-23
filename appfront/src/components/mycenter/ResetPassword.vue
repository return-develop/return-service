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
            this.$refs['form'].validate((valid) => {
                if (valid) {
                    this.infoValid = true;
                } else {
                    this.$Message.error('修改失败');
                }
                if ( this.password1 != this.password2) {
                    this.$Message.warning("两次密码不同")
                    return
                }
                if (this.infoValid == true) {
                    let res = await this.fetchBase('/reset_password', {
                        "email": this.getCookieValue("email"),
                        "oldPwd": this.password,
                        "newPwd": this.password1
                    })
                    // console.log(res)
                    if (res['flag'] === global_.CONSTGET.SUCCESS) {
                        this.$Message.success('修改成功');
                        this.addCookie("password", this.password1, 7, '/')
                    } else if (res['flag'] === global_.CONSTGET.FAIL) {
                        if (res['message'] === "password wrong") {
                            this.$Message.error("原密码错误")
                        } else {
                            this.$Message.error("修改失败")
                        }
                        
                    }
                }
            })
        },
        cancel() {
            this.form.password = ''
            this.form.password1 = ''
            this.form.password2 = ''
            this.$Message.success('已取消');
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
        addCookie(name,value,days,path){  /**添加设置cookie**/
            var name = escape(name);
            var value = escape(value);
            var expires = new Date();
            expires.setTime(expires.getTime() + days * 3600000 * 24);
            //path=/，表示cookie能在整个网站下使用，path=/temp，表示cookie只能在temp目录下使用
            path = path == "" ? "" : ";path=" + path;
            //GMT(Greenwich Mean Time)是格林尼治平时，现在的标准时间，协调世界时是UTC
            //参数days只能是数字型
            var _expires = (typeof days) == "string" ? "" : ";expires=" + expires.toUTCString();
            document.cookie = name + "=" + value + _expires + path;
        },
        getCookieValue(name){ /**获取cookie的值，根据cookie的键获取值**/
            //用处理字符串的方式查找到key对应value
            var name = escape(name);
            //读cookie属性，这将返回文档的所有cookie
            var allcookies = document.cookie;
            //查找名为name的cookie的开始位置
            name += "=";
            var pos = allcookies.indexOf(name);
            //如果找到了具有该名字的cookie，那么提取并使用它的值
            if (pos != -1){                       //如果pos值为-1则说明搜索"version="失败
            var start = pos + name.length;         //cookie值开始的位置
            var end = allcookies.indexOf(";",start);    //从cookie值开始的位置起搜索第一个";"的位置,即cookie值结尾的位置
            if (end == -1) end = allcookies.length;    //如果end值为-1说明cookie列表里只有一个cookie
            var value = allcookies.substring(start,end); //提取cookie的值
            return unescape(value);              //对它解码
            }else{ //搜索失败，返回空字符串
            return "";
            }
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