from model.group import Group
from fixture.string_helper import random_string
import os.path
import json
import getopt
import sys

try:
    opts, arga = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except  getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/group.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

constant = [Group(name="name1", header="header1", footer="footer1"),
            Group(name="name2", header="header2", footer="footer2")]

testdata = [Group(name="", header="", footer="")] + \
          [Group(name= random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
          for i in range(n)]

file = full_config_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default = lambda x: x.__dict__, indent = 2))