# 1. Create a list of given structure and get the Access list as provided below:
# x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# Access list: [1, 2, 3, 4]Access list: [600, 700]
# Access list: [100, 300, 500, 600, 800]
# Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
# Access list: [10]
# Access list: [ ]

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][0:4])
print(x[6:8])
print(x[0::2])
print(x[::-1])
print([x[5][5][0]])
x.clear()
print(x)


# 2. Create a list of thousand numbers using range and xrange and see the difference between each
# other.
# (For reference:https://www.techbeamers.com/python-xrange-range/)

x = range(1,1000,2)
y = xrange(1,1000,2)

#xrange is fastert than range
#range returns a static lsit type object where as xrange returns xrange object


# 3. How Tuple is beneficial as compared to the list?

# Tuple is faster tahn list because of its static nature
# Some Tuple can be used as dictionary keys becuase they are immutable, whereas lists can never be used as dictionary keys


# 4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
# the number which is divisible by 3 and is a multiple of 2.

import random
randomlist = []
for i in range(0,10):
    n = random.randint(1,100)
    randomlist.append(n)
print(randomlist)
x = [i for i in randomlist if i%3 == 0 and i%2 ==0]
print(x)



# 5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
# string with their index.

string = "Hello How are you"
reversed_string = string[::-1]
for i in reversed_string:
    if set('aeiou').intersection(i.lower()):
        print(i)
    



# 6. Write a program in Python to iterate through the string “hello my name is abcde” and print the
# string which is having an even length.

string = "hello my name is abcde"
words = string.split()
x = [i for i in words if len(i)%2 ==0]
print(x)



# 7. Write a program in python to print the pair of numbers whose sum is equal to the result
# number that is let's say 8.
# x=[1,2,3,4,5,6,7,8,9,-1]

def getPairs(x, result_number):
    n = len(x)
    pair = []
    for i in range(0, n):
        for j in range(i + 1, n):
            if x[i] + x[j] == result_number:
                pair.append((x[i],x[j]))
    return pair
                
 
x = [1,2,3,4,5,6,7,8,9,-1]
result_number = 8
print(getPairs(x, result_number))



# 8. Write a program in Python to complete the following task:
# Create two lists such as even_list and odd_list
# Ask user to enter a number in the range of 1,50 and make sure if the entered number is 
# even, append it to the even_list and if the entered number is odd append it to the odd_list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you enter all the 5 elements, calculate the sum of the list and return the
# maximum of the list.

even_list = [2,4,6,8,10]
odd_list = [1,3,5,7,9]
evn_len = len(even_list)
odd_len = len(odd_list)
odd_count =0
even_count =0
while True:
    user_input = int(input("Enter the number between 1 and 50: "))
    if user_input%2 ==0:
        even_count += 1
        if even_count <= 5:
            even_list.append(user_input)
        else:
            print("Reached maximum limit of even numbers")
    else:
        odd_count += 1
        if odd_count <=5:
            odd_list.append(user_input)
        else:
            print("Reached maximum limit of odd numbers")
    if len(even_list) == evn_len+5 and len(odd_list) == odd_len+5:
        print("Even List: sum:",sum(even_list), ",max:",max(even_list))
        print("Odd List: sum:", sum(odd_list),",max:",max(odd_list))
        break
        


# 9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
# Sample input: 12abcbacbaba344ab 
# Expected output: a=5 b=5 c=2
# NOTE: Make sure to avoid counting the occurrence of numeric values in the string.

sample_input ="12abcbacbaba344ab"
dict = {}
for i in sample_input:
    if i.isnumeric():
        continue
    else:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] =1
print(dict)


# 10. Generate and print another tuple whose values are even numbers in the given tuple
# (1,2,3,4,5,6,7,8,9,10).

tup = (1,2,3,4,5,6,7,8,9,10)
x = tuple(i for i in tup if i%2 ==0)
print(x)