<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-12">
        <div class="card">
          <div class="card-header">
            <h5 style="text-align: center">主机性能报告</h5>
          </div>
          <div class="card-body">
            <div class="row">
              <div class="col-md-6">
                <p class="text-center">
                  <strong>CPU信息</strong>
                </p>
                <div class="progress-group">
                  用户
                  <span class="float-right">
                    <b v-text="host.cpu.user"></b>%
                  </span>
                  <div class="progress progress-sm">
                    <div
                      class="progress-bar bg-primary"
                      v-bind:style="{ width: host.cpu.user + '%' }"
                    ></div>
                  </div>
                </div>
                <div class="progress-group">
                  系统
                  <span class="float-right">
                    <b v-text="host.cpu.system"></b>%
                  </span>
                  <div class="progress progress-sm">
                    <div
                      class="progress-bar bg-primary"
                      v-bind:style="{ width: host.cpu.system + '%' }"
                    ></div>
                  </div>
                </div>
                <div class="progress-group">
                  <span class="progress-text">空闲</span>
                  <span class="float-right">
                    <b v-text="host.cpu.idle"></b>%
                  </span>
                  <div class="progress progress-sm">
                    <div
                      class="progress-bar bg-success"
                      v-bind:style="{ width: host.cpu.idle + '%' }"
                    ></div>
                  </div>
                </div>
              </div>
              <div class="col-md-6">
                <p class="text-center">
                  <strong>内存信息</strong>
                </p>
                <div class="progress-group">
                  使用率
                  <span class="float-right">
                    已使用:
                    <b v-text="host.mem.percent"></b>%,
                    <b v-text="host.mem.used +'G'"></b>,共:
                    <b v-text="host.mem.total+'G'"></b>
                  </span>
                  <div class="progress progress-sm">
                    <div
                      class="progress-bar bg-primary"
                      v-bind:style="{ width: host.mem.percent + '%' }"
                    ></div>
                  </div>
                </div>
                <div class="progress-group">
                  <span class="progress-text">可用</span>
                  <span class="float-right">
                    <b v-text="host.mem.available+'G'"></b>
                  </span>
                  <div class="progress progress-sm">
                    <div
                      class="progress-bar bg-primary"
                      v-bind:style="{ width: host.mem.available/host.mem.total*100  + '%' }"
                    ></div>
                  </div>
                </div>
                <div class="progress-group">
                  <span class="progress-text">空闲</span>
                  <span class="float-right">
                    <b v-text="host.mem.free +'G'"></b>
                  </span>
                  <div class="progress progress-sm">
                    <div
                      class="progress-bar bg-success"
                      v-bind:style="{ width: host.mem.free  + '%' }"
                    ></div>
                  </div>
                </div>
              </div>
            </div>
            <br />
            <hr />
            <p class="text-center">
              <strong>磁盘</strong>
            </p>
            <div class="row">
              <div v-for="(item, index) in host.disk" :key="index" class="col-md-12">
                <div class="progress-group">
                  <b v-text="item.mount"></b>&nbsp;&nbsp;使用率:
                  <span v-text="item.percent"></span>%
                  <span class="float-right">
                    <b v-text="item.use"></b>G/
                    <b v-text="item.total"></b>G
                  </span>
                  <div class="progress progress-sm">
                    <div
                      class="progress-bar bg-primary"
                      v-bind:style="{ width: item.percent + '%' }"
                    ></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <br />
          <hr />
          <div class="table-responsive">
            <table class="table m-0">
              <thead>
                <tr>
                  <th>说明</th>
                  <th>统计</th>
                  <th>说明</th>
                  <th>统计</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="text-info">开机时间</td>
                  <td v-text="host.boot"></td>
                  <td class="text-info">网络发送</td>
                  <td v-text="host.net.bytes_sent / 1073741824 +' GB'"></td>
                </tr>
                <tr>
                  <td class="text-info">获取时间</td>
                  <td v-text="host.time"></td>
                  <td class="text-info">网络接收</td>
                  <td v-text="host.net.bytes_revc / 1073741824 +' GB'"></td>
                </tr>
                <tr>
                  <td class="text-info">磁盘读次数</td>
                  <td v-text="host.disk_io.read_count"></td>
                  <td class="text-info">网络发送包</td>
                  <td v-text="host.net.packets_sent"></td>
                </tr>
                <tr>
                  <td class="text-info">磁盘写次数</td>
                  <td v-text="host.disk_io.write_count"></td>
                  <td class="text-info">网络接收包</td>
                  <td v-text="host.net.packets_recv"></td>
                </tr>
                <tr>
                  <td class="text-info">磁盘读字节</td>
                  <td v-text="host.disk_io.read_bytes / 1073741824 +' GB'"></td>
                  <td class="text-info">网络errin</td>
                  <td v-text="host.net.errin"></td>
                </tr>
                <tr>
                  <td class="text-info">磁盘写字节</td>
                  <td v-text="host.disk_io.write_bytes / 1073741824 +' GB' "></td>
                  <td class="text-info">网络errout</td>
                  <td v-text="host.net.errout"></td>
                </tr>
                <tr>
                  <td class="text-info">磁盘读时间</td>
                  <td v-text="host.disk_io.read_time"></td>
                  <td class="text-info">网络dropin</td>
                  <td v-text="host.net.dropin"></td>
                </tr>
                <tr>
                  <td class="text-info">磁盘写时间</td>
                  <td v-text="host.disk_io.write_time"></td>
                  <td class="text-info">网络dropout</td>
                  <td v-text="host.net.dropout"></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "monitor",
  beforeRouteLeave(to, from, next) {
    // 导航离开该组件的对应路由时调用
    // 可以访问组件实例 `this`
    clearInterval(this.crontab);
    next();
  },
  mounted() {
    // 每2秒种向后端请求一次数据
    this.crontab = setInterval(() => {
      this.$store.dispatch("monitor_handler");
    }, 2000);
  },
  beforeDestroy() {
    clearInterval(this.crontab);
  },
  data() {
    return {
      cpu: 20,
      crontab: ""
    };
  },
  computed: {
    host: {
      get() {
        return this.$store.state.monitor;
      }
    }
  }
};
</script>
