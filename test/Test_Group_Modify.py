# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_first_group(app):
    edition = Group(name="Group_first")

    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    edition.id = old_groups[0].id
    app.group.modify_first(edition)
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)
    old_groups[0] = edition
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


