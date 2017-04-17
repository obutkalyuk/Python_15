from model.group import Group
from fixture.string_helper import random_string

constant = [Group(name="name1", header="header1", footer="footer1"),
            Group(name="name2", header="header2", footer="footer2")]

testdata = [Group(name="", header="", footer="")] + \
          [Group(name= random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
          for i in range(5)]