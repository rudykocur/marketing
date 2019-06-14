from flask import request
from flask_restful import Resource
from injector import Injector

from marketing_api.session import SessionManager


class SessionHandler(Resource):
    def __init__(self, ctx: Injector):
        self.sessionManager = ctx.get(SessionManager)

    def get(self):
        return self.sessionManager.getUser()

    def post(self):
        self.sessionManager.login(request.form['login'], request.form['password'])

        return self.sessionManager.getUser()


class SessionLogoutHandler(Resource):
    def __init__(self, ctx: Injector):
        self.sessionManager = ctx.get(SessionManager)

    def post(self):
        self.sessionManager.logout()
