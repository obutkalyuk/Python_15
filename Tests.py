# -*- coding: utf-8 -*-
import unittest
import pytest
from application import Application
from contact import Contact
from group import Group


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_and_group(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login( user="admin", password="secret")
        self.app.create_group( Group(name="Group1", header="header", footer="footer1"))
        self.app.return_to_group_page()
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(user="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.return_to_group_page()
        self.app.logout()

    def test_add_contacts(self):
        self.app.login(user="admin", password="secret")
        self.app.create_contact(Contact(firstName="James", lastName="Bond", address="London", homePhone="123",
                                        mobilePhone="456", workPhone="789", email1="email1@com.com",
                                        email2="email2@com.com", email3="email3@com.com"))
        self.app.return_to_home_page()
        self.app.logout()

    def test_add_empty_contact(self):
        self.app.login( user="admin", password="secret")
        self.app.create_contact(Contact(firstName="", lastName="", address="", homePhone="", mobilePhone="",
                                        workPhone="", email1="", email2="", email3=""))
        self.app.return_to_home_page()
        self.app.logout()

    def tearDown(self):
        self.app.destroy()
if __name__ == '__main__':
    unittest.main()



