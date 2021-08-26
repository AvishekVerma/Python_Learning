# -*- coding: utf-8 -*-


#------------------------------ Section - 15 -------------------------------------#
#(18th-Aug-2021)

#----------------------------- Python Functions ----------------------------#

#----------- Need of Functions and Advantages -------------------#

a=20
b=10
print('The sum : ',a+b)
print('The difference : ',a-b)
print('The product : ',a*b)

a=200
b=100
print('The sum : ',a+b)
print('The difference : ',a-b)
print('The product : ',a*b)

#This is not preffered
def calculate(a,b):
    print('The sum : ',a+b)
    print('The difference : ',a-b)
    print('The Product : ',a*b)

calculate(20,10)
calculate(200,100)
calculate(200,20)

#if any block of code used repetedly then we define our own custom function
# Biggest advantage --> Code reusability

#---------- Types of Functions and syntax to difine user define function --------#

# Two types
#1. Built-in function/predefined function
# id()  | type()  | print()   | input()  | eval()

# User defined function / customized function
#syntax
# def function_name( parameters):
    #''' doc string'''
    #body
    # return value

#1. def(mandatory)    2. return(optional)

#1. Write a function to print wish message 
def wish():
    print('Hello friends, Good Evening : ')
    
wish()
wish()
wish()

#---------------- Function parameteres and Demo programs ---------------#

#WAP to take name of the student as input and print wish message by name.

def wish(name):
    print('Hello, ',name,' Good evening')
wish() #ivalid TE
wish('Durga')
wish('sunny')

# WAP to take a no. as input and print its square value

def squareit(num):
    sq=num*num
    print('The Square of {} is : {}'.format(num,sq))
squareit(2)
squareit(3)
squareit(7)

#---------------------- Return Statement ----------------------#

#WAP to accept 2 number as input and return sum

def add(a,b):
    sum=a+b
    return sum
add(10,20)
result=add(10,20)
print('The sum : ',result)
print('The sum : ',add(100,200))

def f1():
    print('Hello')
x=f1() #valid
print('The return value : ',x) #valid

# default return ==> None
#WAP to find factorial of given +ve int value
#4! = 4*3*2*1
#3! = 3*2*1

def factorial(num):
    result=1
    while num >=1:
        result=result*num
        num=num-1
    return result
print('Factorinal of 3 is : ',factorial(3))

for i in range(1,6):
    print('The factorial of ',i,' is ',factorial(i))

#----------------- Returning Multiple values for a function --------------#

def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
x,y=sum_sub(20, 10)
print('THe sum :',x)
print('The sub :',y)

def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
# tuple ==> will return one tuple which contains multiple value
t=calc(20,10)
print(type(t))
print(t)
print('The results are',t)

for x in t:
    print(x)

#-------------- Types of Arguments : Positional Arguments

def f1(a,b): # here a and b are Formal parameter
    print(a+b)
f1(10,20) # actual arguments
#1. Positional argument
#2. keyword argument
#3. default argument
#4. variable argument

#1. Positional argument :
# order is important

def sub(a,b):
    print(a-b)
sub(200,100)

#---------------- Types of Arguments : keyword arguments --------------#

#2. keyword arguments

def sub(a,b):
    print(a-b)
sub(200,100)  #<-- Positional
sub(a=200,b=100)
sub(b=100,a=200)
#Order is not important
sub(200,100) #valid
sub(a=200,b=100) #valid
#sub(a=200,100) #invalid
sub(200,b=100) #valid
# first positional then keyword argument.

#---------------- Types of Arguments : Default arguments --------------#

#3. Default arguments

def wish(name):
    print('Hello,',name,'Good evening')
wish() #error
wish('Durga')

def wish(name='Guest'):
    print('Hello,',name,'Good evening')
wish()
wish('durga')

def wish(name,msg):
    pass
def wish(name='Guest',msg='Good Morning'):
    pass
#def wish(name='Guest',msg): # first default and next non default will give error.
 #   pass 

#If we are not passing any name then only default value will ve considered.
#After default arguments, we should not take non-default arguments

#------------- Types of Arguments : Variable length arguments --------------#

def f1(*n):   # tuple        # f1(*n) --> *n--> variable length argument
    print('variable length argument function')
f1()
f1(10)
f1(10,20,30,40)

#where to use 

def f1(*n):
    print(type(n))
    print(n)
f1()
f1(10,20,30,40)
sum(10,20)
sum(20,30,10)
#should go for variable length argument

def sum(*n):
    total=0
    for x in n:
        total=total+x
    print('The sum : ',total)
sum(10,20,30,40)
sum(10,20)
sum(20,30,10)
sum()

