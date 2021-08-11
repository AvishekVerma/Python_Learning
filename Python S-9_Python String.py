# -*- coding: utf-8 -*-


#------------------------------ Section - 9 -------------------------------------#
#(11th-Aug-2021)
#------------------------------ Python String -----------------------------------#

#---------------- Importance of string and ways of declaring string ------------#

# String data type :-
# If any app contains 1000 objects then more than 900 are strings objects only
# that's why by default input has given str data type
x=input('Enter some data')  #String type 
#Give special importance to string :-
s='durga'
ch='a'
s="durga"
#no char type we delear char as string in python
#Triple quote -- to define multi line string lateral

#'This is ' symbol #-- invalid
"This is ' symbol"  # Valid
'This is \' symbol' # Valid
''' This is 'symbol''' # Valid

s=''' The "python notes" by 'durga' is very good''' # Very easy

#-------------- How to access characters of string and application ----------#
#1. By using index
#2. By using slice

# Python support +ve and -ve both index
#  +ve index -- Left to right(Forward direction)
#  -ve index -- Right to Left(Backward direction)

s='durga'
s[0]
s[-1]
s[100] #index error

# WAP to display character of given string index wise(both +ve and -ve)

s=input('Enter some string : ')
i=0
for x in s:
    print('The character present at +ve index : {} and at -ve index : {} is : {}'.format(i,i-len(s),x))
    i+=1 # i=i+1

#------------------ Slice operator introduction --------------------#
#by using index we got one character
#but by using slice we get sequence of character.

# s[Begin:end:step]
# substring from begin to end-1 index.
# begin is optional and default value is 0
# end is optional and default value is len(s)

s='abcdefghijk'
s[2:7]
s[:7]
s[2:]
s[:]
#by default step is 1

s='abcdefghijk'
s[2:7]
s[2:7:1] #both are same
s[2:7:2]
s[2:7:3]
s[::2]

#------------------------ Slice operator Rules ------------------------#

# s[begin:end:step]
#step either +ve or -ve

# if step is +ve => Left to right(forward direction) -- begin to end-1
# if step is -ve => right to left(backward direction) -- begin to (end+1)
# Step value can not be zero.

#NOTE :- if Forward end value is 0 then result is always empty
         # Backward end value is -1 then result is always empty
         
#Syntax : s[begin:end:step]
#step value can be either +ve or -ve
#If step value is +ve then we have to consider forward direction(from left to right) 
  # from begin index to end-1 index
#If step value is -ve, then we have to consider backward direction(from right ot left)
  # form begin index to end+1 index.
  
#------------- Slice Operator Case study -----------------#

s='sbcdefghij'
s[1:6:2]  
s[::1]  
s[::-1]
s[3:7:-1] #empty
s[7:4:-1]
s[0:10000:1] #slice operator will not raise index error
s[-4:1:-1]
s[-4:1:-2]
s[5:0:1] #empty
s[9:0:0] #value error # if end '0' in forward dir.
s[0:-10:-1]
s[0:-11:-1] #empty
s[0:0:1] #empty
s[0:-9:-2] #empty
s[-5:-9:-2]
s[10:-1:-1] #end '-1' in backward dir. so empty

s[10000:2:-1]

#--------- Mathmatical, Membership and Comparison operation for string ---------#
#  + -- Concatenation
#  * -- Repetition
'durga'+'software'
'durga'+ 10 #TE
'durga'*10
'durga'*'10' #TE

'string'+ 'string'  #correct
'string'+ int # wrong
'string'*int  #correct
'string'*'string' #wrong

#Membership operator

# in , not in 
'd' in 'durga'
'z' in 'durga'
'z' not in 'durga'

s=input('Enter main string : ')
subs=input('Enter substring : ')
if subs in s:
    print('Substirng present in main string')
else:
    print('Substring not present in main string')

# Comparison operator
# <, <=, >, >=, ==, !=
#based on unicode value { a=97, b=98, A=65, B=66}
ord('A')
ord('a')
'durga'<'ravi'
'ramba'<'ramya'

s1=input('Enter first string : ')
s2=input('Enter second string : ')
if s1==s2:
    print('Both string are equal')
elif s1>s2:
    print('First string is greater than second string')
else:
    print('First stringis less than second strin')

#----- Methods: strip(), istrip(),rstrip() to remove spaces present in given string -------#

