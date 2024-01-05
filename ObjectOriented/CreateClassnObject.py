"""
Author : Sudharsan Vishvanath
Contact : L00179143@atu.ie
Purpose : Tutorials and demonstration for Lists in python programming
Pre-requisites : Python3 installation.
"""

class Employee:
    # class variables
    company_name = 'Sudharsan Telephony'

    # constructor to initialize the object
    def __init__(self, name, salary):
        # instance variables
        self.name = name
        self.salary = salary

    # instance method
    def show(self):
        print('Employee:', self.name, self.salary, self.company_name)

# create first object
emp1 = Employee("Sudharsan", 200000)
emp1.show()

# create second object
emp2 = Employee("Swats", 150000)
emp2.show()
