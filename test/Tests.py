# -*- coding: utf-8 -*-
import pytest

from contact import Contact
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

def test_add_contacts(app):
    app.session.login(user="admin", password="secret")
    app.create_contact(Contact(firstName="James", lastName="Bond", address="London", homePhone="123",
                                    mobilePhone="456", workPhone="789", email1="email1@com.com",
                                    email2="email2@com.com", email3="email3@com.com"))
    app.return_to_home_page()
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login( user="admin", password="secret")
    app.create_contact(Contact(firstName="", lastName="", address="", homePhone="", mobilePhone="",
                                    workPhone="", email1="", email2="", email3=""))
    app.return_to_home_page()
    app.session.logout()




