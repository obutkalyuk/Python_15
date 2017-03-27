# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_firstgroup(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    app.group.delete_first()

