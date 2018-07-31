# Overridden - Take the method that already exist in super class and instead make it obey what i have in this class so
# in the current class

from Test.Class.AbstractInheritance import Shape


class Rectangle(Shape):

    def __init__(self, width, height):

        self.width = width
        self.height = height

        super(Rectangle, self).__init__()

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return self.width * 2 + self.height*2


if __name__ == "__main__":
    rect = Rectangle(5, 6)
    print(rect.area())
    print(rect.perimeter())