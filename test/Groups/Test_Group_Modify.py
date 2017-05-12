# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_modify_random_group(app, db, check_ui):

    edition = Group(name="Group_first")

    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = db.get_group_list()
    updated_group = random.choice(old_groups)
    edition.id = updated_group.id
    app.group.modify_by_id(edition, updated_group.id)

    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(updated_group)
    old_groups.append(edition)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)




