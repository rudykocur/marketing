/**
 * @param {ContactsService} contactsService
 */
export default function createContactsStore(contactsService) {
    return {
        namespaced: true,

        state: {
            busy: false,
            contacts: [],
        },
        mutations: {
            addContact(state, newContact) {
                state.contacts.push(newContact);
            },

            setContacts(state, newContacts) {
                state.contacts = newContacts;
            },

            removeContactsById(state, toRemoveIds) {
                state.contacts = state.contacts.filter(row => toRemoveIds.indexOf(row.id) < 0);
            },

            setBusy(state, isBusy) {
                state.busy = isBusy;
            }
        },
        actions: {

            createContact: function({commit}, newContact) {
                commit('setBusy', true);

                return contactsService.create(newContact.email, newContact.firstName, newContact.lastName)
                    .then(newContact => {
                        commit('addContact', newContact);
                    })
                    .finally(() => commit('setBusy', false));
            },

            addToGroups: function({commit}, data) {
                commit('setBusy', true);

                return contactsService.addToGroups(
                    data.contacts.map(row => row.id),
                    data.groups,
                )
                    .finally(() => commit('setBusy', false));
            },

            removeContacts: function({commit}, toRemove) {
                commit('setBusy', true);

                let idsToRemove = toRemove.map(row => row.id);

                return contactsService.removeById(idsToRemove)
                    .then(newContacts => {
                        commit('removeContactsById', idsToRemove);
                    })
                    .finally(() => commit('setBusy', false));
            },

            loadContacts: function ({commit, state}) {

                if(state.contacts.length > 0) {
                    return Promise.resolve(state.contacts);
                }

                commit('setBusy', true);

                return contactsService.loadAll()
                    .then(newContacts => {
                        commit('setContacts', newContacts);

                        return newContacts;
                    })
                    .finally(() => commit('setBusy', false));
            }
        }
    }
}