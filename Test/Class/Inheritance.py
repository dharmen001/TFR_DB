# to inherit the method and properties of one class to another class


# Super Class

class Car(object):
    def __init__(self, car_type, color):

        self.car_type = car_type
        self.color = color

    def drive(self):
        print("Driving My {} {}".format(self.color, self.car_type))

    def park(self):
        print("parked car")


if __name__ == "__main__":
    c = Car('Toyota', 'Yellow')
    c.drive()
    c.park()