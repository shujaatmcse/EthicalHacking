#!/bin/python3
print("hello world")
# forcing to create variable as str, so later we can just print it with others
hieght =  str(5.7);
# you can convert variable , but you want to receive inout as int you can use th eint function
age =int (input("Enter your age"));

print(" printing age " + str(age))

name= input( "Enter your name ")

#note that hieght is not converted to str becasue at the creation time we specifically said it str
print ("Your name is "+ name+ " and your age is "+ str(age) + " your hieght is" + hieght )

# rememeber the syntax, espacialy : after if clause and else and just a space for indentation
if(age> 16):
 print ("You are old enough to apply for G1 license")
else: 
 print ( " wait untill you become 16")
