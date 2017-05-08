# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random

def test_add_contacts_to_group(app, db, check_ui):
    # PRETEST

    #  select random contact not included in this group
    #  ACTIONS
    #  add contact to group
    #  VERIFICATIONS
    #  group should contain contact


    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact().random())
    if len(db.get_group_list()) == 0:
        app.group.create(Group().random())

    all_groups = db.get_group_list()
    group = random.choice(all_groups)
    old_contacts_from_group = db.get_contact_list_for_group(group.id)
    old_contacts_extra_group = db.get_contact_list_extra_group(group.id)
    contact = random.choice(old_contacts_extra_group)
    app.contact.add_contact_to_group(contact, group)


    all_groups = db.get_group_list()


    contact =
    new_contact = contact
    old_contacts = db.get_contact_list()
    app.contact.create(new_contact)
    app.return_to_home_page()
    new_contacts = db.get_contact_list()

    old_contacts.append(new_contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


