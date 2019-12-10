# Python is a general purpose high level programming language.
'''
# Identifires:
#------------------------------
# A name in python is called identifire.It can be class name or function name or module name or variable name.--->a=10
# alphabet symbols(either lower case or upper case)
# digits(0 to 9)
# underscore symbol(_)

# Rreserved words:
#------------------------------
# There are 33 reserved words available in Python.
# Ture, False, None, or, and , not, is, if, elif, else, while, for, breake, continue and so on......
# To get all key words:
# import keyword
# print(keyword.kwlist)

# Data Types:Python contains the following inbuilt data types
#--------------
# int, float, complex, boolean, string, bytes bytearray, range, list, tuple, set, frozenset, dict, None.

# Type casting:
#---------------------------
# int()----->Used to convert from other type to int type
# float()------>Used to convert from other type to flote type, We can convert any type value to float type except complex type.
# complex()------>Used to convert from other type to complex type
# bool()------>Used to convert from other type to bool type
# str()------>Used to convert from other type to str type
# Fundamental Data Types vs Immutability: All Fundamental Data types are immutable. i.e once we creates an object,we cannot perform any changes in that object. If we are trying to change then with those changes a
# new object will be created. This non-chageable behaviour is called immutability.

# Escape Character:
#-------------------------
# \n = New line
# \t= Horizontal tab
# \r= Carriage Return
# \b= Back Space
# \f= Form Feed
# \v= Vertical Tab
# \'= Single Quote
# \"= Double Quote
# \\= Back Slash symbol

# Operators:Operator is a symbol that performs certain operations.
#----------------
# 1.Arithmetic Operators:
#-------------------------
# +: Addition
# -: Subtraction
# *: Multiplication
# /: Division ---->/ operator always performs floating point arithmetic. Hence it will always returns float value.
# %: Modulo Operator
# //: Floor Division operator ----->Floor division (//) can perform both floating point and integral arithmetic. If arguments are int type then result is int type. If atleast one argument is float type then result is float type.
# **: Double Exponential Operator

# 2.Relational Operators:
#-------------------------
# >,>=,<,<=

# 3.Equality operators:
#-----------------------
# ==, !=

# 4.Logical Operator:
#--------------------
# and, or, not

# 5. Bitwise Operator:
#---------------------
# &,|,^,~,<<,>> ------>These operators are applicable only for int and boolean type.

# 6. Shift operator:
#-------------------
# Dont know what is this

# 7. Assignment Operator: We can use assign operator to assign value to the variable. Ex: x=10
#-------------------------
# x+=10 -----> x=x+10: We can combine asignment operator with some other operator to form compound assignment operator.
# +=, -=, *=, /=, %= and so on.....

# 8.Ternary Operator: Syntex: x= firstValue if condition else second value -----> If condition is True then first value will be considered else second value
#-------------------
# Ex: Nesting of ternary operator is possible.
a,b=10,20
x=30 if a>b else 45
print(x)

# 9. Special operator:
#----------------------
# a. Identity operator: Use for address comparision
# is: r1 is r2 ----> Returns True if both r1 and r2 pointing to the same object
# is not: r1 is not r2 -----> Returns True if both r1 and r2 is not pointing to the  same object
# Demo:
a, b=10,10
print(a is b)
x=True
y=False
print(x is not y)

# b. Membership operator:It is used to check weather the given object is present in the given collection.(It may be String,List,Set,Tuple or Dict)
# in: Returns True if the given object is present in the collection
# not in: Returns True if the given object is not present in the given collection
# Demo:
list1=["sunny","bunny","chinny","pinny"]
print("sunny" in list1)
print("tunny" in list1)
print("tunny" not in list1)

# Operator Precedence: If multiple operators are present then which operator will evaluate first is decided by operator precedence.
# for more information refer page 43 of Durga Sir pdf
print(10+2*2)

# Input And Output Statements:
# input(): Its behaviour is exactly same as raw_input() of python 2 ie. every input value is treated as str type only
a,b=[int(x) for x in input("enter two numbers:").split()]
print("product of a and b is:",a*b)
# Note:split() function can take space as seperator by default .But we can pass anything as seperator.

# eval(): Eval function takes a string and evaluate the result, it can evaluate input to list, tuple, set etc based on provided input
x=eval(input("Enter Expression:"))
print(x)
l=eval((input("Enter List:")))
print(type(l))
print(l)
'''









