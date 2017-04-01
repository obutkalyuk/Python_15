# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstName="Jack", lastName="London", address="Alaska", homePhone="123",
                                           mobilePhone="456", workPhone="789", email1="email1@com.com",
                                           email2="email2@com.com", email3="email3@com.com"))

    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1]=[]
    assert old_contacts==new_contacts
