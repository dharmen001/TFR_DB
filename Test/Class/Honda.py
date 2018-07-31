from Test.Class.Inheritance import Car


class Honda(Car):

    def __init__(self, color):

        # super(Honda, self).__init__("Honda", color)
        Car.__init__(self, "Honda", color)


myHonda = Honda("Green")
myHonda.drive()
myHonda.park()