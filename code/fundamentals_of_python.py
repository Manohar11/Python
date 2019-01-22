# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 21:48:21 2019

@author: manarayanan
"""
#Fundamentals of python programming
#Python data types
#Numeric data types examples - int, float, complex
def printDTypes():
    x = 10
    print("Int ",type(x))
    y = 11.5
    print("Float ",type(y))
    z = 10 + 11.5j
    print("Complex ", type(z))
	
#String data type example - str
s = "Explore and Exploy"
print(s," - ", type(s))

# Data structure - List
a = [1, 3, 6, "Hai", 0.2, "Hello"]
print(a)

#Using slicing operator[]:
#1. To retrieve all the items in the lisst
print(a[:])

#2. To get specific element and range
print(a[0])
print(a[2:6])

# Data structure - set
a = {10, 20.3, "Hai"}

print(a)
print(type(a))

# Data structure - dict
a = {1: "Hai", 2: "Hello"}

print(a)

print(type(a))
print(a[1]," ", a[2])

# Data structure - tuple
a = (10, 50,  "Hai", 30.20, "Hello")

#Using slicing operator[]:
print(a[:])
print(a[2:5])
a[0] = 20
#Changes are not allowed, It's immutable

# Looping Constructs

# Traverse list of elements
l1 = range(0, 100)

for i in l1:
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")


#Python functions
#Python user defined function - Syntax
"""
def function_name(parameters):
	'''doc string '''
	[Block statements]
	[return statement]
"""
  
#Example
x, y = 10, 30
#Python user defined function
def summation(x, y):
    ''' Summation of two numbers
    example: c = a + b '''
    z = x + y
    return z

#Function call
print("Sum of two numbers = ", summation(x, y))


#Defualt function arguments

#Python default arguments function - Syntax
"""
def function_name(par1, par2 = value):
	'''doc string '''
	[Block statements]
	[return statement]
"""
x, y = 10, 30
#Python defualt arguments function
def summation(x, y = 100):
    ''' Summation of two numbers
    example: c = a + b '''
    z = x + y
    return z

#Function call
print("Sum of two numbers = ", summation(x))

#Variable length arguments
#Python variable length arguments function - Syntax
"""
def function_name(par1, *args):
	'''doc string '''
	[Block statements]
	[return statement]
"""
x = 10
#Python variable length arguments function
def var_args(x, *args):
    ''' Return tuple of numbers'''
    return args

#Function call
print("Number of arguments = ", var_args(x, 1, 10, 20))


#Python keyword arguments

#Python keyword arguments function - Syntax
"""
def function_name(par1, **args):
	'''doc string '''
	[Block statements]
	[return statement]
"""

x = 10
#Python keyword arguments function
def kw_args(x, **args):
    ''' Return dictionary of numbers'''
    return args

#Function call
print("Key-value pairs of keyword arguments = ", kw_args(x, a = 10, b = 20, c = 100))

#Lambda functions

#Python lambda functions - Syntax
'''
lambda args: return statement

'''



