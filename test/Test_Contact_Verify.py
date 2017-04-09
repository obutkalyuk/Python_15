from model.contact import Contact
from random import randrange

def test_verify_random_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstName="Sophie", lastName="Marceau", address="Paris", homePhone="1-2-3",
                                   mobilePhone="4 5 6", workPhone="(7) 89", email1="email1@com.com",
                                    email3="email3@com.com"))



    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))

    contact_from_home_page = app.contact.get_info_from_home_page_by_index(index)
    contact_from_edit_page = app.contact.get_info_from_edit_page(index)

    assert contact_from_home_page.firstName == contact_from_edit_page.firstName
    assert contact_from_home_page.lastName == contact_from_edit_page.lastName
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones == contact_from_edit_page.merge_phones()
    assert contact_from_home_page.all_emails == contact_from_edit_page.merge_emails()