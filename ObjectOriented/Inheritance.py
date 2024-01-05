
"""
Author : Sudharsan Vishvanath
Contact : L00179143@atu.ie
Purpose : Tutorials and demonstration for Lists in python programming
Pre-requisites : Python3 installation.
"""

# Here we created a CLASS named "PersonalDetails"

class PersonalDetails:
  def __init__(my, fname, lname):
    my.firstname = fname
    my.lastname = lname

  def printname(my):
    print(my.firstname, my.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = PersonalDetails("Sudharsan", "Vishvanath")
x.printname()

# We created a subclass named student and inherited the same properties
class Student(PersonalDetails):
  pass

# Now we will use the student class to create an object and it Inherits the details from Main class
x = Student("Rahul", "Gopikrishnan")
x.printname()
