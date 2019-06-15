from logging import getLogger

from flask import request
from injector import Injector

from marketing_api.db.stores import ContactStore
from marketing_api.resource import SecuredResource, require

_logger = getLogger(__name__)


class ContactsHandler(SecuredResource):
    def __init__(self, ctx: Injector):
        self.store = ctx.get(ContactStore)

    @require('view', 'Contacts')
    def get(self):
        result = []

        for contact in self.store.getAll():
            result.append({
                'id': contact.id,
                'email': contact.email,
                'firstName': contact.firstName,
                'lastName': contact.lastName,
            })

        return result

    @require('manage', 'Contacts')
    def post(self):
        contact = self.store.create(request.form['email'], request.form['firstName'], request.form['lastName'])

        self.store.commit()

        return {
            'id': contact.id,
            'email': contact.email,
            'firstName': contact.firstName,
            'lastName': contact.lastName,
        }


class ContactsDeleteHandler(SecuredResource):

    def __init__(self, ctx: Injector):
        self.store = ctx.get(ContactStore)

    @require('manage', 'Contacts')
    def post(self):
        contacts = request.form.getlist('contacts')

        self.store.delete(list(map(int, contacts)))

        self.store.commit()
