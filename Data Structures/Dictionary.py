"""
Author : Sudharsan Vishvanath
Contact : L00179143@atu.ie
Purpose : Tutorials and demonstration for Dictionary in python programming
Pre-requisites : Python3 installation.
"""
# Dictionaries in Python is a data structure, used to store values in key:value format. 
# This makes it different from lists, tuples, and arrays as in a dictionary each key has an associated value.

a = {}
print("Empty Dictionary: ")
print(a)
a[0] = 'Baleno'
a[2] = 'car'
a[3] = 6695
print("\nDictionary after adding 3 elements: ")
print(a)

a['Value_set'] = 6, 6, 9, 5
print("\nDictionary after adding 4 elements as a value set: ")
print(a)

a[2] = 'flight'
print("\nUpdated key value here is : ")
print(a)
a[5] = {'Nested': {'1': 'Life', '2': 'Baleno'}}
print("\nAdding a Nested Key: ")
print(a)
