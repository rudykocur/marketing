import BaseService from './BaseService';
import axios from "axios";

export default class MailingService extends BaseService{
    constructor() {
        super();
    }

    loadAll() {
        return this._get('mailing/');
    }

    dispatch(groupId, templateId) {
        let data = new FormData();
        data.set('groupId', groupId);
        data.set('templateId', templateId);

        return this._post('mailing/dispatch', data);
    }
}