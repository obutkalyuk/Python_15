# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contacts(app):
    app.contact.create_contact(Contact(firstName="James", lastName="Bond", address="London", homePhone="123",
                                    mobilePhone="456", workPhone="789", email1="email1@com.com",
                                    email2="email2@com.com", email3="email3@com.com"))
    app.return_to_home_page()

def test_add_empty_contact(app):
    app.contact.create_contact(Contact(firstName="", lastName="", address="", homePhone="", mobilePhone="",
                                    workPhone="", email1="", email2="", email3=""))
    app.return_to_home_page()

