# Objects are pass by value and refrence

# pass by value
"""its not changing as the value gets passed in function"""
x = 56


def change_value(num):
    num = 90


print(x)
change_value(x)
print(x)


# pass by refrence
# ship is changing the address not copy the address
# only taking refrence

class Boat(object):

    def __init__(self):
        self.cargo_weight = 23  # tons


def change_cargo_weight(ship):
    ship.cargo_weight = 45


boat = Boat()

print(boat.cargo_weight)
change_cargo_weight(boat)
print(boat.cargo_weight)


