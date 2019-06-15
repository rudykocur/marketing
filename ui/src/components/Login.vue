<template>
    <v-container>
        <h1>Login</h1>
        <p>Speak friend, and enter</p>

        <v-card>
                <v-form ref="form">
                    <v-container grid-list-md>
                        <v-layout wrap>
                            <v-flex md8>
                                <v-text-field
                                        label="Login"
                                        v-model="formData.login"
                                        :rules="requiredRules"
                                        required></v-text-field>

                                <v-text-field
                                        label="Password"
                                        v-model="formData.password"
                                        :rules="requiredRules"
                                        type="password"
                                        required></v-text-field>
                            </v-flex>
                            <v-flex md8>
                                <v-alert type="error" :value="error">
                                    {{ error }}
                                </v-alert>
                            </v-flex>
                            <v-flex md8 text-xs-right>
                                <v-progress-circular
                                        v-if="busy"
                                        indeterminate></v-progress-circular>
                                <v-btn
                                        color="info"
                                        :disabled="busy"
                                        @click="onLogin">Login</v-btn>
                            </v-flex>
                        </v-layout>
                    </v-container>
                </v-form>
        </v-card>
    </v-container>
</template>

<script>

    import defineRightsFor from '../rights';
    import {mapState} from "vuex";

    export default {
        data: () => ({
            error: null,
            valid: true,
            formData: {
                login: '',
                password: [],
            },
            requiredRules: [
                v => !!v || 'Required'
            ],
        }),
        computed: Object.assign(
            {},
            mapState({
                busy: state => state.session.busy,
            })
        ),
        methods: {
            async onLogin() {
                this.error = '';

                let session = await this.$store.dispatch('session/login', this.formData);

                if(!session.role) {
                    this.error = 'Invalid login/password';
                    this.formData.login = '';
                    this.formData.password = '';
                }

                this.$ability.update(defineRightsFor(session).rules);
            }
        }
    }
</script>