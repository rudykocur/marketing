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
                <v-btn v-if="$can('view', 'Server')" flat to="/server">Server</v-btn>
                <v-btn v-if="$can('view', 'Contacts')" flat to="/contacts">Contacts</v-btn>
                <v-btn v-if="$can('view', 'Groups')" flat to="/groups">Groups</v-btn>
                <v-btn v-if="$can('view', 'Templates')" flat to="/templates">Templates</v-btn>
                <v-btn v-if="$can('view', 'Mailing')" flat to="/mailing">Mailing</v-btn>
                <v-btn v-if="$can('view', 'Logout')" flat class="logout"  @click="logout">
                    <v-icon>power_settings_new</v-icon>
                </v-btn>
            </v-toolbar-items>
        </v-toolbar>

        <v-content>
            <router-view/>
        </v-content>
    </v-app>
</template>

<style scoped>
    .logout {
        padding: 8px;
        min-width: 0;
    }
</style>

<script>

    import defineRightsFor from './rights';

    export default {
        name: 'App',
        data () {
            return {
                //
            }
        },
        methods: {
            logout() {
                this.$ability.update(defineRightsFor({}).rules);
                this.$router.push('/')
            }
        },
    }
</script>
