# -*- coding: utf-8 -*-


#------------------------------ Section - 17 -------------------------------------#
#(27th-Aug-2021)

#----------------------------- Python Packages ----------------------------#

#----------- Basic Review of Function and Modules -------------------#

# code reusibility
# Module is a group of variables, functions, classes, group of functions

#----------------------------
developer= 'Durga'
location='Hbd'
def add(a,b):
    print('The sum :',a+b)

class Test:
    pass
#----------------------------
# durgacalc.py

#----------- Introduction to python Packages ------------------#

# Basic java package   core java+ Advance Java + oracle
# A group of related items ==> package
#loan app  account.py, customer.py, process.py

#---- It is encapsulasation mechanism
# __init__.py  ---> compulsary
# after Python 3.3 this file is not mandatory

# Package can contain sub-package also

# A collection of related modules into a single unit is nothing but package.
# Package is an encapsulation mechanism to group related modules into a single unit.
# Package is simply forlder or directory
# Package contains a group of related modules and sub packages also.

#----------- Advantage of Packages --------------#

#1. Naming Conflicts resolved
#2. Unique identification
#3. Modularity improved
#4. Readability improved
#5. Maintainability improved

#--------- Demo programs to cteate and use packages ---------------#

# module1.py
def f1():
    print('This is from f1 function')

# test.py
import pack1.module1
pack1.module1.f1()

from pack1.module1 import f1
f1()

#---------- Importance of __init__.py file

# At the time of using a package if we want to perform any activity automatically
 #then we have to define any activity automatically then we have to define that 
 # activity inside this __init__.py file.
# hence, __init__.py file meant for initialization activity

# Relationship : Function, Module, package and Library

# Functions contains a group of repeatedly required lines of code
# Module contains a group of repeatedly required functions.
# Package contains a group of related modules(sub-pkgs)
# Library contains a group of related packages.

#--------- Need of Installing a Python Package ---------------#

from pattern.shapes import *
squres()

# If we want to use a package, cumpulsory it should be available in the current working directory
# we cannot use from anywhere in our system
# To make package available through out our system, then we have to install package.

#------------- How to install a python package --------------#

from setuptools import setup
setup(name='patterns',version='.1',packages=['patterns'])
#pip install .
# we have to write setup.py file. which is also known as setup script.
# we have to use setup() fn. from setuptools module.

#pip install django
#pip install pymysql











































































































