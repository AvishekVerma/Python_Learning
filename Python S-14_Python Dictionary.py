# -*- coding: utf-8 -*-


#------------------------------ Section - 14 -------------------------------------#
#(17th-Aug-2021)
#----------------------- Python Data Structure : Dictionary ----------------------------#

#------------------------------ Dictionary Properties ----------------------------------#

#What is the need
#key-value pairs
# Roll no. - Name
#d={k1:v1,k2:v2,k3:v3}
#1. key-value pairs
#2. Duplicate keys not allowed --- Values can be duplicated
#3. Insertion order is not preserved 
# it is vased on hash code of the keys.
#4. Indexing and slicing are not allowed
#5. Heterogeneous objects keys--- values
#6. Mutable
#7. Dynamic in size
#8. d={k1:v1,k2:v2,k3:v3}
d={100:'durga','A':300,200:'Ravi','B':400}
# old value will be replaced with new value
print(d)

#-------- Creation of Dictionary object --------------#

#1. Empty object
d={}
d=dict()
#2. If we know data already
d={100:'durga',200:'ravi'}
#3. By using dice()
l=[(100,'A'),(200,'B'),(300,'C')] #list of tuple
d=dict(l)
print(d)

# Tuples of tuples | Set of Tuples | List of Lists | Tuple of lists
#Set of lists --- not allowed TE
l=[(100,'A',200)] #VE -- only should two elements -- error

#4. By using dynamic input:
d=eval(input('Enter Dictionary : '))
print(d)

#-------- How to access, add, update and delete data from the dict. -------#

#Access
d={100:'durga',200:'Shiva',300:'Ravi'}
# d[key]
print(d[100])
print(d[300])
print(d[700]) #KE

d={100:'durga',200:'Shiva',300:'Ravi'}
key=int(input('Enter key to find value : '))
if key in d:
    print('The corresponding value : ',d(key))
else:
    print('The provided key is not available')

# Add and update
# d[key]=value -- if available then value will be replaced
#              -- if not available then value will be added to dict.

d={100:'durga',200:'Shiva'}
d[300]='Ravi'
print(d)

# Delete
# del d[key] -- if not availavle then KE
del d[200]
del d[400] #KE
# del d[key1],d[key2] -- deleting multiple value
del d[100],d[200]

#-------- WAP to enter name and marks into dict and display on the screen --------#

n= int(input('Enter no of students : '))
d={}
for i in range(n):
    name= input('Enter name of student : ')
    marks= input('Enter marks of student : ')
    d[name]= marks
print(d)
print('*'*30)
print('Name','\t\t','Marks')
print('*'*30)
for name in d:
    print(name,'\t\t',d[name])

#--------- Mathematical, Equality, Relational and Membership operator for dict. ----#

d1={100:'A',200:'B'}
d2={300:'C',400:'D'}
d3=d1+d2 #TE 
d4=d1*3  #TE
#Concatination and repetation operator are not applicable for dictionary
print(d1==d2)
d3={200:'B',100:'A'}
print(d1==d3)
# Equality operator--> will compare content only
# Reational opt. --> Not applicable
print(d1>d2) #TE

# Membership --> check only for keys
print(100 in d1)
print(300 in d1)

#--------------- Important Methods and Functions for Dict : len(), get() and update() ------#

#1. len(d) --> no. of items in dict
d={100:'A',200:'B', 300:'C'}
len(d)
#2. get()  --> d[key] -- key error if data is not available
# d.get(key) --> if not available then will return None
print(d.get(100))
print(d.get(300))
print(d.get(700))
# d.get(key,default_value)
# IF data is not available then return my specified value.
print(d.get(100,'Guest'))
print(d.get(700,'Guest'))
#3. Update()
d1={100:'A',200:'B'}
d2={400:'D', 300:'C'}
d1.update(d2)
print(d1)
# If key already exist it will update value

#--------- Important Methods and Functions for Dict : keys(), values(), items() ------#

d={100:'A',200:'B', 300:'C'}
k=d.keys()
print(k)
for key in d.keys():
    print(key)

values=d.values()
print(values)
for value in d.values():
    print(value)

i=d.items()
print(i)
for i in d.items():
    print(i)

for k,v in d.items():
    print(k,'   ',v)

#-------- Programs to get value based on key and to get key based on value -------------#

#WAP to get value from the dict. for the given key 
d={100:'A',200:'B', 300:'C'}
# Based on kty finding value
key=int(input('Enter key to get value : '))
if key in d:
    print('The corresponding value is : ',d.get(key))
else:
    print('The key is not available')

#Finding key vased on value:
d={100:'A',200:'B', 300:'C'}
value=input('Enter value to find key : ')
available=False
for k,v in d.items():
    if v==value:
        print('The corresponding key is : ',k)
        available=True
if available==False:
    print('The specified value not in dict.')

#what if multiple value present then it will provide all keys

#--------- Important Methods and Functions for Dict : pop(), popitem(), clean() ------#

#1. pop(key) --> removes item associated with specific key and return the corresponding value
#if key not available -->KE
d={100:'A',200:'B', 300:'C'}
print(d.pop(300))
print(d.pop(700)) #KE
#2. d.pop(key,value)
print(d.pop(300,'Guest'))
print(d.pop(700,'Guest'))
#3. d.popitem() --> it will remove one item randomly
print(d)
print(d.popitem())
print(d)
#4. d.clear() --> it remoes all items from dict
d.clear()
print(d)

#--------- Important Methods and Functions for Dict : setdefault() and copy() ------#

