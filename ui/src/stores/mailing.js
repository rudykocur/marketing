/**
 * @param {MailingService} mailingService
 */
export default function createMailingStore(mailingService) {
    return {
        namespaced: true,

        state: {
            busy: false,
            jobs: [],
        },
        mutations: {
            addJob(state, newJob) {
                state.jobs.push(newJob);
            },

            setBusy(state, isBusy) {
                state.busy = isBusy;
            }
        },
        actions: {
            dispatch({commit}, data) {
                commit('setBusy', true);

                return mailingService.dispatch(data.group, data.template)
                    .then(newJob => {
                        commit('addJob', newJob);

                        return newJob;
                    })
                    .finally(() => commit('setBusy', false));
            },
        }
    }
}