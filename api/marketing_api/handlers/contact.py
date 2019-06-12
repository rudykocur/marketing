from logging import getLogger

from flask import request
from flask_restful import Resource
from injector import Injector

from marketing_api.db.stores import ContactStore


_logger = getLogger(__name__)


class ContactsHandler(Resource):
    def __init__(self, ctx: Injector):
        self.store = ctx.get(ContactStore)

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

    def post(self):
        contact = self.store.create(request.form['email'], request.form['firstName'], request.form['lastName'])

        self.store.commit()

        return {
            'id': contact.id,
            'email': contact.email,
            'firstName': contact.firstName,
            'lastName': contact.lastName,
        }


class ContactsDeleteHandler(Resource):

    def __init__(self, ctx: Injector):
        self.store = ctx.get(ContactStore)

    def post(self):
        contacts = request.form.getlist('contacts')

        self.store.delete(list(map(int, contacts)))

        self.store.commit()
