# 1. Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# D is a variable whose values should be input to your program in a comma-separated sequence.

import math
def fun(C,H):
    D_list = input("Enter D:")
    D_list= D_list.split(',')
    result = []
    for D in D_list:
        Q = round(math.sqrt((2*C*int(D))/H))
        result.append(Q)
    return result
C = 50
H = 30
Q = fun(C,H)
print(Q)


# 2. Define a class named Shape and its subclass Square. The Square class has an init function which
# takes length as argument. Both classes have an area function which can print the area of the shape
# where Shape’s area is 0 by default.

class Shape:
    area1 = 0
    def area(self):
        print("Area of the shape:",self.area1)

class Square(Shape):

    def __init__(self,length):
        self.length = length


    def area(self):
        print("Area of the shape:",self.length)

sh_ob = Shape()
sq_ob = Square(15)
sh_ob.area()
sq_ob.area()


# 3. Create a class to find three elements that sum to zero from a set of n real numbers
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Expected output: [[-10,2,8],[-7,-3,10]]

class ele:

    def sum(self,x):
        n = len(x)
        pair = []
        for i in range(0, n):
            for j in range(i + 1, n):
                for k in range(j+1,n):
                    if x[i] + x[j]+x[k] == 0:
                         pair.append([x[i],x[j],x[k]])
        
        return pair
                
 
x = [-25,-10,-7,-3,2,4,8,10]
ob = ele()
pair = ob.sum(x)
print(pair)


# 4. Create a Time class and initialize it with hours and minutes.
# Create a method addTime which should take two Time objects and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Create another method displayTime which should print the time.
# Also create a method displayMinute which should display the total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minute

class Time:
    def __init__(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes

    def  addTime(a,b):
        time = Time(0,0)
        if  a.minutes +b.minutes > 60:
            time.hours = round((a.minutes+b.minutes)/60)
        time.hours = time.hours+a.hours+b.hours
        time.minutes = (a.minutes + b.minutes)%60
        return time

    def displayTime(self):
        print("Time is", self.hours ,"hours",self.minutes,"minutes")

    def displayMinute(self):
        print("Totalminutes in time: ",(self.hours*60)+self.minutes)

a = Time(1,50)
b = Time(2,100)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinute()



# 5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a
# parameter. The constructor must assign the integer value to the age variable after confirming the
# argument passed is not negative; if a negative argument is passed then the constructor should set
# age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
# methods:
# yearPasses() should increase age by the integer value that you are passing inside the function.
# amIOld() should perform the following conditional actions:I
# f age is between 0 and <13, print “You are young”.
# If age is >=13 and <=19 , print “You are a teenager”.
# Otherwise, print “You are old”.

class Person:
    age = 0
    def __init__(self,integer):
        if integer < 0:
            self.age = 0
            print("Age is not Invalid,setting age to 0")
        else:
            self.age = integer
    
    def yearPasses(self,a):
        self.age += a
        #print(self.age)


    def amIOld(self):
        if 0 <= self.age < 13:
            print("You are young")
        elif 13 <= self.age <= 19:
            print("You are teenager")
        else:
            print("YOu are old")
        
ob = Person(10)
ob.yearPasses(5)
ob.amIOld()






