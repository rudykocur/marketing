import Vue from 'vue'
import './plugins/vuetify'
import { abilitiesPlugin } from '@casl/vue'
import App from './App.vue'
import router from './router'
import createStore from './store'
import SettingsService from './services/SettingsService'
import ContactsService from './services/ContactsService'
import GroupsService from './services/GroupsService'
import TemplatesService from './services/TemplatesService'
import MailingService from "./services/MailingService";
import SessionService from "./services/SessionService";

import defineRightsFor from './rights';

Vue.config.productionTip = false;

let store = createStore(new SettingsService(), new ContactsService(), new GroupsService(), new TemplatesService(),
    new MailingService(), new SessionService());

Vue.use(abilitiesPlugin, defineRightsFor({}));

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
