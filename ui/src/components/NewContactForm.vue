<template>
    <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on }">
            <v-btn color="primary"
                   :disabled="!enabled"
                   v-on="on">Add new
            </v-btn>
        </template>

        <v-card>
            <v-card-title>
                <span class="headline">Add new contact</span>
            </v-card-title>
            <v-card-text>
                <v-form v-model="valid" ref="form">
                    <v-container grid-list-md>
                        <v-layout wrap>
                            <v-flex xs12>
                                <v-text-field
                                        label="Email"
                                        v-model="formData.email"
                                        :rules="requiredRules"
                                        required></v-text-field>
                                <v-text-field
                                        label="First name"
                                        v-model="formData.firstName"
                                        :rules="requiredRules"
                                        required></v-text-field>
                                <v-text-field
                                        label="Last name"
                                        v-model="formData.lastName"
                                        :rules="requiredRules"
                                        required></v-text-field>
                            </v-flex>
                        </v-layout>
                    </v-container>
                </v-form>
                <v-alert type="error" :value="error">
                    {{ error }}
                </v-alert>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-progress-circular v-if="loading" indeterminate></v-progress-circular>
                <v-btn
                        flat
                        @click="cancel"
                        :disabled="loading">Close
                </v-btn>
                <v-btn
                        color="blue"
                        flat
                        @click="add"
                        :disabled="loading">Add
                </v-btn>
            </v-card-actions>
        </v-card>

    </v-dialog>


</template>

<script>
    export default {
        props: ['enabled', 'loading'],
        data: () => ({
            dialog: false,
            error: null,
            valid: true,
            formData: {
                email: '',
                firstName: '',
                lastName: '',
            },
            requiredRules: [
                v => !!v || 'Required'
            ],
        }),

        methods: {
            setError(message) {
                this.error = message;
            },
            close() {
                this.dialog = false;
                this.error = null;

                this.$refs['form'].reset();
            },
            cancel() {
                this.dialog = false;
                this.error = null;

                this.$refs['form'].reset();
            },
            add() {
                if(!this.$refs['form'].validate()) {
                    return;
                }

                this.$emit('new-contact', this.formData);

                this.error = null;
            },
        },
        computed: {},

        mounted() {
        }
    }
</script>