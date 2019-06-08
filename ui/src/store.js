import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

/**
 * @param {SettingsService} settingsService
 */
function createSettingsStore(settingsService) {
    return {
        namespaced: true,

        state: {
            busy: false,
            settings: {
                address: null,
                password: null,
                fromName: null,
                fromAddress: null,
            }
        },
        mutations: {
            setSettings: (state, settings) => {
                state.settings = settings;
            },
            setBusy(state, isBusy) {
                state.busy = isBusy;
            }
        },
        actions: {
            saveSettings: function ({commit}, newSettings) {
                commit('setBusy', true);

                return settingsService.saveSettings(newSettings)
                    .then(() => commit('setSettings', newSettings))
                    .finally(() => commit('setBusy', false));
            },

            loadSettings: function ({commit, state}) {

                if(state.settings.address) {
                    return Promise.resolve(state.settings);
                }

                commit('setBusy', true);

                return settingsService.loadSettings()
                    .then(newSettings => {
                        commit('setSettings', newSettings);

                        return newSettings;
                    })
                    .finally(() => commit('setBusy', false));
            }
        }
    }
}

export default function createStore(settingsService) {
    return new Vuex.Store({
        modules: {
            settings: createSettingsStore(settingsService),
        }
    })
}
