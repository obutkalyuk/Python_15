# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_first_group(app):
    edition = Group(name="Group_first")
    app.session.login( user="admin", password="secret")
    app.group.modify_first(edition)
    app.session.logout()

