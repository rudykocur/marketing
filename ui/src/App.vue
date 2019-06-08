<template>
  <v-app>
    <v-toolbar app>
      <router-link tag="div" to="/">
        <v-toolbar-title class="headline text-uppercase">
        <span>Marketing platform</span>
      </v-toolbar-title>
      </router-link>

      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat to="/server">Server</v-btn>
        <v-btn flat to="/contacts">Contacts</v-btn>
        <v-btn flat to="/groups">Groups</v-btn>
        <v-btn flat to="/templates">Templates</v-btn>
        <v-btn flat to="/mailing">Mailing</v-btn>
      </v-toolbar-items>
    </v-toolbar>

    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  data () {
    return {
      //
    }
  }
}
</script>
