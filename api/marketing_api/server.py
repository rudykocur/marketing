#!/usr/bin/python3

import logging

from injector import Injector

from marketing_api.app import app, api

from marketing_api.handlers.contact import ContactsHandler, ContactsDeleteHandler
from marketing_api.handlers.group import GroupsHandler, GroupsDeleteHandler
from marketing_api.handlers.template import TemplatesHandler, TemplatesDeleteHandler
from marketing_api.handlers.mailing import MailingHandler

logging.basicConfig()

logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
logging.getLogger().setLevel(logging.INFO)

injector = Injector()


api.add_resource(ContactsHandler, '/contacts/', resource_class_kwargs={'ctx': injector})
api.add_resource(ContactsDeleteHandler, '/contacts/delete', resource_class_kwargs={'ctx': injector})
api.add_resource(GroupsHandler, '/groups/', resource_class_kwargs={'ctx': injector})
api.add_resource(GroupsDeleteHandler, '/groups/delete', resource_class_kwargs={'ctx': injector})
api.add_resource(TemplatesHandler, '/templates/', resource_class_kwargs={'ctx': injector})
api.add_resource(TemplatesDeleteHandler, '/templates/delete', resource_class_kwargs={'ctx': injector})

api.add_resource(MailingHandler, '/mailing/', resource_class_kwargs={'ctx': injector})


if __name__ == '__main__':
    from marketing_api.db import model
    from marketing_api.app import db

    db.create_all()

    app.run(debug=True, use_reloader=False, port=5000, host="0.0.0.0")
