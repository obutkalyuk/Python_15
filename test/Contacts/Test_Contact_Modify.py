# -*- coding: utf-8 -*-
from model.contact import Contact
import random

#todo move to another place. later.
def find_index(source_list, id):
    for element in source_list:
        if element.id == id:
            return source_list.index(element)



def test_modify_contacts(app, db, check_ui):
    FirstContact = Contact(firstName="James", lastName="Corleone", address="London", homePhone="123",
                                    mobilePhone="456", workPhone="789", email1="email1@com.com",
                                    email2="email2@com.com", email3="email3@com.com")

    edition = Contact(firstName="Jina", lastName="Lolobridgida", address="Milan")

    app.contact.create(FirstContact)
    old_contacts = db.get_contact_list()
    id = app.contact.get_id_from_table(FirstContact)
    app.contact.open_for_edit(FirstContact)
    app.contact.update(edition)
    app.return_to_home_page()

    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    index = find_index(old_contacts, id)
    edition.id = id
    old_contacts[index] = edition
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

def test_modify_random_contacts(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstName="Jack", lastName="London", address="Alaska", homePhone="123",
                                   mobilePhone="456", workPhone="789", email1="email1@com.com",
                                   email2="email2@com.com", email3="email3@com.com"))


    edition = Contact(firstName="Alice", lastName="Milano", address="Chickago")

    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = find_index(old_contacts, contact.id)
    edition.id = contact.id
    old_contacts[index] = edition
    app.contact.modify_by_id(contact.id, edition)
    app.return_to_home_page()

    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()


    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



