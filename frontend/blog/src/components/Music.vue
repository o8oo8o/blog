<template>
      <li class="nav-item dropdown show">
        <a class="nav-link" data-toggle="dropdown" href="#" aria-expanded="true">
          <i class="far fa-pause-circle"></i>
        </a>
        <div v-if="none_music">
          <div class="dropdown-menu dropdown-menu-right" style="margin-right: -1px; width: 280px;">
            <span class="dropdown-item dropdown-header">没有音乐!</span>
          </div>
        </div>
        <div v-else >
          <div @click.stop="function(e){e.target.style.backgroundColor = 'aliceblue'}" id="music_body" class="dropdown-menu dropdown-menu-right" style="width: 280px;">
            <!-- dropdown-menu 的默认样式有问题,点击的时候会改变背景,所以使用了上面的方法 -->
            <span class="dropdown-item" style="background-color: aliceblue;">
                <div class="text-center">
                  <div v-if="load_finish">
                    <audio @ended="play_end" @loadedmetadata="update_metadata" @timeupdate="update_progress" id="player" ref="player"  preload="metadata" >
                      <source :src="current_music.path" id="source" type="audio/mp3" />
                    </audio>
                  </div>
                  <div  class="btn-group" style="width: 100%;">
                    <button @click.stop="play_prev" type="button" class="btn btn-default">
                      <i class="fas fa-angle-double-left" title="上一曲"></i>
                    </button>
                    <button @click.stop="play_control"  type="button" class="btn btn-default"><span v-html="control"></span></button>
                    <button @click.stop="play_next" type="button" class="btn btn-default">
                      <i class="fas fa-angle-double-right" title="下一曲"></i>
                    </button>
                    <button @click.stop="play_mode" type="button" class="btn btn-default"><span v-html="mode"></span></button>
                  </div>
                </div>
                
                <!-- ###################### -->
                  <span style="margin-right: 65%;" class="text-muted">
                      <span v-text="played_time"></span>     
                  </span>
                  <span class="text-muted">
                      <span v-text="duration"></span>
                  </span>
                  <div class="input-group" >
                    <input v-model="played_percentage" @input="update_played" type="range" class="custom-range" id="progress"  min="0" max="1" step="0.01" />
                  </div>
                  <div class="input-group" style="margin-top: 3%;">
                    <span @click.stop="play_muted" v-html="volume_icon" style="margin-right: 5%; cursor:pointer"></span>
                    <input v-model="play_volume" @input="update_volume" style="width: 85%;" type="range" id="volume"  min="0" max="1" step="0.001" />
                  </div>               
                <!-- ###################### -->

                <div class="input-group input-group-sm" >
                  <input type="text" v-model.trim="search_name" name="table_search" class="form-control float-right" placeholder="歌曲搜索">
                </div>

            </span>
            
            <!-- ========================================== -->
            <div class="card">
                <div class="card-body table-responsive p-0" style="height: 250px;">
                  <table class="table table-sm  table-condensed table-hover text-nowrap">
                    <tbody>
                      <tr v-for="(item, index) in music_list" :key="index" @click.stop="play_current(index,item)">
                        <td v-if="item.name === current_music.name" class="bg-primary disabled color-palette">
                          <i class="fas fa-play"></i>&nbsp;
                          <span v-text="item.name"></span>
                        </td>
                        <td v-else class="text-muted">
                          <i>•</i>&nbsp;
                          <span v-text="item.name"></span>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
            </div>
            <!-- ========================================== -->
            <span class="text-muted dropdown-footer" style="padding-bottom: 0px; padding-top: 0px;">共有<b v-text="count"></b>首音乐</span>
          </div>
        </div>

      </li>
</template>

<script>
import axios from "axios";

