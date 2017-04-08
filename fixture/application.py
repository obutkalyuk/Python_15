from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
import re

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.session =SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def return_to_home_page(self):
        wd = self.wd
        if not wd.current_url.endswith("addressbook/"):
            wd.find_element_by_link_text("home").click()

    def type_text(self, attribute,  text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(attribute).click()
            wd.find_element_by_name(attribute).clear()
            wd.find_element_by_name(attribute).send_keys(text)

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def merge_phones(self, contact):
        a0 = filter(lambda x: x is not None,
                    [contact.homePhone, contact.mobilePhone, contact.workPhone, contact.secondaryPhone])
        a = map(lambda x: self.clear(x), a0)
        b = filter(lambda x: x != "", a)
        c = "\n".join(b)
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.homePhone, contact.mobilePhone, contact.workPhone,
                                            contact.secondaryPhone]))))

    def merge_emails(self, contact):
        a0 = filter(lambda x: x is not None,
                    [contact.email1, contact.email2, contact.email3])
        a = map(lambda x: self.clear(x), a0)
        b = filter(lambda x: x != "", a)
        c = "\n".join(b)
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.email1, contact.email2, contact.email3]))))
    def destroy(self):
        self.wd.quit()