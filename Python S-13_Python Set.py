# -*- coding: utf-8 -*-


#------------------------------ Section - 13 -------------------------------------#
#(16th-Aug-2021)
#----------------------- Python Data Structure : Set ----------------------------#

#------------------------------ Set Properties ----------------------------------#

#When to go for set
#Don't want duplicate value  and order are not required  then Go for Set

#1. Duplicates are not allowed
#2. Order is not applicable 
#3. Indexing and Slicing concepts not allowed
#4. {10,20,30}
#5. Heterogeneous objects
#6. Mutable
#7. Union, Intersection, Difference applicable

s={} #Dict.
print(type(s))
s=set()
s.add(10)
s.add('z')
s.add('A')
print(s)
s.add(10)
print(s)

#---------------- Creation of Set Object --------------------#
#1. Empty set:
s={} # dict but not set
s=set()
#2. If we heve data already
s={10,20,30}
#3. By using set() function
l=[10,20,30,40]
s=set(l)
print(s)
s=set('apple')
print(s)
#4. By dynamic input
s=eval(input('Enter set of values : '))
print(s)

#------------- Mathematical, Equality, Relational and Membership operator for Set -------#

s1={10,20,30}
s2={30,40,50}
s3=s1+s2 #TE
s3=s1*3 #TE
s1={10,20,30}
s2={30,10,20}
print(s1==s2)
# number of element and value same | order not important
s1={10,20,30}
s2={20,10,5,6,7}
print(s1<s2) #Not meaningful
print(s1>s2) #Not meaninggul
#Membership ( in, not in)
s={10,20,30,100}
print(10 in s)
print(40 not in s)
print(50 in s)

#-------- Important Method and Functions for Set : len(), add() and update() ----------#

#1. len()   : Return number of element present in set
s={10,20,30,40,50}
len(s)
#2. add()   : it will add single element at a time
s={10,20,30,40,50}
s.add(50)
print(s)
#3. Update : To add multiple items to the set.
s1={10,20}
s2={30,40,50}
s3=[60,70]
s.update(s1,s2) # it should be an iterable objects{list,set,tuple,string}
s.update(s1)
s.update(s1,s2,s3)
s={10,20}
l=[40,70]
s.update(l)
print(s)
s.update(range(1,6),'durga')
print(s)
s.add(10)
s.add(10,20,30) #TE
s.update(10) #TE
s.update(range(1,10,2),range(0,10,2))
print(s)

#-------- Important Method and Functions for Set : remove(),discard(), pop() and clear() ----------#

#1. remove() -- s.remove(x)  will remove specific element
s={10,20,30,40}
s.remove(30)
print(s)
s.remove(50) #KE
#2. discard() -- will not give error if element is not present
s={10,20,30,40}
s.discard(30)
print(s)
s.discard(50)
print(s)
#3. pop() -- will remove random element and that element as an output
s={10,20,30,40}
s.pop()
#will give error if set is empty
#4. clear() -- all element will be removed
s={10,20,30,40}
s.clear()
print(s)

#------ Operators : union(),intersection(), difference() and symmetric_difference() -------#

#1. Union()
s1={10,30,40,20}
s2={30,40,50,60}
s3=s1.union(s2)
print(s3)
s3=s1|s2
print(s3)
#2. Intersection()
s3=s1.intersection(s2)
s3=s1&s2
print(s3)
#3. Difference() -- present in s1 but not in s2
s3=s1.difference(s2)
print(s3)
s3=s1-s2
#4. symmetric_difference()
s3=s1.symmetric_difference(s2)
s3=s1^s2
print(s3)

#----------- Aliasing, Cloning and Comprehension of Set ------------------#

s1={10,20,30}
s1=s2 #Aliasing
s2=s1.copy() #cloning
#Adv. of cloning -- if you change values it will not change old set

#------------ Set Comprehension ------------#

# 1 to 5 -- square values
s={x*x for x in range (1,6)}
print(s)
# 2^x
s={2**x for x in range(1,6)}
print(s)

#------------- Practice programs for set ---------------#
#WAP to eliminate duplicates present in the list 
#Approach -1
l=[10,10,20,30,10,40,20,30]
s=set(l)
print(s)
l1=list(s)
print(l1)

#Approach - 2
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)

#WAP to print different vowels present in the given string

word=input('Enter any world :')
s=set(word)
v={'a','e','i','o','u'}
result=s.intersection(v)
print(result)











































