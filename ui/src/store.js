import Vue from 'vue'
import Vuex from 'vuex'

import createSettingsStore from './stores/settings'
import createContactsStore from './stores/contacts'

Vue.use(Vuex);

export default function createStore(settingsService, contactsService) {
    return new Vuex.Store({
        modules: {
            settings: createSettingsStore(settingsService),
            contacts: createContactsStore(contactsService)
        }
    })
}
