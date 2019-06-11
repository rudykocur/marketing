from flask import request
from flask_restful import Resource

from marketing_api.app import db
from marketing_api.model import Group, Template


class TemplatesHandler(Resource):
    def get(self):
        result = []

        for template in Template.query.all():
            result.append({
                'id': template.id,
                'name': template.name,
                'content': template.content,
            })

        return result

    def post(self):
        template = Template(name=request.form['name'], content=request.form['content'])

        db.session.add(template)
        db.session.commit()

        return {
            'id': template.id,
            'name': template.name,
            'content': template.content,
        }


class TemplateHandler(Resource):
    def delete(self, templateId):
        template = Template.query.get(templateId)

        db.session.delete(template)
        db.session.commit()
