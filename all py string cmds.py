'''
Basic String Func:
    unlike list slicing, string slicing also works but has different ways.
    split() # converts string into list. Also breaks string using separator.
    endswith(),startswith()  # checks wheather provided string endswith or startswith provided argument
    upper(),lower() # to change word to lower or upper accordingly
    len() # returns length. it counts num of items between 2 appostropes (i.e. elements and commas)
    count() # returns how many times the item is in the string
    tuple unpacking of values
    string formating # i.e. % and {}.format
    join() # joins strings. Doesn't work on integer join
    rjust(),ljust() # takes 2 argument and justifies the string in left or right way.

'''

'''
# All String Basic to advance functions 
Q. To print a string in reversed format

a = raw_input("Enter something:")
print a[::-1]

Q. Basic string function

word = 'baNanA'
print sorted(word)
print word.upper() 
print word.lower()
print word.find('na',3,6) # 3 for starting pt and 6 for end pt
print len(word)
print word.count('a') # counts how many times 'a' has occured
print word[1:5]

a = ["nandan",'adeshara','dhirenbhai']
print len(a)
b,c,d = a
print b,c,d
#string format works for len greater than len of string
print "%7s"%b
print "%8s"%b
print "%9s"%b
print "%.4s"%b # prints 1st four items in string
print "%37s"%a
print "%10.2s\n%2s"%(a,'1')
print "%+d"%(7)

print "{} {}".format(1,2)
print "{1} {0}".format(1,2) # 1,0 indicates index position of formatting 
print "{:>10}".format('test')
print "{:_>10}".format("test")
print "{:_<10}".format("test")
print "{:_^10}".format("test")
print "{:10.5} {}".format('xylophone',"hi")
print "{:d}".format(3)
print "{:f}".format(3.212)
print "{:+d}".format(4

s = 'nandan is best'
for str in s:
    print str
print list(s)
print tuple(s) 

list = ['n','a','n','d','a','n']
str = ''
print str.join(list)  

Q. To return string with 'is' added in front to it

def is_string(str):
    if str[0:2] == 'is':
        return "string '{}'".format(n)
    else:
        return "New string is 'IS{}'".format(n)

n = raw_input("enter a string:")        
print is_string(n)

Q. Some of the string operation cases

def any_lowercase1(s): # checks for any lowercase char
    for c in s:
        if c.islower():
            return True
        else:
            return False
            
def any_lowercase2(s): # checks for lowercase 'c'
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s): # checks for first 'c' to be lowercase or not
    for c in s:
        flag = c.islower()
        return flag
        
def any_lowercase4(s): # checks from all 'c' to be lowercase or not
    flag=False
    for c in s:
        flag = flag or c.islower()
    return flag
    
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
        else:
            return True
            
s = 'NCnancdanNanDaNC'
print any_lowercase1(s)
print any_lowercase2(s)
print any_lowercase3(s)
print any_lowercase4(s)
print any_lowercase5(s)

Q. Concat N strings

list_of_colors = ['Red', 'White', 'Black']  
colors = '-'.join(list_of_colors)

print("All Colors: "+colors)

Q. Check if any lowercase letters in the string

str1 = 'A8238i823acdeOUEI'
print(any(c.islower() for c in str1))


Q. Adding leading zeros to a string

str1='122.22'
print("Original String: ",str1)
str1 = str1.ljust(8, '0')
print(str1)
str1 = str1.rjust(10, '0')
print(str1)

Q. To count a specific character from a list/string

s = 'nandan'
print "'%s'"%s
c=raw_input("enter character to count from above string:")
a = s.count(c,0,5) # 0 and 5 are starting and ending points
 
print "char '{}' is repeated {} times".format(c,a)

Q. To concetenate all elements of a list into a string and return it
(syntax for join)

list = ['n','a','n','d','a','n']
str = ''
print str.join(list)

print ("Hi Supp" .startswith("Hi"))
print ("Hi Supp" .endswith("Hupp"))