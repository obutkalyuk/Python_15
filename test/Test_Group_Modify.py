# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_modify_random_group(app, db):

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
    # old_groups[index] = edition
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



def test_group_list(app):
    edition = Group(name="Group_first")
    ui_list = app.group.get_group_list()
    ui_list2 = [Group(name="test2", header="header", footer='footer')]

    assert sorted(ui_list, key=Group.id_or_max) == sorted(ui_list2, key=Group.id_or_max)

def test_group_list2():
   ui_list = [Group(name="1"), Group(name='2'), Group(name='3')]
   ui_list2 = list(ui_list)
   ui_list2[0] = Group(name='5')

   assert sorted(ui_list, key=Group.id_or_max) == sorted(ui_list2, key=Group.id_or_max)
