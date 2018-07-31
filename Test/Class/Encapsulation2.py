from Test.Class.Encapsulation import ClassName


class EncapsulationNew(object):

    def __init__(self, person):

        self.person = person

    @staticmethod
    def person_name(text):
        print(text)

    def main_new(self):
        self.person_name("harsh")


e = EncapsulationNew(ClassName)
e.main_new()
EncapsulationNew.person_name("ravi")