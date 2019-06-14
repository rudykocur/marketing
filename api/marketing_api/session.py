from flask import session


class SessionManager(object):
    """
    Pseudo in-memory session manager. By using dependency to some kind of "UserStore" it could authenticate in
    users from database.
    """
    def __init__(self):
        self.users = {
            'admin': {
                'role': 'admin',
                'password': 'admin',
            },
            'agent': {
                'role': 'agent',
                'password': 'agent',
            },
            'user': {
                'role': 'user',
                'password': 'user',
            },
        }

    def login(self, username, password):

        if username not in self.users:
            return None

        if password != self.users[username]['password']:
            return None

        session['role'] = self.users[username]['role']
        session['user'] = username

    def logout(self):
        if 'role' in session:
            del session['role']

        if 'user' in session:
            del session['user']

    def getUser(self):
        return {
            'user': session.get('user'),
            'role': session.get('role'),
        }
