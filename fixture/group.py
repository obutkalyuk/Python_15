from model.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app

    group_cache = None

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        self.set_fields(group)
        wd.find_element_by_name("submit").click()

        self.return_to_group_page()
        self.group_cache = None

    def select_group_by_index(self, index):
        wd = self.app.wd
        xpath = "//span[%s]/input[@name='selected[]']" % str(index+1)
        wd.find_element_by_xpath(xpath).click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        css = "input[value='%s']" % str(id)
        wd.find_element_by_css_selector(css).click()

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def modify_by_index(self, edition, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.set_fields(edition)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def modify_first(self, edition):
        self.modify_by_index(edition, 0)

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def open_group_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))>0):
            wd.find_element_by_link_text("groups").click()

    def set_fields(self, group):
        self.app.type_text("group_name", group.name)
        self.app.type_text("group_header", group.header)
        self.app.type_text("group_footer", group.footer)


    def get_group_list(self):
        if self.group_cache is None:
            self.group_cache = []
            wd = self.app.wd
            self.open_group_page()
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

