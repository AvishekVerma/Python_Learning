# -*- coding: utf-8 -*-


#------------------------------ Section - 6 -------------------------------------#
#(7th-Aug-2021)
#---------------------------- Python Flow Control: Part -1 -----------------------#

#Selection Statement
# if    if-else     if-elif-else     if-elif

#Iterative Statement
# for     while

#Transfer statement
# break    continue

# pass and del

# There is no switch statement
# do-while and goto are also not available

#----------------------------- if Statement ------------------------#

# if condition:
    #Statement1
    #...........
#Statement4

#If you don't follow proper indentation then we will get indentation error.

#---------------------- if-elif-else statement --------------------------#

name= input('Enter name : ')
if name=='durga':
    print('Hello Durga, Good morning')
print('How are you!!!')

#------------------------- if-else statement ------------------------#

# if condition:
    #Action-1
# else:
    #Action-2
    
name=input('Enter name: ')
if name=='durga':
    print('Hello Durga, Good morning')
else:
    print('Hello Guest, Good morning')
print('How are you!!!')

#------------------------- if-elif-else --------------------------#

#if condition1:
    #Action1
#elif condition2:
    #Action2
#elif condition3:
    #Action3
#else:
    #Default Action
    
brand=input('Enter you Favurite Brand: ')
if brand=='KF':
    print("It is children's brand")
elif brand=='KO':
    print('It is too light')
elif brand=='RC':
    print('It is not that much kick')
elif brand=='FO':
    print('Buy one get one Free')
else:
    print('Other brands are not recommended')


#------------ Finding smallest and Biggest number by using if-elif-else------------#

#Q. WAP to find biggest of 2 given number.
a=int(input('Enter First number: '))
b=int(input('Enter Second number:'))
if a>b:
    print('Biggest number is : ',a)
else:
    print('Biggest number is: ',b)

#Q. WAP to find Smallest number of 2 given number.
a=int(input('Enter First number: '))
b=int(input('Enter Second number:'))
if a<b:
    print('Smallest number is : ',a)
else:
    print('Smallest number is: ',b)

#Q. WAP to find biggest of 3 given number.
a=int(input('Enter First number: '))
b=int(input('Enter Second number: '))
c=int(input('Enter Third number: '))
if a>b and a>c:
    print('Biggest number is : ',a)
elif b>c:
    print('Biggest number is : ',b)
else: 
    print('Biggest number is : ',c)

#Q. WAP to find Smallest of 3 given number.
a=int(input('Enter First number: '))
b=int(input('Enter Second number: '))
c=int(input('Enter Third number: '))
if a<b and a<c:
    print('Smallest number is : ',a)
elif b<c:
    print('Smallest number is : ',b)
else: 
    print('Smallest number is : ',c)

#Q.WAP to check whether the given number is in between 1 to 100 or not?
n= int(input('Enter any number : '))
if n>=1 and n<100:
    print('The number {} is in between 1 and 100'.format(n))
else:
    print('The number {} is not in between 1 and 100'.format(n))


#------------------- Digit to words conversion Programs --------------------#

#Q. WAP to take a single digit number from the keyboard and print its value in English work.
n= int(input('Enter any digit form 0 to 9 : '))
if n==0:
    print('ZERO')
elif n==1:
    print('ONE')
elif n==2:
    print('TWO')
elif n==3:
    print('THREE')
elif n==4:
    print('FOUR')
elif n==5:
    print('FIVE')
elif n==6:
    print('SIX')
elif n==7:
    print('SEVEN')
elif n==8:
    print('EIGHT')
elif n==9:
    print('NINE')
else:
    print('Please enter Number form 0 to 9')

