# -*- coding: utf-8 -*-


#------------------------------ Section - 11 -------------------------------------#
#(13th-Aug-2021)
#----------------------- Python Data Structure : List ----------------------------#

#------------------------------ List Properties ----------------------------------#

#If we want to represent group of objects as a single entity and duplicates are allowed
 # and inception order must be preserved then we go for List.

l=[] #empty string
l.append(10)
l.append('durga')
l.append(10)
print(l)
l[0]=77
print(l)

#1. Insertion order preserved
#2. Duplicate object allowed
#3. Hetrogenous object allowed
#4. List is Dynamic (add or remove element)
#5. List is mutable
#6. To represent index [] 

#---------------------- Creation of list object ----------------------------------#

#1. Empty list object
l=[]
print(type(l))
print(l)
#2. If we know data already
l=[10,20,30,50]
#3. Dynamic input
l=eval(input('Enter a list : '))
print(l)
#4. By using list()



l=list('durga')
print(l)
l=list(range(0,10,2))
print(l)
#5. split method ==> will return list always
s='learning python is easy'
l=s.split()
print(l)

#--------- Accessing element of list by using index and slice operator -----------#

#1. By using index
#2. By using slice operator

#1. By using index
l=[10,20,30,40]
print(l[0])
print(l[-1])
print(l[100]) #IE

#2. By using slice operator
#l('begin':'end':'step')
# +ve => forward direction => begin to end-1
# -ve => backward direction => begin to end+1

l=[10,20,30,40,50,60,70,80,90,100]
l[2:7]
l[2:7:2]
l[4::2]
l[8:4:2]
l[4:100] #will not give error
l[4:0:2] #Empty
l[::1]
l[::-1] # Reverse

#------------------- Tranversing Elements of the List and Applications -----------#
l=[1,2,3,4,5,6,7,8,9,10]
#1. By using while loop
i=0
while i < len(l):
    print(l[i])
    i=i+1

#2. By using for loop
for i in l:
    print(i)

#3. to print every even number
for x in l:
    if x%2==0:
        print(x)

#print +ve and -ve index
l=[10,20,30,40,50,60]
i=0
while i<len(l):
    print('The element at +ve index : {} and at -ve index : {} is : {} '.format(i,i-len(l),l[i]))
    i=i+1
 
#---------------------- Mathematical Operatiors for list -----------------------#

#1. concatenation operator(+)
#2. Repetation operator(*)
#3. Concatenation operator

#1. concatenation operator(+)
l1=[10,20,30]
l2=[40,50,60]
l3=l2+l1
print(l3)
l2=l1+40  #TE
#Both should be list only
l2=l1+[40]
print(l2)
l2=l1+(20,50,60) #TE can't add tuple object

#2. Repetation operator(*)
l1=[10,30]
l2=l1*2
print(l2)
l3=l1+l2
l4=l3*3
print(l4)

#-------------- Equality, Relation and Membership operator for list -------------#
# ==, !=
# Equality operator
l1=['Dog','Cat','Rat']
l2=['Dog','Cat','Rat']
l3=['DOG','CAT','RAt']
l4=['Cat','Dog','Rat']
print(l1==l2)
print(l1==l3)
print(l1==l4)
#1. The number of elements must be same
#2. The order of element must be same.
#3. The content must be same inclucing casa
print(l1!=l4)

# Relational operator
# <, <=, >, >=
l1=[10,20,30,40]
l2=[50,60]
print(l1<l2)
print(l1<=l2)
print(l1>l2)
print(l1>=l2)
# for the content only
# it will compare element by element
# if first element can't decide then moce to next
l1=['Ramba','Ramya']
l2=['Roja','sunny']
print(l2<l1)

# Membership operator
#  in,  not in
l1=[10,20,30,40]
print(10 in l1)
print(30 not in l1)
print(70 in l1)

#----- Important Functions and method for list : len(), count() and index() ------------#

l=[10,20,30,40]
len(l)
l=[]
l.append(10)
l.append(20)
l.append(30)
sorted(l)
print(l.count(10))
print(l.count(50))
print(l.count(30))
l=[1,2,4,2,1,5]
print(l.index(1))
print(l.index(100)) #VE

