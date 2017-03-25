# -*- coding: utf-8 -*-
import pytest
from application import Application
from contact import Contact
from group import Group

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizser(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login( user="admin", password="secret")
    app.create_group( Group(name="Group1", header="header", footer="footer1"))
    app.return_to_group_page()
    app.logout()

def test_add_empty_group(app):
    app.login(user="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.return_to_group_page()
    app.logout()

def test_add_contacts(app):
    app.login(user="admin", password="secret")
    app.create_contact(Contact(firstName="James", lastName="Bond", address="London", homePhone="123",
                                    mobilePhone="456", workPhone="789", email1="email1@com.com",
                                    email2="email2@com.com", email3="email3@com.com"))
    app.return_to_home_page()
    app.logout()

def test_add_empty_contact(app):
    app.login( user="admin", password="secret")
    app.create_contact(Contact(firstName="", lastName="", address="", homePhone="", mobilePhone="",
                                    workPhone="", email1="", email2="", email3=""))
    app.return_to_home_page()
    app.logout()




