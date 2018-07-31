#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __init__(method): allows us to immediately give our object instance variables when its created.
# self : represents the object itself. Whenever you self.something its actually creating a new variable or assigning a
# value to it. and you can access the self variable everywhere through out the programme. sometimes you don't need a
# self you can create functions but still you need self as parameter. self is a implied argument, its implicit that way.
# so self needs to be there, though its not used but it should be there. self is the object.

# methods vs functions: Methods are different from functions because its part of class and it can only be called from
# the object. methods is specif for objects that is class.

# to get more realistic lets create a Human class
# python leading and trailing underscores has some special meaning some sort of significance that puts other side of
# different method


class Human(object):
    # initializer # in other programming language its a constructor because its construct the object.
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# object is going to speak the name so that self

    def speak_name(self):
        print("My name is {}".format(self.name))

    def speak(self, text):
        print(text)

    # method
    def perform_math_operation(self, math_operation, *args):
        print("{} performed the math operation and the result was: {}".format(self.name, math_operation(*args)))


@function
def add(a, b):
    return a+b


John = Human("John", "Male")
print(John.name)
print(John.gender)
John.speak_name()
John.speak("I love python")
John.perform_math_operation(add, 24, 24)

