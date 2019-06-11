#!/usr/bin/python3

import logging
import os

from marketing_api.app import app, api, db

from marketing_api.handlers.contact import ContactsHandler, ContactHandler
from marketing_api.handlers.group import GroupsHandler, GroupHandler
from marketing_api.handlers.template import TemplatesHandler, TemplateHandler
from marketing_api.model import Template

logging.basicConfig()

logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
logging.getLogger().setLevel(logging.INFO)

api.add_resource(ContactsHandler, '/contacts/')
api.add_resource(ContactHandler, '/contacts/<contactId>')
api.add_resource(GroupsHandler, '/groups/')
api.add_resource(GroupHandler, '/groups/<groupId>')
api.add_resource(TemplatesHandler, '/templates/')
api.add_resource(TemplateHandler, '/templates/<templateId>')


def populateDb():
    from marketing_api.model import Contact, Group

    janek = Contact(email='jk@gmail.com', firstName='janek', lastName='kowalski')
    mietek = Contact(email='mt@gmail.com', firstName='mietek', lastName='trąba')

    group1 = Group(name='group 1')
    group2 = Group(name='group 2')

    tmpl1 = Template(name='Powitanie', content='Powtać waszmościa!')
    tmpl2 = Template(name='Nowy ekscytujący produkt', content='Lorem ipsum dolor sit amet')

    db.session.add(janek)
    db.session.add(mietek)
    db.session.add(group1)
    db.session.add(group2)
    db.session.add(tmpl1)
    db.session.add(tmpl2)

    group1.users.append(janek)
    group2.users.append(janek)
    group2.users.append(mietek)

    db.session.commit()


if __name__ == '__main__':
    if not os.path.exists(os.path.join('marketing_api', 'test.db')):
        db.create_all()
        populateDb()

    app.run(debug=True, use_reloader=False, port=5000, host="0.0.0.0")
