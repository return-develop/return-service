<template>
    <Tree :data="data4" show-checkbox multiple></Tree>
</template>
<script>
    export default {
        data () {
            return {
                data4: [
                    {
                        title: '全国',
                        expand: true,
                        children: [
                            {
                                title: '北京',
                            },
                            {
                                title: '杭州'
                            },
                            {
                                title: "深圳"
                            },
                            {
                                title: "上海"
                            },
                            {
                                title: '广州'
                            },
                            {
                                title: '其他城市',
                                children: [
                                    {
                                        title: '天津',
                                    },
                                    {
                                        title: '南京'
                                    },
                                    {
                                        title: "苏州"
                                    },
                                    {
                                        title: "成都"
                                    },
                                    {
                                        title: '济南'
                                    
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }
    }
</script>
