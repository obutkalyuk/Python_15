from sys import maxsize
from fixture.string_helper import clear

class Contact:
    def __init__(self, id= None, firstName=None, lastName=None, address=None, all_phones = None, all_emails = None, homePhone=None,mobilePhone=None,
                 workPhone=None, secondaryPhone = None,  email1=None, email2=None, email3=None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.all_phones = all_phones
        self.all_emails = all_emails
        self.homePhone = homePhone
        self.mobilePhone = mobilePhone
        self.workPhone = workPhone
        self.secondaryPhone = secondaryPhone
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return "%s: %s %s" % (self.id, self.firstName, self.lastName)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.firstName == other.firstName) \
               and (self.lastName == other.lastName)



    def merge_phones(self):
        a0 = filter(lambda x: x is not None,
                    [self.homePhone, self.mobilePhone, self.workPhone, self.secondaryPhone])
        a = map(lambda x: clear(x), a0)
        b = filter(lambda x: x != "", a)
        c = "\n".join(b)
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                           [self.homePhone, self.mobilePhone, self.workPhone,
                                            self.secondaryPhone]))))

    def merge_emails(self):
        a0 = filter(lambda x: x is not None,
                    [self.email1, self.email2, self.email3])
        a = map(lambda x: clear(x), a0)
        b = filter(lambda x: x != "", a)
        c = "\n".join(b)
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                           [self.email1, self.email2, self.email3]))))
