"""
 Inheritance is a fundamental concept in object-oriented programming (OOP)
that allows a class (called a child or derived class) to inherit attributes
and methods from another class (called a parent or base class).
"""
# Example

class person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def infomation(self):
        print(f"i am {self.name},and my age is {self.age},and my height is {self.height}")

class student(person):

    def student_infomation(self,roll_number,uni_name,depart_name):
        self.roll_number=roll_number
        self.uni_name=uni_name
        self.depart_name=depart_name

        print(f"my name is {self.name},and my age is {self.age},and my height is {self.height}, i study in {uni_name} and my roll number is {roll_number}, my depart name {depart_name}")

class teacher(student):
    def teach_infomation(self,coruse_name,depart_name):
        self.coruse_name=coruse_name
        self.depart_name=depart_name
        print(f"I am teacher my Name {self.name},i teach a course {self.coruse_name},and my depart name {self.depart_name}")



student1=student("Muhammad Usman Ghani","22","5.09")
teacher1=teacher("Muhammad Usman Ghani","22","5.09")
student2=student("Muhammad Waqas","23","5.10")


student1.student_infomation(roll_number="23",uni_name="IUB",depart_name="SE")
teacher1.teach_infomation(coruse_name="Python",depart_name="IT")
student2.student_infomation(roll_number="23",uni_name="IUB",depart_name="SE")
