#-------1----------------
def print_dharmendra():
    for _ in range(6):
        print ("dharmendra")

print_dharmendra()

#-----------2--------------
def print_dharmendra(amount):

    for _ in range(amount):
        print ("dharmendra")

a = 6
print_dharmendra(a)

#-------3---------------

from math import pi
def circle_area(radius):
    return pi * (radius ** 2)

area = circle_area(50)
print(area)

#-----4--------
from math import  pi
import sys
def circle_area(radius):
    return pi * (radius **2)

for _ in range(6):
    user_radius = int(sys.argv[1])
    print(circle_area(user_radius))

#-----5--------------
from math import pi

def circle_area(radius):
    return pi * (radius **2)

while True:
    user_radius = int(input("Enter a radius: "))
    print(circle_area(user_radius))

# ---------------6------------------------

def remove_volwels(string):
    vowels = 'aeiou'
    new_string = ''

    for characters in string:
        if characters  not in vowels:
            new_string += characters

    return new_string

text = 'i love my india'
text2 = 'i love you dharmendra'
text_without_vowels = remove_volwels(text)
text_without_vowels2 = remove_volwels(text2)
print(text_without_vowels, text_without_vowels2)


























