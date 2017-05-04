# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contacts(app, db, json_contacts):
    contact = json_contacts
    new_contact = contact
    old_contacts = db.get_contact_list()
    app.contact.create(new_contact)
    app.return_to_home_page()
    new_contacts = db.get_contact_list()

    old_contacts.append(new_contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