l=[1,2,2,3,3]
x=int(input('Enter element fo find : '))
if x in l:
    print('{} present at index : {}'.format(x,index(x))
#else:
 #   print(x,'not available in list')

          
#------- Important method and functions for list : append() and insert() -------------------#

#1. append()
# add end of the list
l = []
l.append(10)
l.append(20)
l.append(30)
print(l)

#WAP to add numbers which is divisible by 10 from 1 to 100
l=[]
for x in range(1,101):
    if x%10==0:
        l.append(x)
print(l)

# insert()
# to add element at specified index
# l.insert(index, object)
l=[10,20,30,40]
l.insert(1,7777)
print(l)
l.insert(100,9999)
l.insert(-1,6666)
print(l)
# If specified index is greater than maximum index then element will be added at last index
#if -ve then at first index

#-------- Important method and functions for list : extend() -----------------------#
#3. extend
# To add all elements of given sequence to the list.
l1.extend(l2)
order1=['Chicken','Mutton','Fish']
order2=['KO','KF','RC']
order1.extend(order2)
print(order1)
# append() and insert() method add one element 
# extend() method add multiple element
# some loop holes :-
l1=[10,20,30]
l2=[40,50]
l1.append(l2) # will treat l2 as one element
print(l1)
print(len(l1))
l1.extend(l2) #added individually
l1=[10,20,30]
l1.append('ABC')
print(l1)
l1.extend('ABC')
print(l1)

#------------- Important method and functions for list : remove() -----------------------#

# remove()      pop()       clear() 
# l.remove(x)
# it is used to remove specified element from list
# if multiple element present will remove 1st occurrence
l=[10,20,30,40,20,10]
l.remove(40)
print(l)
l.remove(50) #VE

l=[1,2,3,4,5,6]
print('Before removal: ',l)
x=int(input('enter element to remove : '))
if x in l:
    l.remove(x)
    print('After removal: ',l)
else:
    print(x,'not present in list')

# How to remove all occurrences?
l=[1,1,2,2,2,3,4,5]
x=int(input('enter element to remove : '))
while True:
    if x in l:
        l.remove(x)
    else:
        break
print('After removal : ',l)

#------------- Important method and functions for list : pop() and clear() -----------#

#2. pop()       l.pop()
#it removes the last element and return removed elemtent 
l=[10,20,30]
print(l.pop())
print(l.pop())
print(l.pop())
print(l.pop()) #IE
# if empty list then IE
# l.pop(index)
# remove at specified index
l=[10,20,30,40]
print(l.pop(1))
print(l)
print(l.pop(100)) #IE

#3. clear()
# if want to remove all element ==>  clear()
l=[10,20,30,40]
print(l)
l.clear()
print(l)


# List
# To increase size/to add element    append(), insert(), extend()

# To decrease size/ To remove element   remove(), pop(), clear()

#---------- Ordering elements of list: reverse() and reversed()  ----------------#

#1. Reversing order :   l.reverse()
l=[10,20,30,40]
print(l)
l.reverse()
print(l)
#in existing list only it will reverse elements.

#2. reverse()     vs       reversed()
# only for list   | inbuild function of python
l.reverse()
l=[10,20,30,40]
r=reversed(l) #reversed iteratior object
l1=list(r)
print(type(r))
print(r)
s='durga'
r=reversed(s)
for x in r:
    print(x)

#------------ Ordering element of List : sort() and sorted() -----------------------#

#1. Sorting elements of list:   
#       l.sort()
#    numbers --> Ascending order
#    string --> Alphabetical order
l=[20,5,15,0,10]
print(l)
l.sort()
print(l)
l=['Bananna','Cat','Apple']
l.sort()
print(l)

# If i want in descending order
l.sort(reverse=True)
l=['Mango','Apple','Banana']
l.sort(reverse=True)
print(l)
l=[40,20,'B','A']
l.sort(l) #TE
# If want to use sort method compulsary all elements should be same type(homodeneous type)

#sort()           vs sorted()
# list specific    | python inbuilt fn
# l.sort()           | l1=sorted(l)

#--------------------- Aliasing and cloning of list object -----------------#
#Aliasing ===> Duplicate name
l1=[10,20,30,40]
l2=l1 #Creating of duplicate reference variable
l1[1]=7777
print(l)
print(l2)
#cloning ==> creating brand new object form old object is called cloning

l1=[10,20,30,40]
print(id(l))
l2=l1[::1]
print(id(l2))
l1[1]=7777
print('l1',l1)
print('l2',l2)
l2=l1.copy()

#------------------ Nested Lists ------------------#
l=[10,20,30,[50,40]]
print(l[0])
print(l[3])
print(l[3][0])

#Nested list as matrinx:
l=[[10,20,30],[40,50,60],[70,80,90]]
print(l)
print('Elements Row wise :')
for x in l:
    print(x)
    
for x in l:
    for y in x:
        print(y, end=' ')
    print()

#----------- List Comprehension and Application part-1
l=[1,2,3,4,5,6,7,8,9,10]
#Normal way
l=[]

for i in range(1,11):
    l.append(i)
print(l)

#List comprehension
l=[x for x in range(1,11)]
print(l)
l=[x*x for x in range(1,6)]
print(l)
# [expression for each_element in sequence]
# [expression for each_element in sequence if condition]

# creation of list with square values from 1 to 10
l=[1,4,9,16,25,36,49,64,81,100]
l=[ x*x for x in range(1,11)]
print(l)

# 2^x and x values are 1 to 5
l=[2**x for x in range(1,6)]
print(l)

#list of number from 1 to 100 which are divisible by 10
l=[ x for x in range(1,101) if x%10==0]
print(l)

#-------------- List comprehension and application part-2--------------#

l1=[10,20,30,40]
l2=[30,40,50,60]

#create list with elements present in l1 but not in l2
l3=[x for x in l1 if x not in l2]
print(l3)

#create list with elements present in both l1 and l2
l4=[x for x in l1 if x in l2]
print(l4)

l=['Balaiah','Nag','Venki','China']
l1=['B','N','V','C']
l2=[ words[0] for words in l]
print(l2)

s='The quick brown fox jumps over the laxy dog'  #It contains all words
words= s.split()
l=[[word.upper(),len(word)] for word in words]
print(l)

#------- program to find unique vowels present in the given word ----------------#

vowels=['a','e','i','o','u']
words=input('enter any string : ')
result=[]
for ch in words:
    if ch in vowels:
        result.append(ch)
        
print(result)
print('The no of unique vowels :',len(result))

result=[]
for ch in vowels:
    if ch in words:
        result.append(ch)
print(result)

vowels=['a','e','i','o','u']
words='durga software solutions'

result=[ch for ch in vowels if ch in words]
print(result)



