import Vue from 'vue'
import router from './router'
import ElementUI from 'element-ui';
import VueCookie from 'vue-cookie';
import 'element-ui/lib/theme-chalk/index.css';


Vue.use(ElementUI)
Vue.use(VueCookie)
Vue.config.productionTip = false

import App from './App.vue'

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')


