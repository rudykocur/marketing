import axios from 'axios';
var qs = require('qs');

class ServiceBase {
    constructor() {
        this._path = 'http://localhost:5000/'
    }

    _get(path) {
        return axios.get(this._path + path)
            .then(response => response.data);
    }

    _post(path, data) {
        const config = {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        };

        return axios.post(this._path + path, qs.stringify(data), config)
            .then(response => response.data);
    }
}

export default class ContactsService extends ServiceBase {

    constructor() {
        super();

        this._id = 4;
    }

    create(email, firstName, lastName) {
        return this._post('contact/', {
            email: email,
            firstName: firstName,
            lastName: lastName,
        });
    }

    loadAll() {
        return this._get('contact/');
    }

    removeById(ids) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve();
            }, 1000)
        })
    }
}