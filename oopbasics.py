class Element:
    def __init__(self, name, smell, atomic_number):
        self.name = name
        self.smell = smell
        self.atomic_number = atomic_number

    def number_name(self):
        return "{} {}".format(self.atomic_number, self.name)

    def name_smell(self):
        return f"{self.name} is {self.smell} on smelling"


el_1 = Element("sodium", "eggy", 11)
el_2 = Element("lithium", "fruity", 3)
el_3 = Element("argon", "odourless", 18)


print(el_1.number_name())

print(el_2.name_smell())

print(el_3.name_smell())
