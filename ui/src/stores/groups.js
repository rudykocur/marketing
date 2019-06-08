/**
 * @param {GroupsService} groupsService
 */
export default function createGroupsStore(groupsService) {
    return {
        namespaced: true,

        state: {
            busy: false,
            groups: [],
        },
        mutations: {
            addGroup(state, newGroup) {
                state.groups.push(newGroup);
            },

            setGroups(state, newGroups) {
                state.groups = newGroups;
            },

            setBusy(state, isBusy) {
                state.busy = isBusy;
            }
        },
        actions: {

            createGroup({commit}, data) {
                commit('setBusy', true);

                return groupsService.create(data.name, data.members)
                    .then(newGroup => {
                        commit('addGroup', newGroup);

                        return newGroup;
                    })
                    .finally(() => commit('setBusy', false));
            },

            loadGroups({commit, state}) {

                if(state.groups.length > 0) {
                    return Promise.resolve(state.groups);
                }

                commit('setBusy', true);

                return groupsService.loadAll()
                    .then(newGroups => {
                        commit('setGroups', newGroups);

                        return newGroups;
                    })
                    .finally(() => commit('setBusy', false));
            }
        }
    }
}