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
                            <v-flex md8 text-xs-right>
                                <v-btn color="info" @click="onLogin">Login</v-btn>
                            </v-flex>
                        </v-layout>
                    </v-container>
                </v-form>
        </v-card>
    </v-container>
</template>

<script>

    import defineRightsFor from '../rights';

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
        methods: {
            onLogin() {
                this.$ability.update(defineRightsFor({role: 'admin'}).rules);
                this.$router.push('contacts')
            }
        }
    }
</script>