


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
'''
l1=list(filter(isdivisibl,n))
print(l1)
'''
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







