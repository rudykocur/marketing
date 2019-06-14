/**
 * @param {SessionService} sessionService
 */
export default function createSessionStore(sessionService) {
    return {
        namespaced: true,

        state: {
            busy: false,
            loggedIn: false,
        },
        mutations: {
            setLoggedIn(state, isLogged) {
                state.loggedIn = isLogged;
            },

            setBusy(state, isBusy) {
                state.busy = isBusy;
            }
        },
        actions: {
            login({commit}, data) {
                commit('setBusy', true);

                return sessionService.login(data.login, data.password)
                    .then(session => {

                        commit('setLoggedIn', true);

                        return session;
                    })
                    .finally(() => commit('setBusy', false));
            },

            loadSession({commit}) {

                commit('setBusy', true);

                return sessionService.load()
                    .then(session => {

                        if(session.user) {
                            commit('setLoggedIn', true);
                        }

                        return session
                    })
                    .finally(() => commit('setBusy', false));
            },

            logout({commit}) {

                commit('setBusy', true);

                return sessionService.logout()
                    .then(() => {
                        commit('setLoggedIn', false);
                    })
                    .finally(() => commit('setBusy', false));
            }
        }
    }
}