def f1(*n):
    print(n)
f1(10,20)
f1((10,20,30),(40,50,60))

#----------- Important conclusion about variable length arguments ---------#

def f1(x,*y):
    print(x)
    for y1 in y:
        print(y)
f1(10,20,30,40)
f1(10)
f1()  #TE

def f(*x,y): #valid
    print(x)
    print(y)
f(10,20,30,40) #TE
#we have to provide by keyword argument
f(10,20,30,40,y=50)

#def f1(*x,*y): #Syntax error
 #   print(x)
  #  print(y)
f1(10,20,30,40) #confusion

#we can't take more than one variable length argument
# After variable length argument if we are taking any normal argument then we have to 
 #provide values by using keywords for that normal argument.
#more than one variable length argument are not allowed

#----------- Differences between *args and **kwargs ---------------#

#      *args                   |           *kwargs
# variable length argument     | variable lengtha keyword argument
# f1(*n)  =>tuple              | f1(**kwargs):   => dictionary
# eg. def f1(*n):              |  def f1(**kwargs):
    #print(n)                  |       print(kwargs)
#f1() #()                      | f1()   #{}
#f1(10)  #(10)                 | f1(name='durga',rollno=101) #{name:Durga,rollno:101}

def f1(*args,**kwargs):
    print(args)
    print(kwargs)
f1(10,20,a=30,b=40)

#def f1(**kwargs,*args): #SYNTAX ERROR
 #   print(args)
  #  print(kwargs)
f1(10,20,a=30,b=40)

# first take variable length argument then take keywords argument

#-------------- Types of Arguments : case study --------------------#

def f1(*y,x=10): #defining a function
    print(y)
    print(x)
f1(10,20,30,x=40) #calling a function

#-------------- Positional Vs keyword argument ----------------#
#we can use both positional arg and keyword argument simultaneously
# but, first we have to take positional argument and then keyword argument.
#i.e. After keyword argument we cannot take positional argument

#-------------- Default Vs Non-Default Argument -----------------#

#If we are not passing any value then only default will ve considered.
# After default argument, we should not take non-default argument
# i.e. default argument should be last argument

## Variable length Vs Normal argument
#After variable length argument if we are taking normal argument than we have to 
 #provide values by using keyword for that normal argument
#more than one variable length argument are not allowed

#------------------------- Case Study ----------------------------#

def f(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)
f(3,2)
f(10,20,30,40)
f(25,50,arg=100)
f(arg4=2,arg1=3,arg2=4)
f() #Error
#f(arg3=10,arg4=20,30,40) #invalid
f(4,5,arg2=6)#error
f(4,5,arg3=5,arg5=6) #invalid

#-------------- Types of Variables : Global and Local ------------------#

# Global variables
#A variable which is defined outside the function
a=10
def f1():
    print(a)
f1()

def f2():
    print(a)
f2()

# Local variables
#A variable which is decleared inside a function and used only in that fn. called local variable.
def f1():
    a=10
    print(a)

def f2():
    print(a)

#---------------- Need of Global variable ----------------------#

a=10 #Global variable
def f1():
    a=20 
    print(a)
    
def f2():
    print(a)
f1()
f2()

#Global keyword
d=10
def f1():
    global a
    a=20
    print(a)

def f2():
    print(a)

f1()
f2()

# To make global variable available to the function so that we can perform required modifictions

def f1():
    global a
    a=10
    print(a)

def f2():
    print(a)

#global a=10 #invalid

# To declare global variable directly inside function

#------------ Important conclusion about global keyword ---------------#

a=777
def f1():
    print(a) #not valid
    global a
    a=999
    print(a)
f1()

a=777
def f2():
    global a
    print(a)
    a=999
    print(a)
f2()

# Global Keyword
# to make global variable available to the function so that we can perform required modification
# to declare global variables inside function explicitly.
# Prior to global declaration, we can not use that variable
# global declaration first and then we can use that variable.
a=888
def f():
    a=999
    print(a)
f()
globals().get('a')
print(globals().get('a'))
globals()['a']

#--------------- Recursive function Introduction and Demo programs ------------#
#Recursion --> A function call itself
# complex problems solved
# length of code get reduced

# Want to find factiorial.
# Without recursion

def factiorial(n):
    result=1
    while n>=1:
        result=result*n
        n=n-1
    return result
    
factiorial(10)

# with recursion

def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factiorial(n-1)
    return result
print('Factiorial of 4 is :',factiorial(4))

for i in range(11):
    print('The factorial of {} is : {}'.format(i, factiorial(i)))

