
class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        self.set_fields(group)
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def modify_first(self, edition):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.set_fields(edition)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def set_fields(self, group):
        self.app.type_text("group_name", group.name)
        self.app.type_text("group_header", group.header)
        self.app.type_text("group_footer", group.footer)