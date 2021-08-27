# -*- coding: utf-8 -*-


#------------------------------ Section - 16 -------------------------------------#
#(26th-Aug-2021)

#----------------------------- Python Modules ----------------------------#

#----------- How to write and use Module and its Advantages -------------------#

a=888
b=999
def add(a,b):
    print('The sum :',a+b)

def product(a,b):
    print('the product :',a*b)
    
class A:
    pass
######### durgamath.py
# every .py file is a module only

# import module_name
# module_name.variable_name
# module_name.fuction_name

import durgamath
print(durgamath.a)    
print(durgamath.b)    
durgamath.add(10,20)    
durgamath.product(10,20)    
# test.py

# 1. code reusability
# 2. length of code decreased readability increases
# 3. Maintainability increases

#--------------- Module Aliasing, from ____ import ---------------------------#

# Duplicate name or Aliasing

import durgamath
import durgamath as m
print(durgamath.a)
print(m.a)    
durgamath.add(10,20)    
m.add(10,20)    
durgamath.product(10,20)    

# Once we create alias name then we are not allowed to use original name.
from durgamath import a,b    
from durgamath import *
print(a)    
print(b)    
add(10,20)    
product(10,20)    

#--------- Member Aliasing and Various Possibilities of import statement -----------#

from durgamath import add as a, product as p    
add(110,20) #NE
a(10,20)    
p(10,20)    
    
# 1. import module1
# 2. import module1,module2,module3
# 3. import module1 as m1
# 4. import module1 as m1, module2 as m2
# 5. from module1 import member1    
# 6. from module1 import member1, member2
# 7. from module1 import *
# 8. from module1 import member1 as m1
# 9. from module1 import member1 as m1, member2 as m2    
   
#--------- Module Naming Conflicts -----------------------#

module1.py
def add(a,b):
    print('module1 add fn')

module2.py
def add(a,b):
    print('module2 add fn')
    
test.py
from module1 import *
from module2 import *

add(10,20)    
# New function will override old function.

# sol -1
import module1 
import module2
module1.add(10,20)
module2.add(10,20)

# sol-2
from module1 import add as a1
from module2 import add as a2    
a1(10,20)
a2(10,20)

#------------------------- Module Reloading --------------------#
    
test.py
import module1
import module1
import time
module1.add(10,20)
time.sleep(30)
import module1
module1.product(10,20)
from imp import reload
reload(module1)
module1.product(10,20)

#--------- Difference between dir() and help() frunctions ------------------#

# Finding member of module ==> by using dir()

#1. dir()  # To list out all member of current module
#2. dir(module_name) # To list out all member of specified module

test.py
x=888
y=999
def add(a,b):
    print(a+b)

print(dir())
import math
print(dir(math))    

# difference between dir() and help()
dir(math) # [members]    
help(math) # all documentation    

#----- Extra members Added by Python interpreter for every Module -------------#

__doc__ # to hold doc selftring
__file__ #to handle file
__name__
__loader__
__package__

test.py
''' This module contains some example'''
print(__doc__)
print('File name :',__file__)    
import os    
print('File Absolute Path : ',os.path.abspath(__file__))    
print('Directory Name :',os.path.dirname(os.path.abspath(__file__)))    
    
#------------ Special variable : __name__ part -1 -----------------#

module1.py
print(__name__)
    
test.py
import module1    
print('test module)')        

#CMD py module1.py
 #Direct
# py test.py
# indirect
__main__
test.py
import module1
print('test module')

module1.py
if __name__ == '__main__':
    print('Direct execution')
else:
    print('indirect execution')
    
# py test.py
# py module1.py
    
#---------------------- Special Variable : __name__ part-2 ----------------------#


test.py
import module1
module1.f1()

module1.py
def f1():
    print('f1 execution')
def f2():
    print('f2 execution')
def f3():
    print('f3 execution')

f1()
f2()
f3()

if __name__=='__main__':
    f1()
    f2()
    f3()

#-------------- Working with math module --------------------#

# 1. factiorial(x)
# 2. sqrt(x)
# 3. ceil(x)
# 4. floor(x)
# 5. fmod(x,y)
# 6. fabs(x)
import math
print(dir())
help(math)

