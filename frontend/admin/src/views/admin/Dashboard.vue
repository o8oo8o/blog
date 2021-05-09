<template>
  <div class="container-fluid">
    <div v-if="load_finish">
      <div class="row">
        <div class="col-12 col-sm-6 col-md-3">
          <div class="info-box bg-primary">
            <div class="info-box-content">
              <span class="info-box-text">今日访问</span>
              <span class="info-box-number">
                <b v-text="data.today_user_access"></b>人
              </span>
            </div>
          </div>
        </div>
        <div class="col-12 col-sm-6 col-md-3">
          <div class="info-box bg-primary">
            <div class="info-box-content">
              <span class="info-box-text">
                今日API调用
                <span v-text="data.today_api_call"></span>
              </span>
              <span class="info-box-number">
                日志共
                <span v-text="data.log_count"></span>条
              </span>
            </div>
          </div>
        </div>
        <div class="clearfix hidden-md-up"></div>
        <div class="col-12 col-sm-6 col-md-3">
          <div class="info-box bg-primary">
            <div class="info-box-content">
              <span class="info-box-text">今日后台登陆</span>
              <span class="info-box-number">
                <span v-text="data.today_admin_login_ok"></span>成功/
                <span v-text="data.today_admin_login_fail"></span>失败
              </span>
            </div>
          </div>
        </div>
        <div class="col-12 col-sm-6 col-md-3">
          <div class="info-box bg-primary">
            <div class="info-box-content">
              <span class="info-box-text">今日简历访问</span>
              <span class="info-box-number">
                <span v-text="data.today_resume_login_ok"></span>成功/
                <span v-text="data.today_resume_login_fail"></span>失败
              </span>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-12 col-sm-6 col-md-3">
          <div class="info-box bg-primary">
            <div class="info-box-content">
              <span class="info-box-text">
                博客数量
                <span v-text="data.blog_count"></span>
              </span>
              <span class="info-box-number">
                已发布
                <b v-text="data.blog_publish_count"></b>
              </span>
            </div>
          </div>
        </div>
        <div class="col-12 col-sm-6 col-md-3">
          <div class="info-box bg-primary">
            <div class="info-box-content">
              <span class="info-box-text">评论数量</span>
              <span class="info-box-number">
                <span v-text="data.review_count"></span>
              </span>
            </div>
          </div>
        </div>
        <div class="clearfix hidden-md-up"></div>
        <div class="col-12 col-sm-6 col-md-3">
          <div class="info-box bg-primary">
            <div class="info-box-content">
              <span class="info-box-text">信息发布</span>
              <span class="info-box-number">
                <span v-text="data.resume_publish_count"></span>次
              </span>
            </div>
          </div>
        </div>
        <div class="col-12 col-sm-6 col-md-3">
          <div class="info-box bg-primary">
            <div class="info-box-content">
              <span class="info-box-text">今日阅读组织</span>
              <span class="info-box-number">
                <span v-text="data.today_resume_read"></span>家
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6">
        <div class="card card-info">
          <div class="card-header">
            <h3 class="card-title">用户访问趋势</h3>

            <div class="card-tools">
              <button
                type="button"
                class="btn btn-tool"
                data-card-widget="collapse"
                data-toggle="tooltip"
                title="Collapse"
              >
                <i class="fas fa-minus"></i>
              </button>
              <button
                type="button"
                class="btn btn-tool"
                data-card-widget="remove"
                data-toggle="tooltip"
                title="Remove"
              >
                <i class="fas fa-times"></i>
              </button>
            </div>
            
          </div>
          <div class="card-body">
            <div class="chartjs-size-monitor">
              <div class="chartjs-size-monitor-expand">
                <div class></div>
              </div>
              <div class="chartjs-size-monitor-shrink">
                <div class></div>
              </div>
            </div>
            <canvas
              id="chartb"
              style="height: 250px; min-height: 250px; display: block; width: 395px;"
              width="790"
              height="500"
              class="chartjs-render-monitor"
            ></canvas>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="card card-info">
          <div class="card-header">
            <h3 class="card-title">API调用统计</h3>

            <div class="card-tools">
              <button
                type="button"
                class="btn btn-tool"
                data-card-widget="collapse"
                data-toggle="tooltip"
                title="Collapse"
              >
                <i class="fas fa-minus"></i>
              </button>
              <button
                type="button"
                class="btn btn-tool"
                data-card-widget="remove"
                data-toggle="tooltip"
                title="Remove"
              >
                <i class="fas fa-times"></i>
              </button>
            </div>
            
          </div>
          <div class="card-body">
            <div class="chart">
              <div class="chartjs-size-monitor">
                <div class="chartjs-size-monitor-expand">
                  <div class></div>
                </div>
                <div class="chartjs-size-monitor-shrink">
                  <div class></div>
                </div>
              </div>
              <canvas
                id="charta"
                style="height: 250px; min-height: 250px; display: block; width: 395px;"
                width="790"
                height="500"
                class="chartjs-render-monitor"
              ></canvas>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6">
        <div class="card card-info">
          <div class="card-header">
            <h3 class="card-title">简历访问失败</h3>

            <div class="card-tools">
              <button
                type="button"
                class="btn btn-tool"
                data-card-widget="collapse"
                data-toggle="tooltip"
                title="Collapse"
              >
                <i class="fas fa-minus"></i>
              </button>
              <button
                type="button"
                class="btn btn-tool"
                data-card-widget="remove"
                data-toggle="tooltip"
                title="Remove"
              >
                <i class="fas fa-times"></i>
              </button>
            </div>
            
          </div>
          <div class="card-body">
            <div class="chartjs-size-monitor">
              <div class="chartjs-size-monitor-expand">
                <div class></div>
              </div>
              <div class="chartjs-size-monitor-shrink">
                <div class></div>
              </div>
            </div>
            <canvas
              id="chartc"
              style="height: 250px; min-height: 250px; display: block; width: 395px;"
              width="790"
              height="500"
              class="chartjs-render-monitor"
            ></canvas>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="card card-info">
          <div class="card-header">
            <h3 class="card-title">简历阅读统计</h3>

            <div class="card-tools">
              <button
                type="button"
                class="btn btn-tool"
                data-card-widget="collapse"
                data-toggle="tooltip"
                title="Collapse"
              >
                <i class="fas fa-minus"></i>
              </button>
              <button
                type="button"
                class="btn btn-tool"
                data-card-widget="remove"
                data-toggle="tooltip"
                title="Remove"
              >
                <i class="fas fa-times"></i>
              </button>
            </div>
            
          </div>
          <div class="card-body">
            <div class="chart">
              <div class="chartjs-size-monitor">
                <div class="chartjs-size-monitor-expand">
                  <div class></div>
                </div>
                <div class="chartjs-size-monitor-shrink">
                  <div class></div>
                </div>
              </div>
              <canvas
                id="chartd"
                style="height: 250px; min-height: 250px; display: block; width: 395px;"
                width="790"
                height="500"
                class="chartjs-render-monitor"
              ></canvas>
            </div>
          </div>
        </div>
      </div>
    </div>    
    <div class="row">
      <div class="col-md-6">
        <div class="card card-info">
          <div class="card-header">
            <h3 class="card-title">后台登陆失败</h3>

            <div class="card-tools">
              <button
                type="button"
                class="btn btn-tool"
                data-card-widget="collapse"
                data-toggle="tooltip"
                title="Collapse"
              >
                <i class="fas fa-minus"></i>
              </button>
              <button
                type="button"
                class="btn btn-tool"
                data-card-widget="remove"
                data-toggle="tooltip"
                title="Remove"
              >
                <i class="fas fa-times"></i>
              </button>
            </div>
            
          </div>
          <div class="card-body">
            <div class="chartjs-size-monitor">
              <div class="chartjs-size-monitor-expand">
                <div class></div>
              </div>
              <div class="chartjs-size-monitor-shrink">
                <div class></div>
              </div>
            </div>
            <canvas
              id="charte"
              style="height: 250px; min-height: 250px; display: block; width: 395px;"
              width="790"
              height="500"
              class="chartjs-render-monitor"
            ></canvas>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="card card-info">
          <div class="card-header">
            <h3 class="card-title">后台登陆统计</h3>

            <div class="card-tools">
              <button
                type="button"
                class="btn btn-tool"
                data-card-widget="collapse"
                data-toggle="tooltip"
                title="Collapse"
              >
                <i class="fas fa-minus"></i>
              </button>
              <button
                type="button"
                class="btn btn-tool"
                data-card-widget="remove"
                data-toggle="tooltip"
                title="Remove"
              >
                <i class="fas fa-times"></i>
              </button>
            </div>
            
          </div>
          <div class="card-body">
            <div class="chart">
              <div class="chartjs-size-monitor">
                <div class="chartjs-size-monitor-expand">
                  <div class></div>
                </div>
                <div class="chartjs-size-monitor-shrink">
                  <div class></div>
                </div>
              </div>
              <canvas
                id="chartf"
                style="height: 250px; min-height: 250px; display: block; width: 395px;"
                width="790"
                height="500"
                class="chartjs-render-monitor"
              ></canvas>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="load_finish" class="row">
      <div class="col-md-6">
        <div class="card card-info">
          <div class="card-header">
            <h3 class="card-title">今日访问IP排行榜</h3>
            <div class="card-tools">
              <button
                type="button"
                class="btn btn-tool"
                data-card-widget="collapse"
                data-toggle="tooltip"
                title="Collapse"
              >
                <i class="fas fa-minus"></i>
              </button>
              <button
                type="button"
                class="btn btn-tool"
                data-card-widget="remove"
                data-toggle="tooltip"
                title="Remove"
              >
                <i class="fas fa-times"></i>
              </button>
            </div>
            
          </div>
          <div class="card-body table-responsive p-0" style="height:400px;">
            <div class>
              <table class="table table-head-fixed table-hover text-nowrap">
                <thead>
                  <tr>
                    <th>IP地址</th>
                    <th>请求次数</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(item, index) in data.ip_top" :key="index">
                    <td v-text="item.ip"></td>
                    <td v-text="item.count"></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="card card-info">
          <div class="card-header">
            <h3 class="card-title">今日响应慢请求</h3>
            <div class="card-tools">
              <button
                type="button"
                class="btn btn-tool"
                data-card-widget="collapse"
                data-toggle="tooltip"
                title="Collapse"
              >
                <i class="fas fa-minus"></i>
              </button>
              <button
                type="button"
                class="btn btn-tool"
                data-card-widget="remove"
                data-toggle="tooltip"
                title="Remove"
              >
                <i class="fas fa-times"></i>
              </button>
            </div>  
          </div>
          <div class="card-body table-responsive p-0" style="height:400px;">
            <div class>
              <table class="table table-head-fixed table-hover text-nowrap">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>请求IP</th>
                    <th>响应时长</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(item, index) in data.low_top" :key="index">
                    <td v-text="item.id"></td>
                    <td v-text="item.ip"></td>
                    <td v-text="item.qtime"></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "dashboard",
  mounted() {
    var that = this;
    axios
      .get("/api/admin/dashboard/")
      .then(function(response) {
        if (response.data.code === 0) {
          that.data = response.data.data;
          that.load_finish = true;
          that.create_api_chart();
          that.create_access_chart();
          that.create_resume_login_fail_chart();
          that.create_resume_login_ok_chart();
          that.create_admin_login_fail_chart();
          that.create_admin_login_ok_chart();
        }
      })
      .catch(function(error) {
        console.log("/api/admin/dashboard/,请求异常");
      });
  },
  data() {
    return {
      load_finish: false,
      data: null
    };
  },
  methods: {
    // API调用图表
    create_api_chart() {
      var that = this;
      var api_canvas = document.getElementById("charta").getContext("2d");
      var api_chart = new Chart(api_canvas, {
        type: "bar",
        data: {
          labels: that.data.chart_api_call.date,
          datasets: [
            {
              label: "API调用",
              data: that.data.chart_api_call.count,
              backgroundColor: that.data.conf.chart_bg_color,
              borderColor: that.data.conf.chart_br_color,
              borderWidth: that.data.conf.chart_border_width
            }
          ]
        },
        options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: that.data.conf.chart_zero
                }
              }
            ]
          }
        }
      });
    },
    // 访问人数图表
    create_access_chart() {
      var that = this;
      var access_canvas = document.getElementById("chartb").getContext("2d");
      var access_chart = new Chart(access_canvas, {
        type: "line",
        data: {
          labels: that.data.chart_user_access.date,
          datasets: [
            {
              label: "访问人数",
              data: that.data.chart_user_access.count,
              backgroundColor: that.data.conf.chart_bg_color,
              borderColor: that.data.conf.chart_br_color,
              borderWidth: that.data.conf.chart_border_width
            }
          ]
        },
        options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: that.data.conf.chart_zero
                }
              }
            ]
          }
        }
      });
    },
    // 简历访问失败图表
    create_resume_login_fail_chart() {
      var that = this;
      var fail_canvas = document.getElementById("chartc").getContext("2d");
      var fail_chart = new Chart(fail_canvas, {
        type: "line",
        data: {
          labels: that.data.chart_resume_login_fail.date,
          datasets: [
            {
              label: "简历访问失败",
              data: that.data.chart_resume_login_fail.count,
              backgroundColor: that.data.conf.chart_bg_color,
              borderColor: that.data.conf.chart_br_color,
              borderWidth: that.data.conf.chart_border_width
            }
          ]
        },
        options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: that.data.conf.chart_zero
                }
              }
            ]
          }
        }
      });
    },
    // 简历阅读统计图表
    create_resume_login_ok_chart() {
      var that = this;
      var resume_canvas = document.getElementById("chartd").getContext("2d");
      var success_chart = new Chart(resume_canvas, {
        type: "bar",
        data: {
          labels: that.data.chart_resume_login_ok.date,
          datasets: [
            {
              label: "简历阅读统计",
              data: that.data.chart_resume_login_ok.count,
              backgroundColor: that.data.conf.chart_bg_color,
              borderColor: that.data.conf.chart_br_color,
              borderWidth: that.data.conf.chart_border_width
            }
          ]
        },
        options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: that.data.conf.chart_zero
                }
              }
            ]
          }
        }
      });
    },
    // 后台登陆失败图表
    create_admin_login_fail_chart() {
      var that = this;
      var fail_canvas = document.getElementById("charte").getContext("2d");
      var fail_chart = new Chart(fail_canvas, {
        type: "line",
        data: {
          labels: that.data.chart_admin_login_fail.date,
          datasets: [
            {
              label: "后台登陆失败",
              data: that.data.chart_admin_login_fail.count,
              backgroundColor: that.data.conf.chart_bg_color,
              borderColor: that.data.conf.chart_br_color,
              borderWidth: that.data.conf.chart_border_width
            }
          ]
        },
        options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: that.data.conf.chart_zero
                }
              }
            ]
          }
        }
      });
    },
    // 后台登陆统计图表
    create_admin_login_ok_chart() {
      var that = this;
      var resume_canvas = document.getElementById("chartf").getContext("2d");
      var success_chart = new Chart(resume_canvas, {
        type: "bar",
        data: {
          labels: that.data.chart_admin_login_ok.date,
          datasets: [
            {
              label: "后台登陆统计",
              data: that.data.chart_admin_login_ok.count,
              backgroundColor: that.data.conf.chart_bg_color,
              borderColor: that.data.conf.chart_br_color,
              borderWidth: that.data.conf.chart_border_width
            }
          ]
        },
        options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: that.data.conf.chart_zero
                }
              }
            ]
          }
        }
      });
    },
  }
};
</script>
