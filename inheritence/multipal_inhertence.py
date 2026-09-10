"""Multiple Inheritance
When a class can be derived from more than one base class
this type of inheritance is called multiple inheritances. In multiple inheritances,
 all the features of the base classes are inherited into the derived class. """


class department:
    department_name=""
    def department_name(self):
        print(self.department_name)

class University:
    university_name=""
    def university_name(self):
        print(self.university_name)

class course:
    def __init__(self,course_name):
        self.course_name=course_name

class Student(department,University,course):
    def study_detail(self,student_name):
        self.student_name=student_name
        print(f"my name is {self.student_name} i study in {self.university_name} at this department {self.department_name} and i learn {self.course_name}")


student1=Student("Python")
student1.department_name="Software Engineering"
student1.university_name="Islamia University of Bahawalpur"
student1.study_detail("Muhammad Usman Ghani")



# Another method of Multiple inheritance

class GrandFather:
    def __init__(self,grandfather_name):
        self.grandfather_name=grandfather_name

class Father(GrandFather):
    def __init__(self,father_name,grandfather_name):
        self.father_name=father_name
        GrandFather.__init__(self,grandfather_name)

class Son(Father):
    def __init__(self,son_name,father_name,grandfather_name):
        self.son_name=son_name
        Father.__init__(self,father_name,grandfather_name)
        print(f"my name is {self.son_name} and my father is {self.father_name} and my grandfather is {self.grandfather_name}")


object1=Son("Muhammad Usman Ghani","Muhammad Riaz","Muhammad Hanif")
