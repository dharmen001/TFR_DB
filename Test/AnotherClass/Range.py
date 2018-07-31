from math import pi
import sys


class CircleRadius(object):

    def __init__(self, radius):
        self.radius = radius

    def circle_radius(self):
        return pi * (self.radius ** 2)

    def main(self):
        self.circle_radius()
        print(self.circle_radius())


if __name__ == "__main__":
    r = int(sys.argv[1])
    obj = CircleRadius(r)
    obj.main()







