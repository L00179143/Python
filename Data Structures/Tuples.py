"""
Author : Sudharsan Vishvanath
Contact : L00179143@atu.ie
Purpose : Tutorials and demonstration for Tuples in python programming
Pre-requisites : Python3 installation.
"""

thistuple = ("python", "C++", "java")
print(thistuple)


tuplecheck = (0, [1, 2, 3], (4, 5, 6), 7.0)
print(tuplecheck)
print(type(tuplecheck))

# Indexing and Slicing a Tuple

print('The first element:', tuplecheck[0])
print('The last element:', tuplecheck[-1])
print('The data type of the second element:', type(tuplecheck[1]))

# Concatenation of Python tuples

tuple1 = (0, 1)
tuple2 = ('python', 'c++')

# Concatenating above two
print(tuple1 + tuple2)

