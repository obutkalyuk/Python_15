def test_phones_on_homepage(app):
    contact_from_home_page = app.contact.get_info_from_home_page_by_index(0)
    contact_from_edit_page = app.contact.get_info_from_edit_page(0)
    assert contact_from_home_page.homePhone == contact_from_edit_page.homePhone
    assert contact_from_home_page.mobilePhone == contact_from_edit_page.mobilePhone
    assert contact_from_home_page.workPhone == contact_from_edit_page.workPhone

