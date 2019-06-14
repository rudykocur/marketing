from injector import Injector

# from marketing_api.app import api

from marketing_api.handlers.contact import ContactsHandler, ContactsDeleteHandler
from marketing_api.handlers.group import GroupsHandler, GroupsDeleteHandler
from marketing_api.handlers.server import ServerHandler
from marketing_api.handlers.session import SessionHandler, SessionLogoutHandler
from marketing_api.handlers.template import TemplatesHandler, TemplatesDeleteHandler
from marketing_api.handlers.mailing import DispatchMailingHandler

from marketing_api.db import model


def setup(injector, api, db):

    model.metadata.create_all(db.engine)

    api.add_resource(ContactsHandler, '/contacts/', resource_class_kwargs={'ctx': injector})
    api.add_resource(ContactsDeleteHandler, '/contacts/delete', resource_class_kwargs={'ctx': injector})
    api.add_resource(GroupsHandler, '/groups/', resource_class_kwargs={'ctx': injector})
    api.add_resource(GroupsDeleteHandler, '/groups/delete', resource_class_kwargs={'ctx': injector})
    api.add_resource(TemplatesHandler, '/templates/', resource_class_kwargs={'ctx': injector})
    api.add_resource(TemplatesDeleteHandler, '/templates/delete', resource_class_kwargs={'ctx': injector})

    api.add_resource(DispatchMailingHandler, '/mailing/dispatch', resource_class_kwargs={'ctx': injector})

    api.add_resource(ServerHandler, '/server/', resource_class_kwargs={'ctx': injector})

    api.add_resource(SessionHandler, '/session/', resource_class_kwargs={'ctx': injector})
    api.add_resource(SessionLogoutHandler, '/session/logout', resource_class_kwargs={'ctx': injector})