#Removing spaces from the string :
scity= input('Enter your city name : ')
city=scity.strip()
if city == 'Hyderabad':
    print('Hello,Hydrabadi....Adab')
elif city == 'Bangalore':
    print('Hello,kannadiga........Namskaram')
elif city == 'Chennai':
    print('Hello,Madrasi.......Vanakkam')
else:
    print('your entered city is invalid')

s.strip() # to remove spaces present at both sides of string
s.rstrip() #To remove spaces present at end of string.
s.lstrip() #To remove spaces present at befinning of string.

#------- String Methods : find() and rfind() to find substrings
#Finding sub-string
s='ABCBA'
#WANT  index of that available string
#1. find()
#2. rfind()
#3. index()
#4. rindex()

#1. find()
#index of first occurance
print(s.find('B')) # if yes will return index of first occurance
print(s.find('Z')) # if not will return -1 

#2. rfind()
#right to left
s.rfind('B')

s='ABCDEFGHIJBK'
print(s.find('B'))
print(s.find('B',3,8)) # if want to search for specified indexes

#s.find(substing, begin,end)

#---------- String Method : index() and rindex() to find substring

#3. index() 
#if not available then index error
s='ABCBA'
print(s.index('B'))
print(s.index('Z')) #VE
print(s.rindex('B'))
print(s.rindex('Z')) #VE

#email check
mail=input('Enter your email id : ')
try:
    i=mail.index('@')
    print('mail id contains @ symbol. which is mandatory')
except ValueError:
    print('Mail id does not contain @ symbol')
    
# If sub-string should present mandatory ==> go for .index() method
# if sub-string may or may not present then go for .find() method

#INDEX with boundary
s='ABCDEFGHIJKLMN'
print(s.index('B'))
print(s.index('B',4,8)) #VE
s='ABCDE'
print(s.index('D',3,1000)) #will not give any error

#1. s.find(substring)
#it will returns index of first occurrence of given substring.
#if it is not available then it returns -1

#2. s.find(substring, begin, end)
#To search in the boundary
#It will always search for the substring from begin index to end-1 index.

#3. s.index(substring)
#it returns index of first occurrence of given subtring
#if it is not available then we will get ValueError.

#4. s.index(substring,begin, end)
#To search in the boundary
#It will always search for the given substring from begin index to end-1 index
#if substring is not available then we will get VE

#------------ String method: count() to find the no. of occurrance ----------#

s.count("substring")
s='aBBABBABA'
print(s.count('B'))
s.count('BB')
#if not available will get Zero
print(s.count('B',4,100))
s='BBBBB'
print(s.count('BB'))
print(s.count('B'))
print(s.count('BBB'))
#returns the no. of occurrences of the given substring in the total string.

#------ Application of print index of all occurrences of the given string-------#

s='ABCABCABCC'
print(s.count('ABC'))

#WAP to find index of all occurrence.
s='ABCABCABCC'
len(s)
i=s.find('ABC')
print(i)
i=s.find('ABC',3,10)
print(i)
i=s.find('ABC',6,10)
i=s.find('ABC',9,10)
print(i) #means all occerrance happens

s='ABCABCABCC'
subs='ABC'
i=s.find(subs)
if i==-1:
    print('Substring not found')
while i!=-1:
    print('{} present at index : {}'.format(subs,i))
    i=s.find(subs,i+len(subs),len(s))
print('The number of occurrences : ',s.count(subs))

s='ABCABCABCC'
subs='ABC'
i=s.find(subs)
if i==-1:
    print('Substring not found')
c=0
while i!=-1:
    c+=1
    print('{} present at index : {}'.format(subs,i))
    i=s.find(subs,i+len(subs),len(s))
print('The number of occurrences : ',c)

#------ Method: replace() to perform replacement of one string with another string ----#

s.replace('old', 'new')
s= 'ABABABA'
S1= s.replace('A','B')
print(S1)
s='Durga software solution'
s1 = s.replace(' ','')
print(s1)
#How many spaces available in given string
print('The number of spaces :',s.count(' '))
print('The no. of spaces :',len(s)-len(s1))
#It is case sensitive
#with immutable objects
s= 'ABABABA'
print(id(s))
s1= s.replace('A','B')
print(s)
print(s1)
s= s.replace('A','B')
print(id(s))
#With new changes new object will be created

