"""How to run a python code"""
# print("Hello, World!")

"""Assign values"""
# Height = 170.
# print("The height is",Height,"cm") # the print function could have multiple variables

"""Multiple lines"""
# Weight = \
# 65.
# print("The weight is",Weight,"kg")

"""Types of variables"""
# Name = "Adam"
# Age = 25
# Height = 175.
#
# print("Name:",Name) # String
# print("Age:",Age) # Integer
# print("Height:",Height) # Float

"""Assign values to mulitple variables"""
# Name, Age, Height = "Adam", 25, 175.
#
# print("Name:",Name) # String
# print("Age:",Age) # Integer
# print("Height:",Height) # Float

"""String operation"""
# String1 = "Python"
# String2 = "Hello, World!"
#
# # take a part of the String
# print("the first letter of",String1,"is",String1[0])
# print("the 2nd to 4th letter of",String1,"is",String1[1:4]) # String[1:4] means from the 2nd to the letter before the 5th
# print("Join two strings:", String1 + String2) # + : join strings
# print("If P is in",String1,":","P" in String1)
# print("If p is in",String1,":","p" in String1) # in: return True or False

"""List"""
# List1 = ["Adam",25,175.,65]
#
# print("List1 is:",List1)
# print("The 2nd element of",List1,"is:",List1[1])
# print("The 2nd to 4th:",List1[1:4])
#
# # Assign new value to the list
# List1[1] = 26
# print("The new value of the list is:",List1)
#
# # Append value to the List
# List1.append("Student")
# print("List with Student:",List1)
#
# # remove one element from the list
# del List1[1]
# print("List without age:",List1)
#
# #length of one List
# print("The length of the new List1 is", len(List1))
#
# # Merge two lists
# List2 = ["Python","Hello,World!"]
#
# print("List1 + List2 is",List1+List2)

"""Pay attention when you try to copy a list..."""
# a = ["Adam",25,175.,65]
# b = a
# print("The original list is",b)
# b[2] = 180.
# print("The new b is",b)
# print("a after changing b is",a)

"""If you do not want to change the calue of a..."""
# a = ["Adam",25,175.,65]
# b = a[:] # slice of a
# # b = a.copy() # available after python 3.3
# print("The original list is",b)
# b[2] = 180.
# print("The new b is",b)
# print("a after changing b is",a)

"""Tuple"""
# Tuple1 = ("Adam",25,175.,65)
# print("Tuple1:",Tuple1)
#
# # Can NOT Assgin new values to a Tuple
# # Tuple1[1] = 26
# # or append
# # Tuple1.append("Student")
# # or del
# # del Tuple1[1]
#
# Tuple2 = ("Python","Hello,World")
# print("Tuple1 + Tuple2:",Tuple1+Tuple2)

"""Dictionary"""
# Dict1 = {'Name': 'Adam', 'Age':25,'Height': 175., 'Weight': 65.}
#
# print("The Name in",Dict1,"is",Dict1['Name'])
# print("The Age in",Dict1,"is",Dict1['Age'])
#
# # Modify the value of a key
# # Kaz Sato Oct 18th
# # David Ha OCt 29th
# Dict1['Age'] = 26
# print("The NEW Age in",Dict1,"is",Dict1['Age'])
#
# # Delete
# del Dict1['Age']
# print("The Dict1 without Age is",Dict1)

"""Define new functions"""
# def AddAndSubtract(a,b):
# 	Sum = a + b
# 	Diff = a - b
# 	return Sum,Diff
#
# print("The result of the function is",AddAndSubtract(3.,4.))

"""If"""
# def GreaterThan30(a):
# 	if a > 30:
# 		Result = "True"
# 	else:
# 		Result = "False"
# 	return Result
#
# print("The result of 29 is",GreaterThan30(29))
# print("The result of 55 is",GreaterThan30(55))

"""while loop"""
# a = 0
# while a < 10:
# 	print(a**2) # Square of a
# 	a = a + 1
#
# b = 0
# while True:
# 	print(b**3)
# 	b = b + 1
# 	if b >= 10:
# 		quit()

"""for loop"""
# for letter in "Python":
# 	print(letter)
#
# for x in [0,1,2,3,4,5,6,7,8,9]:
# 	print(x**2)

"""Import packages"""
# import numpy
#
# a = numpy.ones((3,4))
# print(a)

# Or
# import numpy as np
#
# a = np.ones((3,4))
# print(a)

# Or
# from numpy import ones
# a = ones((3,4))
# print(a)

# useful packages
# numpy: http://www.numpy.org
# pandas: https://pandas.pydata.org/index.html (data processing)
# tensorflow: https://www.tensorflow.org (Machine Learning)
