import axios from 'axios';
var qs = require('qs');

axios.defaults.withCredentials = true;

export default class BaseService {
    constructor() {
        this._path = (window.location.hostname === '192.168.56.1' ?
            'http://192.168.56.1:5000/' :
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