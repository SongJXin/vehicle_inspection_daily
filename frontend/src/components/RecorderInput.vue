<template>
  <div style="width: 50%; background: #fff; padding: 8px;position: relative; left: 25%" v-if="active === 0">
    <mu-container>
      <mu-form  :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
        <mu-form-item prop="plate_no" label="车牌号" help-text="" :rules="unNoneRules">
          <mu-text-field prop="plate_no" v-model="form.plate_no"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="vehicle_type" label="车辆类型" :rules="unNoneRules">
          <mu-select v-model="vehicle_type" prop="vehicle_type" @change="typechage">
            <mu-option v-for="type,index in types" :key="type.type" :label="type.type" :value="index"></mu-option>
          </mu-select>
        </mu-form-item>
        <mu-form-item prop="price" label="价格" help-text="" :rules="unNoneRules">
          <mu-text-field prop="price" v-model="form.price" ></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="status" label="状态" :rules="unNoneRules">
          <mu-radio v-model="form.status" value="通过" label="通过"></mu-radio>
          <mu-radio v-model="form.status" value="未通过" label="未通过"></mu-radio>
        </mu-form-item>
        <mu-form-item prop="date" label="日期" :rules="unNoneRules">
          <mu-date-input prop="date" v-model="form.date" value-format="YYYY-MM-DD" label-float full-width landscape></mu-date-input>
        </mu-form-item>
        <mu-form-item label="备注">
          <mu-text-field multi-line :rows="1" :rows-max="6" v-model="form.comment"></mu-text-field>
        </mu-form-item>
        <mu-form-item label="记录人">
          <mu-text-field v-model="form.recorder" ></mu-text-field>
        </mu-form-item>
        <mu-form-item >
          <mu-button color="primary" @click="submit">提交</mu-button>
          <mu-button @click="clear">重置</mu-button>
        </mu-form-item>
      </mu-form>
    </mu-container>
  </div>
</template>

<script>
import Vue from 'vue'
import 'muse-ui/lib/styles/base.less'
import { Form, Button, TextField, Tabs, Grid, Alert, Icon, Select, DateInput, Radio } from 'muse-ui'
import 'muse-ui/lib/styles/theme.less'
import axios from 'axios'
Vue.use(Form)
Vue.use(Button)
Vue.use(TextField)
Vue.use(Tabs)
Vue.use(Grid)
Vue.use(Alert)
Vue.use(Icon)
Vue.use(Select)
Vue.use(DateInput)
Vue.use(Radio)
export default {
  name: 'RecorderInput',
  mounted () {
    this.$nextTick(function () {
      this.get_types()
    })
  },
  data: function () {
    return {
      active: 0,
      vehicle_type: '',
      form: {
        plate_no: '',
        vehicle_type: '',
        price: '',
        status: '通过',
        date: this.nowdate(),
        comment: '',
        recorder: ''
      },
      labelPosition: 'left',
      unNoneRules: [
        {validate: (val) => !!val, message: '必须填写此项'}
      ],
      types:[
        {
          type: '小型车',
          price: 10
        }
      ]
    }
  },
  methods: {
    get_types () {
      let that = this
      axios.get('/settings/vehicle_type/get_all').then(function (response) {
        that.types = response.data.result
      })
    },
    nowdate () {
      var year =new Date().getFullYear();//获取完整的年份(4位,1970-????)
      var month = new Date().getMonth() + 1;//获取当前月份(0-11,0代表1月)
      var day = new Date().getDate();//获取当前日(1-31)
      if (month < 10) {
        month ="0" + month;
      }
      if (day < 10) {
        day ="0" + day;
      }
      return year +"-" + month + "-" + day;
    },
    typechage: function(ele){
      this.form.vehicle_type = this.types[ele].type
      this.form.price = this.types[ele].price
    },
    submit () {
      axios.post('recorder/add',this.form).then(function () {
        location.href = '/#/list'
      })
    },
    clear () {
      this.form = {
        plate_no: '',
        vehicle_type: '',
        price: '',
        status: '通过',
        date: this.nowdate(),
        comment: '',
        recorder: ''
      }
    }
  }
}
</script>

<style scoped>
  .mu-demo-form {
    width: 100%;
    /*max-width: 460px;*/
  }
</style>
