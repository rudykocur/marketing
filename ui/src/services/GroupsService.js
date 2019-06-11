import BaseService from './BaseService';
import axios from "axios";

export default class GroupsService extends BaseService{
    constructor() {
        super();
    }

    create(name, members) {
        let data = new FormData();
        data.set('name', name);
        members.forEach(member => data.append('members', member));

        return this._post('groups/', data);
    }

    loadAll() {
        return this._get('groups/');
    }

    removeById(ids) {
        return axios.all(ids.map(
            groupId => this._delete('groups/'+groupId)
        ))
    }
}