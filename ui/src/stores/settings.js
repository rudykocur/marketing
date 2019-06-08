/**
 * @param {SettingsService} settingsService
 */
export default function createSettingsStore(settingsService) {
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

                return settingsService.save(newSettings)
                    .then(() => commit('setSettings', newSettings))
                    .finally(() => commit('setBusy', false));
            },

            loadSettings: function ({commit, state}) {

                if(state.settings.address) {
                    return Promise.resolve(state.settings);
                }

                commit('setBusy', true);

                return settingsService.load()
                    .then(newSettings => {
                        commit('setSettings', newSettings);

                        return newSettings;
                    })
                    .finally(() => commit('setBusy', false));
            }
        }
    }
}