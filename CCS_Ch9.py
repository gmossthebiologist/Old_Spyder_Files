# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 13:45:12 2021

@author: MOSS
"""

'''


A common programming task is to get input from a file using the open() function.
Open() requires a single argument that specifies the path to the file
(e.g. open('myfile.txt'). Full path names can also be specified: open('C:\\Users\\BWayne\\tax_return.txt')
file.close() closes the file, not allowing anymore reads or writes.
file.read() returns a file's contents as a string. file.readlines() returns a list of strings,
where the first element is the contents of the first string, and so on. (Both methods
can be given an optional argument that specifies the number of bytes to read from the file.
Each method also stops reading at the end-of-file (EOF). file.readline() returns
a single line at a time (useful for dealing with large files where its entire contents
may not fit in available system memory).

Iterating over the lines of a file is supported by for ... in ... syntax

file.write() writes a string argument to a file.

To write integers and floats, you must convert them to a string using str() first,
as write() only supports string arguments.

When writing to a file, the mode of the file must be explicity set in the open()
function call. A mode indicates how a file is opened, whether or not writing to the
file is allowed, if existing contents of the file are overwritten or appended, etc.
Most used modes:
    'r' (read)
    'w' (write)
    'a' (opens file for appending)

The mode is specifed as the second argument in a call to open() (e.g. open('myfile.txt', 'w') opens the file for writing)
If mode isn't specified, the default is 'r'

Mode	Description	         Allow read?	Allow write?	Create missing file?	Overwrite file?

'r'	Open the file for reading.	Yes	            No	                No	                  No

'w'	Open the file for writing. 
    If file does not exist then 
    the file is created.
    Contents of an existing 
    file are overwritten.	     No	          Yes	               Yes	                 Yes

'a'	Open the file for appending. 
    If file does not exist then 
    the file is created. Writes 
    are added to end of existing 
    file contents.	            No	          Yes	               Yes	                  No
    
Also, you can add a '+' at the end of a mode (like 'r+' and 'w+') to specify an
update mode, which allows for both reading and writing.

Output to a file is buffered by the interpreter before being written to the computer's 
hard disk. By default, data is line-buffered, e.g., data is written to disk only when a 
newline character is output. Thus, there may be a delay between a call of write() and that 
data actually being written to the disk.

You can toggle buffering on/off or specify a buffer size with the optional buffering
argument to the open() function. 0 disables buffering (valid only for binary files),
1 enables the default line buffering, and >1 sets a specific buffer size in bytes.
For example, f = open('myfile.txt', 'w', buffering=100) will write the output buffer
to disk every 100 bytes.

The flush() file method can be called to force the interpreter to flush the output 
buffer to disk. Also, the os.fsync() function may have to be called on some operating systems.
Closing an open file also flushed the output buffer.


A program commonly needs to interact with comp's file system. Since the OS controls
the file system, a program must use functions supplied by the OS itself to interact with
files. The os module provides an interface to OS function calls.

Be sure to consider the portability of a program across different OSs. Portability
must be considered when reading and writing files outside the executing program's
directory since file path representations often differ b/w OSs. For example,
"subdir\\bat_mobile.jpg" on Windows vs "subdir/bat_mobile.jpg" on Mac. The character
b/w directories (the '\\' or '/') is called the path separator.

A common error is reducing portability by hardcoding file paths as string literals
with OS specific path separators. To reduce these errors, use the os.path module,
which contains many portable functions for handling file paths. One of the most useful
is os.path.join(), which concatenates the arguments using the correct path separator
for the current OS. Instead of writing

path = "subdir\\bat_mobile.jpg",

use

path = os.path.join('subdir', 'bat_mobile.jpg')

which will asjust the path separators automatically depending on the OS being used.

On Windows systems, when using os.path.join() with a full path such that the first 
argument is a drive letter (e.g., 'C:' or 'D:'), the separator must be included 
with the drive letter. For example, os.path.join('C:\\', 'subdir1', 'myfile.txt') 
returns the string "C:\\subdir1\\myfile.txt".


The inverse operation, splitting a path into individual tokens, can be done using 
the str.split() method. Ex: tokens = 'C:\\Users\\BWayne\\tax_return.txt'.split(os.path.sep) 
returns ['C:', 'Users', 'BWayne', 'tax_return.txt']. os.path.sep stores the path separator for 
the current operating system.


Other os and os.path modules:

    
os.path.split(path) – Splits a path into a 2-tuple (head, tail), where tail is the last token in 
the path string and head is everything else.

import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
print(os.path.split(p))


os.path.exists(path) – Returns True if path exists, else returns False

import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
if os.path.exists(p):
    print('Suit up...')
else:
    print('The Lamborghini then?')


os.path.isfile(path) – Returns True if path is an existing file, and false otherwise 
(e.g., path is a directory).

import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'bat_chopper')
if os.path.isfile(p):
    print('Found a file...')
else:
    print('Not a file...')


os.path.getsize(path) – Returns the size in bytes of path.

import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
print('Size of file:', os.path.getsize(p), 'bytes')


A common task is to check every file and/or subdirectory of a specific part of the
file system. The os.walk() function 'walks' a directory tree like the one above,
visiting each subdirectory in the specified path.

e.g. of how to walk a directory tree

import os

year = input('Enter year: ')
path = os.path.join('logs', year)
print()

for dirname, subdirs, files in os.walk(path):
    print(dirname, 'contains subdirectories:', subdirs, end=' ')
    print('and the files:', files)



Some files are stored as binary data (such as pdf, images, and videos).
A bytes object is used to represent a sequence of single byte values. They're immutable.
bytes() creates a byte object:
    
bytes('A text string', 'ascii') – creates a sequence of bytes by encoding the string using ASCII.
bytes(100) – creates a sequence of 100 bytes whose values are all 0.
bytes([12, 15, 20]) – creates a sequence of 3 bytes with values from the list.

Or, you can create a bytes literal by adding a b prior to the opening quote:

my_bytes = b'This is a bytes literal'


Programs can access files using a binary file mode by adding 'b' to the end of the
mode string used in open() (e.g. open('myfile.txt', 'rb')). When using binary file mode
on Windows, newline characters \n in the file are not automatically mapped to the
Windows format \r\n. In normal text mode python makes this translation automatically
When a file is opened in binary mode, the file.read() method returns a bytes object
instead of a string. Also, file.write() expects a bytes argument.


a .bmp file contains binary data in a format called a bitmap. Opening and reading the 
file with a binary mode creates a new bytes object made of the exact sequence of
bytes found in the file's contents. Opening and reading it with a binary mode creates
a new bytes object consisting of the exact sequence of bytes found in the file's contents.


The struct module is a module for packing values into sequences fo bytes and unpacking
sequences of bytes into values (like strings and integers). The struct.pack() function
packs values such as strings and integers into sequences of byes. (e.g. struct.pack('>h', 5))
The first argument to struct.pack() is a format string that describes how the following
arguments should be converted into bytes. The '<' character indicates the bytes-order,
or endianness, of the conversion, which determines whether the most or least significant
byte is placed first in the byte sequence. '>' places the most significant byte first (big-endian)
and '<' sets the least first. The 'h' character in the format string describes the type
of the object being converted (which importantly determines how many bytes are being used when packing the value)
'h' describes the value being converted as a 2-byte integer (other common format characters are
'b' for 1-byte integer, 'I' for a 4-byte integer, and 's' for a string). The struct.unpack()
module performs the reverse of struct.pack(), unpacking a sequence of bytes into a new object.
Unpacking always returns a tuple with the results, even if only unpacking a single value.




The location of an input or output file may not be known before writing a program. Instead you
can use command line arguments to allow yourself to specify the location of an input file
as shown in the following program. Assume two text files 'myfile1.txt' and 'myfile2.txt'
exist.

import sys
import os

if len(sys.argv) != 2:
    print('Usage: {} input_file'.format(sys.argv[0]))
    sys.exit(1)  # 1 indicates error

print('Opening file {}.'.format(sys.argv[1]))

if not os.path.exists(sys.argv[1]):  # Make sure file exists
    print('File does not exist.')
    sys.exit(1)  # 1 indicates error

f = open(sys.argv[1], 'r')

# Input files should contain two integers on separate lines

print('Reading two integers.')
num1 = int(f.readline())
num2 = int(f.readline())

print('Closing file {}'.format(sys.argv[1]))
f.close()  # Done with the file, so close it

print('\nnum1: {}'.format(num1))
print('num2: {}'.format(num2))
print('num1 + num2: {}'.format(num1 + num2))



A with statement can be used to open a file, executre a block of statements, and
automatically close the file when complete. 


'''

