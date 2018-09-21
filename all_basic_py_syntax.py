'''
1. Importing keyword list

import keyword
print keyword.kwlist

2.printing a statement!  
print "Hello World!!" 

# if your statement is big you can use 'escape char' to continue in next line
print "Hi this statement is the first line statement\
 Next line will be continue but in program it is written below the first\
 using 'escape character'"

# print multiline statement
print (""" hi
    my name is nandan """)

3. Datatypes
import os
a = 10
b = 'a'
c = [1,2,3]
d = {1:'a',2:'b','c':3}
e = (4+1j)
f=2.11
print type(set('g'))
print type(a)
print type(b)
print type(c)
print type(d)
print type(e)
print type(f)
print type(os)
 
4. operations on 2 no. 
a = 10
b = 9
# print 2 no.
print a,"\n",b # '\n' is an new line character
# add 2 no.
print "Add is ",a+b
# sub 2 no.
print "Sub is ",a-b
# multiply 2 no.
print "Multiply is ",a*b
# div 2 no.
print "Div is ",float(a)/b

5. To print random no.
import random
print random.randint(97,99)

6. To clear the screen

import os,time
print 1  #--this will not print because the next line will clear the screen
os.system('cls') # system('ls') can also be used
time.sleep(2) # the interpreter will get inactive for '2 secs'

print 1  #--this will print because the next line doesn't has clear cmd

7. Taking input and printing it!

a = input("Enter  no.:") # input will accept only numeric input
b = raw_input("Enter string:") # raw_input will accepts any type of input

print a,b

8. Some Escape characters
\n--new line character
\t--tab [4 spaces]
\ --to continue the statement on next line 
\b--backspace character; i.e. removes 1 character before it
\" \'--adds double and single quotes respectively
print "Hi!\nMy name is nandan.\bIt is hard to fuck.\tBut not for me\
        this is \"special\". and i know it\ but, what But?\n\
        \rand follow your dream "

12. To get info about the python version using

import sys
print sys.version  # system version
print sys.version_info # version info

13. datetime module

import time 
import datetime
# with the help of dir() and help() we can dig into the module's method and attributes
print time.time()  # time since epoch
print datetime.datetime.now()
print datetime.date.today().strftime("%Y") # current year
print datetime.date.today().strftime("%B") # month of year 
print datetime.date.today().strftime("%W") # week num of the year
print datetime.date.today().strftime("%w") # week day of the week
print datetime.date.today().strftime("%j") # day of the year
print datetime.date.today().strftime("%d") # day of the month
print datetime.date.today().strftime("%A") # day of week / a could be small 

16 . difference between input and raw_input

a = input("Enter any num:")
b= raw_input("Enter a statement:")
# input only takes digits and numbers
# raw_input takes characters, letters and alphanumerics
# while concatenating a and b; a might give error as a is not converted to string
print a + b

17. print info related to built functions

print abs.__doc__
print input.__doc__

18. using calender module; print calender of the given month

import calendar
y = input("Enter current year:")
m = input("Enter current month:")
print calendar.month(y,m)

20. pip syntax - pip is used to install 3 party libraries on the machine

# before installing the libs, see the libs on the PyPI(python package installer)
#pip install [library name]

21. zen of python

import this  #- command for zen of python, indicated 20 lines which are directly/
#              indirectlly associated with this language

22. ternary operators

a = 7
b =1 if a>7 else 42

23. tuple unpacking

t = [1,2,3,4,5]
a,b,c,d,e = t
#x,y,*z = t -- it will assign rest items to z, but this function does not work 
#                in 2.7

24. to print unique items from the list

k = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]
print list(set(k)) #'set' keeps only unique items in its database

25. how to take multiple input on the same line

a,b,c = [input(":"),raw_input(":"),5]
print a,b,c 

26. to check location/identity of an object

obj = 10
a =10 
print id(obj),id(a)

27. print the current call stack

import traceback
traceback.print_stack()

28. special characters used within the language

s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
# | here is used to add/union 2 sets items
print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )


29. print system time
#Note : The system time is important for debugging, network information, 
#       random number seeds, or something as simple as program performance.

import time
print time.ctime()

30. get name on which the host is running

import socket
host_name = socket.gethostname()
print host_name

31. basic lambda function (anonymous function)

g = lambda x: x+3
print g(1)

a = lambda x,y : x * y
print a(g(2),g(3))

def make_incrementor (n): return lambda x: x + n

f = make_incrementor(2)
g = make_incrementor(6)

print f(42), g(42)
#44 48

print make_incrementor(22)(33)
#55

32. basic try & except 

try:
    a = input("enter a num:")
except NameError:
    print "Input a no. instead a string"

33. empty a variable without destroying it

n = 20
d = {"x":200}
l = [1,3,5]
t= (5,7,8)
print(type(n)(5))
print(type(d)())
print(type(l)())
print(type(t)()) 

34. basic dictionary commands

d = {1:'green',2:'red',3:'blue'}
k1,k2,k3 = d.keys()
v1,v2,v3 = d.values()
item = d.items()
print "example of Key:",k1,"\nexample of value:",v2,"\nexample of items:",item

35. convert 'True' to 1 and "False" to 0

x = 'true'
print int(x=='true')
x = 'false'
print int(x == 'False')

36.
'''