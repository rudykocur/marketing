from flask import request
from flask_restful import Resource
from injector import Injector

from marketing_api.db.stores import GroupStore, MailingStore, ContactStore, TemplateStore
from marketing_api import jobs


class MailingHandler(Resource):
    def __init__(self, ctx: Injector):
        self.groupsStore = ctx.get(GroupStore)
        self.contactsStore = ctx.get(ContactStore)
        self.mailingStore = ctx.get(MailingStore)
        self.templatesStore = ctx.get(TemplateStore)

    def get(self):
        result = []

        return result

    def post(self):
        template = self.templatesStore.get(int(request.form['templateId']))
        group = self.groupsStore.get(int(request.form['groupId']))

        contacts = self.contactsStore.getByGroup(group.id)

        jobId = self.mailingStore.createJob(template.id, group.id, group.contacts)

        self.mailingStore.commit()

        for contact in contacts:
            jobs.sendMail.delay(jobId, contact, template.content)

        return {
            'jobId': jobId,
        }
