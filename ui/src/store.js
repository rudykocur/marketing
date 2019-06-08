import Vue from 'vue'
import Vuex from 'vuex'

import createSettingsStore from './stores/settings'

Vue.use(Vuex);

export default function createStore(settingsService) {
    return new Vuex.Store({
        modules: {
            settings: createSettingsStore(settingsService),
        }
    })
}
