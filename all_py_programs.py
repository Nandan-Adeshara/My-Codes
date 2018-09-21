'''
1. printing 1st half of a list on 1 line and 2nd half on next

list = [1,2,3,4,5,6,7,8,9]
print "{}\n{}".format(list[:5],list[5:])

2. importing pi from math

from math import pi
r = input("Enter radius:")
area = pi*r**2 # if import math done then change would be (math.pi * r ** 2)
print area

6. print given date 

exam_date = (11,12,2014)
print "Exam is on %i/%i/%i"%(exam_date)

7. print grid pattern

from __future__ import print_function, division
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()

9. program to calculate days between 2 dates

from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)

10. returning absolute difference if a is lesser than b

a = input("enter A:")
b = input("enter B:")
if a > b:
    diff = a - b
    print "|{} - {}| = {}".format(a,b,diff)
else:
    diff = a - b
    print "|{} - {}| = {}".format(a,b,abs(diff))

13. to get an 'n (non-negative)' copies of a string

s = raw_input("Enter a statement:")
n = len(s)
i = 0
while i < n:
    print s
    i+=1

14. Given num is even or odd

n = input("Enter a num:")
if n%2==0:
    print "{} is even".format(n)
else:
    print "{} is odd".format(n)

Q. To count a specific character from a list/string

def list_count_4(nums): # somewhat len() algo works like this
    count = 0  
    for num in nums:
        if num == 4:
        count = count + 1
    return count

print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))

16. print n copies of string

def substring_copy(str, n):
  flen = 2
  if flen > len(str):
    flen = len(str)
  substr = str[:flen]
  
  result = ""
  for i in range(n):
    result = result + substr
  return result
  
while True:
    m = raw_input("enter string:")
    n =2 if len(m)>= 2 else 3
    print(substring_copy(m,n));

17. whether a passed letter is vowel or not

v = ['a','e','i','o','u']
i = raw_input("Enter a letter:")
flag =False
for p in v:
    if p==i:
        flag = True
        print "%s is a vowel"%i
if flag==False :
    print "%s is not vowel"%i

18. to create num into list
    
a = input("enter a 4 digit num:")
b = str(a)    
c = list(b)
print c
# -- OR --    
a= input("enter a specific chain of num:")
b=str(a)
c =[]
for digit in b:
    c.append(digit)
print c    

19. to create a histogram of a specified num 

a= str(input("enter a specific chain of num:"))
for hist in a:
    print "*"*int(hist)

21. print even num from the list and stop at 237

n = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 
    345,399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
    687, 217,815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831,
    445, 742, 717,958,743, 527]

j =[]
for i in n:
    if i%2==0 and i>237:
        j.append(i)
print j

22. subtract a list from another list & return the common items

list1= ['white','green','red','purple','cyan']
list2 = ['black','green','red']
k =[]
for i in list1:
    for j in list2:
        if i==j:
            k.append(i)

23. program which add no. from the list using 'def'

t = [[1,2],[3],[4,5,6]]
p = [1,2,3,4,5,6]
print sum(p)
# print sum(t) -it will give typeError
def nested_sum(L):
    total = 0  # don't use `sum` as a variable name
    for i in L:
        if isinstance(i, list):  # checks if `i` is a list
            total += nested_sum(i)
        else:
            total += i
    return total
print nested_sum(t)

24. compute gcd of 2 num

def gcd(x, y):
    gcd = 1
    if x % y == 0:
        return y
    
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break  
    return gcd
print(gcd(12, 12))
print(gcd(4, 6))

25. compute lcm of 2 positive num

def lcm(x,y):
    
    if x%2!=0 or y%2!=0:
        return x*y
    if x%y==0 or y%x==0:
        return (x if x>y else y )
        
while True:
    a = input("enter 1st num:")
    b = input("enter 2nd num:")
    print lcm(a,b)

#OR
def lcm(x, y):
   z = (x if x>y else y)

   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1

   return lcm
print(lcm(4, 6))
print(lcm(3,6))    
    
26. sum of 2 num. if sum is between 15-20 print 20   
    
def sum(x,y):
    z = x + y    
    if z >=15 and  z <=20:
        return 20
    else:
        return z

x = input(":")        
y = input(":")
print sum(x,y)    
    
27. print 'true' for 2 nums and their sum or difference is 5    
    
def five(x,y):    
    if x==5 or y==5 or abs(x-y)==5 or (x+y)==5:    
        return True
    else :
        return False
    
print five(1,4)    
    
28. add 2 objects whether str or int or float    
    
def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
         raise TypeError("Hey,Inputs must be integers")
    return a + b

print(add_numbers(10, 20.5))
    
29. to display details in different lines    
    
name = raw_input("enter name:")
age = input("enter age:")    
address = raw_input("enter address:")    
print "{:^9}\n{}\n{}" .format(name,age,address)

30. solve (x+y)**2    

def power(x,y,z):    
    sum = x+y
    res = pow(sum,z)
    return res
    
print power(3,4,2)    
    
31. distance between 2 points (x1,y1) and (x2,y2)
    
from math import sqrt
def dif((x1,y1),(x2,y2)):    
    v_dif = sqrt(abs(x1-x2) + abs(y1-y2))
    return v_dif
print dif((3,5),(5,2))    

33. version is 32bit OR 64 bit     
    
import platform
print platform.architecture()  #returns tuple(bits,linkage)  
#--OR--
import struct    
print struct.calcsize(8*("P"))

34. print os name,platform,release info.

import os,platform
print "{}\n{}\n{} ".format(os.name.upper(),platform.system(),platform.release())

35. to locate site-packages on machine

import site
print site.getsitepackages()

36. program to call an external command in python

from subprocess import call
call(["ls", "-l"])

38. to find num of CPUs being used

import multiprocessing
print(multiprocessing.cpu_count())

39. program to parse a string to float or integer

n = '123.456'
print n
print type(n)
print float(n)        #converts string into float 
print int(float(n))   #converts float into integer

41. to print without newline or space

from __future__ import print_function

n = raw_input("enter your mail user name:")
print (n,end='@')
print ("gmail.com",end='|||||')

print ("Hello",end='World ')
print ("Its",n)

43. to print stderr

from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

eprint("abc", "efg", "xyz", sep="--")

44. to access environment variables

import os
# Access all environment variables 
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable 
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')

45. to get current username

import getpass
print(getpass.getuser())


46. to find local IP address using stdlib

import socket
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
socket.SOCK_DGRAM)]][0][1]]) if l][0][0])



47. to get height and width of console window

def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th

print('Number of columns and Rows: ',terminal_size())



48. program to find execution time for a python method

import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",
sum_of_n_numbers(n))



49. convert height (in feet and inches) to centimeters

#hint = 1 feet = 30.48 cm & 1 feet = 12 inches & 1inch = 2.54cm

def convert(n):
    ht = str(x)
    ht =ht.split('.')
    feet,inch = ht
    ht_cm = (int(feet)*30.48) + (int(inch)*2.54)
    return ht_cm
x = float(input("enter height:"))
print convert(x)


50. calculate hypotenuse of right angle triangle

from math import sqrt

def hypotenuse(x,y):
    res = sqrt((x**2)+(y**2))    
    return res

x = input("enter a side:")
y = input("enter another side:")
print hypotenuse(x,y)



51. to convert distance (in feet ) into inches , yards and miles

#hint: 1 feet = 0.33 yard , 1 mile = 5280 feet


def dist(n):
    list = n*[12,.33,.0001893]
    inch,yard,mile = list
    return "{} feet = {} inches\n{} feet = {} yards\n{} feet = {} miles".format(n,inch,n,yard,n,mile)

x = input("enter in 'feet':")
print dist(x)


52. sum first n num

def sum(n):
    res = (n*(n+1))/2
    return res

x = input("enter a no:")    
print sum(x)


54. sum of 1st n positive num

def sum(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

x = input("enter a positive num:")
print sum(x)


56.  calculate 'body mass index'

def bmi(x,y):
    if x < 10:
        x = str(x)
        x = x.split('.')
        x = (float(x[0]) * 30.48) + (float(x[1]) * 2.54)
        x = (x/100)**2
    else : pass
    
    #print y
    #print x
    #print bmi
    bmi = y/(x)
    if bmi <= 18:
        return "your bmi is %.2f . It indicates that you are underweight" %bmi
    elif bmi > 18 and bmi <=24:
        return "your bmi is %.2f . It indicates that you are normal weight" %bmi
    elif bmi > 24 and bmi<=30:
        return "your bmi is %.2f. It indicates that you are overweight" %bmi
    elif bmi>30:
        return  "your bmi is %.2f. It indicates that you are obese" %bmi
    else: pass    
    
a,b = [float(input("enter your height:")),input("enter your weight in 'kgs':")]
print bmi(a,b)


57. program to calc sum of digits in an integer 

a = list(str(input("enter a num:")))
sum = 0
for i in a:
    sum += int(i)
print "print sum of the num is :",sum



58. to sort 3 num without loops and conditional operators

print 'give 3 nums'
a,b,c = [input(":"),input(":"),input(":")]
list = [a,b,c]
print sorted(list)

61. program to get details of module

import math # module_name
print dir(math)


62. program to hash a word

soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
 
word=raw_input("Input the word be hashed: ")
 
word=word.upper()
 
coded=word[0]
 
for a in word[1:len(word)]:
    i=65-ord(a)
    coded=coded+str(soundex[i])

print("The coded word is: "+coded)



63. copyright info about python

import sys
print("\nPython Copyright Information")
print(sys.copyright)
print()



64. program to get cmd line arguments passed to script

import sys

print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))



65. whether platform is big/little endian

import sys
if sys.byteorder == "little":
    #intel, alpha
    print("Little-endian platform.")
else:
    #motorola, sparc
    print("Big-endian platform.")


66. find all built-in modules

import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))


67. get size of an object

import sys
str1 = "one"
str2 = "four"
str3 = "three"

print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes")
print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes")
print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes")


69. to get current recurssion limit

import sys
print"Current value of the recursion limit:",sys.getrecursionlimit()


70. to count specified letters

s = "The quick brown fox jumps over the lazy dog."
print s.count("o")


72. get the ASCII value of a character

print(ord('a'))
print(ord('A'))
print(ord('1'))
print(ord('@'))


74. swapping 2 variables

a,b = 10,20
a,b = b,a
print a,b


75. if a num is +ve,-ve or zero

a,p,n,z = [float(input('Enter any num:')),'+ve','-ve','0']# this list is taken because the next line gives error
#num = [print '+ve' if a> 0 else [print "-ve" if a<0 else print '0']]
num = [p if a> 0 else [n if a<0 else z]]
print num


76. access and print a URL's content to the console & get system command output

from http.client import HTTPConnection
conn = HTTPConnection("example.com")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)


import subprocess
# file and directory listing
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
print("dir command to list file and directory")
print(returned_text)

77. divide  a path on extension specifier

import os.path
for path in [ 'test.txt', 'filename', '/user/system/test.txt', '/', '' ]:
    print('"%s" :' % path, os.path.splitext(path))


78. convert time hour to sec
    
def conTime(x,y,z):
    a,b = [x * 3600,y*60]
    h_s = a + b + z
    return "{} hour {} min {} sec = {} sec".format(x,y,z,h_s)
    

a,b,c=[ input("enter in 'hour':"),input("\nEnter in 'min':"),input("\nenter in sec:") ]    
print conTime(a,b,c)

def conTime(time):
    # to convert sec into hr min sec
    hr,min,sec = [time/3600,((time%3600)/60),((time%3600)%60)]
    return "{} sec = {} hr {} min {} sec".format(time,hr,min,sec)

print conTime(3661)


82. print unicode char

str = u'\u0050\u0079\u0074\u0068\u006f\u006e\u0045\u0078\u0065\u0072\u0063\
\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\
\u0065\u0073\u006f\u0075\u0072\u0063\u0065'

print(str)


83. largest and smallest size of a float and integer

import sys
print("Float value information: ",sys.float_info)
print("\nMaximum size of an integer: ",sys.maxsize) 


84. to count nums in a list

import collections
num = [2,2,4,6,6,8,6,10,2,4,4]
print(sum(collections.Counter(num)))


85. get module object for an given object

from inspect import getmodule
from math import sqrt
print(getmodule(sqrt))


86. check if value is in 64 bit 

int_val = 30
if int_val.bit_length() <= 63:
    print((-2 ** 63).bit_length())
    print((2 ** 63).bit_length())

89. use double quotes to display strings

import json
print json.dumps({"alexa":1,"amigo":2})


90. split a variable length into variable

var_list = [100, 20.25]
x, y, b = (var_list + [None] * 1)[:3]
print(x, y, b)



91. calculate time runs of a program

from timeit import default_timer
def timer(n):
    start = default_timer()
    # some code here
    for row in range(0,n):
        print(row)
    print(default_timer() - start)

timer(5)
timer(15)


92. valid an IP 

import socket
addr = '127.0.0.01'
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")


93. convert an integer into binary keeping leading zeroes

x = 12
print(format(x, '08b'))
print(format(x, '010b'))
x = 30
print(format(x, '02x')) # decimal to hexadecimal
x = 4
print(format(x, '02x')) # decimal to hexadecimal


94. platform info.

import os, platform
print("Operating system name:")
print(os.name)
print("Platform name:")
print(platform.system())
print("Platform release:")
print(platform.release())


95. Find max and min from list of numbers

def max_min(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))

a,b = [input("Enter numerator:"),input("Enter denomenator:")]

if b == 0:
    print "\nZero Division error. Denomenator should not be '0' "
elif a == 0:
    print "0 as numerator is 0"
else:
    if a%b == 0:
        print "{}/{} = {}".format(a,b,a/b)
    else:
        zero = '0'
        sig_fig = []
        rem = str(a%b) + str(0)
        recur_div = int(rem)/b 
        
        print "{}/{} = {}".format(a,b,str(a/b) + '.'+ str(recursion))   

96. Masking a password into asterisk

import getpass

key = getpass.getpass("Password :: ")
print key


97. Finding GCD of 2 num

''' 
def gcd(num=None,denom=None): 

    if num == None or denom == None: # no None entry should be accepted
        return "Please provide Numerator and Denominator"
    elif denom == 0:
        return "Cannot Divide with 0 Denominator"
    elif num == 0:
        return 0
    elif num%denom==0:
        return denom
    else:
        result = num % denom
        num = denom
        denom = result
        return gcd(num,denom)

print gcd(36,10)
