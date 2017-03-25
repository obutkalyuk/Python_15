# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login( user="admin", password="secret")
    app.group.create(Group(name="Group1", header="header", footer="footer1"))
    app.group.return_to_group_page()
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(user="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.group.return_to_group_page()
    app.session.logout()
