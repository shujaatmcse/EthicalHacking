#!/bin/python3

# Here is a quick intro of function
def hello():
	print("Hello World")

#Function that returns value
def sum(a,b):
	return a+ b;

#Function that do not returns value

def sumPrint(a,b):
	print(a + b);
 
 
 # taking input
 #Note by default python takes input as string, if you want to take as int type int in the beigaing 
x = int (input ("Enter first number"));
y = int (input ("ENter second number"));

hello();
print(sum(x,y));


#calling funtion
sumPrint(x,y)
