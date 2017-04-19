# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contacts(app, json_contacts):
    contact = json_contacts
    new_contact = contact
    old_contacts = app.contact.get_contact_list()
    app.contact.create(new_contact)
    app.return_to_home_page()
    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(new_contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max), "Test message"



