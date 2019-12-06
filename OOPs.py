# Object Oriented Programing(OOPs Concept)
'''
# In python every thing is object. To create an objects we need some Model or plan or Blue Print, which is nothing but class.
# We can write a class to represent properties(attributes) and action behaivour of object.
# Properties are represented by objects.
# Behaviour can be represented by Method.  Hence the class contains both Variables and Methods.

# Object--->Object is nothing but instance of a class. Physical existence of the class is object. We can create any number of objects for a class.
# Reference Variable: The variable which can be used to refer object. By using reference variable, we can access properties and methods of object.

#Program: Write a Python program to create a Student class and Creates an object to it. Call the method talk() to display student details

class student:
    def __init__(self, name, rollno, marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def talk(self):
        print("my name is", self.name, "my roll no is", self.rollno, "and my marks is", self.marks)

t=student("Ram", 313, 73)
t.talk()

# Self Variable:Self is the default variable which is always pointing to current object. By using self we can access instance variables and instance methods of object
# Self should be first parameter inside constructorc: def __init__(self):
# Self should be first parameter inside instance methods: def talk(self):

#Constructor Concept:
# The name of a constructor should be __init__(self):
# Constructor will be executed atomatically at the time of oobject creation.
# The main purpose of constructor is to declare and initialise instance variables.
# Per object constructor will be executed only once.
# Constructor will take atleast one argument(self).

#prograam to demonstrate constructor will execute only once when object is created.

class test:
    def __init__(self):
        print("constructor is getting executed")
    def m1(self):
        print("method execution")
t=test()        #O/P:constructor is getting executed
t2=test()       #O/P:constructor is getting executed
t3=test()       #O/P:constructor is getting executed
t3.m1()         #O/P:method execution
t3.m1()         #O/P:method execution

# Types of Variables:
# 1. Instance variable(object level variable)-->The value of a variable is varied from object to object.
# 2. Static variable(class level variable)
# 3. Local variable(Method level variable)

#Where and how we can declare Instance variables:
class Employee:
    def __init__(self):
        self.name="jayesh" #--------->Inside Constructor by using self variable
        self.rollno=313 #--------->Inside Constructor by using self variable
    def m1(self):
        self.marks=93 #--------->Inside Method by using self variable
s=Employee()
s.m1()
s.sub="english"  #--------->Outside of the class by using object reference variable:
print(s.__dict__)

#O/P: {'sub':'english', 'marks':93, 'rollno':313, 'name':'jayesh'}

# How to delete instance variable from the object:
# Within a class we can delete instance variable as follows:  del self.variableName
# From outside of class we can delete instance variables as follows: del objectreference.variableName

# Static variables:
# If the value of a variable is not varied from object to object, such type of variables we have to declare with in the class directly but outside of methods.
# We can access static variables either by class name or by object reference.

#Various places to declare static variables:
class Test:
    a=10  #-------->In general we can declare within the class directly but from out side of any method
    def __init__(self):
        self.b=20  #----->Instance Variable
        Test.c=30 #-------> Inside constructor by using class name
    def m1(self):
        self.d=40  #-------->Instance Variable
        Test.e=50  #-------->Inside instance method by using class name
    @classmethod
    def m2(cls):
        cls.f=60  #-------->Inside classmethod by using either class name or cls variable
        Test.g=70  #-------->Inside classmethod by using either class name or cls variable
    @staticmethod
    def m3():
        Test.h=80 #-------->Inside static method by using class name
print(Test.__dict__) #-------> To access Static variable
# O/P : {'a':10}

t1=Test()
print(Test.__dict__) #-------> To access Static variable
# O/P : {'a':10, 'c':30}

t1.m1()
print(Test.__dict__) #-------> To access Static variable
print(t1.__dict__)  #-------> --------------> To access Instance variable
# O/P : {'a':10, 'c':30, 'e':50, 'b':20, 'd':40}

Test.m2()
print(Test.__dict__)  #-------> To access Static variable
# O/P : {'a':10, 'c':30, 'e':50, 'f':60, 'g':70}

Test.m3()
print(Test.__dict__)  #-------> To access Static variable
# O/P : {'a':10, 'c':30, 'e':50, 'f':60, 'g':70}

Test.i=90   #------->  To declare Static variable out side all method
print(Test.__dict__) #-------> To access Static variable

# How to delete static variables of a class: del classname.variablename  & del cls.variablename

# Local variables:
#Sometimes to meet temporary requirements of programmer,we can declare variables inside a method directly,such type of variables are called local variable or temporary variables.
# Local variables will be created at the time of method execution and destroyed once method completes.
# Local variables of a method cannot be accessed from outside of method.

class Test:
    def m1(self):
        a=1000
        print(a)
    def m2(self):
        b=2000
        #print(a)  NameError: name 'a' is not defined
        print(b)
t=Test()
t.m1()
t.m2()

# Types of Methods:
#1. Instance Method:
#2. Class Method:
#3. Static Method:

#Instance Method:

# Inside method implementation if we are using instance variables then such type of methods are called instance methods.
# Inside instance method declaration,we have to pass self variable.
# def m1(self):
# Within the class we can call instance method by using self variable and from outside of the class we can call by using object reference.

class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Hi", self.name)
        print("Your marks are:", self.marks)
    def grade(self):
        if self.marks>=60:
            print("You got first grade")
        elif self.marks>=50:
            print("You got second grade")
        elif self.marks>=35:
            print("You got third grade")
        else:
            print("you are Fail")
number_of_student=int(input("No of Student:"))
for i in range(number_of_student):
    name=input("enter name")
    marks=int(input("enter marks"))
    s=Student(name,marks)
    s.display()
    s.grade()
    print()

# Setter and Getter Methods:

# Setter Method: Setter methods can be used to set values to the instance variables. setter methods also known as mutator methods.
#syntax: def setVariable(self,variable):
            #self.variable=variable

# Getter Method: Getter methods can be used to get values of the instance variables. Getter methods also known as accessor methods.
#syntax: def getVariable(self):
             #return self.variable
# Demo Program:
class Student:
    def setName(self, name):
        self.name=name

    def getName(self):
        return self.name

    def setMarks(self,marks):
        self.marks=marks

    def getMarks(self):
        return self.marks
NoofStudents=int(input("Number of Student:"))
for i in range(NoofSnametudents):
    s=Student()
    name=input("Enter Name:")
    s.setName(name)
    marks = int(input("Enter Marks:"))
    s.setMarks(marks)
    print("Hi", s.getName())
    print("your Marks are", s.getMarks())

# Class method:

# Inside method implimentation if we are using class variabls(static variables) then such type of method is class method.
# We can declare class method explicitly by using @class method decorator.
# for class method we should provide cls variable at time of declaration.
# We can call classmethod by using classname or object reference variable.
# Demo Program:
class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print("{} walks with {} legs".format(name, cls.legs))
Animal.walk("dog")
Animal.walk("cat")

# To count numbers of objects created for a class:
class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def NoOfObject(cls):
        print("No Of Objects:",cls.count)
t1=Test()
t2=Test()
Test.NoOfObject()

# Static method:

# In general these methods are general utility method
# Inside these methods we wont use any instance or class variable
# Here we wont provide self or cls arguments at time of declaration
# We can declare static method explicitly by using @staticmethod decorator
# We can access static method by using classname or object reference

# Demo program:
class Math:
    @staticmethod
    def add(x,y):
        a=x+y
        return a
    @staticmethod
    def sub(x,y):
        print("subtraction of x,y:",x-y)
    @staticmethod
    def mul(x,y):
        print("product of x,y:", x*y)

j=Math()
print(j.add(6,5)) #-------> calling with object reference
j.sub(6,5) #-------> calling with object reference
Math.mul(6,5) #-------> calling with Class Name

# Garbage Collector:
# The main objective of garbage collector is to destroy useless objects.
# If an object does not have any reference variable then that object eligible for Garbage Collection.

# By default Gargbage collector is enabled, but we can disable based on our requirement. In this context we can use the following functions of gc module.
# gc.isenabled() ------>Returns True if GC enabled
# gc.disable() ------> To disable GC explicitly
# gc.enable() -------> To enable GC explicitly
# Demo:
import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())

# Destructors:
# Destructor is a special method and the name should be __del__
# Just before destroying an object Garbage Collector always calls destructor to perform clean up activities.
# Once destructor execution completed then Garbage Collector automatically destroys that object.
# The job of destructor is not to destroy object and it is just to perform clean up activities.

# Polymorphism:
# Poly means many. Morphs means forms.
# Related to Polymorphism 4 topics are important

# Duck typing Philosophy of python:  In python we can not specify type explicitly. Based on provided value at run time type will be considered automatically.
# Hence python is a dynamically typed language.
# At run time if it walks like a duck and talk like a duck, it must be duck. Python follows this principle. This is called Duck Typing Philosophy.

# Demo:
class Duck:
    def talk(self):
        print("Quack..Quack")
class Dog:
    def talk(self):
        print("Bhaw...Bhaw")
class Cat:
    def talk(self):
        print("Meaw...Meaw")
class Goat:
    def talk(self):
        print("May...May")
def f1(obj):
    obj.talk()
I=[Duck(),Dog(),Cat(),Goat()]
for obj in I:
    f1(obj)

# Hasattar Function: The problem in this approach is if obj does not contain talk() method then we will get AttributeError
# But we can solve this problem by using hasattr() function:  hasattr(obj,'attributename')

class Duck:
    def talk(self):
        print("Quack...Quack")
class Human:
    def talk(self):
        print("How are you")
class Dog:
    def Bark(self):
        print("Bhaw...Bhaw")
def f1(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'Bark'):
        obj.Bark()
d=Duck()
f1(d)
h=Human()
f1(h)
g=Dog()
f1(g)

# Overloading: In operator overloading we have magic method for each operator
# Demo program for '+' operator is __add__():
class Math:
    def __init__(self, pages):
        self.pages=pages
    def __add__(self, other):
        return self.pages+other.pages
t1=Math(100)
t2=Math(200)
print(t1+t2)

# Method Overloding:
# If two method having same name but different type of arguments then
# Example:        m1(int a)
                # m1(double d)
# In python method over loading is not possible but we can handel if method with variable number of arguments required then we can handle
# with default arguments or with variable number of argument methods.

# Demo:
class Math:
    def sum(self, a=None, b=None, c=None):
        if  a!=None and b!=None and c!=None:
            print("sum of a,b,c:",a+b+c)
        elif a!=None and b!=None:
            print("sum of a,b:",a+b)
        elif a!=None:
            print("a:",a)
        else:
            print("pleas give atleast on value")
s=Math()
s.sum(5,8,6)
s.sum(4,8)
s.sum(4)

# Method Overridding:
#What ever members available in the parent class are bydefault available to the child class through inheritance. If the child class not satisfied with parent class implementation then child class is
# allowed to redefine that method in the child class based on its requirement. This concept is called overriding.
# Demo:
class Parent:
    def property(self):
        print("gold+silver+land")
    def Name(self):
        print("hi i am Jayesh")
class Child(Parent):
    def child(self):
        print("Surname is Kumar")
c=Child()
c.child()
c.property()

# Super(): Super method is used to call all the methods of parent class.

class Parent:
    def property(self):
        print("Land+gold+silver")
    def Name(self):
        print("hi i am Jayesh")
class Child(Parent):
    def child(self):
        super().Name()
        print("Surname is Kumar")

c=Child()
c.child()
c.property()

# Constructor Overriding:
class P:
    def __init__(self):
        print('Parent Constructor')

class C(P):
    def __init__(self):
        print('Child Constructor')
c=C()

#Demo Program to call Parent class constructor by using super():
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,eno,sal):
        self.sal=sal
        self.eno=eno
        super().__init__(name,age)
    def display(self):
        print("name:",self.name)
        print("Age:", self.age)
        print("Eno:", self.eno)
        print("Salary:", self.sal)

e1=Employee("jay",48,20000,131)
e1.display()
e2=Employee("Kumar",52,141,250000)
e2.display()'''

# Abstraction

# Encapsulation



































































































































































































