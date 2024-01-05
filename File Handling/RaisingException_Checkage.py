"""
Author : Sudharsan Vishvanath
Contact : L00179143@atu.ie
Purpose : Tutorials and demonstration for Lists in python programming
Pre-requisites : Python3 installation.
"""

    # Python program to raise an exception by using check_age function checks the age  
def check_age(age):  
    if age < 18:  
        raise Exception(" Age must be 18 or above to attend college ")  
    else:  
        print(" Age is valid for college ")  
  
try:  
    check_age(11)  
except Exception as e:  
    print(" Oops: ", e)  