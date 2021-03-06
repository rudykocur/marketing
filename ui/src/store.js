import Vue from 'vue'
import Vuex from 'vuex'

import createSettingsStore from './stores/settings'
import createContactsStore from './stores/contacts'
import createGroupsStore from './stores/groups'
import createTemplatesStore from './stores/templates'
import createMailingStore from './stores/mailing'
import createSessionStore from "./stores/session";

Vue.use(Vuex);

export default function createStore(settingsService, contactsService, groupsService, templatesService, mailingService,
                                    sessionService) {
    return new Vuex.Store({
        modules: {
            settings: createSettingsStore(settingsService),
            contacts: createContactsStore(contactsService),
            groups: createGroupsStore(groupsService),
            templates: createTemplatesStore(templatesService),
            mailing: createMailingStore(mailingService),
            session: createSessionStore(sessionService)
        }
    })
}
