<template>
    <v-container>
        <h1>Contacts administration page</h1>
        <p>Manage all contacts in database</p>

        <v-card>
            <v-card-title>

                <NewContactForm
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

            <v-data-table
                    v-model="selected"
                    :headers="headers"
                    :items="contacts"
                    :loading="busy"
                    :search="search"
                    :select-all="true"
                    :pagination.sync="pagination"
                    item-key="id"
            >
                <template v-slot:headers="props">
                    <tr>
                        <th>
                            <v-checkbox
                                    :input-value="props.all"
                                    :indeterminate="props.indeterminate"
                                    primary
                                    hide-details
                                    @click.stop="toggleAll"
                            ></v-checkbox>
                        </th>
                        <th
                                v-for="header in props.headers"
                                :key="header.text"
                                :class="['column sortable', pagination.descending ? 'desc' : 'asc', header.value === pagination.sortBy ? 'active' : '']"
                                @click="changeSort(header.value)"
                        >
                            <v-icon small>arrow_upward</v-icon>
                            {{ header.text }}
                        </th>
                    </tr>
                </template>
                <template v-slot:items="row">
                    <tr :active="row.selected" @click="row.selected = !row.selected">
                        <td>
                            <v-checkbox
                                    :input-value="row.selected"
                                    primary
                                    hide-details
                            ></v-checkbox>
                        </td>
                        <td>{{ row.item.email }}</td>
                        <td>{{ row.item.firstName }}</td>
                        <td>{{ row.item.lastName }}</td>
                    </tr>
                </template>
                <template v-slot:footer>
                    <td :colspan="headers.length + 1" style="padding-left: 16px" >
                        <v-btn color="warning"
                               @click="deleteSelected"
                               :disabled="!canDeleteContacts">Delete selected</v-btn>
                    </td>
                </template>
            </v-data-table>
        </v-card>
    </v-container>
</template>

<script>
    import { mapState } from 'vuex'
    import NewContactForm from '../components/NewContactForm.vue'

    export default {
        components: {
            NewContactForm
        },
        data: () => ({
            search: '',
            dialog: false,
            pagination: {
                sortBy: 'email'
            },
            selected: [],
            headers: [
                {text: 'Email address', value: 'email'},
                {text: 'First name', value: 'firstName'},
                {text: 'Last name', value: 'lastName'},
            ],
        }),

        methods: {
            toggleAll() {
                if (this.selected.length) this.selected = [];
                else this.selected = this.contacts.slice()
            },
            deleteSelected() {
                this.$store.dispatch('contacts/removeContacts', this.selected);
            },
            addContact(data) {
                this.$store.dispatch('contacts/createContact', data).then(() => {
                    this.$refs['form'].close();
                }).catch(fail => {
                    this.$refs['form'].setError(fail);
                })
            },
        },
        computed: Object.assign(
            {
                canDeleteContacts() {return this.selected.length > 0 && !this.busy},
                canAddContact() {return !this.busy},
            },
            mapState({
                contacts: state => state.contacts.contacts,
                busy: state => state.contacts.busy,
            })),

        mounted() {
            this.$store.dispatch('contacts/loadContacts')
        }
    }
</script>