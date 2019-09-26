<template>
  <mu-container style="width: 420px">
    <mu-paper :z-depth="1">
      <h1>车辆类型</h1>
      <mu-data-table selectable select-all :selects.sync="selects" checkbox :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="list">
        <template slot-scope="scope">
          <td>{{scope.row.type}}</td>
          <td >{{scope.row.price}}</td>
        </template>
      </mu-data-table>
      <mu-row justify-content="center">
        <mu-col span="4">
          <mu-text-field required="required"  style="width: 100px"  v-model="vehicleType.type" placeholder="类型"></mu-text-field>
        </mu-col>
        <mu-col span="4">
          <mu-text-field type="number" required="required" style="width: 100px"  v-model="vehicleType.prices" placeholder="价格"  ></mu-text-field>
        </mu-col>
      </mu-row>
      <mu-row justify-content="center">
        <mu-col span="4">
          <mu-button color="info" @click="add_V_Type">新增</mu-button>
        </mu-col>
        <mu-col span="4">
          <mu-button color="error" @click="remove_V_Type" >删除</mu-button>
        </mu-col>
      </mu-row>
      <mu-flex align-items="center" style="padding: 8px;" wrap="wrap">
        selects: <mu-chip delete v-for="selectIndex in selects" @delete="removeSelect(selectIndex)" style="margin: 8px;" color="green" :key="selectIndex">{{list[selectIndex].type}}</mu-chip>
      </mu-flex>
    </mu-paper>
  </mu-container>
</template>

<script>
/* eslint-disable standard/object-curly-even-spacing */
import Vue from 'vue'
import 'muse-ui/lib/styles/base.less'
import 'muse-ui-message/dist/muse-ui-message.css'
import 'material-design-icons/iconfont/material-icons.css'
import { Paper, DataTable, Button, Grid, Icon, Checkbox, Chip, Dialog } from 'muse-ui'
import MuseUIMessage from 'muse-ui-message'
import 'muse-ui/lib/styles/theme.less'
import axios from 'axios'
Vue.use(Paper)
Vue.use(DataTable)
Vue.use(Button)
Vue.use(Grid)
Vue.use(Icon)
Vue.use(Checkbox)
Vue.use(Chip)
Vue.use(MuseUIMessage)
Vue.use(Dialog)
export default {
  name: 'Settings',
  mounted () {
    this.$nextTick(function () {
      this.get_All_V_Tpye()
    })
  },
  data () {
    return {
      alert: false,
      selects: [],
      vehicleType: {
        prices: '',
        type: ''
      },
      sort: {
        name: '',
        order: 'asc'
      },
      columns: [
        {title: '类型', width: 200, name: 'type'},
        {title: '价格', name: 'price', width: 126, align: 'center', sortable: true}
      ],
      list: [
        {
          type: '小型车',
          price: 10
        }
      ]
    }
  },
  methods: {
    handleSortChange ({name, order}) {
      this.list = this.list.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name])
    },
    removeSelect (selectIndex) {
      const index = this.selects.indexOf(selectIndex)
      this.selects.splice(index, 1)
    },
    get_All_V_Tpye () {
      let that = this
      axios.get('/settings/vehicle_type/get_all').then(function (response) {
        that.list = response.data.result
      })
    },
    add_V_Type () {
      let that = this
      axios.post('/settings/vehicle_type/create', this.vehicleType).then(function () {
        that.get_All_V_Tpye()
      })
    },
    remove_V_Type () {
      this.$confirm('确定要删除？', '提示', {
        type: 'warning'
      }).then(({result}) => {
        if (result) {
          let that = this
          for (var i = this.selects.length - 1; i >= 0; i--) {
            var vtdict = {
              prices: this.list[this.selects[i]].price,
              type: this.list[this.selects[i]].type
            }
            axios.delete('/settings/vehicle_type/delete', {data: vtdict}).then(function () {
              that.get_All_V_Tpye()
            })
          }
          this.selects = []
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
