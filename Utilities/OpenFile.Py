
"""
Author : Sudharsan Vishvanath
Contact : L00179143@atu.ie
Purpose : Tutorials and demonstration for Lists in python programming
Pre-requisites : Python3 installation.
"""

# Python program to demonstrate
# opening a file
 
 
# Open function to open the file "myfile.txt"
# (same directory) in read mode and store
# it's reference in the variable file1
 
file1 = open("C:\InfraCode\myfile.txt")
 
# Reading from file
print(file1.read())
 
file1.close()