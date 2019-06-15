from flask import request
from injector import Injector

from marketing_api import jobs
from marketing_api.db.stores import GroupStore, MailingStore, ContactStore, TemplateStore, ServerStore
from marketing_api.resource import SecuredResource, require


class MailingJobsHandler(SecuredResource):
    def __init__(self, ctx: Injector):
        self.mailingStore = ctx.get(MailingStore)

    @require('view', 'Mailing')
    def get(self):
        result = []

        for job in self.mailingStore.getAll():
            result.append({
                'id': job.id,
                'templateId': job.templateId,
                'templateName': job.templateName,
                'groupId': job.groupId,
                'groupName': job.groupName,
                'sent': job.sent,
                'total': job.total,
            })

        return result


class DispatchMailingHandler(SecuredResource):
    def __init__(self, ctx: Injector):
        self.groupsStore = ctx.get(GroupStore)
        self.contactsStore = ctx.get(ContactStore)
        self.mailingStore = ctx.get(MailingStore)
        self.templatesStore = ctx.get(TemplateStore)
        self.serverStore = ctx.get(ServerStore)

    @require('manage', 'Mailing')
    def post(self):
        template = self.templatesStore.get(int(request.form['templateId']))
        group = self.groupsStore.get(int(request.form['groupId']))

        contacts = self.contactsStore.getByGroup(group.id)
        server = self.serverStore.get()

        jobId = self.mailingStore.createJob(template.id, group.id, group.contacts)

        self.mailingStore.commit()

        for contact in contacts:
            jobs.sendMail.delay(jobId, server, contact, template)

        return {
            'jobId': jobId,
        }
