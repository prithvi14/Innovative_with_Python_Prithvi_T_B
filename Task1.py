# 1. Create three variables in a single line and assign values to them in such a manner 
# that each one of them belongs to a different data type.

a , b , c = 1 , 2.01 , "hello"
print("a =",a,"\nb =",b,"\nc=",c)


# 2. Create a variable of type complex and swap it with another variable of type integer.

x = 2+3j
y = 10
print("Before Swaping: ", x, y)
x,y = y,x
print("After Swaping: ", x ,y)


# 3. Swap two numbers using a third variable and do the same task without using any third variable.

# swaping using a third variable
x , y = 7 , 8 
print("Before Swaping:", x , y)
temp = x
x = y
y = temp
print("After Swaping:", x , y)

# swaping without using any third variable
x , y = 7, 8
print("Before Swaping:", x , y)
x , y = y, x
print("After Swaping:", x , y)


# 4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.

#python 2.x
txt = raw_input("Enter the text: ")
print "User Input: ", txt

#python 3.x
txt = input("Enter the text: ")
print("User Input:", txt)


# 5. Write a program to complete the task given below:
# Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
# another variable called z. Add 30 to z and store the output in variable result and print result as the
# final output.

num = input("Enter any two numbers between 1 to 10:").split()
if 1 <= int(num[0]) <= 10 and 1 <= int(num[1]) <= 10:
    print("Number not in range")
else:
    z = int(num[0]) +int(num[1])
    result = 30+z
    print(result)


# 6. Write a program to check the data type of the entered values.
# HINT: Printed output should say - The data type of the input value is : int/float/string/etc

from ast import literal_eval

def check_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):

        return str

x = input("Enter the data: ")
print("The data type of the input value is :", check_type(x))

# 7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.
# (Refer: https://capitalizemytitle.com/camel-case/)


def create_format(data):
    upper_camelcase = data.title()
    print(upper_camelcase)
    lower_camelcase = data.lower()
    print(lower_camelcase)
    snakecase = ''.join([c.lower() if c.isupper() else c for c in data +'_'])
    print(snakecase)
    uppercase = data.upper()
    print(uppercase)


create_format("ILoveIndiaAndI")


# 8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. 
# Will it change the value? If Yes then Why?

a = 1000
print(a)
a = "string"
print(a)
# yes, because python is dynamically typed programming language.

