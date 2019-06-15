from collections import defaultdict
from typing import List

from flask import session
from injector import inject


class AccessRules(object):
    def __init__(self):
        self._allowed = defaultdict(list)

    def add(self, actions: List[str], objects: List[str]) -> None:
        for action in actions:
            for object in objects:
                self._allowed[action].append(object)

    def can(self, action: str, obj: str) -> bool:
        objects = self._allowed.get(action, [])

        return obj in objects


class AccessRulesBuilder(object):
    def __init__(self):
        pass

    def build(self, role: str) -> AccessRules:
        rules = AccessRules()

        if role == 'admin':
            rules.add(['view', 'manage'], ['Contacts', 'Groups', 'Templates', 'Mailing', 'Server'])

        elif role == 'agent':
            rules.add(['view', 'manage'], ['Contacts', 'Groups'])
            rules.add(['view'], ['Mailing', 'Templates'])

        elif role == 'user':
            rules.add(['view'], ['Contacts', 'Groups', 'Mailing', 'Templates'])

        return rules


class SessionManager(object):
    """
    Pseudo in-memory session manager. By using dependency to some kind of "UserStore" it could authenticate in
    users from database.
    """

    @inject
    def __init__(self, builder: AccessRulesBuilder):
        self.builder = builder

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

    def getRules(self) -> AccessRules:
        return self.builder.build(session.get('role'))

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
