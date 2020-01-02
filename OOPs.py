# Object Oriented Programing(OOPs Concept)
'''
# In python every this is object. To create an objects we need some Model or plan or Blue Print, which is nothing but class.
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

# Self Variable:Self is the default variable which is always pointing to current object. By using self we can access instance variables and instance methods of object.
# Self should be first parameter inside constructorc: def __init__(self):
# Self should be first parameter inside instance methods: def talk(self):

#Constructor Concept:
# The name of a constructor should be __init__(self):
# Constructor will be executed automatically at the time of object creation.
# The main purpose of constructor is to declare and initialise instance variables.
# Per object constructor will be executed only once.
# Constructor will take atleast one argument(self).

#prograam to demonstrate constructor will execute only once when object is created.

class test:
    def __init__(self):
        print("constructor is getting executed")
    def m1(self):
        print("method execution")
t=test()
t2=test()
t3=test()
t3.m1()
t3.m1()

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

t1=Test()
print(Test.__dict__) #-------> To access Static variable

t1.m1()
print(Test.__dict__) #-------> To access Static variable
print(t1.__dict__)  #-------> --------------> To access Instance variable

Test.m2()
print(Test.__dict__)  #-------> To access Static variable

Test.m3()
print(Test.__dict__)  #-------> To access Static variable

Test.i=90   #------->  To declare Static variable out side all method
print(Test.__dict__) #-------> To access Static variable

# How to delete static variables of a class: del classname.variablename  & del cls.variablename

# Local variables:
# Sometimes to meet temporary requirements of programmer,we can declare variables inside a method directly,such type of variables are called local variable or temporary variables.
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
             #return self.va riable
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

# Inside method implementation if we are using class variabls(static variables) then such type of method is class method.
# We can declare class method explicitly by using @classmethod decorator.
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
#--------------------
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
#----------------
# Destructor is a special method and the name should be __del__
# Just before destroying an object Garbage Collector always calls destructor to perform clean up activities.
# Once destructor execution completed then Garbage Collector automatically destroys that object.
# The job of destructor is not to destroy object and it is just to perform clean up activities.

# Related to OOPs Four topics are important:
#-------------------------------------------
# 1.Inheritance
# 2.Polymorphism
# 3.Abstraction
# 4.Encapsulation

# 1.Polymorphism:
#-------------
# Poly means many. Morphs means forms.
# Related to Polymorphism 4 topics are important

# Duck typing Philosophy of python:  In python we can not specify type explicitly. Based on provided value at run time type will be considered automatically.
#-----------------------------------
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

# Operator Overloading: In operator overloading we have magic method for each operator
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
# What ever members available in the parent class are by default available to the child class through inheritance. If the child class not satisfied with parent class implementation then child class is
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
e2.display()

# 2.Inheritance in Python:
#------------------------
# Inheritance is the capability of one class to inherit or drive properties from some other class. The benefit of inheritance are:
# 1. It represent hte real world relationship well.
# 2. It provides the reusability of code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
# 3. It is transitive in nature, which means that if class B inherits from class A, then all subclasses of B would automatically inherit from class A.

# Demo:
class parent():
    def first(self):
        print("first function")
class child(parent):
    def second(self):
        print("second function")
c=child()
c.second()
c.first()

# Types of Inheritance:
#----------------------
# 1.Single Inheritance: When a child class inherits only a single parent class.
class parent():
    def func1(self):
        print("first function")
class child(parent):
    def func2(self):
        print("second function")
c=child()
c.func1()
c.func2()

# 2. Multiple Inheritance: When a child class inherits from more than one parent class.
class Parent1():
    def func1(self):
        print("First function")
class Parent2():
    def func2(self):
        print("Second function")
class Child(Parent1,Parent2):
    def func3(self):
        print("Third function")
c=Child()
c.func1()
c.func2()
c.func3()

# Multilevel Inheritance: When a child class becomes parent for another child class.
class Parent():
    def func1(self):
        print("First function")
class Child1(Parent):
    def func2(self):
        print("Second function")
class Child2(Child1):
    def func3(self):
        print("Third function")
c=Child2()
c.func1()
c.func2()
c.func3()

# Hierarchical Inheritance: It involves multiple inheritance from the same parent or base class
class Parent():
    def func1(self):
        print("First function")
class Child1(Parent):
    def func2(self):
        print("Second function")
class Child2(Parent):
    def func3(self):
        print("Third function")
c=Child1()
c.func1()
c.func2()
c2=Child2()
c2.func1()
c2.func3()

# Hybrid Inheritance: Hybrid inheritance involves multiple inheritance in a single program.
class Parent():
    def func1(self):
        print("Function first")
class Child1(Parent):
    def func2(self):
        print("Second function")
class Child2():
    def func3(self):
        print("Third function")
class Child3(Parent , Child2):
    def func4(self):
        print("Fourth function")
c=Child3()
c.func1()
c.func3()
c.func4()

# 3.Abstraction: Abstraction means hiding the complexity and only showing the essential features of the object.
#---------------(for more information:https://netjs.blogspot.com/2019/05/abstract-class-in-python.html)
# So in a way, Abstraction means hiding the real implementation and we, as a user, knowing only how to use it.
# Real world example would be a vehicle which we drive with out caring or knowing what all is going underneath.A TV set where we enjoy programs with out knowing the inner details of how TV works.
# Abstraction in python is achieved by abstract classes and interfaces.
# An Abstract class is a class that contains one or more abstract method.
# Abstract methods are methods that generally dont have any implementation, It is left to sub classes to provide implementation for the abstract method.
# Here note that in python abstract can have implementation in the  abstract class too but the sub class inheriting that abstract class is still forced to override the abstract method.

# Syntex: It is created by driving from the meta class ABC which belongs to the abc(Abstract Base class) module.
# from abc import ABC, abstractmethod
# class MyClass(ABC):      ---->From abc module ABC meta class has to be imported and abstract class has to inherit ABC class in order to be considered as an abstract class.
#    @abstractmethod        ----->For defining abstract methods in an abstract class method has to be decorated with @abstractmethod decorator. From abc module @abstractmethod decorator has to be imported to use that annotation.
#    def my method(self):
#    pass     ------->Empty body

# Important Points:
# 1. Abstract class can have both concrete method as well as abstract method.
# 2. Abstract class cant be instantiated so it is not possible to create objects of an abstract class.
-4]w

# 3. Generally abstract method defined in abstract class dont have any body but it is possible to have abstract method with implementation in abstarct class. Any sub class deriving from sub abstract class still needs to provide implimentation for such abstract class.
# 4. If an abstract method is not implemented by derived class python throws error.

from abc import ABC, abstractmethod
class Parent():
    def common(self):     # concrete(common) method
        print("In common method of parent")
    @abstractmethod
    def vary(self):
        pass
class Child1(Parent):
    def vary1(self):
        print("In vary method of child1")
class Child2(Parent):
    def vary2(self):
        print("In vary method of Child2")
c1=Child1()
c1.common()
c1.vary1()
c2=Child2()
c2.common()
c2.vary2()

# 4. Encapsulation: https://pythonprogramminglanguage.com/encapsulation/
#-------------------
# An object variable should not always be directly accessible.
# To prevent accidental change, an object variable can sometimes only be changed with an object methods. Those type of variables are private variables.
# The method can ensure the coreect values are set. If an incorrect values are set, the method can return an error.
# Example: Python does not have the private key, unlike some other object oriented languages, but encapsulation can be done.
# instead, it relies on the convection: a class variable should not be directly be accessed should be prefixed with an underscore.
# Examples:
class Robot(object):
    def __init__(self):
        self.a=123
        self._b=123
        self.__c=123
r=Robot()
print(r.a)
print(r._b)
print(r.__c)
# Out Put--->  File "D:/pro/OOPs.py", line 583, in <module>
#     print(r.__c)
# AttributeError: 'Robot' object has no attribute '__c'
# 123
# 123
# A single under score: Private variable, It should be access directly. But nothing stops you from doing that(except convection)
# A Double under score: Private variable harder to access but still possible
# Both are still accessible;Python has private variable by convection
# Getter And Setter: Private variables are intended to be changed using getter and setter methods. This provides indirect access to them.

class Robot(object):
    def __init__(self):
        self.__version=22
    def getVersion(self):
        print(self.__version)
    def  setVersion(self,version ):
        self.__version=version
R=Robot()
R.getVersion()
R.setVersion(23)
R.getVersion()
print(R.__version)
# The class with private attribute and methods.
#The values are changed within the class methods. You could do additional checks, like if the value is not negative or to large.
'''

