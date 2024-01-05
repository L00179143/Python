"""
Author : Sudharsan Vishvanath
Contact : L00179143@atu.ie
Purpose : Tutorials and demonstration for Tuples in python programming
Pre-requisites : Python3 installation.
"""

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# In below function 10 is added with the number passed. 
x = lambda a : a + 10
print (x(5))

# Below function is to sum the values passed. 
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))