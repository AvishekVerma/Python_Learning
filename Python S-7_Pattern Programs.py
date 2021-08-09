# -*- coding: utf-8 -*-


#------------------------------ Section - 7 -------------------------------------#
#(8th-Aug-2021)
#---------------------------- Python Pattern Programs -----------------------#

#---------------- To print given number of *s in a row ------------#

n=int(input('Enter n value : '))
for i in range(n):
    print('*',end=' ')

#---------------- To print Square pattern of * ---------------#

n=int(input('Enter number of rows : '))
for i in range(n):
    print('* '*n)
    
#------ To print square pattern with provided fixed digit in every row ----------#

n=int(input('Enter number of rows : '))
for i in range(n):
    print((str(i+1)+" ")*n)

#---------------- To print square pattern with alphabet symbols ---------------#

n=int(input('Enter number of rows : '))
for i in range(n):
    print((chr(65+i)+' ')*n)

#---------------- To print Right Angle Triangle pattern with * symbols ------------#

n=int(input('Enter number of rows : '))
for i in range(n):
    for j in range(i+1):
        print('* ',end=" ")
    print()
        
#---------------- To print Inverted Right Angle Traingle pattern with * symbols------------#

n=int(input('Enter number of rows : '))
for i in range(n):
    for j in range(n-i):
        print('* ',end=" ")
    print()
    
n=int(input('Enter number of rows : '))
for i in range(n):
    print('* '*(n-i))

#---------------- To print Pyramid pattern with * symbols ---------------#

n=int(input('Enter number of rows : '))
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))

#---------------- To print Inverted Pyramid pattern with * symbols ----------#

n=int(input('Enter number of rows : '))
for i in range(n):
    print(' '*i +'* '*(n-i))

#---------------- To print Diamond Pattern with * symbols ---------------#

n=int(input('Enter number of rows : '))
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))
for i in range(n-1):
    print(' '*(i+1) +'* '*(n-i-1))













