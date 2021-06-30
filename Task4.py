# 1. Write a program to reverse a string.
# Sample input: “1234abcd”
# Expected output: “dcba4321”

input =  "1234abcd"
output = input[::-1]
print(output)

# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12

def fun(data):
    uppercases = 0
    lowercases = 0
    for i in data:
        if i.isupper():
            uppercases += 1
        elif i.islower():
            lowercases += 1
    return uppercases,lowercases

uppercases,lowercases = fun("abcSdefPghijQkl")
print("No. of Uppercase characters :", uppercases ,"No. of Lower case Characters :",lowercases)


# 3. Create a function that takes a list and returns a new list with unique elements of the first list.

def fun1(list1):
    list2 =[]
    [list2.append(x) for x in list1 if x not in list2]
    return list2
list1= [1,2,3,4,5,6,2,7,9,10,1,10]
list2 = fun1(list1)
print(list2)

# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.

txt = input("Enter the text: ")
word = txt.split('-')
word.sort()
word= '-'.join(word)
print(word)

# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT

seq = input("Enter the sequence:")
seq = seq.upper()
print(seq)
        
# 6. Define a function that can receive two integral numbers in string form and compute their sum and
# print it in the console

def fun(a,b):
    sm = int(a) +int(b)
    print(sm)
a,b = input("enter two numbers: ").split()
fun(a,b)

# 7. Define a function that can accept two strings as input and print the string with the maximum length
# in the console. If two strings have the same length, then the function should print both the strings line
# by line.

def fun(a,b):
    if len(a) == len(b):
        print("\n",a,"\n",b)
    elif len(a) > len(b):
        print(a)
    else:
        print(b)
a =input("Enter sting a: ")
b = input("Enter string b: ")
fun(a,b)


# 8. Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).

def fun():
    tup = ()
    l = list(tup)
    for i in range(1,21):
        l.append(i**2)
    print(tuple(l))

fun()

# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.
# Sample input: show Numbers(3) (where limit=3)
# Expected output:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

def showNumbers(limit):
    for i in range(0,limit+1):
        if i%2 == 0:
            print(i,"EVEN")
        else:
            print(i,"ODD")
    
showNumbers(20)

# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)

l =[]
for i in range(1,21):
    l.append(i)
print(l)
lis = list(filter(lambda x : x%2 ==0,l))
print(lis)

# 11. Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
# numbers in the filtered list. Use lambda() to define anonymous functions.

list1 = [1,2,3,4,5,6,7,8,9,10]
d = list(filter(lambda x: x %2 == 0,list1))
d = list(map(lambda x : x*x , d))
print(d)

# 12. Write a function to compute 5/0 and use try/except to catch the exceptions

def fun():
    return 5/0

try:
    fun()

except ZeroDivisionError:
        print("Cant divisible by zero")
except:
    print("other Exceptions")
    


# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().

from functools import reduce
import operator
list1 = [1,2,3,4,5,6,7,8,9]
li = [str(i) for i in list1]
d = reduce(operator.add,li)
print(d)


# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.

list1 = [3,7,21,6,14,42,49,18,15]
d = list(filter(lambda x: x % 3 != 0 and x %7 == 0,list1))
print(d)



# 15. Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.

def fun(n):
    return n*n
list1 = [1,2,3,4,5,6,7,8]
d = map(fun,list1)
print(list(d))

# 16. What is the output of the following codes:

def foo(): 
    try: 
        return 1 
    finally: 
        return 2
k = foo()
print(k)
# #2

def a(): 
    try: 
        f(x, 4) 
    finally: 
        print('after f') 
        print('after f?')
a()
# after f
# after f?
# NameError: name 'f' is not defined