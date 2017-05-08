from sys import maxsize
from fixture.string_helper import *

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

    def random(self, id=None):
        self.id = id
        self.firstName = random_string("First", 7)
        self.lastName = random_string("Last", 7)
        self.address = random_string("address", 20)
        self.homePhone = random_digits(10)
        self.mobilePhone = random_digits(10)
        self.workPhone = random_digits(10)
        self.email1 = "%s@%s.%s" % ("email1", random_set(5), random_set(3))
        self.email2 = "%s@%s.%s" % ("email2", random_set(5), random_set(3))
        self.email3 = "%s@%s.%s" % ("email3", random_set(5), random_set(3))
        return self

    def clean(self):
        self.firstName = self.firstName.strip()
        self.lastName = self.lastName.strip()
        self.address= self.address.strip()
        return self

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return "%s: '%s' '%s'" % (self.id, self.firstName, self.lastName)

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
