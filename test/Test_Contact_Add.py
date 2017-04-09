# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
from fixture.string_helper import random_string
from fixture.string_helper import random_set
from fixture.string_helper import random_digits

testdata = [Contact(firstName="", lastName="", address="", homePhone="", mobilePhone="",
                               workPhone="", email1="", email2="", email3="")] + \
          [Contact(firstName= random_string("First", 7),
                   lastName=random_string("Last", 7),
                   address = random_string("address", 20),
                   homePhone = random_digits (10),
                   mobilePhone = random_digits (10),
                   workPhone = random_digits (10),
                   email1= "%s@%s.%s" % ("email1", random_set(5), random_set(3)),
                   email2="%s@%s.%s" % ("email2", random_set(5), random_set(3)),
                   email3="%s@%s.%s" % ("email3", random_set(5), random_set(3)))
          for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids= [repr(x) for x in testdata])
def test_add_contacts(app, contact):
    new_contact = contact
    old_contacts = app.contact.get_contact_list()
    app.contact.create(new_contact)
    app.return_to_home_page()
    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(new_contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_empty_contact(app):
#     app.contact.create(Contact(firstName="", lastName="", address="", homePhone="", mobilePhone="",
#                                workPhone="", email1="", email2="", email3=""))
#     app.return_to_home_page()

