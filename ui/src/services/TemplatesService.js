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
}