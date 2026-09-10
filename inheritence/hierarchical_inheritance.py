"""
Hierarchical Inheritance

When more than one derived class are created from
 a single base this type of inheritance is called hierarchical inheritance.
  In this program,
 we have a parent (base) class and two child (derived) classes.
 """


class parents:
    def func1(self):
        print("we are parents 🥰")

class child1(parents):
    def func2(self):
        print("I am first child of my parents")

class child2(parents):
    def func3(self):
        print("I am second child of my parents")


object1=child1()
object2=child2()
object1.func1()
object1.func2()
object2.func3()
object2.func1()
