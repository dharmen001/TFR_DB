from Test.Class.Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side_length):

        self.side_length = side_length
        super(Square, self).__init__(side_length, side_length)

    # Override Rectangle area method

    def area(self):
        print("Using Square area method")
        return self.side_length * self.side_length


s = Square(5)
print(s.area())
print(s.perimeter())

