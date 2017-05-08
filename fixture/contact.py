from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    contact_cache = None

    #  table page
    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.set_fields(contact)
        wd.find_element_by_name("submit").click()
        self.app.wait.until(lambda d: d.find_element_by_id("maintable"))
        self.contact_cache = None

    def delete_by_index(self, index):
        wd = self.app.wd
        self.select_by_index(index)
        wd.find_element_by_css_selector("[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.select_by_id(id)
        wd.find_element_by_css_selector("[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_by_id(self, id):
        wd = self.app.wd
        css = "input[value='%s']" % str(id)
        checkbox = wd.find_element_by_css_selector(css)
        checkbox.click()

    def open_for_edit(self, contact):
        row = self.get_row(contact)
        editLink = row.find_element_by_css_selector("[href^='edit']")
        editLink.click()

    def open_for_edit_by_index(self, index):
        row = self.get_row_by_index(index)
        editLink = row.find_element_by_css_selector("[href^='edit']")
        editLink.click()

    def open_for_edit_by_id(self, id):
        row = self.get_row_by_id(id)
        editLink = row.find_element_by_css_selector("[href^='edit']")
        editLink.click()

    def open_for_view(self, contact):
        row = self.get_row(contact)
        editLink = row.find_element_by_css_selector("[href^='view']")
        editLink.click()

    def open_for_view_by_index(self, index):
        row = self.get_row_by_index(index)
        editLink = row.find_element_by_css_selector("[href^='view']")
        editLink.click()

    def get_row(self, contact):
        wd = self.app.wd
        locator = "//tr[td[.='%s'] and td[.='%s']]" % (contact.firstName, contact.lastName)
        row = wd.find_element_by_xpath(locator)
        return row

    def get_row_by_index(self, index):
        wd = self.app.wd
        xpath = "//tr[%s]" % str(index + 2)  # 1st row is header
        row = wd.find_element_by_xpath(xpath)
        return row

    def get_row_by_id(self, id):
        wd = self.app.wd
        locator = "//tr[td[input[@value='%s']]]" % str(id)
        row = wd.find_element_by_xpath(locator)
        return row

    def get_id_from_table(self, contact):
        row = self.get_row(contact)
        id = row.find_element_by_name("selected[]").get_attribute("value")
        return id

    def modify_by_index(self, index, edition):
        wd = self.app.wd
        self.open_for_edit_by_index(index)
        self.set_fields(edition)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def modify_by_id(self, id, edition):
        wd = self.app.wd
        self.open_for_edit_by_id(id)
        self.set_fields(edition)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for row in wd.find_elements_by_css_selector("tr[name='entry']"):
                contact = self.get_info_from_home_page_by_row(row)
                self.contact_cache.append(contact)
        return list(self.contact_cache)

    def get_info_from_home_page_by_index(self, index):
        row = self.get_row_by_index(index)
        return self.get_info_from_home_page_by_row(row)

    def get_info_from_home_page_by_id(self, id):
        row = self.get_row_by_id(id)
        return self.get_info_from_home_page_by_row(row)

    def get_info_from_home_page_by_row(self, row):
        id = row.find_element_by_name("selected[]").get_attribute("id")
        last_name = row.find_element_by_xpath(".//td[2]").text
        fisrt_name = row.find_element_by_xpath(".//td[3]").text
        address = row.find_element_by_xpath(".//td[4]").text
        emails = row.find_element_by_xpath(".//td[5]").text
        phones = row.find_element_by_xpath(".//td[6]").text
        contact = Contact(id=id, firstName=fisrt_name, lastName=last_name, address=address, all_phones = phones, all_emails = emails
                          )
        return contact



    def get_info_from_edit_page(self, index):
        self.open_for_edit_by_index(index)
        return self.get_fields()

    def get_info_from_view_page(self, index):
        self.open_for_view_by_index(index)
        return self.get_info()

    # work with first elements
    def delete_first(self):
        self.delete_by_index(0)

    def modify_first(self, edition):
        self.modify_by_index(0)

    # methods for edit page
    def update(self, edition):
        wd = self.app.wd
        self.set_fields(edition)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def set_fields(self, contact):
        self.app.type_text("firstname", contact.firstName)
        self.app.type_text("lastname", contact.lastName)
        self.app.type_text("address", contact.address)
        self.app.type_text("home", contact.homePhone)
        self.app.type_text("mobile", contact.mobilePhone)
        self.app.type_text("phone2", contact.secondaryPhone)
        self.app.type_text("work", contact.workPhone)
        self.app.type_text("email", contact.email1)
        self.app.type_text("email2", contact.email2)
        self.app.type_text("email3", contact.email3)

    def get_fields(self):
        wd = self.app.wd
        fisrt_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homePhone = wd.find_element_by_name("home").get_attribute("value")
        mobilePhone = wd.find_element_by_name("mobile").get_attribute("value")
        workPhone = wd.find_element_by_name("work").get_attribute("value")
        secondaryPhone = wd.find_element_by_name("phone2").get_attribute("value")

        fax = wd.find_element_by_name("fax").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")

        contact = Contact(id=id, firstName=fisrt_name, lastName=last_name, address=address, homePhone=homePhone,
                          mobilePhone=mobilePhone, workPhone=workPhone, secondaryPhone=secondaryPhone,
                          email1=email1, email2 = email2, email3 = email3)
        return contact

#     method for view page

    def get_info(self):
        wd = self.app.wd
        info = wd.find_element_by_id("content").text
        homePhone = re.search("H: (.*)", info).group(1)
        mobilePhone = re.search("M: (.*)", info).group(1)
        workPhone = re.search("W: (.*)", info).group(1)
        secondaryPhone = re.search("P: (.*)", info).group(1)

        contact = Contact( homePhone=homePhone,
                          mobilePhone=mobilePhone, workPhone=workPhone, secondaryPhone=secondaryPhone)
        return contact


