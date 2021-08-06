# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 16:29:58 2021

@author: admin
"""
#------------------ Section - 1 : Introduction to python -----------------------#


a = 10
b = 20
c = a+b
print(a+b )
c
x = 30 if 10>20 else 40
x

#Read data from a text file
print(open('C:/Users/admin/Desktop/Useful Stuff.txt').read())

a = 10
print(type(a))
a = "Avishek"
print((type(a)))
a = True
print(type(a))

# To generate 6 digit Bank OTP code

from random import randint  #Importing randint function from random library

print(randint(0, 9),randint(0, 9),randint(0, 9),randint(0, 9),randint(0, 9),randint(0, 9), sep='') #Calling randint function 6 times for six digit OTP and printing it

#To generate 10 six digit OTP at a time

for i in range(10): 
    
    print(randint(0, 9),randint(0, 9),randint(0, 9),randint(0, 9),randint(0, 9),randint(0, 9), sep='') #Calling randint function 6 times for six digit OTP and printing it


#------------------ Section - 2 : Python installation and Run -----------------------#

# Read 2 numbers from the keyboard and print their sum and Product
n1 = int(input('Inter first number: '))
n2 = int(input('Inter Second number: '))
print('The sum :', n1+n2)
print('The product :', n1*n2)

# Print welcome messsage for given no. of times

n = int(input('Enter Some Number : '))
for i in range(n):
    print("Welcome to Avishek's Python Code")








#----------------------------- Type Casting -------------------------------#
#Converting one data type to another type
#int(), float(), complex(), bool(), str()

#1 int() 

#A) Float ---- int
int(10.987)
#B) complex to int
int(10+20j)  #can't convert complex to int
#C) bool to int
int(True)
int(False)
#C) str to int
# string internally should contains only integral value with base 10
int('15')
int('0B1111') #invalid literal for int() with base 10: '0B1111'
int('10.5')  #invalid literal for int() with base 10: '10.5'

#2) float() 

#A) int to float
float(15)
float(0B1111)
float(0)
#B) comples to float
float(10+20j) #can't convert complex to float
#C) bool to float
float(True)
float(False)
#D) str to float
#should contain int and float value with base 10
float("10")
float("20.7")
float("0xFace") #could not convert string to float: '0xFace'
float("Durga") #could not convert string to float: 'Durga'

#3) complex() 

#Form: 1 complex(x)
complex(10)
complex(0B1111)
complex(True)
complex('10')
#Form: 2 complex(x,y)
complex(10,20)
complex(10.5,20.8)
complex('10','20') #complex() can't take second arg if first is a string
complex(10,'20') #complex() second arg can't be a string
complex('79',46) #complex() can't take second arg if first is a string

#4) bool()

#A) int to bool
bool(29)
bool(0)
bool(87)
#any int value other than zero will be true
#B) complex to bool
bool(0+0j) #only in this case it will false rest all true
bool(7+98j)
#C) float to bool
bool(0.0)
bool(5.0)
#D) str to bool
bool("")
bool('True')
bool('avishek')

#5) str()

str(10)
str(56.9)
str(True)
str(False)
str(10+50j)
#str will convert all data type to string data type

#Immutability

#All fundamental data types are immutable
x=10
print(id(x))
x = x + 1
print(id(x)) #one new object created older one is eligible for gargabe collection

x = 20
y = x
print(id(x))
print(id(y)) #both has same id
y = y + 1
print(x)
print(y)
print(id(x))
print(id(y)) #different id because one new object is created

# Collection related data types

#list, tuple, set, frozenset, dict, range, bytes, bytearray
#Fundamental data type can only holds one value but collection realted data types can holds multiple values.

#-------------------------------1 list ---------------------------------------#

#Order is important
#Duplicate is allowed
#Slice oreatior []
#Hetrogeneous object allowed
#indixing and slicing allowed
#to add element to list we use append()
#list is growable
#LIst is mutable

l = [10,'durga',20,10,30]
print(type(l))
print(l[0])
print(l[-1])
print(l[1:4]) #indexing start from 1
l = [] #an emplty list
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
print(l)
l.remove(40) #to remove object form a list we use remove()
print(l)

#-------------------------------2 Tuple ---------------------------------------#

#Exactly same as list except that it is IMMUETABLE
t = (10,20,30,10,'durga')
print(type(t))
print(t[0])
print(t[-1])
print(t[1:4])
t[0] = 7777 #'tuple' object does not support item assignment
t.append(50) #'tuple' object has no attribute 'append'
t.remove(10) #'tuple' object has no attribute 'remove'
t = ()
print(type(t))
#Special care
t = (10) #int not tuple
print(type(t))
t = (10,) #for single object comma is mandatary to create tuple
print(type(t))

#-------------------------------3 Set ---------------------------------------#

#Duplicates are not allowed
#Order is not required
#Indexing or slicing is not allowed
#Heterogeneous data are allowed
#Growable and Mutable
#to create empty set we have to use set() function

s= {10,20,30,40}
print(type(s))
s = {10,20,'durga',10,30,40}
print(s) #{'durga', 40, 10, 20, 30}
print(s[0]) #'set' object is not subscriptable
print(s[1:4]) #'set' object is not subscriptable
s.add(50) #to add new object in a set
print(s)
s.remove(30)
print(s)
s = {}
type(s) #dict---- bar example, regular customer, Udhari wine
s = set() #an empty set
type(s)

#-------------------------------4. Frozenset ---------------------------------------#

#Exactly same as set but IMMUTABLE
s = {10,20,30,40}
fs = frozenset(s)
print(type(fs))
fs.add(50) #Attribute error
fs.remove(30) #Attribute error

#------------------------------- 5. Dictionary ---------------------------------------#

#key - value pairs --- roll no - name, mob.no - address
#d = {k1:v1, k2:v2}
#to add an object in dict d[key] = value
#Duplicate keys are not allowed but value is allowed
#If we try to use same key old value will be replaced by new value
#Order not applicable
#Heterogeneous object allowed
#MUTABLE
#Indexing, slicing not allowed
d = {100:'durga',200:'ravi',300:'chinny'}
print(type(d))
d = {}
d[100] = 'durga'
d[200] = 'ravi'
d[300] = 'Suraj'
print(d)
d[100] = 'Avishek'
print(d)

#------------------------------- 6. Range ---------------------------------------#

#Sequence
#range(10), range(10,21), range(10,21,3)
#Order, Index and slice is applicable
#IMMUTABLE
r = range(10)
print(type(r))
print(r) #range(0, 10)
for r in r:
    print(r)  #0,1,....,9
    
#Form 1: range(n)
# from 0 to n-1
r = range(10)
for r in r:
    print(r)

#Form 2: range(begin,end)
#from begin to end-1
r = range(10,21)
for r in r:
    print(r)  #10,11,.....,20
    
#Form 3: range(begin, end, increment/dectement)
r = range(1,21,1) #1,2,3.....,20
r = range(1,21,3) #1,4,7.....
r = range(20,1,-5) #20,15,10,5
for r in r:
    print(r)

print(r[0])
print(r[-1])
r1 = r[1:5]
for x in r1:
    print(x)

r[1] = 1000 #typeError

#------------------------------- 7. bytes ---------------------------------------#

#To store byte/binary data types like video, images
#value only form 0 to 255
#IMMUTABLE
l = [10,20,30,40]
b = bytes(l)
print(type(b))
for x in b:
    print(x)

l = (10,20,30,40,256)
b = bytes(l) #ValueError
print(b[0])
b[0] = 77 #Type error

#------------------------------- 8. bytearray ---------------------------------------#

#same as bytes but bytearry is MUTABLE
l = [10,20,30,40]
b = bytearray(l)
print(type(b))
for x in b:
    print(x) 

print(b[0])
print(b[-1])

b[0] = 77
for x in b:
    print(x)


#------------------------------- None data type ----------------------------------#

#None with nothing :- No value associated
a=10
a=None
print(id(a))
print(type(a))

def f1():
    return 10

x=f1()
print(x)

def f1():
    print("Hello")

x = f1()
print(x)
#Only one none object is being created.

#---------------------- Excape Character, Comments and Constants -----------------#

# \n -- New line          \k -- Horizontal tab     \r -- Carriage retas
# \b -- Back space         \f -- from feed         \' -- Single quote
# \" -- Double quote       \\ -- Back Slash

# Comment -- #
# '''  '''  -- Document string
# Constant -- There is no constant function in python.
# We use upper case As convention.





















