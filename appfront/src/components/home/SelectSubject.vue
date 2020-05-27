<template>
    <Tree :data="data4" show-checkbox multiple></Tree>
</template>
<script>
    export default {
        data () {
            return {
                data4: [
                    {
                        title: '航天技术',
                        expand: false,
                        // selected: true,
                        children: [
                            {
                                title: '空气动力学',
                            },
                            {
                                title: '航空学'
                            },
                            {
                                title: "航天技术"
                            },
                                {
                                title: "航空电子学"
                            }
                        ]
                    },
                    {
                        title: '城市/建筑学',
                        expand: false,
                        children: [
                            {
                                title: '土木工程',
                                // checked: true
                            },
                            {
                                title: '城市管理'
                            }
                        ]
                    },
                    {
                        title: '电子科技',
                        expand: false,
                        children: [
                            {
                                title: '计算机科学',
                                // checked: true
                            },
                            {
                                title: '软件工程'
                            }
                        ]
                    },
                    {
                        title: '化学加工',
                        expand: false,
                        children: [
                            {
                                title: '化学分析',
                                // checked: true
                            },
                            {
                                title: '材料工程'
                            }
                        ]
                    }
                ]
            }
        }
    }
</script>
