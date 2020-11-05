# Classes, objects and instantion

# How to create class
# Syntax: class name_of_class starting with Capital letter
# good naming convention is required

# classes are a way to bring data and functionality together

class Dog:


    def __init__(self, name, colour): # initialising Dog class
        self.name = name
        self.colour = colour
        self.animal_kind = "Canin"

    def bark(self):
        return "woof"
fido = Dog("fido", "brown") # creating an object of Dog class

print(fido.name)
print(fido.colour)
print(fido.animal_kind)
print(fido.bark())

































# class Dog:
#
#     animal_kind = "Canin is running "
# # defining class variable
#     # using __init__(self): to initialise a class
#     def __init__(self, name, colour):
#         self.name = name
#         self.colour = colour
#
#     def bark(self): # self refers to current class
#         self.animal_kind = "barking inside bark function"
#         return "woof"
#
# # In order to execute a class we have to create an object of this class
# fido = Dog("shahrukh", "white") # creating an object of our Dog class
#
# # print(fido.animal_kind)
# print(fido.bark())
#
# fido.animal_kind = "started flying"
# print(fido.animal_kind) # This is the prime example of Polymorphism


# print(" This is an outcome is from Lassie object")
# lassie = Dog() # creating an object of our Dog class
# print(lassie.bark())
# print(lassie.animal_kind)

#