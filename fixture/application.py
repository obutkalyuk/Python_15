from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session =SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def create_contact(self, contact):
        wd = self.wd
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

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()