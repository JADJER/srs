
class Person(object):

    first_name = ""
    sur_name = ""
    last_name = ""

    def __init__(self, first, sur, last):
        self.first_name = first
        self.sur_name = sur
        self.last_name = last

    def get_first_name(self) -> str:
        return self.first_name

    def get_sur_name(self):
        return self.sur_name

    def get_last_name(self):
        return self.last_name
