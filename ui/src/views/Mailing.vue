<template>
    <v-container>
        <h1>Mailing sending page</h1>
        <p>Execute mailing jobs</p>

        <v-card>
            <v-card-title>
                <NewMailingForm
                        ref="form"
                        :enabled="true"
                        @submit="dispatchNewMailing"></NewMailingForm>
            </v-card-title>
        </v-card>

    </v-container>
</template>

<script>
    import NewMailingForm from '../components/NewMailingForm.vue'
    import SelectableTable from '../components/SelectableTable.vue'

    export default {
        components: {
            SelectableTable,
            NewMailingForm,
        },
        methods: {
            async dispatchNewMailing(data) {

                try{
                    await this.$store.dispatch('mailing/dispatch', data);
                    this.$refs['form'].close();
                }
                catch(e) {
                    this.$refs.form.setError(e.response.data.message);
                }
            }
        }
    }
</script>