# -*- coding: utf-8 -*-


#------------------------------ Section - 10 -------------------------------------#
#(12th-Aug-2021)
#------------------------------ Python String Coading ----------------------------#

#----------------- WAP to reverse content of the given string -----------------#

#1. Using slice operator

s= input('Enter any string : ')
output= s[::-1]
print('The reversed string is : ',output)

#---------- WAP to REVERSE  content using reversed() function ------------#

s=input('Enter any string : ')
r=reversed(s)
output= ''.join(r)
print('The reversed string is : ',output)

#----------- Reverse content by using while loop --------------#

s=input('Enter a string to reverse : ')
output=''
i=len(s)-1
while i>=0:
    output= output+s[i]
    i=i-1
print('Reversed string is : ',output)

#--------- WAP to REVERSE order of words present in the given string ------------#

s=input('Enter your string : ')
#s='Learning Python is very easy'
l=s.split()
output=' '.join(l[::-1])
print(output)

#---------------- WAP to reverse internal content of each word ----------------#

s= input('Enter your sentence : ')
#s='learning python is easy'
l=s.split()
l1=[]
for word in l:
    l1.append(word[::-1])
    output =' '.join(l1)
print(output)

#--- WAP to reverse internal content of every second word present in the given string ---#

s=input('Enter any string : ')
#s='one two three four five six'
l=s.split()
print(l)
i=0
l1=[]
while i<len(l):
    if i%2==0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i=i+1
    
output=' '.join(l1)
print(output)
        
#------ Programe : Print character present at even and odd index separately for given string ---#

s=input('Enter any string')
#s='durgasoft'
i=0
print('Character present at even indes : ')
while i<len(s):
        print(s[i])
        i=i+2
i=1
print('Character present at odd indes : ')
while i<len(s):
        print(s[i])
        i=i+2
        
# By using slice operator 
s=input('Enter any string : ')
print('character present at even index : ',s[0::2])
print('character present at odd index : ',s[1::2])

#---- WAP to merge character of 2 string by taking character alternatively ------#

s1=input('Enter first string : ')
s2=input('Enter second string : ')
s1='RAVI'
s2='TEZA'
i,j=0,0
output=''
while i<len(s1) or j<len(s2):
    output=output+s1[i]+s2[j]
    i=i+1
    j=j+1
print(output)
# Above code will only work for equal length of string

# What is string has different lenagth
s1='RAVIKIRAN'
s2='TEZA'
i,j=0,0
output=''
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
        i=i+1
    if j<len(s2):
        output=output+s2[j]
        j=j+1
print(output)

#---- Sort character of the string, first alphabet symbol followed by digit -----#

#Assume input string contains only alphabet symbols and digit. WAP to sort characters of the string
 # first alphabet symbol followed by digits?

s=input('Enter alphanumeric string : ')
s='B4A1D3'  #OUTPUT = ABD123
print(sorted(s))
#can't use direct sorted() function
alphabets =[]
digits=[]
output=''
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)
output= ''.join(sorted(alphabets)+sorted(digits))
print(output)

# Alernative way :
    
s=input('Enter alphanumeric string : ')
#s='B4A1D3' 
alphabets =[]
digits=[]
output=''
for ch in s:
    if ch.isalpha():
        alphabets +=ch
    else:
        digits +=ch
        
for ch in sorted(alphabets):
    output= output+ch
    
for ch in sorted(digits):
    output = output +ch
print(output)

#------- Program for the requirement, input a4b3c2 and expected output aaaabbbcc -----#

#input : a4b3c3         output : aaaabbbcc
s=input('Enter required output like a4b3c3 : ')
s= 'a4b3c3'
output=''
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        output=output+x*d
print(output)

# This program will work for this form only.

#------ Program for the requirerement , input a3z2b4 and expected output aaabbbbzz

# input a3z2b4          output aaabbbbzz
s=input('Enter required output like a3z2b4 : ')
s= 'a3z2b4'
target=''
output=''
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        target=target+x*d
print(target)
output=''.join(sorted(target))
print(output)

#------ Program for requirement, input aaaabbbcccz and expected output 4a3b2c1z

#input aaaabbbcccz             output 4a3b2c1z
s=input('Enter required output like aaaabbbcccz : ')
s='aaaabbbcccz'
previous=s[0]
c=1
i=1
output=''
while i<len(s):
    if s[i] == previous:
        c=c+1
    else:
        output=output+str(c)+previous
        previous=s[i]
        c=1
        i=i+1
print(output)

