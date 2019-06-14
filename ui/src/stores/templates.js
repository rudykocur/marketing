/**
 * @param {TemplatesService} templatesService
 */
export default function createTemplatesStore(templatesService) {
    return {
        namespaced: true,

        state: {
            busy: false,
            templates: [],
        },
        mutations: {
            addTemplate(state, newTemplate) {
                state.templates.push(newTemplate);
            },

            setTemplates(state, newTemplates) {
                state.templates = newTemplates;
            },

            setBusy(state, isBusy) {
                state.busy = isBusy;
            }
        },
        actions: {

            createTemplate({commit}, data) {
                commit('setBusy', true);

                return templatesService.create(data.name, data.subject, data.content)
                    .then(newTemplate => {
                        commit('addTemplate', newTemplate);

                        return newTemplate;
                    })
                    .finally(() => commit('setBusy', false));
            },

            loadTemplates({commit, state}) {

                if(state.templates.length > 0) {
                    return Promise.resolve(state.templates);
                }

                commit('setBusy', true);

                return templatesService.loadAll()
                    .then(newTemplates => {
                        commit('setTemplates', newTemplates);

                        return newTemplates;
                    })
                    .finally(() => commit('setBusy', false));
            }
        }
    }
}