#-------- String Method : split() and join() for substring and joining of strings -------#

#splitting of strings:
s= 'Durga software solution'
l= s.split()
print(l)

for x in l:
    print(x)

#Default seperation in split method is space.
d= '05-07-2021'
l=d.split("-")
print(l)

for x in l:
    print(l)

#------------------------ Joining of string 

l=['Durga', 'software', 'solution']
s=' '.join(l)
print(s)
d=['05', '07', '2021']
s='-'.join(d)
print(s)

#--------- Changing case of characters of the string and application-1 -----------#

#1. upper()
#2. lower()
#3. swapcase()
#4. title
#5. capitalize()


#1. upper()
#To convert all character to upper case

#2. lower()
#To convert all character to lower case

#3. swapcase()
#To convert lower case character to upper case and upper case character to lower case

#4. title
#To convert all character to title case. ie. first character in every string word should 
 #be upper case and all remaining charcter should be in lower case.
 
#5. capitalize()
#Only first character will be converted to upper case and all should be in lower case

s='Learning python is very easy'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())

#WAP to check whether the given 2 string are equal or not by ignoring case.

s1=input('Enter first string : ')
s2=input('Enter second string : ')
if s1.lower()==s2.lower():
    print('Both string are same')
else:
    print('Strings are not equal')

#below code will also check whether case is equal or not

s1=input('Enter first string : ')
s2=input('Enter second string : ')
if s1==s2:
    print('Both string are same')
else:
    print('Strings are not equal')

#-------- Changing case of character of the string : Application -2 -------------#

#WAP to check whether provided username and password are valid or not
#username is not case sensitive, but password should be case sensitive

username=input('Enter your username : ')
pwd= input('Enter your passward : ')
if username.lower() == 'durga' and pwd == 'anushka':
    print('Valid user')
else:
    print('Invalid user')
    
#WAP to convert first and last character as upper case and all remaining characters
 #should be lower case

s=input('Enter any string : ')
output = s[0].upper()+s[1:len(s)-1].lower()+s[-1].upper()
print(output)

#------ Checking starting and ending part of the string ---------#

s.startswith('substring')
#Returns True if the string starts with provided substring

s.endswith('substring')
#Returns True if the string ends with provided substring

s='Learning python is very easy'
print(s.startswith('Learning'))
print(s.startswith('Lea'))
print(s.startswith('lea'))
print(s.endswith('easy'))
print(s.endswith('Easy'))

#---------- Checking type of character present in the given string -------#

s.isalnum()  # a to z, A to Z, 0 to 9 
s.isalpha()  #Only alphabets
s.islower()  #Only lowercase
s.isupper()  #Only uppercase
s.isdigit()  #Only digits
s.istitle()  #Title case
s.isspace()  #Only space

print('Durga786'.isalnum())
print('Durga876'.isalpha())
print('durga'.isalpha())
print('durga'.isdigit())
print('4590378345'.isdigit())
print('abc'.islower())
print('Abd'.islower())
print('abc123'.islower()) #will only check for alphabets
print('ABC'.isupper())
print('Durga Software Solutions'.istitle())
print('Durga soft solution'.istitle())
print('      '.isspace())

#WAP to check the type of character entered from the keyboard

s=input('Enter any character : ')
if s.isalnum():
    print('It is alphanumeric character')
    if s.isalpha():
        print('It is alphabets symbols')
        if s.lower():
            print('It is lower case alphabets symbols')
        else:
            print('It is upper case alphabets symbols')
    else:
        print('It is a digit symbol')
elif s.isspace():
    print('It is space character')
else:
    print('It is non-space special character')

#-------------------------- String Method Summary --------------------#

#Remove spaces from the string: 1. .strip() 2. .rstrip() 3. .lstrip()
#Finding substring 1. .find() 2. .rfind() 3. .index() 4. .rindex()
#Counting of substring 1. .count()
#Replacing a string with another 1. .replace(Old,New)
#Spliting of string 1. .split(separator)
#Joining of string  ' '.join(group of strings)
#Changing case of a strint 1 .upper() 2 .lower() 3 .swapcase() 4 .title() 5 capitalize()
#Checking start and end of string 1. .stratwith() 2. .endswith() 
#To check type of character present 1 .isalnum() 2 .isalpha() 3 .isdigit() 4 .islower() 5 .isupper() 
#                                   6 .istitle() 7 .isspace()















