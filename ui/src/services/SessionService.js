import BaseService from './BaseService';

export default class SessionService extends BaseService{

    load() {
        return this._get('session/')
    }

    login(login, password) {
        let data = new FormData();
        data.set('login', login);
        data.set('password', password);

        return this._post('session/', data);
    }

    logout() {
        let data = new FormData();

        return this._post('session/logout', data);
    }
}