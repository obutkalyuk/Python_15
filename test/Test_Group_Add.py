# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    new_group = Group(name="Group1", header="header", footer="footer1")
    old_groups = app.group.get_group_list()
    app.group.create(new_group)
    new_groups = app.group.get_group_list()

    assert len(old_groups)+ 1 == len(new_groups)
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



def test_add_empty_group(app):
    new_group = Group(name="", header="", footer="")
    old_groups = app.group.get_group_list()
    app.group.create(new_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(new_group)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
