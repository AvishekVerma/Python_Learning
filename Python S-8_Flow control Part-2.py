# -*- coding: utf-8 -*-


#------------------------------ Section - 8 -------------------------------------#
#(10th-Aug-2021)
#---------------------------- Python Flow Control : Part-2 -----------------------#

#---------------- Transfer Statements : break statement ------------#

# 1. break      2. Continue
# 1. break:
#to break the execution of loop based on some condition.
for i in range(10):
    if i==7:
        print('Processing is enough, break loop execution')
        break
    print(i)
print('Outside of loop')

cart=[10,20,30,600,70,80]
for item in cart:
    if item>500:
        print('To place this order insurence must be required, we can not process further')
        break
    print('Processing item : ',item)

x=10
if x>40:
    print('We are stopping program')
   # break   #Syntax error
print('Hello')

# If you want to use break statement compulsary it should be inside loop only either for loop or while loop.

#------------------- Transfer statements : continue statement ----------------#

#To skip current iteration and continue fro the next iteration.

for i in range(10):
    if i%2==0:
        break
    print(i)

for i in range(10):
    if i%2==0:
        continue
    print(i)

#YOU can use break statement with your girfriend but you can't use it with your wife then
#you have to use continue statement.
#break ==> Girlfriend
#continue ==> wife

#cart example
cart=[10,20,30,600,70,80,700,90]
for item in cart:
    if item>500:
        print('Insurence must be required, just skipping this item',item)
        continue
    print('Processing item : ',item)

#When we use break statement. It stopped in between while with continue statement it process all item.

l=[10,20,30,0,50,0,30]
for x in l:
    print('100/{}={}'.format(x,100/x)) #Zero division error
    
for x in l:
    if x==0:
        print('Hello stupid, How we can divide with zero')
        continue
    print('100/{}={}'.format(x,100/x))

x=10
if x>40:
    print('Hello')
    #continue   should only in loop
print('HI')

#----------------- Transfer Statement : break & coninue i nested loop -------#

for i in range(3):
    for j in range(3):
        if i==j:
            break
        print(i,j)

#In nested loop if use break then inner loop will break

for i in range(3):
    for j in range(3):
        if i==j:
            continue
        print(i,j)

#----------------------- Loops with else block -------------------------#

#employee without break
#employee with break
# if   |  for  | while 
# else |  else | else

cart=[10,20,30,40,50]
for item in cart:
    if item>500:
        print("we can't place this order")
        break
    print('processing item : ',item)
else:
    print('Congratulations all items processed successfully')
    
#If 600 is in between break statement will be executed and it will come out of loop.
# else is meaningful with break statement not meaningful with continue statement

#Q for loop and while loop
# Repeat code for every item in sequence : for loop
# Repeat code as long as some codition iis True : while loop

#Q How to exit from the loop?
# by using break statement

#Q How to skip some iteration inside loop?
# by using continue statement

#Q When else part will be executed in loops?
# if loop executed without break then only else block will be executed.

#-------------------------- Pass statement -----------------------------#

# Whenever we have to create empty block we use pass function
def f1():
    pass

#Pass statement act like place holder.
class A:
    pass

class B:
    pass
class C:
    pass

x=100
if x>100:
    print('Success')
else:
    pass    
    
#after 2 days    
if x>100:
    print('Success')
else:
    print('Failur')    

# Abstract method
# method without body
from abc import *
class loan(ABC):
    @abstractclassmethod()
    def getInterestRate(self):
        pass
class Homeloan(Loan):
    def getInterestRate(self):
        return 8
class Vehicleloan(Loan):
    def getInterestRate(self):
        return 12
        
# Conclusion about pass:
#1. pass statement acts as empty statement in python.
#2. It acts as a placeholder to implement future code.
#3. It can be used to define minimal classes and function.
#4. To define abstract method, pass statement is the best choice.

#-------------------------------- del statement --------------------------#

#1. delete a variable
x=10
del x
print(x) #Name error

s1='durga'
s2=s1
s3=s2
del s1
print(s2)
print(s3)
del s2,s3

#2. del vs immutable objects
s='durga'
del s
#del[4] #Type error
#we can delete reference variable but we can not delete element of immutable object  
    
#3. del vs None
x=10
del x
print(x) #name error

x=10
x=None
print(x)

#We can use del to delete a variable
#The main advantage of del is we can make objects eligible for Garbage collection
#So, that memory will be improved.
#The chance of failing Python program with memory problems will be very less 
#so that python application will become more robust    

#1. del Vs multiple variables
#We can use del to delete multiple variables. if we delete all reference variables
# then only object eligible for Garbage Collection(GC)

#2. del Vs Immutable Object
#we can delete reference variable which is pinting to the immutable object. 
#but we can not delete elements of the immutable object.

#3. del Vs None
#After del we can not use that variable but after assigning with None value, we can access that variable.

#------------------- Prime numbers introduction ---------------#
#Only two factor
# 1-> neither prime nor composit

#---- Program to check wheter the given number is prime or not? --------#

# WAP to check wheter the given number is prime number or not?
# Logic no.>1 and only two factor

n=int(input('Enter any number :'))
if n<=1:
    print('It is not prime number')
else:
    is_prime=True
    for i in range(2,n): # (n//2+1)
        if n%i==0:
            is_prime=False
            break
    if is_prime==True:
        print('It is prime number')
    else:
        print('It is not prime number')

#---- Generate prime number which are less than or equal to Given no. ----------#

# WAP to generate prime numbers which are less than or equal to the given number

n=int(input('Enter any number : '))
n1=2
while n1<=n:
    #code to check whether n1 is prime or not.
    is_prime=True
    for i in range(2,n1//2+1):
        if n1%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(n1)
    n1=n1+1
    
#--------------- Programe to generate first n prime numbers? ------------#

# WAP to generate n prime numbers?

n=int(input('Enter any number : '))
count=0
n1=2
while True:
    #code to check whether n1 is prime or not.
    is_prime=True
    for i in range(2,n1//2+1):
        if n1%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(n1)
        count=count+1
    if count==n:
        break
    n1=n1+1



