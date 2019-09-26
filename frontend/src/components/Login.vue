<template>
  <mu-container id="login">
    <mu-tabs :value.sync="active" style="width: 50%;position: relative; left: 25%;;top: 25%">
      <mu-tab>登陆</mu-tab>
    </mu-tabs>
    <div style="width: 50%; background: #fff; padding: 8px;position: relative; left: 25%" v-if="active === 0">
      <mu-container>
        <mu-form ref="form" :model="validateForm" class="mu-demo-form" :label-position="labelPosition" label-width="100">
          <mu-form-item label="用户名" help-text="" prop="username" :rules="usernameRules">
            <mu-text-field v-model="validateForm.username" prop="username"></mu-text-field>
          </mu-form-item>
          <mu-form-item label="密码" prop="password" :rules="passwordRules">
            <mu-text-field  type="password" v-model="validateForm.password" prop="password"></mu-text-field>
          </mu-form-item>
          <mu-alert color="error" delete v-if="alert" @delete="closeAlert()">
            <mu-icon left value="warning"></mu-icon> 用户名密码错误
          </mu-alert>
          <mu-form-item >
            <mu-button color="primary" @click="submit">登录</mu-button>
            <mu-button @click="clear">重置</mu-button>
          </mu-form-item>
        </mu-form>
      </mu-container>
    </div>
  </mu-container>
</template>
<script>
import Vue from 'vue'
import 'muse-ui/lib/styles/base.less'
import { Form, Button, TextField, Tabs, Grid, Alert, Icon } from 'muse-ui'
import 'muse-ui/lib/styles/theme.less'
import axios from 'axios'
Vue.use(Form)
Vue.use(Button)
Vue.use(TextField)
Vue.use(Tabs)
Vue.use(Grid)
Vue.use(Alert)
Vue.use(Icon)
export default {
  name: 'Login',
  data: function () {
    return {
      alert: false,
      labelPosition: 'left',
      usernameRules: [
        {validate: (val) => !!val, message: '必须填写用户名'},
        {validate: (val) => val.length >= 3, message: '用户名长度大于3'}
      ],
      passwordRules: [
        {validate: (val) => !!val, message: '必须填写密码'},
        {validate: (val) => val.length >= 3 && val.length <= 10, message: '密码长度大于3小于10'}
      ],
      validateForm: {
        username: '',
        password: ''
      },
      active: 0
    }
  },
  methods: {
    showAlert: function () {
      this.alert = true
    },
    closeAlert () {
      this.alert = false
    },
    submit () {
      let that = this
      this.$refs.form.validate().then(() => {
        axios.post('/login', this.validateForm).then(function (response) {
          location.href = response.data
        }).catch(function (error) {
          console.log(error.message)
          that.showAlert()
        })
      })
    },
    clear () {
      this.$refs.form.clear()
      this.validateForm = {
        username: '',
        password: ''
      }
    }
  }
}
</script>

<style>
  #login {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  .mu-demo-form {

    width: 100%;
    /*max-width: 460px;*/
  }
</style>
