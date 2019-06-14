import axios from 'axios';
var qs = require('qs');

export default class BaseService {
    constructor() {
        this._path = (window.location.hostname === 'localhost' ?
            'http://localhost:5000/' :
            window.location.origin + '/api/');
    }

    _get(path) {
        return axios.get(this._path + path)
            .then(response => response.data);
    }

    _post(path, data) {
        const config = {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        };

        return axios.post(this._path + path, data, config)
            .then(response => response.data);
    }
}