# -*- coding: utf-8 -*-


#------------------------------ Section - 12 -------------------------------------#
#(14th-Aug-2021)
#----------------------- Python Data Structure : Tuple ----------------------------#

#------------------------------ Tuple Properties ----------------------------------#

#1. Order is applicable
#2. Duplicates are allowed
#3. Heterogneous objects allowed
#4. Idexing and slicing is allowed
#5. Immutable
#6. (       )

t=(10,'durga',20,10)
k=10,'durga',20,10
print(type(t))
print(type(k))
print(t[0])
print(k[2])
l=[10,20,30,40]
t=(10,20,30,40)
l[0]=777
t[0]=777 #TE
print(l)
print(t)

# Youtube comment ---> List type
# Vending machine ---> Tuple type
# server ---> 'START', 'STOP', 'TERMINATED', 'RUNNING'

#------------------------- Single valued Tuple --------------------#
t=(10,20,30)
t=(10,20)
t=(10) # int type not tuple
print(type(t)) 
t=(10,)
print(type(t))
t=() #valid
t=(10) #valid
t=10 #invalid
t=(10,) #valid
t=10, #valid
t=(10,20,30) # valid
t=10,20,30 #valid
t=(10,20,30,) #valid
t=10,20,30, #valid

#----------------------- Creation of Tuple Object -------------------------#

#1. Empty tuple
k=()
type(k)

#2. Single valued Tuple
t=(10,)
t=10,

#3. Multi valued Tuple
t=(10,20,30)
t=10,20,30
t=(10,20,30,)
t=10,20,30,

#4. By using tuple() function
t=tuple('Sequence')
l=[10,20,30,40]
t=tuple(l)
print(t)
t=tuple(range(1,11,2))
print(t)
t=tuple('durga')
print(t)

#5. with dynamic input
t=eval(input('Enter tuple object :'))
print(t)

#--------- Accessing elements of Tuple by using index and slice operator ---------#

#1. By using index :
t=(10,20,30,40,50,60)
print(t)
print(t[2])
print(t[-1])
print(t[100]) #IE

#2. By using slice operator :
t=(10,20,30,40,50,60,70,80)
print(t[1:5])
print(t[0:7:2])
print(t[::2])
print(t[::-1]) # will reverse tuple

#-------------- Mathematical Operators for Tuple --------------------#

#1. concatenation(+)
t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2 #here we are creating new tuple, not changing t1 and t2
print(t3)
print(t2)
print(t1)
#both argument should be tuple only

#2. Repetition
t1=(10,20,30)
t2=t1*3
print(t2)
t1=10,20
t2=30,40
t3=t1+t2
t4=t3*4
print(t4)

#------- Equality, Relational and Membership operators for Tuple

# Equality    --> ==, !=
t1=('Cat','Dog','Rat')
t2=('Cat','Dog','Rat')
t3=('CAT','DOG','RAT')
t4=('Dog','Cat','Rat')
#1. number of elements
#2. Order of elements
#3. Content of element(including case)
t1==t2
t1==t3
t==t4

# Relational operator  ( <, <=, >, >=)
t1=(10,20,30)
t2=(40,50,60)
print(t1<t2)
print(t1>t2)
t1=(10,20,30)
t2=(10,5,70)
print(t1>t2)
t1=(10,20,30)
t2=(10,20,30,50,40)
print(t1<t2)

# Membership operator
t=(10,20,30)
print(10 in t)
print(40 not in t)
print(30 not in t)

#-------------- Important Methods and Functions for Tuple : len(), count() and index() ------------#

#1. len() ==> return number of elements in given tuple
l=(10,20,30,30)
len(l)
#2. count() ==> return number of occurrence of specified element
t=(1,1,2,2,2,3,3,4,4,5)
t.count(1)
t.count(7)
#3. index() --> returns index of first occurence of specified object
t=(1,10,20,30,10)
print(t.index(10))
print(t.index(40)) #VE

#-------------- Reversing and sorting elements of Tuple ------------#

#reverse() function will not applicable in tuple because it is immutable.
t=(10,20,30,40,50)
r= reversed(t)
t1=tuple(r)
print(r)
print(t1)

# sorting
t=(20,5,10,7,0)
t.sort() #AE
l=sorted(t) # list
t1=tuple(l)
print(t1) 
#want decreasing order
l=sorted(t,reverse=True)
print(l)

# max() and min() functions for tuple
t=(20,10,0,50,10)
print(max(t))
print(min(t))

#append() insert() extend() ---->Not applicable
#remove() pop() clear()     ---->Not applicable

#----------- Tuple Packing and unpacking ------------------#

a=10
b=20
c=30
d=40
#Packing
t=(a,b,c,d)
print(t)
l=[a,b,c,d]
print(l)
#Unpacking
t=(10,20,30,40)
a,b,c,d=t
print(a,b,c,d)
a,b,c=t #will get error VE

#while unpacking number of variable should be same as number of element
a,b,c,d,e=t #VE

a,*b=t #first value to a and remaining to b
print(a)
print(b)

#----------------------- Tuple comprehension --------------------#

l=[x*x for x in range(1,6)]
print(type(l))
print(l)
t1=(x*x for x in range(1,6)) #it is  a generator object
print(type(t1))
t1=tuple(t1)
print(type(t1))
print(t1)
#Comprehension concept not applicable for the tuple it is applicable for list object.

#----------------- Difference between List and Tuple : Extra Theory -----------------#
 
#     List               |               Tuple
#                        |
# l=[10,20,30,40]        |  t=(10,20,30,40)
# more memory            |  #less memory
# performance is low     | # performance is high
# list is unhashable     | tuple is hashable

# Set
# liner serach  o-->o-->o-->o
# time complaxity ---  O(n)
# binary serach 
# time complaxity  --- O(log(n)) 
# hash code serarch
# time complaxity  --- O(1)
# hash code

# so search operation SET is most prefered because it uses hash table to store the data
# dict. --- Based on hash code of keys.

import collections
l=[10,20,30]
t=(10,20,30)
print(isinstance(l,collections.Hashable))
print(isinstance(t,collections.Hashable))
print(hash(t)) # we will get hash code
print(hash(l)) #TE
# Set
s={10,20}
l=[10,20,30]
t=(10,20,30)
s.add(t)
print(s)
s.add(l) #TE
d={}
l=[10,20,30]
t=(10,20,30)
d[t]='A'
print(d)
d[l]="B" #TE

#------ Program to take tuple of numbers from the keyboard and print sum, average ------#

t= eval(input('Enter tuple of numbers : '))
sum=0
for x in t:
    sum=sum+x
print('The sum : ', sum)
print('The Average: ',sum/len(t))
print(sum(t))
sum(t)/len(t)






