from flask import request
from injector import Injector

from marketing_api.db.stores import GroupStore
from marketing_api.resource import SecuredResource, require


class GroupsHandler(SecuredResource):
    def __init__(self, ctx: Injector):
        self.store = ctx.get(GroupStore)

    @require('view', 'Groups')
    def get(self):
        result = []

        for group in self.store.getAll():

            result.append({
                'id': group.id,
                'name': group.name,
                'contacts': group.contacts,
            })

        return result

    @require('manage', 'Groups')
    def post(self):
        group = self.store.create(
            request.form['name'],
            list(map(int, request.form.getlist('members')))
        )

        self.store.commit()

        return {
            'id': group.id,
            'name': group.name,
            'contacts': group.contacts,
        }


class GroupsDeleteHandler(SecuredResource):

    def __init__(self, ctx: Injector):
        self.store = ctx.get(GroupStore)

    @require('manage', 'Groups')
    def post(self):
        groups = request.form.getlist('groups')

        self.store.delete(list(map(int, groups)))

        self.store.commit()
