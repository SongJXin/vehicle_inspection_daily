<template>
  <mu-container>
    <mu-paper :z-depth="1">
      <mu-expansion-panel>
        <div slot="header">搜索</div>
        <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
          <mu-row>
            <mu-col span="12" lg="4" sm="6">
              <mu-form-item label="车牌号">
                <mu-text-field v-model="form.plate_no"></mu-text-field>
              </mu-form-item>
            </mu-col>
            <mu-col span="12" lg="4" sm="6">
              <mu-form-item label="车辆类型">
                <mu-select v-model="form.vehicle_type" prop="vehicle_type">
                  <mu-option v-for="type,index in types" :key="type.type" :label="type.type" :value="type.type"></mu-option>
                </mu-select>
              </mu-form-item>
            </mu-col>
          </mu-row>
          <mu-form-item prop="status" label="状态">
            <mu-radio v-model="form.status" value="通过" label="通过"></mu-radio>
            <mu-radio v-model="form.status" value="未通过" label="未通过"></mu-radio>
          </mu-form-item>
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
        <mu-button slot="action" flat color="primary" @click="search_V_Recorder">搜索</mu-button>
      </mu-expansion-panel>
      <mu-data-table border stripe height="300" selectable select-all :selects.sync="selects" checkbox :columns="columns"
                     :sort.sync="sort" @sort-change="handleSortChange" :data="list">
        <template slot-scope="scope">
          <td>{{scope.row.plate_no}}</td>
          <td class="is-left">{{scope.row.vehicle_type}}</td>
          <td class="is-right">{{scope.row.price}}</td>
          <td class="is-right">{{scope.row.number}}</td>
          <td class="is-right">{{scope.row.totle}}</td>
          <td class="is-left">{{scope.row.status}}</td>
          <td class="is-right">{{scope.row.date}}</td>
          <td class="is-left">{{scope.row.comment}}</td>
        </template>
      </mu-data-table>
      总计 {{count}} 个<br/>
      <mu-row justify-content="center">
        <mu-col span="2">
          <mu-button color="info" href="#/recorderinput">新增</mu-button>
        </mu-col>
        <mu-col span="2">
          <mu-button color="error" @click="remove_V_Recoder" >删除</mu-button>
        </mu-col>
      </mu-row>
      <mu-flex align-items="center" style="padding: 8px;" wrap="wrap">
        selects:
        <mu-chip delete v-for="selectIndex in selects" @delete="removeSelect(selectIndex)" style="margin: 8px;"
                 color="green" :key="selectIndex">{{list[selectIndex].plate_no.slice(0,10)}}
        </mu-chip>
      </mu-flex>
    </mu-paper>
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
  import axios from 'axios'

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
    name: 'List',
    mounted () {
      this.$nextTick(function () {
        this.search_V_Recorder()
        this.get_types()
      })
    },
    data() {
      return {
        labelPosition: 'left',
        selects: [],
        sort: {
          name: '',
          order: 'asc'
        },
        types: [
          {
            type: '小型车',
            price: 10
          }
        ],
        count: 1,
        form: {
          plate_no: '',
          vehicle_type: '',
          status: '',
          fromdate: '',
          todate: '',
          number: ''
        },
        columns: [
          {title: '车牌号', width: 150, name: 'plate_no'},
          {title: '车辆类型', name: 'vehicle_type', width: 100, align: 'center', sortable: true},
          {title: '价格(元)', name: 'price', width: 100, align: 'center', sortable: true},
          {title: '数量', name: 'number', width: 100, align: 'center', sortable: true},
          {title: '总额', name: 'totle', width: 100, align: 'center', sortable: true},
          {title: '状态', name: 'status', width: 100, align: 'left', sortable: true},
          {title: '日期', name: 'date', width: 126, align: 'left', sortable: true},
          {title: '备注', name: 'comment',  align: 'center', sortable: true}
        ],
        list: [
          {
            id: '',
            plate_no: '鲁A7896G',
            vehicle_type: '小型车',
            price: '10',
            status: '通过',
            date: '2019-09-18',
            comment: '',
            totle: '10',
            number: '1'
          }
        ]
      }
    },
    methods: {
      remove_V_Recoder () {
        this.$confirm('确定要删除？', '提示', {
          type: 'warning'
        }).then(({result}) => {
          if (result) {
            let that = this
            for (var i = this.selects.length - 1; i >= 0; i--) {
              var vtdict = {
                id: this.list[this.selects[i]].id,
              }
              axios.delete('/recorder/delete',{data: vtdict}).then(function () {
                that.search_V_Recorder()
              })
            }
            this.selects = []
          }
        })
      },
      get_types () {
        let that = this
        axios.get('/settings/vehicle_type/get_all').then(function (response) {
          that.types = response.data.result
        })
      },
      clear () {
        this.form = {
          plate_no: '',
          vehicle_type: '',
          status: '',
          fromdate: '',
          todate: ''
        }
        this.search_V_Recorder()
      },
      search_V_Recorder() {
        let that = this
        axios.post('/recorder/search', this.form).then(function (response) {
          that.list = response.data.result
          that.count = response.data.count
        })
      },
      get_All_V_Recorder() {
        let that = this
        axios.get('/recorder/get/all').then(function (response) {
          that.list = response.data.result
          that.count = response.data.count
        })
      },
      handleSortChange({name, order}) {
        this.list = this.list.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name])
      },
      removeSelect(selectIndex) {
        const index = this.selects.indexOf(selectIndex)
        this.selects.splice(index, 1)
      }
    }
  }
</script>

<style scoped>

</style>
