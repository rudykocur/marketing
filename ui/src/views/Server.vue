<template>

    <v-container>
        <v-snackbar :timeout="5000" :top="true" v-model="showNotification">
            Settings saved
        </v-snackbar>

        <h1>Server configuration page</h1>

        <p>Provide setting for email provider</p>

        <v-card>
            <v-form>
                <v-container>
                    <v-flex md8>
                        <v-text-field
                                :disabled="busy"
                                v-model="formData.address"
                                label="Email server address"></v-text-field>
                        <v-text-field
                                :disabled="busy"
                                v-model="formData.password"
                                label="Password"
                                type="password"></v-text-field>
                        <v-text-field
                                :disabled="busy"
                                v-model="formData.fromName"
                                label="Sender email name"></v-text-field>
                        <v-text-field
                                :disabled="busy"
                                v-model="formData.fromAddress"
                                label="Sender email address"></v-text-field>

                    </v-flex>
                    <v-flex md8 text-xs-right>
                        <v-progress-circular v-if="busy" indeterminate></v-progress-circular>
                        <v-btn color="info" :disabled="busy" @click="saveForm">Save</v-btn>
                    </v-flex>
                </v-container>
            </v-form>
        </v-card>

    </v-container>
</template>

<script>
    import { mapState } from 'vuex'

    export default {
        data: () => ({
            showNotification: false,
            savedOk: false,
            formData: {
                address: null,
                password: null,
                fromName: null,
                fromAddress: null,
            }
        }),

        computed: mapState({
            busy: state => state.settings.busy
        }),

        methods: {
            saveForm: function() {
                this.$store.dispatch('settings/saveSettings', this.formData).then(() => {
                    this.showNotification = true;
                    this.savedOk = true;
                });
            }
        },
        mounted() {
            this.$store.dispatch('settings/loadSettings').then(result => {
                this.formData = result;
            })
        }
    }
</script>