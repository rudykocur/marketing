<template>
    <v-container>
        <h1>Contacts administration page</h1>
        <p>Manage all contacts in database</p>

        <v-card>
            <v-card-title>

                <NewContactForm
                        v-if="$can('manage', 'Contacts')"
                        ref="form"
                        :loading="busy"
                        :enabled="canAddContact"
                        @new-contact="addContact"></NewContactForm>

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
                    default_sort="email"
                    :search="search"
                    :busy="busy"
                    :items="contacts" @selection-changed="selectionChanged">
                <template v-slot:row="{row}">
                    <td>{{ row.item.email }}</td>
                        <td>{{ row.item.firstName }}</td>
                        <td>{{ row.item.lastName }}</td>
                </template>

                <template v-slot:actions>
                    <AddContactsToGroups
                            v-if="$can('manage', 'Contacts')"
                            ref="addGroupsForm"
                            :loading="busy"
                            :enabled="canOperateOnSelectedRows"
                            @submit="addToGroups"></AddContactsToGroups>

                    <v-btn class="deleteButton"
                           v-if="$can('manage', 'Contacts')"
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

<style scoped>
    .v-btn.deleteButton:hover:before {
        background: red;
        opacity: 0.6;
    }
</style>

<script>
    import { mapState } from 'vuex'
    import NewContactForm from '../components/NewContactForm.vue'
    import AddContactsToGroups from '../components/AddContactsToGroups.vue'
    import SelectableTable from '../components/SelectableTable.vue'

    export default {
        components: {
            NewContactForm,
            SelectableTable,
            AddContactsToGroups,
        },
        data: () => ({
            search: '',
            selected: [],
            headers: [
                {text: 'Email address', value: 'email'},
                {text: 'First name', value: 'firstName'},
                {text: 'Last name', value: 'lastName'},
            ],
        }),

        methods: {
            selectionChanged(newSelection) {
                this.selected = newSelection;
            },
            deleteSelected() {
                this.$store.dispatch('contacts/removeContacts', this.selected);
            },
            addContact(data) {
                this.$store.dispatch('contacts/createContact', data).then(() => {
                    this.$refs['form'].close();
                }).catch(fail => {
                    this.$refs['form'].setError('Failed to create new contact.');
                })
            },
            async addToGroups(data) {
                try{
                    await this.$store.dispatch('contacts/addToGroups', {
                        contacts: this.selected,
                        groups: data.groups,
                    });
                    await this.$store.dispatch('groups/loadGroups', true);
                    this.$refs['addGroupsForm'].close();
                }
                catch(e) {
                    this.$refs['addGroupsForm'].setError('Failed to add groups to contacts.');
                }
            }
        },
        computed: Object.assign(
            {
                canOperateOnSelectedRows() {
                    return this.selected.length > 0 && !this.busy
                },
                canAddContact() {return !this.busy},
            },
            mapState({
                contacts: state => state.contacts.contacts,
                busy: state => state.contacts.busy,
            })),

        mounted() {
            this.$store.dispatch('contacts/loadContacts');
            this.$store.dispatch('groups/loadGroups');
        }
    }
</script>