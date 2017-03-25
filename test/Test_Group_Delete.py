# -*- coding: utf-8 -*-

def test_delete_firstgroup(app):
    app.session.login( user="admin", password="secret")
    app.group.delete_first()
    app.session.logout()