# Another Example of Encapsulation:https://linuxconfig.org/python-encapsulation
#------------------------------------
'''
Introduction:
Encapsulation is one of the fundamental aspects of Object Oriented Programming. 
It allows programmers better control of how data flows in their programs, and it protects that data. 
Encapsulation also makes objects into more self-sufficient and independently functioning pieces.

The concept of encapsulation builds on what you did in the last two guides with classes and constructors.
Constructors usually are usually used in close conjunction with encapsulation and actually aid in making encapsulation work seamlessly.

Access Modifiers:
Before you can take advantage of encapsulation, you have to understand how Python restricts access to the data stored in variables and methods.
Python has different levels of restriction that control how data can be accessed and from where. Variables and methods can be public, private, or protected. 
Those designations are made by the number of underscores before the variable or method.

Public:
Every variable and method that you've seen so far with the exception of the constructors has been public.
Public variables and methods can be freely modified and run from anywhere, either inside or outside of the class. To create a public variable or method, don't use any underscores.

Private:
The private designation only allows a variable or method to be accessed from within its own class or object. You cannot modify the value of a private variable from outside of a class.
Private variables and methods are preceded by two underscores. Take a look at the example below.
Ex: __make = 'Dodge'
Try using that class from before. Set the variables in the constructor to private. Then try to print one of the variables after an object has been instantiated.
'''
class Car(object):

    def __init__(self, make = 'Ford', model = 'Pinto', year = '1971', mileage = '253812',      color = 'orange'):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__color = color

    def move_forward(self, speed):
        print("Your %s is moving forward at %s" % (self.__model, speed))

    def move_backward(self, speed):
        print("Moving backward at %s" % speed)
