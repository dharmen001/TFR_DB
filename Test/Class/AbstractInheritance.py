# Abstract methods: An abstract method is a method that must be overridden. It must be overridden.
# / Interfaces:- Is basically a template that tells your class How to behave. its just a structure.
# Overriding

from abc import ABCMeta, abstractmethod

# interface


class Shape(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


if __name__ == "__main__":
    s = Shape()
    print(s)
    s.area()
    s.perimeter()