export default {
  name: "Music",
  mounted(){
    var that = this;
    //axios.defaults.headers.common["Content-Type"] = "audio/mp3";
    axios.get(`/api/open/music/`)
      .then(function(response) {
          var data = response.data;
          if (data.code != 0) {
              console.log("/api/open/music/,服务端错误");
          }
          if (data.code == 0) {
              if(data.count > 0){
                // 音乐数量大于0
                that.music_list = data.music_list;
                that.music_list_backup = data.music_list;
                that.count = data.count;
                that.current_music = data.music_list[0];
                that.load_finish = true;
              }else{
                that.none_music = true;
              }
          }
      }).catch(function(error) {
          console.log("/api/open/music/,请求异常");
      })
  },
  data() {
    return {
      load_finish: false,
      count: 0,
      music_list: [],
      music_list_backup:[],
      current_music: {name:"",path:""},
      index: 0,
      control:'<i class="fas fa-circle" title="暂停"></i>',
      mode:'<i class="fas fa-exchange-alt" title="顺序播放"></i>',
      volume_icon: '<i class="fas fa-volume-up"></i>',
      order:true,
      duration:"00:00",
      played_percentage:0,
      played_time:"00:00",
      play_volume:0.5,
      search_name:"",
      none_music:false
    };
  },
  methods: {

    format_play_time(sec){
      // 格式化展示播放时间字符串
        var duration = parseInt(sec);
        var minute = parseInt(duration/60);
        var sec = duration%60+'';
        var isM0 = ':';
        if(minute == 0){
            minute = '00';
        }else if(minute < 10 ){
            minute = '0'+minute;
        }
        if(sec.length == 1){
            sec = '0'+sec;
        }
        return minute+isM0+sec;
    },
    update_metadata(){
      // 更新元数据,总时长,已经播放到时长
        var audio = this.$refs.player;
        this.duration =  this.format_play_time(audio.duration);
    },
    update_progress(){
      // 更新range播放进度显示
      var audio = this.$refs.player;
      this.played_percentage = audio.currentTime / audio.duration ;
      this.played_time = this.format_play_time(audio.currentTime);
    },
    update_played(){
      // range条控制播放进度
      this.update_metadata();
      var audio = this.$refs.player;
      audio.currentTime = audio.duration * this.played_percentage;
      this.play_start(false);
    },
    update_volume(){
      // 调整音量
      var audio = this.$refs.player;
      audio.volume = this.play_volume;
    },
    play_muted(){
      // 设置静音
      var audio = this.$refs.player;
      audio.muted = ! audio.muted ;
      this.volume_icon = audio.muted ? '<i class="fas fa-volume-mute"></i>': '<i class="fas fa-volume-up"></i>';
    },
    play_prev() {
      // 播放上一首
      if(this.index === 0){
        this.index = this.music_list.length -1;
      }else{
        this.index -= 1;
      }
      this.current_music = this.music_list[this.index];
      this.play_start();
    },
    play_next() {
      // 播放下一首
      if(this.index === (this.music_list.length -1)){
        this.index = 0;
      }else{
        this.index += 1;
      }
      this.current_music = this.music_list[this.index];
      this.play_start();
    },
    play_current(index,item){
      // 播放当前点击的tr对象
      this.index = index;
      this.current_music = item;
      this.play_start();
    },
    play_end(){
      if(! this.order){
        // 判断是单曲循环还是顺序播放
        this.play_start();
      }else{
        this.play_next();
      }
    },
    play_control(){
      // 播放控制:(暂停,播放)
       var audio = this.$refs.player;
       if(audio.paused){
         this.play_start(false);
       }else{
         this.control = '<i class="fas fa-circle" title="暂停"></i>';
         audio.pause();
       }
    },
    play_mode(){
      // 切换模式:(顺序播放,单曲循环)
      this.order = ! this.order;
      this.mode = this.order ? '<i class="fas fa-exchange-alt" title="顺序播放"></i>':'<i class="fas fa-sync" title="单曲播放"></i>';
    },
    play_start(is_load=true){
      // 开始播放
      this.control = '<i class="fas fa-bullseye" title="播放"></i>';
      var audio = this.$refs.player;
      if(is_load){
        audio.load();
      }
      audio.play();
    }
  },
  watch:{
    search_name:function(oldVal,newVal){
      // 当搜索框当内容为空的时候,把全部播放列表恢复回来
      if(this.search_name == ""){
        this.music_list = JSON.parse(JSON.stringify(this.music_list_backup));
      }else{
        this.music_list = JSON.parse(JSON.stringify(this.music_list_backup)).filter((i)=>{return i.name.search(this.search_name) != -1});
      }
    }
  }
};


/*
方法               方法描述
addTextTrack()    为音视频加入一个新的文本轨迹    
canPlayType()    检查指定的音视频格式是否得到支持    
load()    重新加载音视频标签    
play()    播放音视频    
pause()    暂停播放当前的音视频    
-------------------------
属性           属性描述
audioTracks    返回可用的音轨列表（MultipleTrackList对象）    
autoplay    媒体加载后自动播放    
buffered    返回缓冲部件的时间范围(TimeRanges对象)    
controller    返回当前的媒体控制器（MediaController对象）    
controls    显示播控控件    
crossOrigin    CORS设置    
currentSrc    返回当前媒体的URL    
currentTime    当前播放的时间，单位秒    
defaultMuted    缺省是否静音    
defaultPlaybackRate    播控的缺省倍速    
duration    返回媒体的播放总时长，单位秒    
ended    返回当前播放是否结束标志    
error    返回当前播放的错误状态    
initialTime    返回初始播放的位置    
loop    是否循环播放    
mediaGroup    当前音视频所属媒体组 (用来链接多个音视频标签)    
muted    是否静音    
networkState    返回当前网络状态    
paused    是否暂停    
playbackRate    播放的倍速    
played    当前播放部件已经播放的时间范围(TimeRanges对象)    
preload    页面加载时是否同时加载音视频    
readyState    返回当前的准备状态    
seekable    返回当前可跳转部件的时间范围(TimeRanges对象)    
seeking    返回用户是否做了跳转操作    
src    当前音视频源的URL    
startOffsetTime    返回当前的时间偏移(Date对象)    
textTracks    返回可用的文本轨迹(TextTrackList对象)    
videoTracks    返回可用的视频轨迹(VideoTrackList对象)    
volume    音量值    
事件
事件描述
abort    当音视频加载被异常终止时产生该事件    
canplay    当浏览器可以开始播放该音视频时产生该事件    
canplaythrough    当浏览器可以开始播放该音视频到结束而无需因缓冲而停止时产生该事件    
durationchange    当媒体的总时长改变时产生该事件    
emptied    当前播放列表为空时产生该事件    
ended    当前播放列表结束时产生该事件    
error    当加载媒体发生错误时产生该事件    
loadeddata    当加载媒体数据时产生该事件    
loadedmetadata    当收到总时长，分辨率和字轨等metadata时产生该事件    
loadstart    当开始查找媒体数据时产生该事件    
pause    当媒体暂停时产生该事件    
play    当媒体播放时产生该事件    
playing    当媒体从因缓冲而引起的暂停和停止恢复到播放时产生该事件    
progress    当获取到媒体数据时产生该事件    
ratechange    当播放倍数改变时产生该事件    
seeked    当用户完成跳转时产生该事件    
seeking    当用户正执行跳转时操作的时候产生该事件    
stalled    当试图获取媒体数据，但数据还不可用时产生该事件    
suspend    当获取不到数据时产生该事件    
timeupdate    当前播放位置发生改变时产生该事件    
volumechange    当前音量发生改变时产生该事件    
waiting    当视频因缓冲下一帧而停止时产生该事件
*/
</script>

