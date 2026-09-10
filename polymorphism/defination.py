"""
Polymorphism means "many forms" and allows the same method,
function or operator to behave differently depending on the object or
 data it works with. This flexibility helps create more reusable, maintainable
 and scalable code.

"""

class Animal:
    def make_sound(self):
        print("that Animal sound ")
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")


dog =Dog()
dog.make_sound() # Output: "Woof!"
cat=Cat()
cat.make_sound() # Output: "Meow!"
