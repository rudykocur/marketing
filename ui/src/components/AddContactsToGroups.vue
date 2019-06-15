<template>
    <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on }">
            <v-btn
                   :disabled="!enabled"
                   v-on="on"><v-icon>group_add</v-icon><span>Set groups</span>
            </v-btn>
        </template>

        <v-card>
            <v-card-title>
                <span class="headline">Set groups for users</span>
            </v-card-title>
            <v-card-text>
                <v-form v-model="valid" ref="form">
                    <v-container grid-list-md>
                        <v-layout wrap>
                            <v-flex xs12>
                                <v-autocomplete
                                        label="Groups"
                                        multiple
                                        :items="allGroups"
                                        item-text="name"
                                        item-value="id"
                                        v-model="formData.groups">
                                </v-autocomplete>
                                <p>
                                    Select groups that will be set on users. Previous assignmnets will be removed.
                                </p>
                            </v-flex>
                        </v-layout>
                    </v-container>
                </v-form>
                <v-alert type="error">
                    {{ errorMessage }}
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
            errorMessage: null,
            valid: true,
            formData: {
                groups: [],
            },
            requiredRules: [
                v => !!v || 'Required'
            ],
        }),

        methods: {
            setError(message) {
                this.errorMessage = message;
            },
            close() {
                this.dialog = false;
                this.errorMessage = null;

                this.$refs['form'].reset();
            },
            cancel() {
                this.dialog = false;
                this.errorMessage = null;

                this.$refs['form'].reset();
            },
            add() {
                if(!this.$refs['form'].validate()) {
                    return;
                }

                this.$emit('submit', this.formData);

                this.errorMessage = null;
            },
        },
        computed: {
            allGroups() {
                return this.$store.state.groups.groups;
            }
        },

        mounted() {
        }
    }
</script>