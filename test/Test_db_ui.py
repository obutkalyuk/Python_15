from model.group import Group
from model.contact import Contact
from timeit import timeit


def test_group_db_list(app, db):
    print(timeit(lambda:app.group.get_group_list(), number=1))
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name = group.name.strip())

    db_list = map(clean, db.get_group_list())
    print(timeit(lambda:map(clean, db.get_group_list()), number=1000))
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_db_list(app, db):
    app.return_to_home_page()
    ui_list = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, firstName = contact.firstName.strip(),lastName = contact.lastName.strip() )
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)


def test_group_list2(app):

    ui_list = [Group(name="1"), Group(name='2'), Group(name='3')]
    ui_list2 = list(ui_list)
    ui_list2[0] = Group(name='5')

    assert sorted(ui_list, key=Group.id_or_max) == sorted(ui_list2, key=Group.id_or_max)
