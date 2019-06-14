import requests
from injector import inject
from requests.auth import HTTPBasicAuth

from marketing_api.db.stores import ServerDTO, ContactDTO
from marketing_api.encrypter import Encrypter


class MailSender(object):
    """
    Workhorse for sending email.

    {requests} dependency could be further injected as 'HttpClient', but there is plenty of examples of
    dependency injection.
    """

    @inject
    def __init__(self, encrypter: Encrypter):
        self.encrypter = encrypter

    def send(self, server: ServerDTO, contact: ContactDTO, body: str):
        respone = requests.post(
            server.address,
            auth=HTTPBasicAuth(
                server.login,
                self.encrypter.decrypt(server.password).encode('utf8')
            ),
            json={
                "from": {
                    "name": server.fromName,
                    "email": server.fromAddress
                },
                "to": {
                    "name": "{} {}".format(contact.firstName, contact.lastName),
                    "email": contact.email,
                },
                "subject": "Test email subject",
                "text": body,
                "headers": {}
            })

        respone.raise_for_status()
