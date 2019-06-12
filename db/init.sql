create database marketing;

CREATE TABLE contacts (
        id INTEGER NOT NULL AUTO_INCREMENT,
        email VARCHAR(80) COLLATE utf8_general_ci,
        `firstName` VARCHAR(80) COLLATE utf8_general_ci,
        `lastName` VARCHAR(80) COLLATE utf8_general_ci,
        PRIMARY KEY (id)
);

CREATE TABLE `groups` (
        id INTEGER NOT NULL AUTO_INCREMENT,
        name VARCHAR(80) COLLATE utf8_general_ci,
        PRIMARY KEY (id)
);

CREATE TABLE templates (
        id INTEGER NOT NULL AUTO_INCREMENT,
        name VARCHAR(80) COLLATE utf8_general_ci,
        content TEXT COLLATE utf8_general_ci,
        PRIMARY KEY (id)
);

CREATE TABLE contact_to_group (
        contact_id INTEGER NOT NULL,
        group_id INTEGER NOT NULL,
        PRIMARY KEY (contact_id, group_id),
        FOREIGN KEY(contact_id) REFERENCES contacts (id),
        FOREIGN KEY(group_id) REFERENCES `groups` (id)
);

CREATE TABLE mailing_jobs (
        id INTEGER NOT NULL AUTO_INCREMENT,
        template_id INTEGER,
        group_id INTEGER,
        total INTEGER,
        sent INTEGER,
        PRIMARY KEY (id),
        FOREIGN KEY(template_id) REFERENCES templates (id),
        FOREIGN KEY(group_id) REFERENCES `groups` (id)
);

COMMIT;