<template>
    <v-data-table
            class="contactTable"
            v-model="selected"
            :headers="headers"
            :items="items"
            :loading="busy"
            :search="search"
            :select-all="true"
            :pagination.sync="pagination"
            :item-key="item_key"
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
            <tr :active="row.selected" @click="selectionChanged(row)">
                <td>
                    <v-checkbox
                            :input-value="row.selected"
                            primary
                            hide-details
                    ></v-checkbox>
                </td>
                <slot name="row" v-bind:row="row"></slot>
            </tr>
        </template>
        <template v-slot:footer>
            <td :colspan="headers.length + 1">
                <slot name="actions"></slot>
            </td>
        </template>
    </v-data-table>
</template>

<style scoped>
    table.v-table tfoot tr td {
        padding-left: 16px;
    }
</style>

<script>
    export default {
        props: ['busy', 'items', 'item_key', 'headers', 'search', 'default_sort'],
        data: function() {
            return {
                pagination: {
                    sortBy: this.default_sort
                },
                selected: [],
            }
        },
        methods: {
            toggleAll() {
                if (this.selected.length) this.selected = [];
                else this.selected = this.items.slice();

                this.$emit('selection-changed', this.selected);
            },
            changeSort(column) {
                if (this.pagination.sortBy === column) {
                    this.pagination.descending = !this.pagination.descending
                } else {
                    this.pagination.sortBy = column;
                    this.pagination.descending = false
                }
            },
            selectionChanged(row) {
                row.selected = !row.selected;

                this.$emit('selection-changed', this.selected);
            },
        },
        computed: {
        }
    }
</script>