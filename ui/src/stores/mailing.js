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

            setJobs(state, newJobs) {
                state.jobs = newJobs;
            },

            setBusy(state, isBusy) {
                state.busy = isBusy;
            }
        },
        actions: {
            loadJobs({commit, state}) {

                commit('setBusy', true);

                return mailingService.loadAll()
                    .then(newJobs => {
                        commit('setJobs', newJobs);

                        return newJobs;
                    })
                    .finally(() => commit('setBusy', false));
            },

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