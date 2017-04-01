# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_delete_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstName="Jack", lastName="London", address="Alaska", homePhone="123",
                                           mobilePhone="456", workPhone="789", email1="email1@com.com",
                                           email2="email2@com.com", email3="email3@com.com"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)

    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()

    old_contacts[index:index+1]=[]
    assert old_contacts==new_contacts
