from injector import Key
from sqlalchemy import MetaData, Table, Integer, String, Text, ForeignKey, Column, DateTime

Database = Key('Database')  # Marker for pseudo-interface used in injecting database in DataStores

metadata = MetaData()

contacts = Table(
    'contacts', metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String(80,collation='utf8_general_ci')),
    Column('firstName', String(80, collation='utf8_general_ci')),
    Column('lastName', String(80, collation='utf8_general_ci')),
)

groups = Table(
    'groups', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(80, collation='utf8_general_ci')),
)

contact_to_group = Table(
    'contact_to_group', metadata,
    Column('contact_id', Integer, ForeignKey('contacts.id', ondelete='CASCADE'), primary_key=True),
    Column('group_id', Integer, ForeignKey('groups.id', ondelete='CASCADE'), primary_key=True),
)

templates = Table(
    'templates', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(80, collation='utf8_general_ci')),
    Column('subject', String(200, collation='utf8_general_ci')),
    Column('content', Text(collation='utf8_general_ci')),
)

mailing_jobs = Table(
    'mailing_jobs', metadata,
    Column('id', Integer, primary_key=True),
    Column('template_id', Integer, ForeignKey('templates.id', ondelete='RESTRICT')),
    Column('group_id', Integer, ForeignKey('groups.id', ondelete='RESTRICT')),
    Column('total', Integer),
    Column('sent', Integer),
    Column('created', DateTime),
)

servers = Table(
    'servers', metadata,
    Column('id', Integer, primary_key=True),
    Column('address', String(200, collation='utf8_general_ci')),
    Column('login', String(80, collation='utf8_general_ci')),
    Column('password', String(200, collation='utf8_general_ci')),
    Column('from_name', String(80, collation='utf8_general_ci')),
    Column('from_address', String(80, collation='utf8_general_ci')),
)
