from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import  Contact



class ORMFizture:

    db = Database()

    class ORM_Group(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORM_Contact(db.Entity):
        _table_ ='addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column = 'firstname')
        lastname = Optional(str, column = 'lastname')
        deprecated = Optional(str, column = 'deprecated')

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id = str(group.id), name = group.name, header = group.header, footer = group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFizture.ORM_Group))