#!/usr/bin/python3

import argparse
import logging

from injector import Injector, singleton, Binder

from marketing_api.app import createApp
from marketing_api import startup
from marketing_api.db.model import Database

logging.basicConfig()

logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
logging.getLogger().setLevel(logging.INFO)


parser = argparse.ArgumentParser(description='Start Marketing backend server')
parser.add_argument("--dbhost", help="database host to connect", default='db')
parser.add_argument("--dbport", type=int, help="database port to connect", default=3306)

args = parser.parse_args()

if __name__ == '__main__':
    app, api, db = createApp(args.dbhost, args.dbport)

    def databaseProvider(binder: Binder):
        binder.bind(Database, to=db, scope=singleton)

    injector = Injector([databaseProvider])

    startup.setup(injector, api, db)

    app.run(debug=True, use_reloader=False, port=5000, host="0.0.0.0")
