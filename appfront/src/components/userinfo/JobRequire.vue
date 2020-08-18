<template>
    <div class="content-info">
        <div class="person-info">
            <p class="add-title">以下职位方向，有哪些是你比较感兴趣的？<span class="add-warning" v-if="isWarning">(您最多选择四项！)</span></p>
            <div class="add-content">
                <Row>
                    <Col v-for="(value, index) in select_job" span="4">
                        <div class="save-style" @click="deleteJob(value)">
                            <Icon type="md-remove" style="float: left; padding-left: 5px; padding-top: 1px;color:red;font-weight:1000;font-size:16px"/>
                            {{value}}
                        </div>
                    </Col>
                </Row>
            </div>
            <div class="add-select">
                <Row style="margin-top:0.5vh">
                    <Col v-for="(value, index) in job" span="4">
                        <div class="item-style" @click="addJob(value)">
                            <Icon type="md-add" style="float: left; padding-left: 5px; padding-top: 1px;color:blue;font-weight:blod;font-size:16px" />
                            {{value}}
                        </div>
                    </Col>
                </Row>
            </div>
            <p class="add-title title-style">你希望寻找哪个城市的岗位呢？</p>
            <Form>
                <FormItem prop="education">
                    <Select multiple @input="limitcount" v-model="select_city">
                        <Option v-for="(item,index) in cities" :value = "item">{{item}}</Option>
                    </Select>
                </FormItem>
            </Form>
            <p class="add-title title-style">期望薪酬是？</p>
            <div class="add-content">
                <Row>
                    <Col v-for="(value, index) in select_salary" span="4">
                        <div class="save-style" @click="deleteSalary(value)">
                            <Icon type="md-remove" style="float: left; padding-left: 5px; padding-top: 1px;color:red;font-weight:1000;font-size:16px"/>
                            {{value}}
                        </div>
                    </Col>
                </Row>
            </div>
            <div class="add-select">
                <Row style="margin-top:0.5vh">
                    <Col v-for="(value, index) in salary" span="4">
                        <div class="item-style" @click="addSalary(value)">
                            <Icon type="md-add" style="float: left; padding-left: 5px; padding-top: 1px;color:blue;font-weight:blod;font-size:16px" />
                            {{value}}
                        </div>
                    </Col>
                </Row>
            </div>
            <Button type="primary" @click="submit" class="btn">完成职位筛选</Button>
        </div>
        <div class="result-info">
            <div class="result-note">你的筛选项越多，最终的岗位越少，也越精准</div>
        </div>
        <Modal
            title="筛选完成!"
            v-model="modal"
            class-name="vertical-center-modal"
            @on-ok="ok"
            @on-cancel="cancel">
            <p>已为你准备好已筛选的岗位,去“<span style="color: black;font-weight:800;font-size:16px">定制企业清单</span>”查看结果？</p>
        </Modal>
    </div>
</template>
<script>
export default {
    data() {
        return {
            isWarning: false, //最多添加4项
            job: ['经营管理',"市场营销",'贸易业务','人力资源','文职类','新闻传媒',
            '互联网','电子通讯','机械类','建筑规划','房地产','金融经济',
            '设计策划','物流交通','咨询顾问','化工生物','文化教育','医疗卫生'
            ],
            select_job:[],
            cities: [
                '北京','上海','广州','深圳','杭州','天津','成都','重庆','南京','苏州','武汉','合肥','济南','西安',
                '沈阳','大连','长春','哈尔滨','郑州','呼和浩特','昆明','南昌','贵阳','南宁','东莞','福州','厦门','三亚'
            ],
            select_city:[],
            salary: [
                '不限','5k以下','5k-10k','10k-20k','20k以上'
            ],
            select_salary: [],
            modal: false
        }
    },
    methods: {
        addJob(name) {
            if (this.select_job.length >= 4) {
                this.isWarning = true
            } else {
                this.job.forEach(function(item, index, arr) {
                    if(item == name) {
                        arr.splice(index, 1);
                    }
                });
                this.select_job.push(name)
                this.isWarning = false
                // console.log(this.job)
                // console.log(this.select_job)
            }
        },
        deleteJob(name) {
            this.select_job.forEach(function(item, index, arr) {
                if(item == name) {
                    arr.splice(index, 1);
                }
            });
            this.job.push(name)
            this.isWarning  = false
        },
        limitcount(e) {
            if (e.length > 3) {
                this.$Message.warning('最多选3项哦');
                // console.log("pop前" + this.select_city)
                this.select_city.pop()
            }
        },
        addSalary(name) {
            if (this.select_salary.length >=1) {
                return
            } else {
                this.salary.forEach(function(item, index, arr) {
                    if (item == name) {
                        arr.splice(index, 1)
                    }
                });
                this.select_salary.push(name)
            }
        },
        deleteSalary(name) {
            this.select_salary.forEach(function(item, index, arr) {
                if(item == name) {
                    arr.splice(index, 1);
                }
            });
            this.salary.push(name)
        },
        submit() {
            if (this.select_job.length == 0 || this.select_city.length == 0 || this.select_salary.length == 0) {
                this.$Message.warning("还有选项没填写哦")
                return
            }
            var dic = {}
            dic['goal'] = this.select_job
            dic['city'] = this.select_city
            dic['salary'] = this.select_salary
            this.$emit("getForm", dic)
            this.$emit("getCurrent", 3)
            this.modal = true
        },
        ok() {
            window.location.href = '/'
        },
        cancel() {
            window.location.href = '/home'
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
.add-warning {
    color: red;
    padding-left: 1em;
}
.add-content {
    width: 100%;
    height: 50px;
    background-color: #d8d8d8;
    border-radius: 2px;
}
.add-select {
    width: 100%;
    height: 110px;
}
.item-style {
    border:2px solid grey;
    border-radius: 10px;
    margin: 2px 5px;
    text-align: center;
    font-size: 13px;
}
.save-style {
    border:2px solid grey;
    border-radius: 10px;
    margin: 12px 5px 0;
    text-align: center;
    font-size: 13px;
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
.vertical-center-modal{
    /* margin-top: 20vh; */
    display: flex;
    align-items: center;
    justify-content: center;
}
/* .content-info >>> .ivu-modal-header-inner {
    font-size: 16px;
}
.content-info >>> .ivu-modal-body {
    font-size: 14px;
    text-align: center;
} */
</style>