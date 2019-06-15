<template>
    <v-container>
        <h1>Templates configuration page</h1>
        <p>Define templates for sending mailing</p>

        <v-card>
            <v-card-title>

                <NewTemplateForm
                        v-if="$can('manage', 'Templates')"
                        ref="form"
                        :loading="busy"
                        :enabled="canAddTemplate"
                        @new-template="addTemplate"></NewTemplateForm>
                <v-spacer></v-spacer>

                <v-text-field
                        v-model="search"
                        append-icon="search"
                        label="Search"
                        single-line
                        hide-details
                ></v-text-field>
            </v-card-title>


            <SelectableTable
                    :headers="headers"
                    item_key="id"
                    default_sort="name"
                    :search="search"
                    :busy="busy"
                    :items="templates" @selection-changed="selectionChanged">
                <template v-slot:row="{row}">
                    <td>{{ row.item.name }}</td>
                    <td>{{ row.item.subject }}</td>
                    <td @click.stop="row.expanded = !row.expanded" class="clickable">
                        <v-icon v-if="!row.expanded">keyboard_arrow_down</v-icon>
                        <v-icon v-if="row.expanded">keyboard_arrow_up</v-icon>
                    </td>
                </template>

                <template v-slot:actions>
                    <v-btn class="deleteButton"
                           v-if="$can('manage', 'Templates')"
                           @click="deleteSelected"
                           :disabled="!canOperateOnSelectedRows">
                        <v-icon>delete</v-icon>
                        Delete
                    </v-btn>
                </template>
                <template v-slot:expand="{row}">
                    <v-card flat>
                        <v-card-text>{{row.item.content}}</v-card-text>
                    </v-card>
                </template>
            </SelectableTable>
        </v-card>
    </v-container>
</template>

<style scoped>
    .clickable .v-icon {
        cursor: pointer;
    }
</style>

<script>
    import { mapState } from 'vuex'
    import SelectableTable from '../components/SelectableTable.vue'
    import NewTemplateForm from '../components/NewTemplateForm.vue'

    export default {
        components: {
            SelectableTable,
            NewTemplateForm,
        },

        mounted() {
            this.$store.dispatch('templates/loadTemplates')
        },

        data: () => ({
            search: '',
            headers: [
                {text: 'Name', value: 'name'},
                {text: 'Subject', value: 'subject'},
                {text: '', value: '', sortable: false},

            ],
            selected: [],
        }),
        methods: {
            deleteSelected() {
                this.$store.dispatch('templates/removeTemplates', this.selected);
            },
            selectionChanged(newSelection) {
                this.selected = newSelection;
            },
            async addTemplate(data) {
                try{
                    await this.$store.dispatch('templates/createTemplate', data);
                    this.$refs['form'].close();
                }
                catch(e) {
                    this.$refs.form.setError('Failed to create new template');
                }
            },
        },
        computed: Object.assign(
            {
                canOperateOnSelectedRows() {
                    return this.selected.length > 0 && !this.busy
                },
                canAddTemplate() {return !this.busy},
            },
            mapState({
                templates: state => state.templates.templates,
                busy: state => state.templates.busy,
            })
        ),
    }
</script>