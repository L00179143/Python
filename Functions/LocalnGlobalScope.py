"""
Author : Sudharsan Vishvanath
Contact : L00179143@atu.ie
Purpose : Tutorials and demonstration for Tuples in python programming
Pre-requisites : Python3 installation.
"""

# A variable is only available from inside the region it is created. Is called as scope. Lets see with an example.


# Below a local variable is accessed from a function within a function

def customfunction():
  value = 1111
  def inner():
    print(value)
  inner()

customfunction()

# using Local and Global Scope

x = 3333

def SudharsanFunction():
  x = 2222
  print(x)

SudharsanFunction()

print(x)