d.setdefault(k,v)
# if key already available then simply returns associated value without any replacement.
# if key is not available then new key-value pair will be added.
d={100:'A',200:'B', 300:'C'}
print(d.setdefault(300,'durga'))
print(d.setdefault(400,'Sunny'))
print(d)
#Aliasing and cloning 
d1={100:'A',200:'B'}
d2=d1
d1[300]='C'
print(d1)
print(d2)
d2=d1.copy()

#--------- Important Methods and Functions for Dict : Summary ------#

len(d)    # will return no. of items present
d.get(key) # returns value associated with key #KE
d.get(key,'default_value') # if key is not available will return degault value
d1.update(d2) # to add all items to d1
d1.keys() # Return all keys present in the dict.
d1.values() #Return all values present in the dict.
d1.items() #Return all items (key-value pairs) of dict.
d.pop(key)  #Remove item of specified key #KE
d.pop(key,value) #Remove and give provide value
d.popitem() #Remove random item and return thet item #KE
d.clear() #Remove all items
d.setdefault(k,v) #items available don't change. if not then add that item
d.copy() #cloned dict

#------ Program to take dict. from the keyboard and print sum of values --------#
d=eval(input('Enter dictionary : '))
d={100:'A',200:'B', 300:'C'}
sum=0
for item in d.items():
    sum=sum+item[0]
print('The sum of values',sum)

#using sum
d={'A':100,'B':200}
print('The sum of values : ',sum(d.values()))

#------ Program to find no. of occurrences of each letter present in the given string ----#

word= input('Enter any string : ')
d={}
for ch in word:
    d[ch]=d.get(ch,0)+1
print(d)

for k,v in d.items():
    print(k,'occurs',v,'times')

#----- Program to find no.of occurrences of each vowel present in the given string -----#
word=input('Enter any string : ')
vowels={'a','e','i','o','u'}
d={}
for ch in word:
    if ch in vowels:
        d[ch]=d.get(ch,0)+1
for k,v in sorted(d.items()):
    print(k,'occurred',v,'times')

#------- Student Management Application by using dict --------------#

#WAP to accept student name and marks from the keyboard and creates a dictionary. Also display
 # student marks by taking student name as input.
 
n=int(input('Enter no. of students : '))
d={}
for i in range(n):
    name=input('Enter Student name : ')
    marks=int(input('Enter student marks : '))
    d[name]=marks
print('Student data insertion completed')
print('*'*30)
print('NAME','\t\t','Marks')
print('*'*30)
for k,v in d.items():
    print(k,'\t\t',v)

print('search operation started.......')
while True:
    name=input('Enter student name to get marks : ')
    marks=d.get(name,-1)
    if marks==-1:
        print('Student not found')
    else:
        print('marks of ',name,'are : ',marks)
    option=input('Do you want to find another student marks(yes/No) : ')
    if option.lower()=='no':
        break
print('Thanks for using our applicaion')
    
#------------------ Dictionary Comprehension ------------#
# list ok  Tuple no   set ok  Dict ok
l=[x*x for x in range(1,6)]
print(l)
d={ x:x*x for x in range(1,6)}
print(d)

#------------ Merging of collections --------------#

#1. List merging
l1=[10,20]
l2=[30,40]
l3=l1+l2
print(l3)
l4=[*l1,*l2]
print(l4)

#2. Tuple merging
t1=(10,20)
t2=(30,40)
t3=t1+t2
print(t2)
t4=(*t1,*t2)
print(t4)

#3. Set merging
s1={10,20}
s2={30,40}
s3=s1+s2 #not allowed
s3={*s1,*s2}
print(s3)

#4. Dict merging
d1={100:'A',200:'B'}
d2={300:'C',400:'D'}
d3=d1+d2  #Not allowed
d3={*d1,*d2}
print(d3)

#old value d1 will be replaced by new value d2

#---------- Nested collection introduction and Examples
l1=[(10,20,30),(40,50,60)] #LIst of tuple
print(l1[0][1])
print(l1[1][2])
d={'cars':('Innova','Honda','Maruti'),
   'Mobile':('Samsung','Nokia','Iphone')}
#1. to display second car name
print(d['cars'][1])
print(d.get('Mobile')[1])
#2. To display all mobiles name
for x in d['Mobile']:
    print(x)

#------------- Implementation of Supermarket by using dict. ----------#

Supermarket={
    { 'store1':{
        'name':'Durga General store',
        'items':[
            {'name':'soap','quantity':20},
            {'name':'brush','quantity':30},
            {'name':'pen','quantity':40}
            ]
        }
        'store2':{
            'name':'Sunny Book Store',
            'items':[
                {'name':'Python','quantity':100},
                {'name':'Django','quantity':200},
                {'name':'Java','quantity':300}
                ]
            }
        }
    }

#1. To print name of store 1
print((Supermarket['store1']['name']))
print(Supermarket.get('store1').get('name'))
#2. To print names of all items present in store 1
for d in Supermarket['store1']['items']:
    print(d['name'])
#3. To print quantity of  django
for d in Supermarket['store2']['items']:
    if d['name']=='Django':
        print(d['quantity'])

#------------ List inside set and dictionary ---------------#

# set ==> hashcode
# tuple ==> hashable
# dict --> key==> hashcode
# list  ==> unhashable
# can't add list as key in dict.
s={(10,20,30)}
print(s)
s={(10,20,30),[40,50,60]} #TE
d={(10,20):'item1',[30,40]:'item2'} #TE
d={(10,20):'item1',(30,40):'item2'} # will work


































