

#------------------------------ Section - 5 -------------------------------------#
#(6th-Aug-2021)
#---------------------------- Input and Output Statements -----------------------#

# For python 3.x we have only input()
# input() -- will return str type only
x=input('enter something: ')
print(type(x))

# Demo Programe -1 To read input data from the keyboard

#Q Read two int function and print their sum.

x=input('Enter first number: ')
y=input('Enter second number: ')
x=int(x)
y=int(y)
print('the sum is ',x+y)

#Another way and recommended way
x=int(input('Enter first number: '))
y=int(input('Enter second number: '))
print('The sum is',x+y)

#One more another way
print('The sum is',int(input('Enter first number'))+int(input('enter second number')))
#but not recommended

#De mo P -2 To read input data from the keyboard

#Q Write a program to read employee data from the keyboard and print the data.
eno=int(input('Enter emplyee no: '))
ename=input('Enter emplyee name: ')
esal=float(input('Enter emplyee salary: '))
eadd=input('Enter emplyee address: ')
married=eval(input('Enter Married[True|False]: '))
print('Confirm entered Data')
print(eno)
print(ename)
print(esal)
print(eadd)
print(married)
print(eno,ename,esal,eadd,married)

# Reading Multiple values from the keyboard in a single line
a,b=[int(x) for x in input('Enter two numbers: ').split()]
print('The sum is ',a+b)

input('Enter two numbers: ')
input('Enter two numbers: ').split()
a,b=[int(x) for x in input('Enter two numbers: ').split()] #List comprehension

s=input('Enter 2 number: ')
print(s)
l=s.split()
l1=[int(x) for x in l]
print(l1)
a,b=l1
print(a)
print(b)
print('The sum is ',a+b)

#Q write a programe to read three float values from the keyboard with',' separation and print the sum.
a,b,c=[float(x) for x in input('Enter three float value with , sepration: ').split(",")]
print('The sum is ',a+b+c)

# eval() function
# will evaluate x value
x=eval(input('Enter someting: '))
print(type(x))
x= eval("10+20+30")
print(x)
print(type(x))
x= eval("10+20/3**4//5*40")
print(x,type(x))
#It is alternative of typecasting function

#------------------------------ Command Line Argument -----------------------------#

#It is another way to provide user input
#py test.py 10 20 30
# sys -- Module
# argv -- Variable -- list type
from sys import argv
print(type(argv))
print(argv[0])
print(argv[1])
# First value in command line

# Program to print command line argument in format
from sys import argv
print('The number of cmd line arguments:', len(argv))
print('The list of cmd line argument',argv)
print('The cmd line arguments one by one: ')
for x in argv:
    print(x)

# cmd line argument Part-2
#Q Program to print sum of given numbers provided as cmd line arguments
from sys import argv
args=argv[1:]
sum=0
for x in argv:
    sum = sum+int(x)
    print('The sum: ', sum)
    
#What is use of cmd line argument
#file Merge appication
f1=open('file1.txt')
f2=open('file.ext')
f3=open('output.txt','w')
for x in f1:
    f2.write(x)

for x in f2:
    f3.write(x)

f1=open(argv[1])
f2=open(argv[2])
f3=open(argv[3])

# py.test.py a.txt b.txt c.txt
# py.test.py x.txt y.txt z.txt

#The main use of cmd line argument is that we can customised our program behivior.

# Imoprtant conclusions about Command line argument
#Case 1 :- from sys import argv
# print(argv[1])  #py test.py sunny leone  #sunny
#ONly double quote
# space is seperation in a cmd line arg.

#Case 2 :- from sys import argv
#print(argv[1]+argv[2]) # py.test.py 10 20  #1020
#print(int(argv[1])+int(argv[2])) 

#Case 3 :- from sys import argv
#print(argv[100]) #index error

#cmd line argument is available as string form we have to perform typecasting
#If we try to access argument without range index we will get Index error.

#------------- Output Statements : print() function & sep attribute------------#

#1. print() wihtout any line -- it will give \n means new line
print('durga')
print()
print('soft')
#2. print(string)  
print('durga')
print('durga\nsoftware')
print('durga\tsoftware')    
print('durga'+'soft')    
print(10*'durga')    
#3.
a,b,c=10,20,30    
print('values are:',a,b,c)    
#4. Sep attribute
a,b,c,d = 10,20,30,40
print(a,b,c,d)    
print(a,b,c,d,sep=':')    

#--------------------------- end attribute --------------------#
#5. end attribute -- default \n
print('hello')    
print('durga')    
print('software') 
   
print('hello',end='')    
print('durga',end='')    
print('soft') 
   
print('hello',end='::')
print('durga',end='***')
print('soft')

print(10,20,30,40,sep=':',end="***")
print(50,60,70,sep=':')
print(80,90,sep='**',end='$$')
print(100,110)

print('durga'+'soft')
print('durga','soft')

#-------------------------- print(object) and with replacemtnt operator -----------#

#6. print(object)
l=[10,20,30,40]
print(l)
t=(10,20,30,40)
print(t)

#7. print() with replacemnt operator {}
name = 'durga'
salary=10000
gf='sunny'
print('Hello {}, your salary is {} and your friend {} is waiting'.format(name,salary,gf))
#Order is very important
print('Hello {0}, your salary is {1} and your friend {2} is waitng'.format(name,salary,gf))
print('Hello {n}, your salary is {s} and your friend {f} is waiting'.format(n=name,s=salary,f=gf))
#Adv.:- Order is not important
#Most commonly used is first one.
a,b,c,d=10,20,30,40
print('a={},b={},c={},d={}'.format(a,b,c,d))

#------------------- print() with formatted string -----------------------------#

# %i --> signed decimal value
# %d --> signed decimal value
# %f --> float value
# %s --> string,   any other objects list,set,............

a=10
print('a value : %i'%a)
a=10;b=20;c=30
print('a=%d,b=%d,c=%d'%(a,b,c))
name='Durga'
marks=[10,20,30,40]
print('Hello %s, your marks list: %s'%(name,marks))
#formatted string is more powerful than replacement operator
price=70.9235954380
print('Price value= {}'.format(price))
print('Price value = %f'%price)
#Only two points after decimal
print('price value = %2f'%price)






