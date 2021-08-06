# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 18:08:33 2021

@author: admin
"""
#----------------------------- OPERATORS ---(5th-Aug-2021)----------------------#

#Introduction

#Operators are used to perform mathmatical operation

#-------------------------------- 1. Arthmetic Operators -----------------------#

# + -- Addition
# - -- Substraction
# * -- Multiplication
# / -- Normal division operator   will give floating point value
# % -- Will give reminder
# ** -- Exponential operator or power operator
# // -- Floor division operator  integral and floating both arthimetic

a= 10
b= 2
print(a+b) #Addition
print(a-b) #Subtraction
print(a*b) #multipliction
print(a/b) #NOrmal division
print(a%b) #Modulus

print(10//2) #Floor division
print(10.0//2)
print(10/3)
print(10.0/3)
print(10//3)
print(10.0//3)
print(20/2)
print(20.5/2)
print(20//2)
print(20.5//2)
print(30//2)
print(10**2)
print(3**3)
print("durga"+"soft")
print('durgal'+10) #Both should be string
print('durga'+'10')
# * for string
print('durga'*3)
print(3*'durga')
print('durga'*'soft') #One argument should be int
print('durga'*'3')
print('durga'*int('3'))
#  + for string(Concatenation)
# str+str
# * for string (string multiplication or repetitation operator)
# str*int
# int*str

print(10/0) #zero division error
print(10.0/0)
print(10//0)
print('durga'*True) #it will take True value i.e. 1
print('durga'*False) #will give empty




#-------------------------------- 2. Relation Operators -----------------------#

# >, >=, <, <=
a=10 ;b=20
print(a<b)
print(a<=b)
print(a>b)
print(a>=b)
s1 = 'a'; s2 = 'b'
ord('a') # will give ascii value
chr(97) #will give character
s1='durga'; s2='sunny'
print(s1<s2)
print(s1<=s2)
print(s1>s2)
print(s1>=s2)
# Compare on the basis of ascii value
print(True>False)
print(True>=False)
print(True<False)
print(True<=False)
print(10<'durga') #TE
a = 10;b=20
if a>b: print('a is greater than b')
else:print('a is not greater than b')
10<20
10<20<30
10<20<30<40>50
# If any condition will not satisfy =>False


#-------------------------------- 3. Equality Operators -----------------------#

#  ==, !=
10==20
10!=20
1==True
10==10.0
'durga'=='durga'
10=='durga' #NO erroer -- NO compatibility
10=='10'
#Chaining of Equality operators
10==20==30==40
10==10==10==10

#Differaence between == operator and is operator
# is -- Reference Comparision or address comparision
# == -- Content comparision
l1=[10,20,30]; l2=[10,20,30]
print(l1 is l2)
print(l1==l2)
l3=l2
print(l1 is l3 )
print(l2 is l3)


#-------------------------------- 4. Logical Operators -----------------------#

# and, or, not
#---------------- For boolean type ------------#
# and -- return true iff both arguments are True
True and True
True and False
False and True
False and False
# or -- return True iff atleast one argument is True
True or True
True or False
False or True
False or False

# not -- Complement
not True
not False

#Q Take user name and password form keyboard
#(durga, sunny)-- valid user otherwise invalid
input()
username = input('Enter username: ')
password = input('Enter Password: ')
if username=='durga' and password=='sunny':
    print('Valid user')
else:
    print('invalid user')

#------------------- for Non-boolean type

# 0 -- means False, non-zero means True
# empty string, list, set, tuple, dist ---> False

# 1. x and y  => result is x|y but not boolean type
# if 'x' evalutes to False, then result is 'x'
# if 'x' evalutes to True, then result is 'y'
10 and 20
0 and 20
'durga' and 'soft'
'' and 'soft'

# 2. x or y => x|y but not boolean type
# if 'x' evaluates to True then result is  'x'
# if 'x' evaluates to False then result is  'y'
10 or 20
0 or 20
[] or 'durga'
'durga' or 'soft'

# 3. not -- for non-boolean type
# The result is always boolean
not 'durga'
not ()
not ''
not 0
not 10


#-------------------------------- 5. Bitwise Operators -----------------------#

# & -- Bitwise AND
# | -- Bitwise OR
# ^ -- Bitwise X-OR
# ~ -- Bitwise Complement operator
# << -- Bitwise Left-shift operator
# >> -- Bitwise Right-shift operator

4 & 5
#We can only apply for int and bool 
10.5 & 20.6 # TE
# & -- If both bits are '1' then result is '1' otherwise '0'
# | -- If atleast one bit is '1' then result is '1' otherwise result is '0'
# ^ -- If both bits are different then result is '1' else result is '0'
print(4&5)
print(4|5)
print(4^5)
print(~4)
# The most significant bit(MSD) outs as SIGN BIT
# 0 -- positve number, 1 -- -- negitive number
# positive number will be represented directly in the memory
# negitive number will be represented in 2's compliment form
# 1's compliment => 0 -> 1,  1 -> 0
# 2's compliment => 1's compliment +1
~4
~5
~7
~10
~-4


#-------------------------------- 6. Shift Operators -----------------------#

# << -- Left shift      >> -- Right shift operator
10<<2
10>>2
# for boolean
True & False
True | False
True ^ False
~True
True<<2
True>>2


#-------------------------------- 7. Assignment Operator -----------------------#

# = -- Assignment operator
# +=, -=  -- Compound Assignment

x=10
x+=20
x-=20
print(x)
x=10
x&=5
print(x)
x=2
x**=2
print(x)
# x++, x-- NOt possible is python
x =10

print(+++++++x)
print(-x)
print(--x)
print(---x)


#-------------------------------- 8. Ternary operator -----------------------#

# ~a -- Unary operator
# a+b -- Binary operator
# 3 -- Ternary operator
a = 10;b = 20
c = 30 if a>b else 40
print(c)
# Syntax :- c = First_value if condition else second_value

#Q Read 2 int values from keyboard and print minimum value
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
min = a if a<b else b
print("The Minimum value is:",min)

# Nesting of Ternary operator
a = int(input('Enter first number: '))
b = int(input('Enter Second number: '))
c = int(input('Enter Third number: '))
min = a if a<b and a<c else b if b<c else c
print( 'The minumum number is: ',min)


a = int(input('Enter first number: '))
b = int(input('Enter Second number: '))
c = int(input('Enter Third number: '))
min = a if a<b<c else b if b<c else c # Any logic fail will return wrong 
print( 'The minumum number is: ',min)
#not right logic

#Q print max. value
a = int(input('Enter first number: '))
b = int(input('Enter Second number: '))
c = int(input('Enter Third number: '))
max = a if a>b and a>c else b if b>c else c
print( 'The maximum value is: ',max)

#Q Both number is equal, first number is smaller than second number or first 
#number is greater than second number.
a = int(input('Enter first number: '))
b = int(input('Enter Second number: '))
result = print('equal' if a==b else 'smaller' if a<b else 'bigger')
result = 'Both number is equal' if a==b else 'First number is smaller than second number' if a<b else 'First no. is greater than second no.'


#-------------------------------- 9. Special Operator -----------------------#

#1. Identity operatior
# is, is not
# r1 is r2 => True iff both reference pointing to the same object
# r1 is not r2 => True iff both are not pointing to the same object

a= 10; a=b=10
print(a is b)
l1 =[10,20,30,40]
l2 =[10,20,30,40]
print(id(l1))
print(id(l2))
print(l1 is l2)
print(l1 is not l2)
print(l1==l2) # content comparison

#2. Membership operator
#Whether this object is member of that collection or not
# a in sequence -> True
# a not in sequence -> True
s = 'Hello learning python is very easy!!!'
print('h' in s)
print('d' in s)
print('d'not in s)
print('Python' in s) #Case sensitive python
l = ['sunny','bunny','chinny','vinny']
print('sunny'in l)
print('pinny'in l)

#----------------------- Operator Precedence ---------------------------------#

# ()              -- Parenthesis
# **              -- Exponential operator
# ~,-             -- Bitwise complement, unary minus operator
# *,/,%,//        -- Multiplication, Division, Modulo, Floor division
# +,-             -- Addition, substraction
# <<,>>           -- left shift and right shift
# &               -- Bitwise AND
# ^               -- Bitwise X-OR
# |               -- Bitwise OR
# >,>=,<,<=,==,!= -- Relation or Comparision operator
# =,+=,-=,*=      -- Assignment operators
# is, is not      -- Membership operators
# not             -- Logical NOT
# and             -- Logical AND
# or              -- Logical OR

a=30;b=20;c=10;d=5
print((a+b)*c/d)
print((a+b)*(c/d))
print(a+(b*c)/d)
50*10/5 # Predidence Left to Right
3/2*4+3+(10/5)**3-2


#-------------------------- Basic Idea about Python MOdule(library)--(6th-Aug-2021)---#

#Mathematical function from math module:
#Module is a .py file where it contains multiple variable, classes, function
#help in code reuseability 

#Import a Module
from math import *

print(sqrt(4))
def f1():
    print('f1 old function')
def f2():
    print('f2 new function')
#available math function
print(floor(71.5))
print(ceil(76.2))
print(pow(8, 2))
print(gcd(8,4))
print(sin(90))
print(cos(1))
print(pi)
print(e)
print(inf)
print(nan)

#Find area of circle for the given radius
from math import *

r = int(input('Enter radius of circle: '))
print('Area of circle is: ', pi*r**2)
print('Area of circle is: ',pi*pow(r,2))

#Important functions and variable of math module
import math
print(dir(math)) #Show all functions and variable
print(math.sqrt(9))
math.pi
math.pow(3,2)
import math as m #Aliyasing
m.sqrt(9)
m.pi
m.floor(7.9)

from math import sqrt
sqrt(36)
print(pi)

from math import sqrt,pi
from math import sqrt as s,pi as p
s(49)
p










