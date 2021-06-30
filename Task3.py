# 1. Create a list of 10 elements of four different data types like int, string, complex and float.

list1 = [1 , 2, 1.23, "Hello", "Hi", 6, 2+7j, 8, 3-10j, 100.123]
print(list1)
print(len(list1))
print(type(list1))

# 2. Create a list of size 5 and execute the slicing structure 

list1 = [1.23, "Hello", "Hi", 8, 3-10j]
print(list1[1:4]) #prints 2nd and 3rd elemets


# 3. Write a program to get the sum and multiply of all the items in a given list.

from functools import reduce
list2 = [1, 2, 3, 4, 5, 6, 7,8]
sm = 0
mt = 1
for i in list2:
    sm = sm+i
    mt= mt*i
print("Sum:",sm)
print("Product:",mt)

# 4. Find the largest and smallest number from a given list.

list3 = [10, 30, 100, 200, 1000, 40, 200]
print("Maximum:",max(list3))
print("Minimun:",min(list3))

# 5. Create a new list which contains the specified numbers after removing the even numbers from a
# predefined list. 
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [x for x in list1 if x%2 == 0]
print(list2)

# 6. Create a list of elements such that it contains the squares of the first and last 5 elements between
# 1 and30 (both included).

li = []
for i in range(1,31):
    li.append(i**2)

print("First five elemts: ",li[:5])
print("last five numbers: ",li[-5:])


# 7. Write a program to replace the last element in a list with another list.
# Sample input: [1,3,5,7,9,10], [2,4,6,8]
# Expected output: [1,3,5,7,9,2,4,6,8]

list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]
list1[-1:] = list2
print(list1)
# 8. Create a new dictionary by concatenating the following two dictionaries:
# Sample input: a={1:10,2:20} b={3:30,4:40}
# Expected output: {1:10,2:20,3:30,4:40}
a={1:10,2:20} 
b={3:30,4:40}
a.update(b)
print(a)
 
# 9.Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
# and n(both 1 and n included).
# Sample input: n=5
# Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}

dict1 = {}
n =5
for i in range(1,n):
    dict1[i] = i*i
print(dict1)

# 10. Write a program which accepts a sequence of comma-separated numbers from console and
# generates a list and a tuple which contains every number in the form of string.
# Sample input: 34,67,55,33,12,98
# Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)

data = input("Enter the list of numbers :").split(',')
list1 =[]
tupl = ()
l = list(tupl)
for i in data:
    list1.append(i)
    l.append(i)
    tupl= tuple(l)
print("List:",list1)
print("Tuple: ",tupl)

