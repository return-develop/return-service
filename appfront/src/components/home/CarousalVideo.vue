<template>
    <div class="father">
        <video id="video" controls="controls"  style="width:100%;height:16em">
            <source src="../../../static/img/v1.mp4" type="video/ogg" />
            <source src="../../../static/img/v1.mp4" type="video/mp4" />
        </video>
 
        <div id="poster" class="yourDiv" @click="play">
            <div class="div1"></div>
            <div class="div2">
                <Icon type="ios-play-outline" size="36"/>
            </div>
            <div class="div3">留学生回国怎么找工作，看这个就全懂了</div>
        </div>
    </div>
</template>
<script>
    export default {
        data () {
            return {
            }
        },
        methods: {
            play () {
                var video = document.getElementById("video");
                document.getElementById("poster").style.display = "none";
                video.play();
            }
        }

    }
</script>
<style>
.yourDiv {
 background-color: black;
 height:16em;
 /* background-image: url('../../../static/img/curry.jpg'); */
 background-size: contain;
 background-repeat: no-repeat;
 background-position: center;
  
 display:flex;
 flex-direction: column;
  
 position: absolute;
 top: 0px;
 left: 0px;
 width: 100%;
}
.div1, .div3{
    height: 3em;
}
.div2{
    height: 10em;
    display: flex;
    align-items: center;
    justify-content: center;
}
.div3{
    text-align: left;
    color:#d8d8d8;
    margin-left: 1em;
}
/* .yourDiv img { 
 width:20%;
 margin-left: 40%;
} */
 
.father {
 background-color: black;
 width:100%;
 height:16em;
 position: relative;
}
.father p{
    color: white;
}
</style>
