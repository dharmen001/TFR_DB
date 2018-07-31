# Python Encapsulation (The Art of data hiding): Why we need that: when we look at third party framework
# What is an API? Framework
# Public: are only known to other, Private: Are only known to class, (Protected which has nothing to do with security)
# _Variable, _method


class ClassName(object):

    def __init__(self, name, name2):

        self._name = name
        self.name2 = name2

    def print_name(self):
        print(self._name, self.name2)

    def main(self):
        self.print_name()


c = ClassName("John", "Mai")
c.main()
