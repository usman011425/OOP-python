"""
Hybrid inheritance is a combination of more than one type of inheritance.
It uses a mix like single, multiple, or multilevel inheritance within the same program.
 Python's method resolution order (MRO) handles such cases.
"""


class person:
    def __init__(self,name,father_name):
        self.name=name
        self.father_name=father_name

class business_person:
    def business_person_info(self,cnic,lisense):
        self.lisense=lisense
        self.cnic=cnic


class business_detail(person,business_person):
    def business_person_detail(self,business_type,business_investment,business_revenue):
        self.business_type=business_type
        self.business_investment=business_investment
        self.business_revenue=business_revenue
        profit=business_revenue-self.business_investment
        print(f"my name is {self.name} my father name is {self.father_name}\n"
              f"my cnic is {self.cnic} and my lisense is {self.lisense}\n"
              f"my business type is {self.business_type} and my business investment is {self.business_investment}"
              f"my revenue is {self.business_revenue}\n"
              f"my profit/lose is {profit}")


object1=business_detail("Muhammad Usman ghani","muhammad Riaz")
object1.business_person_info("31205-436632722-2","led-2123")
object1.business_person_detail("Car Deller",5000000,7000000)
