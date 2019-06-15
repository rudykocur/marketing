from flask import request
from injector import Injector

from marketing_api.db.stores import TemplateStore
from marketing_api.resource import SecuredResource, require


class TemplatesHandler(SecuredResource):
    def __init__(self, ctx: Injector):
        self.store = ctx.get(TemplateStore)

    @require('view', 'Templates')
    def get(self):
        result = []

        for template in self.store.getAll():
            result.append({
                'id': template.id,
                'name': template.name,
                'content': template.content,
            })

        return result

    @require('manage', 'Templates')
    def post(self):
        template = self.store.create(request.form['name'], request.form['subject'], request.form['content'])

        self.store.commit()

        return {
            'id': template.id,
            'name': template.name,
            'subject': template.subject,
            'content': template.content,
        }


class TemplatesDeleteHandler(SecuredResource):

    def __init__(self, ctx: Injector):
        self.store = ctx.get(TemplateStore)

    @require('manage', 'Templates')
    def post(self):
        templates = request.form.getlist('templates')

        self.store.delete(list(map(int, templates)))

        self.store.commit()
