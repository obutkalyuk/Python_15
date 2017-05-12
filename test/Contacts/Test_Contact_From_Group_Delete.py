# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random

def test_delete_contacts_from_group(app, db, check_ui):

    if len(db.get_contact_list()) == 0:
        contact = Contact().random()
        app.contact.create(contact)

    group_with_contacts = db.get_group_with_contacts()
    if len(group_with_contacts) == 0:
        group = Group().random()
        app.group.create(group)
        app.return_to_home_page()
        contact = random.choice(db.get_contact_list())
        app.contact.add_contact_to_group(contact, group)
        group_with_contacts = db.get_group_with_contacts()

    group = random.choice(group_with_contacts)
    old_contacts_in_group = db.get_contacts_in_group(group)
    contact = random.choice(old_contacts_in_group)
    app.return_to_home_page()
    app.contact.remove_contact_to_group(contact, group)
    new_contacts_in_group = db.get_contacts_in_group(group)
    old_contacts_in_group.remove(contact)

    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
    if check_ui:
        app.return_to_home_page()
        sorted(new_contacts_in_group, key=Contact.id_or_max) == sorted(app.contact.get_contact_list_for_group(group), key=Contact.id_or_max)


