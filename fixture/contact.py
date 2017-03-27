class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.set_fields(contact)
        wd.find_element_by_name("submit").click()

    def set_fields(self, contact):
        self.app.type_text("firstname", contact.firstName)
        self.app.type_text("lastname", contact.lastName)
        self.app.type_text("address", contact.address)
        self.app.type_text("home", contact.homePhone)
        self.app.type_text("mobile", contact.mobilePhone)
        self.app.type_text("work", contact.workPhone)
        self.app.type_text("email", contact.email1)
        self.app.type_text("email2", contact.email2)
        self.app.type_text("email3", contact.email3)

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("[value='Delete']").click()
        wd.switch_to_alert().accept()

    def find_contact(self, contact):
        wd = self.app.wd
        row = wd.find_element_by_xpath("//tr[td[.='"+contact.firstName+"'] and td[.='"+contact.lastName+"']]")
        editLink = row.find_element_by_css_selector("[href^='edit']")
        editLink.click()

    def modify_contact(self,edition):
        wd = self.app.wd
        self.set_fields(edition)
        wd.find_element_by_name("update").click()

    def modify_first_contact(self,edition):
        wd = self.app.wd
        row = wd.find_element_by_xpath("//tr[2]") #1st row is header
        editLink = row.find_element_by_css_selector("[href^='edit']")
        editLink.click()
        self.set_fields(edition)
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))