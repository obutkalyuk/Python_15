# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_modify_random_group(app):

    edition = Group(name="Group_first")

    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    edition.id = old_groups[index].id
    app.group.modify_by_index(edition, index)

    assert len(old_groups)  == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = edition
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


