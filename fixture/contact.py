class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

        self.app.type_text("firstname", contact.firstName)
        self.app.type_text("lastname", contact.lastName)
        self.app.type_text( "address", contact.address)
        self.app.type_text( "home", contact.homePhone)
        self.app.type_text("mobile", contact.mobilePhone)
        self.app.type_text("work", contact.workPhone)
        self.app.type_text("email", contact.email1)
        self.app.type_text("email2", contact.email2)
        self.app.type_text("email3", contact.email3)

        wd.find_element_by_name("submit").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("[value='Delete']").click()
        wd.switch_to_alert().accept()
