import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Server from './views/Server.vue'
import Contacts from './views/Contacts.vue'
import Groups from './views/Groups.vue'
import Mailing from './views/Mailing.vue'
import Templates from './views/Templates.vue'

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/server',
      name: 'server',
      component: Server
    },
    {
      path: '/contacts',
      name: 'contacts',
      component: Contacts
    },
    {
      path: '/groups',
      name: 'groups',
      component: Groups
    },
    {
      path: '/mailing',
      name: 'mailing',
      component: Mailing
    },
    {
      path: '/templates',
      name: 'templates',
      component: Templates
    },
  ]
})
