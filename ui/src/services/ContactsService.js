import axios from 'axios';
import BaseService from './BaseService';

export default class ContactsService extends BaseService {

    create(email, firstName, lastName) {
        let data = new FormData();
        data.set('email', email);
        data.set('firstName', firstName);
        data.set('lastName', lastName);

        return this._post('contacts/', data);
    }

    loadAll() {
        return this._get('contacts/');
    }

    removeById(ids) {
        return axios.all(ids.map(
            contactId => this._delete('contacts/'+contactId)
        ))
    }
}