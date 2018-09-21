'''
# Basic to advance file and directory commands

Q. To print extention of given file 

f_name = raw_input("Enter a filename and give an extention:")
filename = f_name.split(".")
print "." + filename[-1]

Q. Check whether a file exists    
    
import os.path
open('abc.txt', 'r')
print(os.path.isfile('abc.txt'))    
    
#OR    

from pathlib import Path    
my_file = Path("c:/users/acer/desktop/python/dev_nandan/abc.txt")    
if my_file.is_file():    
    print "file exists"
if my_file.is_dir():    
    print Path
if my_file.exists():    
    print True

Q. To get the file which is currently executing

import os
print("Current File Name :",os.path.realpath(__file__))    

Q. To list all files in a directory in Python
# something wrong in the code

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/c:/python27') if isfile(join('/c:/python27', f))]
print(files_list);

Q. Program to determine profilling of python programs

import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')

Q. To get an absolute path of a file

def absolute_file_path(path_fname): 
        import os
        return os.path.abspath('x') # tells about the current file path       
print("Absolute file path: ",absolute_file_path(""))

Q. Write a program about the time the file created and modified

import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("abc.txt")))
print("Created: %s" % time.ctime(os.path.getctime("abc.txt")))

Q. Sort files by date

import glob
import os

files = glob.glob("*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))

Q. Get a directory listing order by date

from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time

#Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

#all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# regular files, insert creation date
data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))
    
Q. If a file is directory or a normal file

import os  
path="abc.txt"  
if os.path.isdir(path):  
    print("\nIt is a directory")  
elif os.path.isfile(path):  
    print("\nIt is a normal file")  
else:  
    print("It is a special file (socket, FIFO, device file)" )
    
Q. Get the file size

import os
file_size = os.path.getsize("abc.txt")
print"\nThe size of abc.txt is :",file_size,"Bytes"

Q. Retrieve file properties

import os.path
import time

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))

Q. About file

import os.path

for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
    print('File        :', file)
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))

Q. Make a list  from current directory file

import glob
file_list = glob.glob('*.*')
print(file_list)

Q.
'''