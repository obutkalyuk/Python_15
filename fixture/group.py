class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        self.type_text(wd, "group_name", group.name)
        self.type_text(wd, "group_header", group.header)
        self.type_text(wd, "group_footer", group.footer)
        wd.find_element_by_name("submit").click()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group").click()