#!/usr/bin/python3

from marketing_api.app import app, api, db

from marketing_api.handlers import ContactHandler


api.add_resource(ContactHandler, '/contact/')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, use_reloader=False, port=5000, host="0.0.0.0")
