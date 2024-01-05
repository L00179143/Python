"""
Author : Sudharsan Vishvanath
Contact : L00179143@atu.ie
Purpose : Tutorials and demonstration for Lists in python programming
Pre-requisites : Python3 installation.
"""

# Python program to raise an exception after using divide function  
def divide(a, b):  
    if b == 0:  
        raise Exception(" Cannot divide by zero. ")  
    return a / b  
try:  
    result = divide(10, 0)  
except Exception as e:  
    print(" Oops: ", e)  


