# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_and_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_group(self):
        wd = self.wd
        self.login(wd, user="admin", password="secret")
        self.create_group(wd, Group(name="Group1", header="header", footer="footer1"))
        self.return_to_group_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.login(wd, user="admin", password="secret")
        self.create_group(wd, Group(name="", header="", footer=""))
        self.return_to_group_page(wd)
        self.logout(wd)

    def test_add_contacts(self):
        wd = self.wd
        self.login(wd, user="admin", password="secret")
        self.create_contact(wd, Contact(firstName="James", lastName="Bond", address="London", homePhone="123",
                                        mobilePhone="456", workPhone="789", email1="email1@com.com",
                                        email2="email2@com.com", email3="email3@com.com"))
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.login(wd, user="admin", password="secret")
        self.create_contact(wd, Contact(firstName="", lastName="", address="", homePhone="", mobilePhone="",
                                        workPhone="", email1="", email2="", email3=""))
        self.return_to_home_page(wd)
        self.logout(wd)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, user, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def create_group(self, wd, group):
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        self.type_text(wd, "group_name", group.name)
        self.type_text(wd, "group_header", group.header)
        self.type_text(wd, "group_footer", group.footer)
        wd.find_element_by_name("submit").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_contact(self, wd, contact):
        wd.find_element_by_link_text("add new").click()

        self.type_text(wd, "firstname", contact.firstName)
        self.type_text(wd, "lastname", contact.lastName)
        self.type_text(wd, "address", contact.address)
        self.type_text(wd, "home", contact.homePhone)
        self.type_text(wd, "mobile", contact.mobilePhone)
        self.type_text(wd, "work", contact.workPhone)
        self.type_text(wd, "email", contact.email1)
        self.type_text(wd, "email2", contact.email2)
        self.type_text(wd, "email3", contact.email3)

        wd.find_element_by_name("submit").click()

    def type_text(self,wd, attribute,  text):
        wd.find_element_by_name(attribute).click()
        wd.find_element_by_name(attribute).clear()
        wd.find_element_by_name(attribute).send_keys(text)

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()



