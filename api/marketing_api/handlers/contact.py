from logging import getLogger

from flask import request
from flask_restful import Resource

from marketing_api.app import db
from marketing_api.model import Contact

_logger = getLogger(__name__)


class ContactsHandler(Resource):
    def get(self):
        result = []

        for contact in Contact.query.all():
            result.append({
                'id': contact.id,
                'email': contact.email,
                'firstName': contact.firstName,
                'lastName': contact.lastName,
            })

        return result

    def post(self):
        contact = Contact(
            email=request.form['email'],
            firstName=request.form['firstName'],
            lastName=request.form['lastName'],
        )
        db.session.add(contact)
        db.session.commit()

        return {
            'id': contact.id,
            'email': contact.email,
            'firstName': contact.firstName,
            'lastName': contact.lastName,
        }


class ContactHandler(Resource):
    def delete(self, contactId):

        contact = Contact.query.get(contactId)
        db.session.delete(contact)

        db.session.commit()
