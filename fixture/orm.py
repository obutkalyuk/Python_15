from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders



class ORMFixture:

    db = Database()

    class ORM_Group(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORM_Contact, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORM_Contact(db.Entity):
        _table_ ='addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column = 'firstname')
        lastname = Optional(str, column = 'lastname')
        address =  Optional(str, column = 'address')
        homePhone = Optional(str, column = 'homePhone')
        mobilePhone = Optional(str, column = 'mobilePhone')
        workPhone = Optional(str, column = 'workPhone')
        email1 = Optional(str, column = 'email1')
        email2 = Optional(str, column = 'email2')
        email3 = Optional(str, column = 'email3')
        deprecated = Optional(str, column = 'deprecated')
        groups = Set(ORMFixture.ORM_Group,  table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id = str(group.id), name = group.name, header = group.header, footer = group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstName=contact.firstname, lastName=contact.lastname)
        return list(map(convert, contacts))


    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORM_Group))

    def get_contact_list_for_group(self, group_id):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORM_Group))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORM_Contact if c.deprecated is None))



