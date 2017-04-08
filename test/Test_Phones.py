import re


def test_phones_on_homepage(app):
    contact_from_home_page = app.contact.get_info_from_home_page_by_index(0)
    contact_from_edit_page = app.contact.get_info_from_edit_page(0)
    assert contact_from_home_page.homePhone == clear(contact_from_edit_page.homePhone)
    assert contact_from_home_page.mobilePhone == clear(contact_from_edit_page.mobilePhone)
    assert contact_from_home_page.workPhone == clear(contact_from_edit_page.workPhone)
    assert contact_from_home_page.secondaryPhone == clear(contact_from_edit_page.secondaryPhone)

def clear(s):
   return  re.sub("[() -]", "", s)



