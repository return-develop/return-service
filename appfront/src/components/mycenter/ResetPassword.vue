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
            form: {
                password: '',
                password1: '',
                password2: ''
            },
            ruleInline: {
                password: [
                    { required: true, message: '不能为空', trigger: 'blur' },
                    { type: 'string', min: 6, message: '不能少于6位', trigger: 'blur' }
                ],
                password1: [
                    { required: true, message: '不能为空', trigger: 'blur' },
                    { type: 'string', min: 6, message: '不能少于6位', trigger: 'blur' }
                ],
                password2: [
                    { required: true, message: '不能为空', trigger: 'blur' },
                    { type: 'string', min: 6, message: '不能少于6位', trigger: 'blur' }
                ]
            }
        }
    },
    methods: {
        submit() {
            this.$refs['form'].validate((valid) => {
                if (valid) {
                    this.$Message.success('修改成功');
                } else {
                    this.$Message.error('Fail!');
                }
            })
        },
        cancel() {
            this.form.password = ''
            this.form.password1 = ''
            this.form.password2 = ''
            this.$Message.success('已取消');
        }
    }
}
</script>
<style scoped>
.reset-pwd >>> .ivu-form-item-label{
    font-size: 14px;
    font-weight: 600;
}
.reset-pwd {
    width:80%;
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