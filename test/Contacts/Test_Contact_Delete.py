# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_delete_random_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstName="Jack", lastName="London", address="Alaska", homePhone="123",
                                   mobilePhone="456", workPhone="789", email1="email1@com.com",
                                   email2="email2@com.com", email3="email3@com.com"))

    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id(contact.id)

    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts==new_contacts
    if check_ui:
        sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
