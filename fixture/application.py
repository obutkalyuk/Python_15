from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session =SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def type_text(self, attribute,  text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(attribute).click()
            wd.find_element_by_name(attribute).clear()
            wd.find_element_by_name(attribute).send_keys(text)

    def destroy(self):
        self.wd.quit()