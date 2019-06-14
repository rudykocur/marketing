import BaseService from "./BaseService";


export default class SettingsService extends BaseService {
    load() {
        return this._get('server/');
    }

    save(newSettings) {
        let data = new FormData();
        data.set('address', newSettings.address);
        data.set('login', newSettings.login);
        data.set('password', newSettings.password);
        data.set('fromName', newSettings.fromName);
        data.set('fromAddress', newSettings.fromAddress);

        return this._post('server/', data);
    }
}