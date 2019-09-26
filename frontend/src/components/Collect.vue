<template>
  <mu-container style="width: 1000px">
    <mu-expansion-panel>
      <div slot="header">根据日期汇总</div>
      <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
        <mu-row>
          <mu-col span="12" lg="4" sm="6">
            <mu-form-item prop="status" label="起始日期">
              <mu-date-input v-model="form.fromdate" value-format="YYYY-MM-DD" full-width landscape></mu-date-input>
            </mu-form-item>
          </mu-col>
          <mu-col span="12" lg="4" sm="6">
            <mu-form-item prop="status" label="终止日期">
              <mu-date-input v-model="form.todate" value-format="YYYY-MM-DD" full-width landscape></mu-date-input>
            </mu-form-item>
          </mu-col>
        </mu-row>
      </mu-form>
      <mu-button slot="action" flat @click="clear">重置</mu-button>
      <mu-button slot="action" flat color="primary" @click="get_collect">汇总</mu-button>
    </mu-expansion-panel>
    <mu-paper :z-depth="1" id="print">
      <h1 align="center">青州市永佳机动车检测有限公司日报表</h1>
      <p align="right">日期：{{date}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
      <mu-data-table stripe :columns="columns"
                     :sort.sync="sort" @sort-change="handleSortChange" :data="list" align="center">
        <template slot-scope="scope">
          <td class="is-left">{{scope.row.vehicle_type}}</td>
          <td class="is-left">{{scope.row.count}}</td>
          <td class="is-right">{{scope.row.price}}</td>
          <td class="is-right">{{scope.row.totle}}</td>
          <td class="is-right">{{scope.row.comment}}</td>
        </template>
      </mu-data-table>
      <h3 align="left">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;总金额：{{totle}}</h3>
    </mu-paper>
    <mu-row justify-content="center">
      <mu-col span="2">
        <mu-button color="info" v-print="'#print'">打印</mu-button>
      </mu-col>
    </mu-row>
  </mu-container>
</template>

<script>
import Vue from 'vue'
import 'muse-ui/lib/styles/base.less'
import {
  Paper,
  DataTable,
  Button,
  Grid,
  Icon,
  Checkbox,
  Chip,
  ExpansionPanel,
  Form,
  TextField,
  Select,
  DateInput,
  Radio
} from 'muse-ui'
import 'muse-ui/lib/styles/theme.less'
import Print from 'vue-print-nb'
import axios from 'axios'
Vue.use(Print)
Vue.use(Select)
Vue.use(DateInput)
Vue.use(Radio)
Vue.use(Paper)
Vue.use(DataTable)
Vue.use(Button)
Vue.use(Grid)
Vue.use(Icon)
Vue.use(Checkbox)
Vue.use(Chip)
Vue.use(ExpansionPanel)
Vue.use(Form)
Vue.use(TextField)
export default {
  name: 'Collect',
  mounted () {
    this.$nextTick(function () {
      this.get_collect()
    })
  },
  data () {
    return {
      labelPosition: 'left',
      form: {
        fromdate: '',
        todate: ''
      },
      sort: {
        name: '',
        order: 'asc'
      },
      totle: '拾元',
      date: '2019-9-24',
      columns: [
        {title: '机动车类型', name: 'vehicle_type', width: 200, align: 'center', sortable: true},
        {title: '审车数量', name: 'count', width: 100, align: 'left', sortable: true},
        {title: '审车金额', name: 'price', width: 100, align: 'center', sortable: true},
        {title: '审车合计', name: 'totle', width: 100, align: 'left', sortable: true},
        {title: '备注', name: 'comment', width: 200, align: 'left', sortable: true}
      ],
      list: [
        {
          vehicle_type: '小型车',
          price: '10',
          count: '1',
          totle: '10'
        }
      ]
    }
  },
  methods: {
    clear () {
      this.form = {
        fromdate: '',
        todate: ''
      }
    },
    get_collect () {
      let that = this
      axios.post('collect/get', this.form).then(function (response) {
        that.list = response.data.result
        that.totle = response.data.totle
        that.date = response.data.datestr
      })
    },
    handleSortChange ({name, order}) {
      this.list = this.list.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name])
    }
  }
}
</script>

<style scoped>

</style>
