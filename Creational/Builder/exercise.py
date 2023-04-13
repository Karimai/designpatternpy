"""
Builder Coding Exercise
You are asked to implement the Builder design pattern for rendering simple chunks of code.

Sample use of the builder you are asked to create:

cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
print(cb)
The expected output of the above code is:

class Person:
  def __init__(self):
    self.name = ""
    self.age = 0
Please observe the same placement of spaces and indentation.
"""

from unittest import TestCase


class Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return "self.%s = %s" % (self.name, self.value)


class Class:
    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str__(self):
        lines = ["class %s:" % self.name]
        lines.append("  def __init__(self):")
        for field in self.fields:
            lines.append(f"    {field}")
        return "\n".join(lines)


class CodeBuilder:
    def __init__(self, root_name):
        self._class = Class(root_name)

    def add_field(self, type, name):
        self._class.fields.append(Field(type, name))
        return self

    def __str__(self):
        return self._class.__str__()


class Evaluate(TestCase):
    expected_res = """class Person:
  def __init__(self):
    self.name = \"\"
    self.age = 0"""
    @staticmethod
    def preprocess(s: str = ""):
        return s.strip().replace("\r\n", "\n")

    def test_person(self):
        cb = CodeBuilder("Person").add_field("name", '""').add_field("age", 0)
        self.assertEqual(self.preprocess(str(cb)), self.expected_res)


class TestCodeBuilder:
    expected_res = """class Person:
  def __init__(self):
    self.name = \"\"
    self.age = 0"""

    def preprocess(self, s: str=""):
        return s.strip().replace("\r\n", "\n")

    def test_person(self):
        cb = CodeBuilder("Person").add_field("name", '""').add_field("age", 0)
        assert self.preprocess(str(cb)) == self.expected_res