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