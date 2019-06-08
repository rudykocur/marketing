import Vue from 'vue'
import Vuex from 'vuex'

import createSettingsStore from './stores/settings'
import createContactsStore from './stores/contacts'
import createGroupsStore from './stores/groups'

Vue.use(Vuex);

export default function createStore(settingsService, contactsService, groupsService) {
    return new Vuex.Store({
        modules: {
            settings: createSettingsStore(settingsService),
            contacts: createContactsStore(contactsService),
            groups: createGroupsStore(groupsService),
        }
    })
}
