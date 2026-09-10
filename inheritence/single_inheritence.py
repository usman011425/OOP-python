"""
Single Inheritance:
Single inheritance enables a derived class to inherit properties from a
 single parent class, thus enabling code reusability and the addition of new
 features to existing code.
"""

# super() Function
"""
super() function is used to call methods from a superclass following Python’s
Method Resolution Order (MRO). In particular, it is commonly used in the child
class's __init__() method to initialize inherited attributes.
This way, the child class can leverage the functionality of the parent class.
"""


class Business:
    def __init__(self, business_name, owner_name):
        self.business_name = business_name
        self.owner_name = owner_name


class Business_Information(Business):
    def __init__(self, business_name, owner_name, business_type, business_invest, business_revnew):
        super().__init__(business_name, owner_name)
        self.business_type = business_type
        self.business_invest = business_invest
        self.business_revnew = business_revnew
        business_profit = business_revnew - business_invest

        print(f"my business name is {self.business_name}\n my business Owner is {self.owner_name}\n"
              f"my business type is {self.business_type} and my business investment is {self.business_invest}"
              f"my business revnew is {self.business_revnew} now my business profit is {business_profit} ")


business1 = Business_Information("RRMUG", "Muhammad Usman Ghani", "Car Deller", 1000000, 2000000)




class person:
    def func1(self):
        print("i am a person with good nature")

class student(person):
    def func2(self):
        print("i am a student with good nature and have good ablity of hard working")

object1=student()
object1.func1()
object1.func2()