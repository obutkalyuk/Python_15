# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contacts(app):
    new_contact = Contact(firstName="James", lastName="Bond", address="London", homePhone="123",
                                    mobilePhone="456", workPhone="789", email1="email1@com.com",
                                    email2="email2@com.com", email3="email3@com.com")
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(new_contact)
    app.return_to_home_page()
    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(new_contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_add_empty_contact(app):
    app.contact.create_contact(Contact(firstName="", lastName="", address="", homePhone="", mobilePhone="",
                                    workPhone="", email1="", email2="", email3=""))
    app.return_to_home_page()

