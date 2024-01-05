"""
Author : Sudharsan Vishvanath
Contact : L00179143@atu.ie
Purpose : Tutorials and demonstration for Lists in python programming
Pre-requisites : Python3 installation.
"""

# Loops by design keep repeating themselves until the condition to stop the loop is met.
# The technical term is called Iteration.
# For example, if we want to show a message 100 times, then we can use a loop. It's just a simple example; you can achieve much more with loops.

# There are 2 types of loops in Python:

# for loop
# while loop

# Example of For Loop

countries = ['India', 'Lanka', 'Vietnam', 'Thailand']

# runs a loop for each item of the list, till it ends
for country in countries:
    print(country)

# Example of While Loop, The below program displays 6695 till 6699 because a condition is met and the number is incremented every time.

mycar = 6695
othercar = 6699

while mycar <= othercar:
    print(mycar)
    mycar = mycar + 1
