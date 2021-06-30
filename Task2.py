# 1. Write a program in Python to perform the following operation:
#If a number is divisible by 3 it should print “Consultadd” as a string
#If a number is divisible by 5 it should print “Python Training” as a string
#If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string


def fun(number):
    if number%3 == 0:
        print("Consultadd")
    if number%5 == 0:
        print("Pyhton Training")
    if number%3 == 0 and number%5 == 0:
        print("Consultadd - Python Training")

x= int(input("Enter the number: "))
fun(x)

# 2. Write a program in Python to perform the following operator based task
# Ask user to choose the following option first:
# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If User Enter 4 - Multiplication
# If User Enter 5 - Average
# Ask user to enter two numbers and keep those numbers in variables num1 and num2
# respectively for the first 4 options mentioned above.
# Ask the user to enter two more numbers as first and second for calculating the average as
# soon as the user chooses an option 5.
# At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
# NOTE: At a time a user can only perform one action.
def fun():
    option = int(input("Enter the option: "))
    temp = 0
    if 0>= option >= 5:
        print("Wrong option")
    elif 1 <= option<= 4:
        num1,num2 = input("Enter two numbers:").split()
        num1 = int(num1)
        num2 = int(num2)
    elif option == 5:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enetr the second number: "))
    if option == 1:
        temp = num1+num2
    elif option == 2:
        temp = num1-num2
    elif option == 3:
        temp = num1/num2
    elif option == 4:
        temp = num1* num2
    elif option == 5:
        temp = (num1+num2)/2
    return temp
    

temp = fun()
print(temp)
if temp <= 0:
    print("NEGATIVE")



# 3. Write a program in Python to implement the given flowchart:

a , b, c = 10, 20, 30
avg = a+b+c/3
print("abg = ",avg)

if avg > a and avg > b and avg > c:
    print("avg is higher than a,b,c")
else:
    if avg > a and avg > b:
        print("avg is higher than a,b,c")
    else:
        if avg > a and avg > c:
            print("avg is higher than aand c")
        else:
            if avg > b and avg > c:
                 print("avg is higher than b and c")
            else:
                if avg > a:
                    print("avg is just higher than a")
                else:
                    if avg > b:
                         print("avg is just higher than b")
                    else:
                        if avg > c:
                            print("avg is just higher than b")

# 4. Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going


while True:
    number = int(input("Enter the number: "))
    if number < 0:
        print("It's Over")
        break
    elif number > 0:
        print("Good Going")
        continue

# 5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.

for i in range(2000,3201):
    if i%7 == 0 and i%5 != 0:
        print(i,end = " , ")


# 6. What is the output of the following code examples?

x=123
for i in x:
    print(i)
# TypeError: 'init' object is not iterable

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")
# 0
# error
# 1
# error
# 2

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
# 0
# 1
# 2
# 3
# 4

# 7. . Write a program that prints all the numbers from 0 to 6 except 3 and 6.
#Expected output: 0 1 2 4 5
#Note: Use ‘continue’ statement

for i in range(0,7):
    if i == 3 or i == 6:
        continue
    print(i, end= " ")

# 8. Write a program that accepts a string as an input from the user and calculate the number of digits and letters.
#Sample input: consul72
#Expected output: Letters 6 Digits 2

from ast import literal_eval
def fun():
    data = input("Enter a Data: ")
    Letters = 0
    Digits = 0
    for i in data:
        try:
            literal_eval(i)
            Digits += 1
        except (ValueError,SyntaxError):
            Letters += 1
    return Letters, Digits

Letters,Digits = fun()
print("Letters:", Letters,"Digits:", Digits)

# 9. Read the two parts of the question below:
#Write a program such that it asks users to “guess the lucky number”. If the correct number is
#guessed the program stops, otherwise it continues forever.
# Modify the program so that it asks users whether they want to guess again each time. Use two
# variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
# to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
# The program continues as long as a user has not answered “no” and has not guessed the correct
# number)

while True:
    number  = int(input("Guess the lucky number: "))
    if number == 2845:
        break

#Modified program
while True:
    number  = int(input("Guess the lucky number: "))
    if number == 2845:
        break
    else:
        print("Do you want to continue guessing: ")
        answer = input("Enter the answer: ")
        if answer == "no":
            break
        else:
            continue

# 10.Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
# such as
# counter=1
# While counter <= 5:
#           print(“Type in the”, counter, “number”
#             counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not). If the
# correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!

counter = 1
while counter <= 5:
    number  = int(input("Guess the lucky number: "))
    if number == 2845:
        print("Good Guess!")
    elif number != 2845 and counter != 5:
        print("Try Again!")
    if counter == 5:
        print("Game Over")
    counter += 1
    
# 11.In the previous question, insert break after the “Good guess!” print statement. break will terminate
#the while loop so that users do not have to continue guessing after they found the number. If the user
#does not guess the number at all, print “Sorry but that was not very successful”

counter = 1
while counter <= 5:
    number  = int(input("Guess the lucky number: "))
    if number == 2845:
        print("Good Guess!")
        break
    elif number != 2845 and counter != 5:
        print("Try Again!")
    if counter == 5:
        print("Sorry but that was not very successful")
    counter += 1







