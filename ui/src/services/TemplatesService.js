import axios from 'axios';
import BaseService from './BaseService';

export default class TemplatesService extends BaseService {

    create(name, subject, content) {
        let data = new FormData();
        data.set('name', name);
        data.set('subject', subject);
        data.set('content', content);

        return this._post('templates/', data);
    }

    loadAll() {
        return this._get('templates/');
    }

    removeById(ids) {
        let data = new FormData();
        ids.forEach(id => data.append('templates', id));

        return this._post('templates/delete', data);
    }
}