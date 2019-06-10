<template>
    <v-container>
        <h1>Mailing sending page</h1>
        <p>Execute mailing jobs</p>

        <v-card>
            <v-card-title>
                <NewMailingForm :enabled="true" @submit="dispatchNewMailing"></NewMailingForm>
            </v-card-title>
        </v-card>

    </v-container>
</template>

<script>
    import { mapState } from 'vuex'
    import NewMailingForm from '../components/NewMailingForm.vue'
    import SelectableTable from '../components/SelectableTable.vue'

    export default {
        components: {
            SelectableTable,
            NewMailingForm,
        },
        methods: {
            dispatchNewMailing(data) {
                console.log('WILL DISPATCH', data)
            }
        }
    }
</script>