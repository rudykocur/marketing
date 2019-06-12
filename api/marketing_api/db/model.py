from marketing_api.app import db

contacts = db.Table(
    'contacts', db.metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('email', db.String(80,collation='utf8_general_ci')),
    db.Column('firstName', db.String(80, collation='utf8_general_ci')),
    db.Column('lastName', db.String(80, collation='utf8_general_ci')),
)

groups = db.Table(
    'groups', db.metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('name', db.String(80, collation='utf8_general_ci')),
)

contact_to_group = db.Table(
    'contact_to_group', db.metadata,
    db.Column('contact_id', db.Integer, db.ForeignKey('contacts.id'), primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True),
)

templates = db.Table(
    'templates', db.metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('name', db.String(80, collation='utf8_general_ci')),
    db.Column('content', db.Text(collation='utf8_general_ci')),
)

mailing_jobs = db.Table(
    'mailing_jobs', db.metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('template_id', db.Integer, db.ForeignKey('templates.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id')),
    db.Column('total', db.Integer),
    db.Column('sent', db.Integer),
)