#------------ Internal Tracing of Recursive Function Execution --------------#

def factorial(n):
    print('Execution of factorinal function for n:',n)
    if n==0:
        result =1
    else:
        result=n*factorial(n-1)
    print('Returning factorial({}) is : {}'.format(n,result))
    return result

print(factorial(3))

#------------- Maximum recursion depth in python -----------------#
#995 times allowed
count=0
def factorial(n):
    global count
    count=count+1
    print('Execution of factorial function for n:',n)
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print(factorial(3))
print(count)

#--------------- Anonymous Function/ Lambda functions ---------------#

# No name { without name}
#city bus example --- conductor name
#1. Nameless function
#2. Just for instant use ( one time usage)
#NOrmal function
def squareit(n):
    return n*n

#Anonymous function
s=lambda n:n*n

# lambda input_arguments : expression
print(s(4))

#------------ Lambda function Demo programs ------------------#

#Q. Lambda function to find sum of given 2 numbers
s=lambda a,b:a+b
print(s(10,20))
print(s(100,200))

#Q. Lambda function to find biggest of given numbers.
# for two input values a,b
bigger = lambda a,b: a if a>b else b
print(bigger(40, 78))

# for 3 imput valus a,b,c
bigger = lambda a,b,c: a if a>b and a>c else b if b>c else c
print(bigger(30,847,928394))
print(bigger(4,5,6))

#-------------- Function as argument to another function -----------------#

# filter(function, sequence)
# map(function,sequence)
# reduce(function, sequence)

#------------- Shorter code by using filter() function
# filter(function, swquencr)
l=[1,2,3,0,4,5,6,7,8,9,10] #want even number
# without filter() function

def iseven(n):
    if n%2==0:
        return True
    else:
        return False
l1=[]
for n in l:
    if iseven(n)==True:
        l1.append(n)

print(l1)

# using filter function
l=[1,2,3,0,4,5,6,7,8,9,10] #want even number
def iseven(n):
    if n%2==0:
        return True
    else:
        return False
l1=list(filter(iseven,l))
print(l1)

#return of filter function is filter object not list.

# Filter with lambda function
l=[1,2,3,0,4,5,6,7,8,9,10] 
l1=list(filter(lambda n:n%2==0,l))
print(l1)

#--------------- filter() function Demo Programs --------------------#

l=[1,2,3,0,4,5,6,7,8,9,10] 
even=list(filter(lambda n:n%2==0,l))
print(even)
odd=list(filter(lambda n:n%2!=0,l))
print(odd)

#Number which are divisible by 3 and odd [3,,9]
nby3odd=list(filter(lambda n:n%3==0 and n%2!=0,l))
print(nby3odd)

heroines=['Katrina','Kareena','Anushka','Deepika','Sunny','Mallika']
#I only want heroines whose name starts whith k
startswithk=list(filter(lambda name:name[0]=='K',heroines))
print(startswithk)

#name length divisible by 5
lengthby5= list(filter(lambda name: len(name)%5==0, heroines))
print(lengthby5)

#name ength is odd
odd=list(filter(lambda name:len(name)%5==0,heroines))
print(odd)

#--------------- map() Function therory and Demo programs ---------------#

# filter input_list: 10 elemtnts  ==> output_list :  <=10 
#eg. salary less than 10000
# apply function and gererate new values:
l=[1,2,3,4,5]
def squareit(n):
    return n*n
l1=list(map(squareit,l))
print(l1)

# filter() function
# we can use filter() to filter values from the given sequence based on some condition.
# filter(function,sequence)
    # function argument is responsible for perform condition check

# map() function
# for every element present in the given sequence, apply some function and generate new element
 # with the required modification
# map(function, sequence)
 # function argument can be applied to each element of sequence and generate a new sequence
 
# reduce() function
# reduce() function reduces sequence of elements info a single element by applying specified function
# reduce(function, sequence)
#Not python inbuilt function ==> need to import form functools module

l=[1,2,3,4,5]
l1=list(map(lambda n:n*n,l))
print(l1)
l1=[1,2,3,4,5]
l2=[5,10,15,20,25]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)

#what if input list have different length
l4=list(map(lambda x,y,z:x+y+y,l1,l2,l3))
print(l4)

#--------------- reduce() function and Demo programs

# input ---> 10   output ---> 1
from functools import reduce

l=[10,20,30,40,50]
reduce=reduce(lambda x,y:x+y,l)
print(reduce)

#reduce is not python inbuilt function
from functools import reduce # *

#find the sum of first 100 numbers by using reduce() function.
result= reduce(lambda x,y:x+y,range(1,101))
print(result)





























