"""
Author : Sudharsan Vishvanath
Contact : L00179143@atu.ie
Purpose : Tutorials and demonstration for Lists in python programming
Pre-requisites : Python3 installation.
"""

# List comprehension in Python is a easier way of creating lists from the ones that is already present . 
# It is a shorter syntax to create new list from existing list and their including their values.

# using a loop to iterate through items in list and for each number its multiplied by the same number again.

numbers = [1, 2, 3, 4, 5]    
num = [n**2 for n in numbers]  
print(num)  

