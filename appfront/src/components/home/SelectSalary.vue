<template>
    <Tree :data="data4" show-checkbox multiple></Tree>
</template>
<script>
    export default {
        data () {
            return {
                data4: [
                    {
                        title: '不限'
                    },
                    {
                        title: '2K以下'
                    },
                    {
                        title: '2K-5K'
                    },
                    {
                        title: '5K-10K'
                    },
                    {
                        title: '10K-20K'
                    },
                    {
                        title: '20K以上'
                    }
                ]
            }
        }
    }
</script>
