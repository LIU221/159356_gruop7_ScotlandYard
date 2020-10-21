import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

// import  element
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

// import axios
import axios from 'axios'
import VueAxios from 'vue-axios'
// Vue.prototype.$axios = axios
Vue.use(VueAxios, axios);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
