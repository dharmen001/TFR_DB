import sys


class Character(object):
    # static/class Variable
    total_number_of_characters = 0
    MAX_HEALTH = sys.argv[1]

    def __init__(self, name):
        self.name = name
        self.health = Character.MAX_HEALTH
        Character.total_number_of_characters += 1


def name_p(person_name):
    return person_name


bob = Character(name_p(sys.argv[2]))
ryan = Character('Ryan Steve')

print(Character.total_number_of_characters)
print(Character.MAX_HEALTH)

print(bob.name)


