<template>
    <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on }">
            <v-btn color="primary"
                   :disabled="!enabled"
                   v-on="on">Run</v-btn>
        </template>

        <v-card>
            <v-card-title>
                <span class="headline">Dispatch new mailing</span>
            </v-card-title>
            <v-card-text>
                <v-form v-model="valid" ref="form">
                    <v-container grid-list-md>
                        <v-layout wrap>
                            <v-flex xs12>
                                <v-select
                                        :items="groups"
                                        v-model="formData.group"
                                        item-text="name"
                                        item-value="id"
                                        :rules="requiredRules"
                                        label="Group"></v-select>
                                <v-select
                                        :items="templates"
                                        v-model="formData.template"
                                        item-text="name"
                                        item-value="id"
                                        :rules="requiredRules"
                                        label="Template"></v-select>
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
                        :disabled="loading">Close</v-btn>
                <v-btn
                        color="blue"
                        flat
                        @click="add"
                        :disabled="loading">Run</v-btn>
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
                template: 1,
                group: 1,
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

                this.$emit('submit', this.formData);

                this.error = null;
            },
        },
        computed: {
            templates() {return this.$store.state.templates.templates},
            groups() {return this.$store.state.groups.groups},
        },

        mounted() {
            this.$store.dispatch('groups/loadGroups');
            this.$store.dispatch('templates/loadTemplates');
        }
    }
</script>