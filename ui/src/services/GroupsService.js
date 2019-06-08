export default class GroupsService {
    constructor() {
        this._id = 4;
    }

    create(name, members) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve({id: this._id++, name: name, contacts: members.length},);
            }, 1000)
        })
    }

    loadAll() {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve([
                    {id: 1, name: 'Early adopters', contacts: 10},
                    {id: 2, name: 'Beta testers', contacts: 5},
                    {id: 3, name: 'VIP users', contacts: 2},
                ]);
            }, 1000)
        })
    }
}