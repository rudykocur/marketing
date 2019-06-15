from logging import getLogger

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


logger = getLogger(__name__)


def createApp(dbHost: str, dbPort: int):
    logger.info('Connecting to database %s:%s', dbHost, dbPort)

    app = Flask(__name__)
    app.secret_key = b'xk_X-SVU8-83PCkWMMYJr85AnKqacKQ19TqqmRNKny0='
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@{}:{}/marketing'.format(dbHost, dbPort)

    db = SQLAlchemy(app)
    api = Api(app)
    cors = CORS(app, supports_credentials=True)

    return app, api, db
