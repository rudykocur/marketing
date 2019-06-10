from marketing_api.app import db


class Contact(db.Model):
    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    firstName = db.Column(db.String(80), nullable=True)
    lastName = db.Column(db.String(80), nullable=True)


class Group(db.Model):
    __tablename__ = 'group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    users = db.relationship(Contact, lazy="dynamic", secondary="contact_to_group")


class ContactToGroup(db.Model):
    __tablename__ = 'contact_to_group'

    contactId = db.Column(db.Integer, db.ForeignKey('contact.id'), primary_key=True)
    groupId = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)


class Template(db.Model):
    __tablename__ = 'template'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.Text())

