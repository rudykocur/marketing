<template>
    <v-container>
        <h1>Groups administration page</h1>
        <p>Create groups and manage contacts assignments</p>

        <v-card>
            <v-card-title>

                <NewGroupForm
                        v-if="$can('manage', 'Groups')"
                        ref="form"
                        :loading="busy"
                        :enabled="canAddGroup"
                        @new-group="addGroup"></NewGroupForm>

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
                    :items="groups" @selection-changed="selectionChanged">
                <template v-slot:row="{row}">
                    <td>{{ row.item.name }}</td>
                    <td>{{ row.item.contacts}}</td>
                </template>

                <template v-slot:actions>
                    <v-btn class="deleteButton"
                           v-if="$can('manage', 'Groups')"
                           @click="deleteSelected"
                           :disabled="!canOperateOnSelectedRows">
                        <v-icon>delete</v-icon>
                        Delete
                    </v-btn>
                </template>
            </SelectableTable>
        </v-card>
    </v-container>
</template>

<script>
    import { mapState } from 'vuex'
    import NewGroupForm from '../components/NewGroupForm.vue'
    import SelectableTable from '../components/SelectableTable.vue'

    export default {
        components: {
            SelectableTable,
            NewGroupForm,
        },

        mounted() {
            this.$store.dispatch('groups/loadGroups')
        },

        data: () => ({
            search: '',
            headers: [
                {text: 'Group name', value: 'name'},
                {text: 'Contacts', value: 'contacts'},
            ],
            selected: [],
        }),
        methods: {
            deleteSelected() {
                this.$store.dispatch('groups/removeGroups', this.selected);
            },
            selectionChanged(newSelection) {
                this.selected = newSelection;
            },
            async addGroup(data) {

                try{
                    await this.$store.dispatch('groups/createGroup', data);
                    this.$refs['form'].close();
                }
                catch(e) {
                    this.$refs.form.setError('Failed to create new group');
                }

            },
        },
        computed: Object.assign(
            {
                canOperateOnSelectedRows() {
                    return this.selected.length > 0 && !this.busy
                },
                canAddGroup() {return !this.busy},
            },
            mapState({
                groups: state => state.groups.groups,
                busy: state => state.groups.busy,
            })
        ),
    }
</script>