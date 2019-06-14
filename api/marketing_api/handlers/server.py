from flask import request
from flask_restful import Resource
from injector import Injector

from marketing_api.db.stores import ServerStore
from marketing_api.encrypter import Encrypter


class ServerHandler(Resource):
    def __init__(self, ctx: Injector):
        self.store = ctx.get(ServerStore)
        self.encrypter = ctx.get(Encrypter)

    def get(self):
        server = self.store.get()

        if not server:
            return {
                'address': '',
                'login': '',
                'password': '',
                'fromAddress': '',
                'fromName': '',
            }

        return {
            'address': server.address,
            'login': server.login,
            'password': self.encrypter.decrypt(server.password),
            'fromAddress': server.fromAddress,
            'fromName': server.fromName,
        }

    def post(self):
        self.store.set(
            request.form['address'],
            request.form['login'],
            self.encrypter.encrypt(request.form['password']),
            request.form['fromAddress'],
            request.form['fromName'],
        )

        self.store.commit()
