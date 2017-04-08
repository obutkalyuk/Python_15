from sys import maxsize
class Contact:
    def __init__(self, id= None, firstName=None, lastName=None, address=None, homePhone=None,mobilePhone=None,
                 workPhone=None, secondaryPhone = None,  email1=None, email2=None, email3=None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
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

