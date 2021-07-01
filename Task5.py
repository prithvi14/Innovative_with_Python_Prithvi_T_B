# 1. Write a program in Python to allow the error of syntax to be handled using exception handling.
# HINT: Use SyntaxError

try:
    inp = eval("Enter the data:")
    if inp.isnumeric():
        print("integer")
    else:
        print(inp.upper())
except SyntaxError:
    print("There is something wrong in your code")


# 2. Write a program in Python to allow the user to open a file by using the argv module. If the
# entered name is incorrect throw an exception and ask them to enter the name again. Make sure
# to use read only mode.

import sys 
try:
    f = open(sys.argv[1],"r")
    print(f.read())
except IOError:
    print("No such file or dirctory! Enter the correct file name")



# 3. Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits” 

try:
    i = input("Enter a four digit number: ")
    print(len(i))
    if len(i) != 4:
        raise Exception
    else:
        print(i)
except Exception:
    print("The length is too short/long !!! Please provide only four digits" )
    


# 4. Create a login page backend to ask users to enter the username and password. Make sure to
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
# should not be more than 3 times.

def fun():
    username = input("Enter the username: ")
    count = 1
    actual_password = "prithvi"
    while count<=3:
        password = input("Enter the password: ")
        if password != actual_password:
             print("password doesn't match! please enter the password again")
             count += 1

        else:
            print("successful login")
            break
    
fun()


# 5. Go through the link provided below to understand finally and raise concept:
# https://www.programiz.com/python-programming/exception-handling


# 6. Read doc.txt file using Python File handling concept and return only the even length string from
# the file. Consider the content of doc.txt as given below:
# Hello I am a file
# Where you need to return the data string
# Which is of even length
# Make sure you return the content in The same link as it is present.

f = open("doc.txt", "r")
for lne in f:
    words = lne.split()
    for word in words:
        if len(word)%2 == 0:
            print(word,end = " ") 