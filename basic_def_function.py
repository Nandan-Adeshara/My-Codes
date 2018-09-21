'''
Function Defining Basics:
    Argument,parameter
    positional and keyword argument
    num of single and keyword arbitrary argument
    modules and function and alias
    recurssion
    local and global scope    
'''

# All about functions

# function have arguments(information provided to a function) and parameters(info. received by the function)
# arguments are of 2 types - postional arguments and keyword arguments

def person(first,last):
    return "First name is "+first+" ,Last name is "+last

# positional argument
print person('nandan','adeshara')
# keyword argument
print person(last='adeshara',first = 'nandan')

# passing arbitrary num of arguments and arbitrary num of keyword argument

def pizza(size,*toppings):
    print "Size of Pizza is " + size
    print "Toppings : "
    for tops in toppings:
        print "- " + tops

# arbitrary arguments will always be at the end of function definition

# arbitrary arguments
pizza('small','cheese')
pizza('medium','cheese','onion','tomato')
pizza('large','paneer',"cheese",'patato')

def person(first,last,**info):
    per = {'1First Name':first,"2Last Name":last}
    print "Person info:"

    for k,v in info.items():
        per[k] = v

    print per
# passing arbitrary keyword arguments
person('nandan','adeshara',hobbies=['swim','coding'],eats='pure Veg')


# About MODULES
# Module is a special file which contains functions and methods.
# if we import a module it should be in the same directory as the main file

'''
# Eg. understand it as a 'pizza.py' file

def make_pizza(size,*toppings):
    print "Size is "+size
    print "Toppins:"
    for tops in toppings:
        print "- "+tops


# Step 2. understand a new file named a 'making_pizza.py'

# import file

import pizza # importing above pizza file will create a pizza.pyc(compiled file)

pizza.make_pizza('small','cheese','paneer')

# importing a specific function [ only specific function will be allowed to be used, used to minimize space complexity by not importing all functions]

from pizza import make_pizza

make_pizza('medium','cheese','tamoto') # no need to write pizza.make_pizza

# giving module an alias

import pizza as p

p.make_pizza('large','pure Veg')

# giving function as alias

from pizza import make_pizza as mp

mp('small')
'''

# defining a function and calling it from outside of another function
print '------------------------'
def a():
    print "fn: a printed"
def b():
    print "fn: b printed"
def c():
    print "fn: c printed"
def d():
    print "fn: d printed"

def do_twice(x,y,z):
    print "hello"
    #f()   gives error as 'f' not defined
    b()
    #p()   gives error as 'p' not defined
    c()
    #r()    gives error as 'r' not defined
    a()
    d()
    z() # z = a
    y() # y = c
    x() # x = b
    print "hello"

do_twice(b,c,a) # if fn: a,b,c,d were defined below this cmd then it will give name Error

print '---------------'
# example of recursion program (function calling itself)

def countdown(n):
    if n<0:
        print "Blastofff!!"
    else:
        print n
        countdown(n-1)

countdown(10)

# better example of def
# return is used to print the function called and end the function
# anything after return is consider 'dead code'
def b(z):
    prod = a(z,z)
    print (z,prod)
    return prod 
    
def a(x,y):
    x = x+1
    return x*y
    
def c(x,y,z):
    total = x + y + z
    square = b(total)**2
    return square 
    
x = 1
y = x+1
print c(x,y+3,x+y) # ans is (9,90) & 8100