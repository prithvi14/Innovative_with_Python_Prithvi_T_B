# 1. Write a program in Python to find out the character in a string which is uppercase using list
# comprehension.

s = "IloveInDiA"
d = [x for x in s if x.isupper()== True]
print(d)


# 2. Write a program to construct a dictionary from the two lists containing the names of students and
# their corresponding subjects. The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension.
# HINT - Use Zip function also
# Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
# Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}

# using zip
def fun1(c,e):
    d = dict(zip(c,e))
    print(d)

#using dictionary comprehension
def fun2(a,b):
    f = {a[i]:b[i] for i in range(len(a))}
    print(f)


#using for loop
def fun3(a,b):
    s = {}
    for key in a:
        for value in b :
            s[key] = value 
            b.remove(value)
            break
    print(s)

students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']

fun1(students,subjects)
fun2(students,subjects)
fun3(students,subjects)


# 3. Learn More about Yield, next and Generators

# 4. Write a program in Python using generators to reverse the string.
# Input String = “Consultadd Training”

def fun(string):
    s = " "
    for i in string:
        s = i+s
    yield s


String = "Consultadd Training"
val = fun(String)
for i in val:
    print(i)



# 5. Write an example on decorators

def dec_fun(fun):
    def inside_fun(a,b):
        if b>a:
            a,b = b,a,
        return fun(a,b)
    return inside_fun


@dec_fun
def sub(a,b):
    print(a - b)

var = sub(2,5)
