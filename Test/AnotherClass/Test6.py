from Test.AnotherClass.Test5 import Human


class Female(object):

    def __init__(self, name):
        self.name = name

    def good_looking(self):
        print("{} is very smart".format(self.name))

    def main(self):
        self.good_looking()


if __name__ == "__main__":
    r = input("Enter the name: ")
    m = input("Enter the gender: ")
    obj = Female(r)
    obj.main()
    obj = Human(r, m)
    obj.speak_name()
    Human.speak("This is {}".format(r))