if i==len(s)-1:
    output=output+str(c)+previous
#If this line is not their then it will not show last char.

        
#------- Program for requirement, input a4k3b2 and expected output aeknbd

#input a4k3b2               output aeknbd
s=input('Enter required output like a4k3b2 : ')
s='a4k3b2'
output=''
for ch in s:
    if ch.isalpha():
        output=output+ch
        x=ch
    else:
        d=int(ch)
        newc=chr(ord(x)+d)
        output=output+newc
print(output)

#-----Program to remove duplicate character from the given string -------------#

#input : 'AZZBCDEDEFZZAB'
# First way
s=input('Enter required output like AZZBCDEDEFZZAB : ')
s='AZZBCDEDEFZZAB'
output=''
for ch in s:
    if ch not in output:
        output=output+ch
print(output)

# Second way

s='AZZBCDEDEFZZAB'
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
output=''.join(l)
print(output)

# Third way

s='AZZBCDEDEFZZAB'
s1=set(s)
output=''.join(s1)
print(output)
# Order --> No gurantee at all

#------ Find number of occurrences of each character present in given string with count() ----#

s=input('Enter required output like ABBACBA : ')
s='ABBACBA'
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
print(l)
for ch in l:
    print('{} occurs {} items'.format(ch,s.count(ch)))

#In sorted order
    
s='ABBACBA'
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
print(l)
for ch in sorted(l):
    print('{} occurs {} items'.format(ch,s.count(ch)))

# Second way
s1= set(s)
for ch in sorted(s1):
    print('{} occurs {} items'.format(ch, s.count(ch)))

#-------- Important conclusions about dictionary -------------#

# Third way
#  dict ------ k-v pairs
d={}
d['A']=300
d.get('A')
d.get('Z')   #None
d['B']=200

#.get(k,default key)
print(d.get('A',0))
d={}
d['A']=1
d['B']=2
d['A']=d.get('A',0)+1
print(d)
d={'A':100,'B':200,'C':300}
for k,v in d.items():
    print(k,v)

for k,v in sorted(d.items()):
    print(k,v)

#------- No. of occurrences of each character present in given string without count() -------#

s='ABBACBA'
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
print(d)

for k,v in sorted(d.items()):
    print('{} occurs {} times'.format(k,v))

#-------- Program for the requirement, input : ABAABBCA and expected output : 4A3B1C

s=input('Enter any string like ABAABBCA : ')
s='ABAABBCA'
d={}
output=''
for ch in s:
    d[ch]=d.get(ch,0)+1
for k,v in sorted(d.items()):
    output=output+str(v)+k
print(output)

#------ Program for the requirement, input : ABAABBCA  and expected output : A4B3C1

s=input('Enter any string like ABAABBCA : ')
s='ABAABBCA'
d={}
output=''
for ch in s:
    d[ch]=d.get(ch,0)+1
print(d)
for k,v in d.items():
    output=output+k+str(v)
print(output)

#------ Program to find the number of occurrences of each vowel present in given string -----#

s='DURGASOFTWARE'
v={'a','e','i','o','u','A','E','I','O','U'}
d={}
output=''
for ch in s:
    if ch in v:
        d[ch]=d.get(ch,0)+1
        print(d)
for k,v in sorted(d.items()):
    print('{} occurs {} times'.format(k,v))


#------- Program to check whether the given two strings are anagrams or not --------#

s1=input('Enter first string : ')
s2=input('Enter second string :')
if sorted(s1)==sorted(s2):
    print('Both strings are anagroms')
else:
    print('Strings are not snagrams')

#---- program to chec whether the given string is polindrome or not ---------#

s=input('Enter any string : ')
if s==s[::-1]:
    print('Both strings are anagroms')
else:
    print('Strings are not snagrams')

#----- To generate words from givent input strings by taking character alternatively-----#

s1='abc'
s2='xyz'
s3='123'
i=j=k=0
output=''
while i<len(s1) or j<len(s2) or k<len(s3):
    output =s1[i]+s2[j]+s3[k]
    print(output)
    i=i+1
    j=j+1
    k=k+1
# works only if string has equal length

s1='abcdefg'
s2='xyz'
s3='12345'
i=j=k=0
output=''
while i<len(s1) or j<len(s2) or k<len(s3):
    if i<len(s1):
        output=output+s1[i]
        i=i+1
    if j<len(s2):
        output=output+s2[j]
        j=j+1
    if k<len(s3):
        output=output+s3[k]
        k=k+1
        
print(output)







