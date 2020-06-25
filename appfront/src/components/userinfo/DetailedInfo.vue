<template>
     <div class="content-info">
        <div class="person-info">
            <p class="add-title">平时有哪些兴趣爱好？(可选)</p>
            <Form>
                <FormItem >
                    <Input v-model="hobby" type="textarea" :autosize="{minRows: 3,maxRows: 5}" placeholder class="my-input">
                </FormItem>
            </Form>
            <p class="add-title title-style">在校期间，有无获奖情况？(可选)</p>
            <Form>
                <FormItem >
                    <Input v-model="prize" type="textarea" :autosize="{minRows: 5,maxRows: 10}" placeholder class="my-input">
                </FormItem>
            </Form>
            <p class="add-title title-style">是否有获得职业技能证书？(可选)</p>
            <Form>
                <FormItem >
                    <Input v-model="skill" type="textarea" :autosize="{minRows: 5,maxRows: 10}" placeholder class="my-input">
                </FormItem>
            </Form>
            <Button type="primary" @click="submit" class="btn">完成职位筛选</Button>
        </div>
        <div class="result-info">
            <div class="result-note">个性化的履历有助于我们帮你提供更加匹配的职位信息</div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            hobby: '',
            prize: '',
            skill: ''
        }
    },
    methods: {
        submit() {
            var dic = {}
            dic['hobby'] = this.hobby
            dic['prize'] = this.prize
            dic['skill'] = this.skill
            this.$emit("getForm", dic)
            this.$emit("getCurrent", 2)
            console.log(dic)
        }
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
    min-height: 66vh;
    margin-top: 6vh;
}
.result-info {
    width: 30%;
    height: 100%;
    min-height: 66vh;
}
.add-title {
    color:black;
}
.title-style {
    margin-top: 5vh;
}
.my-input {
    width: 100%;
}
.btn {
    margin-top: 5vh;
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