mycar = Car()

print(mycar.__model)

# You will receive an error message stating that the variable doesn't exist.
# This is because that variable is private. Now try running the move_forward method.

mycar.move_forward
'''
Everything works fine. That's because the variable is being accessed by a method within the class, not externally.

There is a catch here. Python doesn't exactly handle protected variables as well as other object oriented languages. 
Instead of actually protecting variables, it changes the name of them within the interpreter. 
This allows for different copies of the variable to be created and exist. 
Try changing one of the protected variables in your mycar object and printing it out.
'''
mycar.__model = 'Mustang'
print(mycar.__model)
# Now, it seems to work, but what you've printed out is a strange copy of the protected variable. Try using the move_forward method again.

mycar.move_forward
#It printed out the original value of __model. The variables exist independently. You can further illustrate this by printing out the object as a dictionary. You will see two different variables.

print(mycar.__dict__)

'''
Protected:

Protected variables and methods are very similar to private ones. You probably won't use protected variables or methods very often, but it's still worth knowing what they are. 
A variable that is protected can only be accessed by its own class and any classes derived from it.
That is more a topic for later, but just be aware that if you are using a class as the basis of another one, protected variables may be a good option. Protected variables begin with a single underscore.

What Is Encapsulation:

So, now that you know how access modifiers work, this next part is going to seem pretty obvious.Encapsulation is the process of using private variables within classes to prevent unintentional or potentially malicious modification of data.
By containing and protecting variables within a class, it allows the class and the objects that it creates to function as independent, self contained, parts functioning within the machine of the program itself.

Through encapsulation variables and certain methods can only be interacted with through the interfaces designated by the class itself.

Setters and Getters:
The interfaces that are used for interacting with encapsulated variables are generally referred to as setter and getter methods because the are used to set and retrieve the values of variables. 
Because methods exist within a class or object, they are able to access and modify private variables, while you will not be able to do so from outside the class. 
When you instantiated your mycar object, you essentially used its constructor as an initial setter method. Try writing a set of methods to set and get the value of one of the mycar variables.
'''
def set_model(self, new_model):
	self.__model = new_model

def get_model(self):
	return self.__model

'''
It might seem like a lot of extra work, but it's really not hard at all. Generally speaking, this is how you should structuring your classes and working with class variables.

Closing Thoughts:
Encapsulation is a major part of Object Oriented Programming. It's a big part of what makes objects in programming perform more like physical objects in the real world. 
data stored within your objects and provides control and conventions for how you should handle the flow of data in and out of classes.
'''




# Another example of encapsulation:
#----------------------------------
# Encapsulation is Data hiding of internal state to protect the object integrity.
# In the example given below, Customer is a class. We have encapsulated (by prepending it with __) the variable accountNumber.
# The only was accountNumber can be retrieved is via the getter method, getAccountNumber.
#class Customer:
	#def __init__(self):
		#self.__accountNumber = 4321
	#def getAccountNumber(self):
		#return self.__accountNumber
# Similarly we can hide access to methods as well. For doing that, we need to prepend the method name with __ (Double underscore).

#class Customer:
	#def __init__(self):
		#self.__accountNumber = 4321
	#def __processAccount(self):
		#print("Processing Account")
	#def getAccountNumber(self):
		#return self.__accountNumber

# Note: Even though it is not possible to directly access the private methods and variables, there is work around to access them indirectly.
# For instance, we can access the account number and processing account variable as shown.
class Customer():
    def __init__(self):
        self.__accountNumber=1234
    def prcessAcount(self):
        print("processing acount")
    def getAccount(self):
        return self.__accountNumber
c=Customer()
print(c.getAccount())
c.prcessAcount()





















































































































































































