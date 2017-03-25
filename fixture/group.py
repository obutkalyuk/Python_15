
class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        self.app.type_text("group_name", group.name)
        self.app.type_text("group_header", group.header)
        self.app.type_text("group_footer", group.footer)
        wd.find_element_by_name("submit").click()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group").click()