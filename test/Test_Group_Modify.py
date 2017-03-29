# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_first_group(app):

    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    edition = Group(name="Group_first")
    app.group.modify_first(edition)
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)


