from flask import request
from flask_restful import Resource
from sqlalchemy.sql.functions import count

from marketing_api.app import db
from marketing_api.model import Group, Contact


class GroupsHandler(Resource):
    def get(self):
        result = []

        query = (
            db.session.query(Group, count(Contact.id))
            .select_from(Group)
            .join(Group.users)
            .group_by(Group.id)
        )

        for group, contactCount in query.all():

            result.append({
                'id': group.id,
                'name': group.name,
                'contacts': contactCount,
            })

        return result

    def post(self):
        group = Group(name=request.form['name'])

        membersList = request.form.getlist('members')

        for memberId in membersList:
            contact = Contact.query.get(memberId)

            group.users.append(contact)

        db.session.add(group)
        db.session.commit()

        return {
            'id': group.id,
            'name': group.name,
            'contacts': len(membersList)
        }


class GroupHandler(Resource):
    def delete(self, groupId):
        group = Group.query.get(groupId)

        db.session.delete(group)
        db.session.commit()
