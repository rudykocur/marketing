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
        let data = new FormData();
        ids.forEach(id => data.append('groups', id));

        return this._post('groups/delete', data);
    }
}