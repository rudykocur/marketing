from collections import namedtuple
from typing import List

from injector import inject
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import count

from marketing_api.db.model import contacts, groups, contact_to_group, templates, mailing_jobs, Database


class DataStore(object):

    @inject
    def __init__(self, db: Database):
        self.db = db

    @property
    def session(self) -> Session:
        return self.db.session

    def commit(self):
        self.session.commit()


ContactDTO = namedtuple('ContactDTO', ['id', 'email', 'firstName', 'lastName'])
GroupDTO = namedtuple('GroupDTO', ['id', 'name', 'contacts'])
TemplateDTO = namedtuple('TemplateDTO', ['id', 'name', 'content'])


class ContactStore(DataStore):
    def create(self, email: str, firstName: str, lastName: str) -> ContactDTO:
        result = self.session.execute(contacts.insert().values(email=email, firstName=firstName, lastName=lastName))

        return ContactDTO(result.inserted_primary_key[0], email, firstName, lastName)

    def getByGroup(self, groupId: int):
        query = (
            select(
                columns=contacts.c,
                whereclause=contact_to_group.c.group_id == groupId
            )
            .select_from(contacts.join(contact_to_group))
        )

        rows = self.session.execute(query)

        return [ContactDTO(
            row[contacts.c.id],
            row[contacts.c.email],
            row[contacts.c.firstName],
            row[contacts.c.lastName],
        ) for row in rows]

    def getAll(self) -> List[ContactDTO]:
        rows = self.session.execute(select(contacts.c))

        return [ContactDTO(
            row[contacts.c.id],
            row[contacts.c.email],
            row[contacts.c.firstName],
            row[contacts.c.lastName],
        ) for row in rows]

    def delete(self, contactIds: List[int]):
        self.session.execute(contacts.delete().where(contacts.c.id.in_(contactIds)))


class GroupStore(DataStore):
    def create(self, name: str, contacts: List[int]) -> GroupDTO:
        result = self.session.execute(groups.insert().values(name=name))

        groupId = result.inserted_primary_key[0]

        if len(contacts) > 0:
            self.session.execute(contact_to_group.insert().values([{
                'group_id': groupId,
                'contact_id': contact,
            } for contact in contacts]))

        return GroupDTO(groupId, name, len(contacts))

    def get(self, groupId: int):
        query = (
            select(
                columns=[
                    groups.c.id,
                    groups.c.name,
                    count(contact_to_group.c.contact_id).label('contacts')
                ],
                whereclause=groups.c.id == groupId
            )
            .select_from(groups.join(contact_to_group))
            .group_by(groups.c.id)
        )

        row = self.session.execute(query).fetchone()

        return GroupDTO(
            row[groups.c.id],
            row[groups.c.name],
            row['contacts'],
        )

    def getAll(self) -> List[GroupDTO]:
        query = (
            select(
                columns=[
                    groups.c.id,
                    groups.c.name,
                    count(contact_to_group.c.contact_id).label('contacts')
                ]
            )
            .select_from(groups.join(contact_to_group))
            .group_by(groups.c.id)
        )

        rows = self.session.execute(query)

        return [GroupDTO(
            row[groups.c.id],
            row[groups.c.name],
            row['contacts'],
        ) for row in rows]

    def delete(self, groupIds: List[int]):
        self.session.execute(groups.delete().where(groups.c.id.in_(groupIds)))


class TemplateStore(DataStore):
    def create(self, name: str, content: str) -> TemplateDTO:
        result = self.session.execute(templates.insert().values(name=name, content=content))

        return TemplateDTO(result.inserted_primary_key[0], name, content)

    def get(self, templateId: int) -> TemplateDTO:
        query = select(templates.c, whereclause=templates.c.id == templateId)
        row = self.session.execute(query).fetchone()

        return TemplateDTO(
            row[templates.c.id],
            row[templates.c.name],
            row[templates.c.content],
        )

    def getAll(self) -> List[TemplateDTO]:
        rows = self.session.execute(select(templates.c))

        return [TemplateDTO(
            row[templates.c.id],
            row[templates.c.name],
            row[templates.c.content],
        ) for row in rows]

    def delete(self, templatesIds: List[int]):
        self.session.execute(templates.delete().where(templates.c.id.in_(templatesIds)))


class MailingStore(DataStore):
    def createJob(self, templateId: int, groupId: int, total: int) -> int:
        result = self.session.execute(mailing_jobs.insert().values(
            template_id=templateId,
            group_id=groupId,
            total=total,
            sent=0
        ))

        return result.inserted_primary_key[0]
