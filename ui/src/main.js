import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import createStore from './store'
import SettingsService from './services/SettingsService'
import ContactsService from './services/ContactsService'
import GroupsService from './services/GroupsService'
import TemplatesService from './services/TemplatesService'

Vue.config.productionTip = false;

let store = createStore(new SettingsService(), new ContactsService(), new GroupsService(), new TemplatesService());

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
