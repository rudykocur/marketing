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
            <template v-if="initLogin">
                <v-container fill-height grid-list-md text-xs-center>
                    <v-layout row wrap align-center>
                        <v-flex>
                            <v-progress-circular indeterminate></v-progress-circular>
                        </v-flex>
                    </v-layout>
                </v-container>
            </template>
            <template v-else-if="loggedIn">
                <router-view/>
            </template>
            <template v-else>
                <Login></Login>
            </template>
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
    import Login from './components/Login.vue'
    import defineRightsFor from './rights';
    import {mapState} from "vuex";

    export default {
        name: 'MarketingApp',
        components: {
            Login,
        },
        data () {
            return {
                initLogin: true,
            }
        },
        mounted: async function() {
            let session = await this.$store.dispatch('session/loadSession');

            this.$ability.update(defineRightsFor(session).rules);

            this.initLogin = false;
        },
        computed: Object.assign(
            {},
            mapState({
                loggedIn: state => state.session.loggedIn,
                busy: state => state.session.busy,
            })
        ),
        methods: {
            async logout() {
                await this.$store.dispatch('session/logout');

                this.$ability.update(defineRightsFor({}).rules);
            }
        },
    }
</script>
