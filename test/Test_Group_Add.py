# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from fixture.string_helper import random_string

testdata = [Group(name="", header="", footer="")] + \
          [Group(name= random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
          for i in range(5)]

@pytest.mark.parametrize("group", testdata, ids= [repr(x) for x in testdata])
def test_add_group(app, group):
    new_group = group
    old_groups = app.group.get_group_list()
    app.group.create(new_group)
    assert len(old_groups)+ 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



