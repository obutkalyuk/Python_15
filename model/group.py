from sys import maxsize
from fixture.string_helper import *

class Group:
    def __init__(self, name=None, header=None, footer=None, id = None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def random(self, id = None):
        self.id = id
        self.name = random_string("name", 10)
        self.header = random_string("header", 20)
        self.footer = random_string("footer", 20)
        return self

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return "%s: '%s', '%s', '%s'" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

