#!/bin/python3
# YOu write this line to tell the linux where phyton program is , its binary files

#stings manuplation
# some strign variables
str1 = " Hello World";

print("Hello World")
#Hello World

print("Hello World"+ " it is my first app")
#Hello World it is my first app

num1 = 53;
num2 = 42;
result = num1 + num2;


#MATH / Division,  squre **,  % Module , // noreminder or float

print (5*6) # Multiplication
print (70 /8 ) # multiplication with reminders
print (70 // 8) # no reminder, so result in integers
print (32 % 6) # only reminder in result 
print("I am printing number "+ str(result))

"""
30
8.75
8
2
I am printing number 95
"""

# using builtin function 
# using lower function 

print("Using builtin function to convert text to lower " + str1.lower())

print("Using builtin function to convert text to upper " + str1.upper())
"""
Using builtin function to convert text to lower  hello world
Using builtin function to convert text to upper  HELLO WORLD
"""

# creating fucntions
# funtion , rememeber indentation  and colin
def what_are_you():
	print("my  name is kali linux") # indentation by using tab

print("Calling the functin that do not return value")
#Calling the functin that do not return value

what_are_you()
#my  name is kali linux


# creating a function that claculate the power of a number
# do not retrun value
def rais_to(base_num, powerTo):
	result= base_num **powerTo
	print(" Printing result " + str(result))
#Printing result 125

	
# calling the function
rais_to(5,3)

# a function that with condition

def greaterNum(num1, num2):
    if num1 > num2:
    	print("some text")
    	print(str(num1) + " is greater than " + str(num2))
    else:
        print(str(num2) + " is greater than " + str(num1))

greaterNum(5, 10)
#10 is greater than 5


""" Let us have another that would retrun a value
def multiply"""

def drink(money):
	if money > 2:
		return " you ca have a drink for your self"
	else:
		return "you cannot have a cup of tea"
 
print(drink(2))
print(drink(2))
"""
you cannot have a cup of tea
you cannot have a cup of tea
"""
