# -*- coding: utf-8 -*-

from model.contact import Contact

def test_modify_contacts(app):
    FirstContact = Contact(firstName="James", lastName="Bond", address="London", homePhone="123",
                                    mobilePhone="456", workPhone="789", email1="email1@com.com",
                                    email2="email2@com.com", email3="email3@com.com")

    Edition = Contact(firstName="Jina", lastName="Lolobridgida", address="Milan")

    app.session.login(user="admin", password="secret")
    app.contact.create_contact(FirstContact)
    app.contact.find_contact(FirstContact)
    app.contact.modify_contact( Edition)
    app.return_to_home_page()
    app.session.logout()



