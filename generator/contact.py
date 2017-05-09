from model.contact import Contact
from fixture.string_helper import *
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, arga = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except  getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 8
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


testdata = [Contact(firstName="", lastName="", address="", homePhone="", mobilePhone="",
                               workPhone="", email1="", email2="", email3="")] + \
          [Contact(firstName= random_string("First", 7),
                   lastName=random_string("Last", 7),
                   address = random_string("address", 20),
                   homePhone = random_digits (10),
                   mobilePhone = random_digits (10),
                   workPhone = random_digits (10),
                   email1= "%s@%s.%s" % ("email1", random_set(5), random_set(3)),
                   email2="%s@%s.%s" % ("email2", random_set(5), random_set(3)),
                   email3="%s@%s.%s" % ("email3", random_set(5), random_set(3)))
          for i in range(n)]



file  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent =2)
    out.write(jsonpickle.encode(testdata))