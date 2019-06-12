
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@db/marketing'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@192.168.99.100:32000/marketing'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@192.168.99.100:32000/marketing?charset=utf8mb4'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)
api = Api(app)
cors = CORS(app)
