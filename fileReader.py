#!/bin/Python3

file = open("Months.txt", "r")


#Mehtod 1.

#note you read file and save its contents to a variable


# Method 1: Read the entire file and print its contents
contents = file.read()
print(contents)
print('\n')

# Method 2: Loop over each line in the file
file.seek(0)  # Reset the file pointer to the beginning
for line in file:
    print(line)

file.close()
