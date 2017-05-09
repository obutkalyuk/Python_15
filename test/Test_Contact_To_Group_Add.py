# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random

def test_add_contacts_to_group(app, db, check_ui):

    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact().random())
    if len(db.get_group_list()) == 0:
        app.group.create(Group().random())

    all_groups = db.get_group_list()
    all_contacts = db.get_contact_list()
    group = random.choice(all_groups)
    old_contacts_in_group = db.get_contacts_in_group(group)
    if old_contacts_in_group == []:
        old_contacts_extra_group = all_contacts
    else:
        old_contacts_extra_group = db.get_contacts_not_in_group(group)
    if len(old_contacts_extra_group) == 0:
        app.contact.create(Contact().random())
        old_contacts_extra_group = db.get_contacts_not_in_group(group)

    contact = random.choice(old_contacts_extra_group)
    app.contact.add_contact_to_group(contact, group)
    new_contacts_in_group = db.get_contacts_in_group(group)
    old_contacts_in_group.append(contact)

    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
    if check_ui:
        app.return_to_home_page()
        sorted(new_contacts_in_group, key=Contact.id_or_max) == sorted(app.contact.get_contact_list_for_group(group), key=Contact.id_or_max)


