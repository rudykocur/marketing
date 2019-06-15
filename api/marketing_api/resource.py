from functools import wraps

from flask_restful import Resource, abort

from marketing_api.session import SessionManager, AccessRulesBuilder


def checkSession(method):
    action = getattr(method, '__require_action', None)
    objectType = getattr(method, '__require_objType', None)

    manager = SessionManager(AccessRulesBuilder())

    if not manager.getRules().can(action, objectType):
        abort(401, message='Required right: {} to {}'.format(action, objectType))

    return method


class SecuredResource(Resource):
    method_decorators = [checkSession]


def require(action, objectType):
    def real_decorator(f):

        setattr(f, '__require_action', action)
        setattr(f, '__require_objType', objectType)

        return f

    return real_decorator


