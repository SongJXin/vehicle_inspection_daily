<template>
  <div id="app">
    <mu-appbar style="width: 100%;" color="primary">
      <mu-button flat slot="right" href="#/login"><h3>登录</h3></mu-button>
      青州市永佳机动车检测有限公司日报系统
      <mu-menu slot="left" open-on-hover>
        <mu-button flat><h3>菜单</h3></mu-button>
        <mu-list slot="content">
          <mu-list-item button  href="/">
            <mu-list-item-content>
              <mu-list-item-title>仪表盘</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
          <mu-list-item button href="#/recorderinput">
            <mu-list-item-content>
              <mu-list-item-title>信息录入</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
          <mu-list-item button href="#/list">
            <mu-list-item-content>
              <mu-list-item-title>信息详情</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
          <mu-list-item button href="#/collect">
            <mu-list-item-content>
              <mu-list-item-title>信息汇总</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
          <mu-list-item button href="#/settings">
            <mu-list-item-content>
              <mu-list-item-title>设置</mu-list-item-title>
            </mu-list-item-content>
          </mu-list-item>
        </mu-list>
      </mu-menu>
    </mu-appbar>
    <router-view/>
  </div>
</template>

<script>
import Vue from 'vue'
import 'muse-ui/lib/styles/base.less'
import { AppBar, Button, Icon, List, Menu } from 'muse-ui'
import 'muse-ui/lib/styles/theme.less'
Vue.use(AppBar)
Vue.use(Button)
Vue.use(Icon)
Vue.use(List)
Vue.use(Menu)
export default {
  name: 'App'
}
</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
