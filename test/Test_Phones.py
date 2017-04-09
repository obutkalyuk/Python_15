
def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_info_from_home_page_by_index(0)
    contact_from_edit_page = app.contact.get_info_from_edit_page(0)

    assert contact_from_home_page.all_phones == contact_from_edit_page.merge_phones()


def test_phones_on_contact_view_page(app):
    app.return_to_home_page()
    contact_from_view_page = app.contact.get_info_from_view_page(0)
    app.return_to_home_page()
    contact_from_edit_page = app.contact.get_info_from_edit_page(0)

    assert contact_from_view_page.homePhone == (contact_from_edit_page.homePhone)
    assert contact_from_view_page.mobilePhone == (contact_from_edit_page.mobilePhone)
    assert contact_from_view_page.workPhone == (contact_from_edit_page.workPhone)
    assert contact_from_view_page.secondaryPhone == (contact_from_edit_page.secondaryPhone)




