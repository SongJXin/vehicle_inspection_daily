<template>
  <div>
    <mu-row>
      <mu-col>
        <div id="number" style="width: 600px;height:400px;"></div>
      </mu-col>
      <mu-col>
        <div id="totle" style="width: 600px;height:400px;"></div>
      </mu-col>
    </mu-row>
  </div>
</template>

<script>
import Vue from 'vue'
import {Grid} from 'muse-ui'
import echarts from 'echarts'
import axios from 'axios'
Vue.use(Grid)
export default {
  name: 'Dashboard',
  mounted () {
    this.$nextTick(function () {
      this.get_date_list()
      this.legendData = this.get_legend_data()
      this.numberChart = this.type_sale_day()
      this.get_type_number(this.numberChart)
      this.totleChart = this.type_sale_totle()
      this.get_type_totle(this.totleChart)
    })
    if (this.timer) {
      clearInterval(this.timer)
    } else {
      this.timer = setInterval(() => {
        this.get_type_number(this.numberChart)
        this.get_type_totle(this.totleChart)
      }, 500000)
    }
  },
  destroyed () {
    clearImmediate(this.timer)
  },
  data: function () {
    return {
      orgOptions: {},
      datelist: [],
      legendData: [],
      numberChart: null,
      totleChart: null
    }
  },
  methods: {
    get_date_list () {
      let nowDate = new Date()
      let nowDateDay = nowDate.getDate()
      let dateList = []
      for (let day = 30; day >= 0; day--) {
        let diffDay = nowDateDay - day
        let newDate = new Date(nowDate)
        newDate.setDate(diffDay)
        let yearstr = newDate.getFullYear().toString()
        let monthstr = (newDate.getMonth() + 1) < 10 ? '0' + (newDate.getMonth() + 1).toString() : (newDate.getMonth() + 1).toString()
        let daystr = (newDate.getDate()) < 10 ? '0' + (newDate.getDate()).toString() : (newDate.getDate()).toString()
        dateList[30 - day] = yearstr + '-' + monthstr + '-' + daystr
      }
      this.datelist = dateList
    },
    get_legend_data () {
      let legendData = []
      axios.get('/settings/vehicle_type/get_all').then(function (response) {
        let resultData = response.data.result
        for (let i = 0; i < resultData.length; i++) {
          legendData.push(resultData[i].type)
        }
      })
      return legendData
    },
    // 每日数量
    type_sale_day () {
      let myChart = echarts.init(document.getElementById('number'))
      let option = {
        title: {
          text: '每月审车数量'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          data: this.legendData
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          data: this.datelist
        },
        yAxis: {
          type: 'value'
        },
        series: []
      }
      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option)
      return myChart
    },
    get_type_number (myChart) {
      let _this = this
      axios.get('/charts/recorder/number').then(function (response) {
        let series = []
        let resData = response.data
        for (let i = 0; i < _this.legendData.length; i++) {
          let serie = {
            name: _this.legendData[i],
            type: 'bar',
            stack: '总数',
            label: {
              normal: {
                show: true,
                position: 'insideRight'
              }
            },
            data: resData[_this.legendData[i]]
          }
          series[series.length] = serie
        }
        myChart.setOption({
          series: series
        })
      })
    },
    // 每日金额
    type_sale_totle () {
      let myChart = echarts.init(document.getElementById('totle'))
      let option = {
        title: {
          text: '每月审车金额'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          data: []
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          data: this.datelist
        },
        yAxis: {
          type: 'value'
        },
        series: []
      }
      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option)
      return myChart
    },
    get_type_totle (myChart) {
      let _this = this
      axios.get('/charts/recorder/totle').then(function (response) {
        let series = []
        let resData = response.data
        for (let i = 0; i < _this.legendData.length; i++) {
          let serie = {
            name: _this.legendData[i],
            type: 'bar',
            stack: '总额',
            label: {
              normal: {
                show: true,
                position: 'insideRight'
              }
            },
            data: resData[_this.legendData[i]]
          }
          series[series.length] = serie
        }
        myChart.setOption({
          legend: {
            data: _this.legendData
          },
          series: series
        })
      })
    }
  }
}
</script>

<style scoped>
</style>