#Another way
n= int(input('Enter any digit form 0 to 9 : '))
list=['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
print(list[n])

#Q. Extend this program to 99
n= int(input('Enter any digit form 0 to 99 : '))
word_upto_19=['','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','ELEVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN','SIXTEEN','SEVENTEEN','EIGHTEEN','NINETEE']
word_for_tens=['','','TWENTY','THIRTY','FORTY','FIFTY','SIXTY','SEVENTY','EIGHTY','NINETY']
if n==0:
    output = 'ZERO'
elif n<=19:
    output = word_upto_19[n]
elif n<=99:
    output = word_for_tens[n//10]+" "+word_upto_19[n%10]
else:
    output = 'Please enter a value from 0 to 99 only'
print(output)

# Extend this program to 999
n= int(input('Enter any digit form 0 to 999 : '))
word_upto_19=['','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','ELEVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN','SIXTEEN','SEVENTEEN','EIGHTEEN','NINETEE']
word_for_tens=['','','TWENTY','THIRTY','FORTY','FIFTY','SIXTY','SEVENTY','EIGHTY','NINETY']
word_for_hundreds=['','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
if n==0:
    output = 'ZERO'
elif n<=19:
    output = word_upto_19[n]
elif n<=99:
    output = word_for_tens[n//10]+" "+word_upto_19[n%10]
elif n==100:
    output = 'ONE hundred'
elif n<=999:
    output = word_for_hundreds[n//100]+" "+ 'hundred'+" "+ word_for_tens[(n-(n//100)*100)//10]+" "+word_upto_19[n%10]
else:
    output = 'Please enter a value from 0 to 999 only'
print(output)

n= int(input('Enter any digit form 0 to 999 : '))
#output = word_for_hundreds[556//100]
y = (n-(n//100)*100)//10
y

#------------------ Iterative Statement : for loop -------------------#
#multiple times

# 1. for loop   2. while loop

# 1. for loop
# we have list, ste, tuple, dict., string, range. if we have to perform someting 
#on every element then we go for 'for loop'

# for x in sequence:
    #Activity

#Ex- Print every letter of given string
s= 'sunny leone'
for x in s:
    print(x)

#Want to print index also
s= 'sunny leone'
i=0
for x in s:
    print('The character present at {} index : {} '.format(i,x))
    i=i+1 #i+=1

#Print any string
s= input('Enter any string : ')
i=0
for x in s:
    print('The character present at {} index : {} '.format(i,x))
    i=i+1 #i+=1

#--------------- Application by using for loop ----------------------#
# want to print 'Hello, welcome to Python' 10 times
for x in range(10):
    print(' Hello, welocme to Python')
    i+=1

# want to print 1 to 10
for x in range(1,11):
    print(x)
    i+=1

# To display odd numbers from 0 to 20
for i in range(0,21):
    if i%2!=0:
        print(i)

for i in range(1,21,2):
    print(i)

# To display number from 10 to 1 in decreasing order.
for i in range(10,0,-1):
    print(i)

# for list
#To print the sum of numbers in the given list.
list=eval(input('Enter a list'))
sum=0
for x in list:
    sum=sum+x
    print('The sum : ',sum)

print(sum(list))

#--------------- While loop and applications -----------------#
# for x in sequence:
    #body

# while condition:
    #body
# It will executed as long as condition is true

i=1
while i<=10:
    print(i)
    print('Hello, welcome to while loop')
    i+=1
    
i=1
while i<=10:
    print(i)
    i+=1

# To print number from 1 to 20 which are divisible by 3
i=1
while i<=20:
    if i%3==0:
        print(i)
    i+=1

# WAP to display sum of first n numbers.
n=int(input('Enter number : '))
sum=0
i=0
while i<=n:
    sum=sum+i
    i=i+1
    print('The sum : ',sum)

# While loop is always based on some condition but for loop is always based on some sequence.

name=' '
while name !='sunny':
    name=input('enter your Faboarite actress : ')
    print('Thanks for confirmation')

#--------------------- Infinite loops and nested loops

# Infinite loops:-
i=1
while True:
    print('Hello : ',i)
    i=i+1

# while True:
    #body
    #if our required condition satisfied
    #break

#If we do not know how many times we have to repeate while loop is best.

# Nested loops
#Loop inside loop.
for i in range(3):
    for j in range(2):
        print('Hello')

for i in range(3):
    for j in range(2):
        print('i = {}, j = {},'.format(i,j))





