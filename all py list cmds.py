'''
List Basics:
    dir(function,method,attribute),help(function)
    builtins.__doc__ # it helps about the builtins parameters and arguments
    append(),insert() # adds elements by index and/or name
    remove(),pop(),del() # deletes element by index or name
    index() # returns index of an element
    list comprehension, and list slicing 
    in # returns True/False if element in list
    type() # returns datatype of the variable
    enumerate(), zip() # are used to unpack elements of lists (generally) in for loop
    sort() # to permanently sort elements of the list
    len() # returns length of the list. it counts num of items inside list (not commas)
    count() # returns how many times the item is in the list
    tuple unpacking of values
    basic arithmetic operations on list (sum() , min() , max())
    isinstance(object,type) # returns True if obj is of provided type
'''

'''
# Basic to advance list commands
 
Q. Some Basic list operation

t =['e','a','b','c']
t.append('d')

t1 = [1,2,3]
print t
t.extend(t1)
print t
t.sort()
print t

print 'e' in t

t = [ 1,2,3,4 ]
p = [3,4,5,6 ]
p.insert(3,100) # insert takes position and element to be added, if position exceeds index it will add at the end
print t or p # 1,2,3,4
print p or t # 3,4,5,6
print t and p # 3,4,5,6 which is equal to [p or t]

t[:] = [1,2,3,4,5,6,7,8,9]
print t

print ("hi  my name is Nandan".split())

#list comprehension
cubes = [i**3 for i in range(4)]
a = [i for i in range(20) if i%3==0]
print cubes,a

list = ['a','b','c']
list.remove('a') # remove method takes 1 argument and removes the element passed
# 0 is the 1st element of the list and 3 indicates that it will print till the 
# 3rd element (list starts with 0,1,2,3) therefore 3rd element is on 4th place
# 2 indicates that it will skip 2 places
print list[0:3:2]  #[] in python is used to call the elements from the list

print ('a' in list) # will say whether a is in the list or not

# to append an item
list.append(2)
print list

# deleting an item using index and pop command
print list.index('c') # show the item position
list.pop(2)  # deletes the given position item
print list

# using insert you can add an item at any position
list.insert(2,'c')
print list

l_t = [1,2,3,],2 # continuing after a list will make a list into tuple
print type(l_t)

a = range(0,100,2) # printing even no. from o to 100
b= range(1,100,2)  # printing odd no. from 0 to 100
print a,b

Q. printing first and last name of user in reverse order

a = raw_input("Enter name and lastname:")
print a[::-1]

Q. display first and last no. from the given list
 
list = ["green","white","purple","red"]
print "{} {}".format(list[0],list[-1])

Q Use of enumerate and zip
'''
x_list = [1,2,3]
y_list = ['amdavad','pune','rajkot']

for i,j in zip(x_list,y_list):
	print i,j

cities = ['amdavad','pune','rajkot','hyderabad']

for p,city in enumerate(cities):
	print p,city