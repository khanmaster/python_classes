# create a Cat class

# one function that returns "MEOWWWWW"

# create 2 class level variable
# create 3 objects
# display all information with each object
# change the class variable values in each object and display
# sudo code each block of code


class Dog:


    def __init__(self, name, colour):
        self.animal_kind = "canin"
        self.name = name
        self.colour = colour
        self.bark()

    def bark(self):
        return "woof"

    def print_name(self):
        return self.name

    def print_colur(self):
        print(self.colour)

fido = Dog("fido", "brown")

print(fido.print_name())
print(fido.print_colur())


# print(fido.colour)
# print(fido.print_colur())
# print(fido.name)
# print(fido.animal_kind)