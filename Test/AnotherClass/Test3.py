
"""-----10--------------"""


def add_number(*numbers):
    print(numbers)
    total = 0

    for number in numbers:
        total += number
    return total


print(add_number(23, 34, 34, 54, 66))


"""------------11------------------"""


def people_information(**people_age):
    print(people_age)
    average_age = 0

    for ages in people_age.values():

        average_age += ages

        average_age /= len(people_age)

    return average_age


print(people_information(dharmen=50, aftab=20))