'''
# Reversing the given string using slicing:
text=input(" enter string:")
Reversed = text[::-1]
print(Reversed)

# Reversing the given string using join function:
text=input("enter string:")
Reversed_string=''.join(reversed(text))
print(Reversed_string)

# WAP to print fibbonacci series up to n
num=int(input("enter number:"))
a,b=0,1
while a<=num:
    a,b=b,a+b
    print(a, end=' ')

# WAP to print fibbonacci series with Generator:
def fib():
    a=0
    b=1
    while True:
        yield a
        a, b = b, a + b
for f in fib():
    if f>100:
        break
    print(f)

# WAP to print sum of N numbers
num=int(input("enter number:"))
i=1
add1=0
while i<=num:
    add1=add1+i
    i=i+1
    print(add1)

# WAP to find even number from 1 to N
num=int(input("enter number:"))
i=1
while i<=num:
    if i%2==0:
        print("i")
        i=i+1

# weather number is even or odd
num=int(input("enter x value:"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")

#WAP to check prime number
num=int(input("enter number:"))
if num>1:
    count=0
    for i in range(2,num):
        if num%i==0:
            print("not prime number")
            break
    else:
        print(" prime number")
elif num==1:
    print("given number is prime number")
else:
    print("enter only positive number")

#Lambda argument_list:expression
a=lambda i:i*i*i
print(a(2))
print(a(3))
a=lambda i,j:i*j
print("multiplication of i,j is",a(5,6))

#Find the maximum of three numbers.
def max(x,y,z):
    if x>y and x>z:
        return x
    elif y>z:
        return y
    else:
        return z
print(max(3,5,7))

#Lambda function.
max=lambda x,y,z:x if x>y and x>z else y if y>z else z
print("Maximum of three numbers:",max(5,9,8))

#Filter Function: filter(): it takes two parameters as function and second parameter as iterable object
#The  filter takes elements one by one from iterable object and perform the operation.
#If condition is true then filter return the value else it ignores the value.
#filter():Function is meant for condition checking
x=[3,4,8,9,1,2]
y=list(filter(lambda i:i%2==0,x))
print(y)

def isdivisible(n):
    if n%3==0:
        return True
    else:
        return False
n=[3,9,12,15,18,22,21]

l1=list(filter(isdivisibl,n))
print(l1)

l2=list(filter(lambda i:i%3==0,n))
print(l2)

#Map(): For every input value need to generate output value.
l1=[2,4,6,8,9]
l2=list(map(lambda i:i%2==0,l1))
print(l2)
l3=list(map(lambda n:n+2,l1))
print(l3)

#Addition of two list object element
x=[1,2,3]
y=[4,5,6]
print(x+y)   #But we need to add elements of two list object
z=list(map(lambda i,j:i+j,x,y))
print(z)
#filter():function is meant for condition checking
#map():Function perform business logic increase all emp. salary etc...

#Reduce():Reducing the value into single object.
from functools import reduce
x=[1,2,3,4,5]
y=reduce(lambda i,j:i+j,x)
print(y)

#Recursion
#It reduces the length of the code .
#A function can call it self is known as recursion.
num=int(input("enter number:"))
def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
x=fact(num)
print("factorial of num is",x)

def fact(n):
    if  n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n= int(input("enter number:"))
for i in range(n+1):
    print("factorial of",i,"is",fact(i))

def cube(i):
    return i*i*i
print(cube(2))
res=cube(3)
print(res)

#Sorting:

#Bubble sort:
def bubble_sort(num):
    swapped=True
    while swapped:
        swapped=False
        for i in range(len(num)-1):
            if num[i]>num[i+1]:
                num[i],num[i+1]=num[i+1],num[i]
                swapped= True
random_list_of_num=[5,2,3,7,1,9]
bubble_sort(random_list_of_num)
print(random_list_of_num)

# Bubble sort other way:
def bubble_Sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp


random_list_of_num=[5,2,3,7,1,9]
bubble_Sort(random_list_of_num)
print(random_list_of_num)

# Selection sort:
def Selection_sort(num):
    for i  in range(len(num)):
        lowest_index_value=i
        for j in range(i+1,len(num)):
            if num[j]<num[lowest_index_value]:
                num[j],num[lowest_index_value]=num[lowest_index_value],num[j]
random_list_of_num=[5,2,3,7,1,9]
Selection_sort(random_list_of_num)
print(random_list_of_num)

def selection_Sort(num):
    for i in range(len(num)):
        minpos=i
        for j in range(i,len(num)):
            if num[j]<num[minpos]:
                minpos=j
        temp=num[i]
        num[i]=num[minpos]
        num[minpos]=temp
random_list_of_num=[5,2,3,7,1,9]
selection_Sort(random_list_of_num)
print(random_list_of_num)

# finding min element inthe list:
def Min_Ele(num):
    for i in range(len(num)):
        minpos = i
        for j in range(i, len(num)):
            if num[j] < num[minpos]:
                minpos = j
        temp = num[i]
        num[i] = num[minpos]
        num[minpos] = temp


random_list_of_num = [5, 2, 3, 7, 1, 9]
Min_Ele(random_list_of_num)
print(random_list_of_num[0])

# File handeling:
# Syntex: f = open(filename, mode)
# With Statement syntex: with open("filename","mode") as f:
# print(filename.tell()): method to return current position of the cursor(file pointer) frombeginning of the file. [ can you plese telll current cursor position]The position(index) of first character in files is zero just like string index.
# Seek: finemane.seek(offset, fromwhere)------>OFFSET->Number of positions, fromwhere-->0:begining, 1:from current position, 2:from end of the file

file=open('jay.txt','r')
for each in file:
    print(each)
print(file.tell())

file=open('jay.txt','r')
print( file.read())

file=open('jay.txt', 'w')
file.write('and surname is kumar')
file.close()
print('done')

file=open('jay.txt', 'a')
file.write('you forgotted to write mu name', )
file.close()
print('done')

with open('jay.txt') as file:
    R=file.read()
    print(R)
file.close()

with open('jay.txt') as file:
    file.write('be in your limits')
file.close()
f=open('jay.txt','w')
write=f.write('jayesh kumar is a good boy')
print('File Name:', f.name)
print('Mode:', f.mode)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)

vowel=['a','e','i','o','u']
string=input("enter string")
found=[]
for letter in string:
    if letter in vowel:
        if letter not in found:
            found.append(letter)
print(found)
print(len(found))
j=string.count('u')
print(j)

# Generator

# To Generate first n numbers from Generator:

def First_n_numbers(num):
    n=1
    while n<=num:
        yield n
        n=n+1
numbers=First_n_numbers(10)
for i in numbers:
    print(i)

# The Special variable __name__=='__main__':

# For every Python program , a special variable __name__ will be added internally.
# This variable stores information regarding whether the program is executed as an individual program or as a module.
# If the program executed as an individual program then the value of this variable is __main__
# If the program executed as a module from some other program then the value of this variable is the name of module where it is defined.

# Modulename: Ram.py
def f1():
    if __name__=='__main__':
        print("the cose executed as program",__name__)
    else:
        print("code executed as a module from some other program", __name__)
f1()
# Output:the cose executed as program __main__

# Module name:Jay.py
import Ram
Ram.f1()
# Output: code executed as a module from some other program Ram

# Random Module:

# random():This function always generate some float value between 0 and 1 ( not inclusive) 0<x<1
from random import *
for i in range(10):
    print(random())
#uniform():It returns random float values between 2 given numbers(not inclusive)
from random import *
for i in range(10):
    print(uniform(1,100))
#randint():To generate random integer beween two given numbers(inclusive)
from random import *
for i in range(10):
    print(randint(1,100))
#randrange():returns a random number from range :start<= x < stop
from random import *
for i in range(10):
    print(randrange(1,100,10))
#choice():It wont return random number.It will return a random object from the given list or tuple.
from random import *
list=["Sunny","Bunny","Chinny","Vinny","pinny"]
for i in range(10):
    print(choice(list))

# Regular Expression:
# If we want to represent a group of Strings according to a particular format/pattern then we should go for Regular Expressions.
# We can write a regular expression to represent all mobile numbers, email ids
# 1. To develop validation frameworks/validation logic
# 2.To develop Pattern matching applications (ctrl-f in windows, grep in UNIX etc)
# 3. To develop Translators like compilers, interpreters etc
# 4. To develop digital circuits
# 5. To develop communication protocols like TCP/IP, UDP etc.

# We can develop Regular Expression Based applications by using python module: re
# Demo:
import re
count=0
# comile()----->used to change in to regex object
pattern=re.compile("ab")
matcher=pattern.finditer("aabababbbbababaaabab")
for match in matcher:
    count=count+1
    print(match.start(), "....", match.end(), match.group())
print("number of occurance",count)

# We can pass pattern directly as argument to finditer() function.
import re
matcher=re.finditer("a", "a7bk@9dz")
for match in matcher:
    print(match.start(),"....", match.group())

# Character class:
#[abc] ------->Either a or b or c
#[^abc] ------->except a or b or c
#[a-z] ------->any lower case alphabet symbol
#[A-Z] ------->any upper case alphabet symbol
#[a-zA-Z] ------->Any alphabet symbol
#[0-9] ------->any digit from 0-9
#[a-zA-Z0-9] ------->any alpha numeric symbols
#[^a-zA-Z0-9] ------->Except alphanumerc symbol

# Pre Defined character class:
#\s= space character
#\S= any character except space character
#\d= any digit from 0-9
#\D= any character except digit
#\w= any word character [a-zA-Z0-9]\
#\W= any character except word character(special character)
# . = any character including special character

    # Quantifiers:
# a= Exactly one "a"
# a+= Atleast one "a"
# a*= Any number of "a" including 0 number
# a?= Atmost one "a" ie either 0 number or 1 number
# a{m}= Exactly m number of a's
# a{m,n}= Minimum m number of a's and maximum n number of a's
#Note:
# ^(argument)  It will check whether target string starts with given argument or not
# (argument)$  It will check whether target string ends with given argument or not

# Important functions of re module:
# match() =====>It will find match only at the starting of the string or else it will return None
import re
n=input("enter string:")
match=re.match(n, "learning python is easy")
if match!=None:
    print("Match is available at the beginning of the String")
    print(match.start(),"....",match.end())
else:
    print("No match is found")

# fullmatch() =======> It will match full string or else it will return None
import re
n=input("enter string to match:")
s=input(" Enter big string:")
match=re.fullmatch(n,s)
if match!=None:
    print("full match found")
else:
    print("Full string not match")

# search()======> Match the given string with the targeted string if matches then fine or else returns None
import re
n=input("Enter string to find")
s=input("Enter big string")
match=re.search(n,s)
if match!=None:
    print("Match found at", match.start(), "ends at", match.end())
else:
    print("Match not found")

# findall() =====>It will find all the given input ant trurn as a list of object
import re
n=input("Enter to find:") #----->[0-9]
s=input("Enter big text") #----->0dfd5fdf8sf65sf4sf5679fs6f4s
match=re.findall(n,s)
if match!=None:
    print("match found",match)
else:
    print("No match found")

# finditer() ====>Returns the iterator yielding a match object for each match. On each match object we can call start(), end() and group() functions.
import re
n=input("Enter Iter obj to find:")
matcher=re.finditer(n,"kjl#md2#m8@s8")
for match in matcher:
    if match!=None:
        print("starts at:",match.start(),"ends at:",match.end(), "found item:", match.group())
    else:
        print("No match found")

# sub() ====>sub means substitution or replacement =====>re.sub(regex,replacement,targetstring)
import re
n=input("Enter string to substitute:")
match=re.sub(n,'#',"a5a5a8a5aa7a6aa49a")
print(match)

# subn(): ====>It is exactly same as sub except it can also returns the number of replacements.
import re
n=input("Enter string to substitute:")
match=re.subn(n,"#","a5a5a8a5aa7a6aa49a")
print(match)
print("The Result String:",match[0])
print("The number of replacements:",match[1])

# split()
import re
l=re.split(",","sunny,bunny,chinny,vinny,pinny")
print(l)
for t in l:
    print(t)

# Note: If we want to ignore case then we have to pass 3rd argument re.IGNORECASE for search() function.
# Eg: res = re.search("easy$",s,re.IGNORECASE)

# Multithreading:--->Multitasking

# Executing several tasks simultaneously where each task is a seperate independent part of the same program, is called Thread based multi tasking, and each independent part is called a Thread.
# Main Uses: To implement Multimedia graphics, develop video games, animations, web and  application servers.
# WAP to print name of a current thread.
import threading
print("current thread:", threading.current_thread().getName())

# The ways of creating thread in pyhton:

# 1.Creating a thread without using a class:
from threading import *
def display():
    for i in range(1,11):
        print("Child thread")
t=Thread(target=display())
t.start()
for j in range(1,11):
    print("Main thread")

# 2.Creating a thread by extending thread class:
from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(4):
            print("Child thread")
t=MyThread()
t.start()
for j in range(4):
    print("Main Thread")

# 3.Creating a thread without extending thread class:
from threading import *
class Test:
    def display(self):
        for i in range(5):
            print("child thread")
obj=Test()
t=Thread(target=obj.display)
t.start()
for i in range(5):
    print("Main thread")

# Without threading:
import time
def doubles(n):
    for i in n:
        time.sleep(1)
        print("doubles of number:", 2*i)
def square(n):
    for i in n:
        time.sleep(1)
        print("Square of number:",i*i)
n=[1,2,3,4,5,6]
begin_time=time.time()
doubles(n)
square(n)
print("Total time taken:",time.time()-begin_time)

# With threading:
from threading import *
import time
def double(n):
    time.sleep(1)
    for i in n:
        print("doubles",2*i)
def square(n):
    time.sleep(1)
    for i in n:
        print("square",i*i)
n=[1,2,3,4,5,6]
start_time=time.time()
t1=Thread(target=double,args=(n,))
t2=Thread(target=square,args=(n,))
t1.start()
t2.start()
t1.join()
t2.join()
print("total time taken",time.time()-start_time)

# Setting and Getting Name of a Thread:
import threading
print("Get Name",threading.current_thread().getName())
# To set name:
threading.current_thread().setName("jay")
print("Get name", threading.current_thread().getName())

# Thread Identification Number (ident):
from threading import *
def test():
    print("child thread")
t=Thread(target=test)
t.start()
print("Identification for main thread",current_thread().ident)
print("Identification number for child thread", t.ident)

# Active_count():--->Returns the of active threads currently running.
from threading import *
import time
def display():
    print(current_thread().getName(),"...started")
    time.sleep(3)
    print(current_thread().getName(),"...ended")
    print("The Number of active Threads:",active_count())
t1=Thread(target=display,name="ChildThread1")
t2=Thread(target=display,name="ChildThread2")
t3=Thread(target=display,name="ChildThread3")
t1.start()
t2.start()
t3.start()
print("The Number of active Threads:",active_count())
time.sleep(5)
print("The Number of active Threads:",active_count())

# Pickling & UnPickling
# Sometime we have to write total state of object to the file and we have to read total object from the file.
# The process of writting state of object to the file is called pickling and the process of reading state of object from the file is called unpickling.
# We can implement pickling and unpickling by using pickle module of python.
# Pickle module contains dump() function to perform pickling ---->pickle.dump(object,file)
# pickle module contains load() function to perform unpickling ----->obj=pickle.load(file)
# Demo:
import pickle
class Employee:
    def __init__(self, ename,eid,esal,eadd):
        self.eid=eid
        self.ename=ename
        self.esal=esal
        self.eadd=eadd
    def display(self):
        print(self.eid,"\t",self.ename,"\t",self.esal,"\t",self.eadd)
with open("emp.dat","wb")as f:
    e=Employee(101,"Jayesh",20000,"Tumaria Tola")
    pickle.dump(e,f)
    print("Pickling done")
with open("emp.dat","rb") as f:
    obj=pickle.load(f)
    print("Unpickling done")
    obj.display()

# Exception Handling:
# In any programming language there are 2 types of errors are possible.
# 1. Syntax error:
# The errors which occurs because of invalid syntax are called syntax errors
# 2. Runtime error:
# Also known as Exception ---->While executing the program if something goes because of end user input or programing logic or memory problems etc then we will get runtime error.
# An unwanted and unexpected event that disturbs normal flow of program is called exception.
# Eg: ZeroDivisionerror, Typeerror, ValueError, FileNotFoundError, EOFError, SleepingError, TyrePuncturedError.
# try:
#   risky code
# except:
#    Handling code/Alternative code

x=int(input("enter first number"))
y=int(input("enter second number"))
try:
    a=x/y
except ZeroDivisionError as msg:                            # We can use multiple except block and it should be in correct order
    print("exception raised and its description is:",msg)   # Other way to write: except (Exception1,Exception2,exception3,..) as msg :
except ValueError as msg:
    print("Only integer values are required")
except:
    print("default except: Please provide valid input") # Default except and it should be in last always
finally:
    print("Process completed")

# Finally block:
# It is not recommended to maintain clean up code inside except block, because if there is no exception then except block won't be executed.
# Hence we required some place to maintain clean up code which should be executed always irrespective of whether exception raised or not raised and whether exception handled or not handled. Such type of best place is nothing but finally block.
# In this particular case finally won't be executed. Whenever we are using os._exit(0) function then Python Virtual Machine itself will be shutdown.

# Nested try-except-funally block:
# We can take try-except-finally blocks inside try or except or finally blocks.i.e nesting of tryexcept-finally is possible.
try:
    print("outer try block")
    try:
        print("Inner try block")
        print(10/0)
    except ZeroDivisionError:
        print("Inner except block")
    finally:
        print("Inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")

# Else block with try-except-finally:
# We can use else block with try except finally blocks. else block will be executed if and only if there is no exceptions inside try block.
# Whenever we are writing else block compulsory except block should be there. i.e without except we cannot write else block
#try:
    print("try")
    print(10/0)--->1
except:
    print("except")
else:
    print("else")
finally:
    print("finally")

# Type of exception:
# 1. Pre Defined exception ----->The exceptions which are raised automatically by Python virtual machine whenver a particular event occurs.
# 2. User Defined exception ----->Also known as programatic or customized exception, sometimes we have to define and raise exception explicitely to indicate that something goes wrong, such type of exception....
# Example:InSufficientFundsExceptio, InvalidInputException, TooYoungException, TooOldException

# How to define and raise customized exception:---->Every exception in a python is a class that extends the exception class directly or indirectly.
# Syntex: class classname(predefined exception class name):
#               def __init__(self,args):
#                   self.msg.args
# Demo:
class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg=arg
class TooOldException(Exception):
    def __init__(self,arg):
        self.msg=arg
age=int(input("Enter Age:"))
if age>60:
    raise TooYoungException("You are Too young to get married wait for some years you will get best match")
elif age<18:
    raise TooOldException("You are too old to get married you will not get match")
else:
    print("You will get details on your email")
'''




# Decorator
# Destructorm
# active count and rest part of threading
# database
#PYTHON DEBUGGING BY USING ASSERTIONS
# Python loging
# file handlingh and its remaining part
# Math module