from math import *
print(factorial(4))
print(sqrt(4))
print(fabs(-10.8))
print(fabs(10.5))
print(ceil(10.7))
print(floor(10.4))

r=int(input('Enter radius : '))    
area = pi*r**2 #pow(r,2)
print(('area of circle: ',area))

#------------ Python certi. practice questions on math module

# You are creating a function that manipulates a number. The function has the
 # following requirements :
# A float value passed to the function
# the function must take absolute value of the float.
# Any decimal points agter the integer must be removes 
# which two math fn. should ve used??
# a) math.frexp(x)  b) .floor()  c) .fabs() d) .fmod() e) .ceil()

#------------- Working with random module : random() and uniform() function --------#

#1.random()  otp, password
#2. uniform()
#3. randint()
#4. randrange()
#5. choice()
 
#1. randon() --> random float no. between 0 and 1 (0<x<1) not inclusive

from random import *
print(random())    
for r in range(10):
    print(random())    

#2. uniform(begin, end) # begin< x < end --> random float
print(uniform(5,10))

#------------- Working with random module : randint() and randrange() function --------#    
    
#3. randint(begin,end)  --> random int value between begin and end
print(randint(1,10))  # begin <= x <= end

#4. randrange(begin,end,step) --> random
# from begin to end - 1
# begin is optional and default value is 0
# step is optional and default value is 1

randrange(5)
randrange(1,11)    
randrange(1,11,2)    

#----------Working with random module : choice() function ---------------#    
    
#5. choice(sequence) indexable sequence
# to generate a random object from list, tuple, string
fruits=['apple','banana','orange','mango']    
print(choice(fruits))    

# set and dict not applicable
alphabets ='ABCDEFGHIJKLAMNOPQRSTUVWXYZ'    
print(choice(alphabets))    
digits = '0123456789'    
print(choice(digits))    

#------------- Programs to generate Random OTP and Passwords ------------#

from random import *    
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')
otp=''
for i in range(6):
    otp=otp+str(randint(0,9))
print(otp)

alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits='0123456789'
print(choice(alphabets),choice(digits),choice(alphabets),choice(digits),choice(alphabets),choice(digits),sep='')

#----------- Program to Generate fake Employee data for Database Testing : Part-1

# 1. Employee Name
#2. Employee Number
#3. Employee Salary
#4. Employee City
#5. Employee MObile Number
#6. Designation

#1. Name cotntains 3 to 10
#2.First character should be upper case remaining lower case
#3. employee no - e-4digit
#4. employee salary 10k to 15k
#5. city - Hyderabad, Mumbai, Bangalore, Delhi

from random import *

alphabets='abcdefghijklmnopqrstuvwxyz'
digits='0123456789'
cities=['Hyderabad','Bangalore','Chennai','Pune','Mumbai','Delhi']
Designation= ['Software eng.','Senior Software eng.','Team Lead','Project Lead','Project Manager']

def get_fake_name():
    name=choice(alphabets).upper()
    n=randint(0,9)
    for i in range(n):
        name=name+choice(alphabets)
        return name
    
def get_fake_eno():
    eno='e-'
    for i in range(4):
        eno=eno+choice(digits)
    return eno
    
#-------------- Program to Generate fake Employee data for Database Testing : Part-2-----#

def get_fake_salary():
    esal=uniform(10000,15000)
    return esal

def get_fake_city():
    city=choice(cities)
    return city
    
def get_fake_mob():
    mno=choice('6789')
    for i in range(9):
        mno=mno+choice(digits)
    return mno

def get_fake_designation():
    designation = choice(Designation)    
    return designation
    
def get_fake_emp_data():
    print('Employee name        : ',get_fake_name())
    print('Employee salary      :  {:.2f}'.format(get_fake_salary()))
    print('Employee Number      : ',get_fake_eno())
    print('Employee city        : ',get_fake_city())
    print('Employee mobile No.  : ',get_fake_mob())
    print('Employee Designation : ',get_fake_designation())
    
get_fake_emp_data()   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    