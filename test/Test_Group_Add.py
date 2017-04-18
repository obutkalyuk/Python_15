# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, data_groups):
    group = data_groups
    new_group = group
    old_groups = app.group.get_group_list()
    app.group.create(new_group)
    assert len(old_groups)+ 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



