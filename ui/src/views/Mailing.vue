<template>
    <v-container>
        <h1>Mailing sending page</h1>
        <p>Execute mailing jobs</p>

        <v-card>
            <v-card-title>
                <NewMailingForm
                        v-if="$can('manage', 'Mailing')"
                        ref="form"
                        :enabled="true"
                        @submit="dispatchNewMailing"></NewMailingForm>
            </v-card-title>

            <v-data-table
                    :headers="headers"
                    :items="items">
                <template v-slot:items="row">
                    <td>{{ row.item.templateName }}</td>
                    <td>{{ row.item.groupName }}</td>
                    <td>{{ row.item.total }}</td>
                    <td>{{ row.item.sent }}</td>
                </template>
            </v-data-table>
        </v-card>

    </v-container>
</template>

<script>
    import NewMailingForm from '../components/NewMailingForm.vue'
    import SelectableTable from '../components/SelectableTable.vue'
    import {mapState} from "vuex";

    export default {
        components: {
            SelectableTable,
            NewMailingForm,
        },
        data: () => ({
            search: '',
            headers: [
                {text: 'Template name', value: 'templateName'},
                {text: 'Group name', value: 'groupName'},
                {text: 'To sent', value: 'total'},
                {text: 'Sent mails', value: 'sent'},
            ],
            selected: [],
            intervalId: null,
        }),
        mounted: function() {
            this.$store.dispatch('mailing/loadJobs');

            this.intervalId = setInterval(() => {
                if (this.$can('view', 'Mailing')) {
                    this.$store.dispatch('mailing/loadJobs')
                }
            }, 3000)
        },
        beforeDestroy: function() {
            clearInterval(this.intervalId);
        },
        computed: Object.assign(
            {
            },
            mapState({
                items: state => state.mailing.jobs,
                busy: state => state.mailing.busy,
            })
        ),
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