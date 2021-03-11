# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:41:20 2021

@author: MOSS
"""

'''

To gain access to a specific string character, you use its index:

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alphabet[0], alphabet[1], alphabet[25])

a negative index will start from the right

'''

'''

string are immutable, you cannot change them once they are created. Instead
you must reassign the variable to the string you want to change it to

alphabet = 'abcde...'

alphabet[0] = 'A' #Will not work

alphabet = 'ABCDE...'

'''


'''

Strings are able to be concatenated. (this does not violate immutability b/c
                                      you're really just creating a new
                                      variable.')
                                      
n = 'New'
y = 'York'

NY = n + y

'''

'''

Lists are a mutable type

list_1 = [1, 2, 3]

list_1[0] = 4

'''

'''
Methods instruct objects to perform actions. You execute
one by specifying the object and followed by .method()

e.g. my_list.append('abc')

list.append(value): adds a value to the end of a list
list.pop(i): removes the element at index i from list
list.remove(v): removes the first element whose value is v

'''

'''
len(list)	Find the length of the list.
list1 + list2	Produce a new list by concatenating list2 to the end of list1.
min(list)	Find the element in list with the smallest value.
max(list)	Find the element in list with the largest value.
sum(list)	Find the sum of all elements of a list (numbers only).
list.index(val)	Find the index of the first element in list whose value matches val.
list.count(val)	Count the number of occurrences of the value val in list.

These are examples of sequence-type functions that act on 
sequences like lists and strings
'''

'''
A tuple is just like a list except it's immutable and 
is denoted by var = (tuple values). It supports len, indexing
sequence type function, and is a sequence in itself.
'''

'''
Some useful functions and methods for lists:
    len(list)	Find the length of the list.
list1 + list2	Produce a new list by concatenating list2 to the end of list1.
min(list)	Find the element in list with the smallest value.
max(list)	Find the element in list with the largest value.
sum(list)	Find the sum of all elements of a list (numbers only).
list.index(val)	Find the index of the first element in list whose value matches val.
list.count(val)	Count the number of occurrences of the value val in list.
'''

sample_tuple = (5, 3, 4)
print(sample_tuple) #printing a tuple always prints parantheses

'''
A tuple is like a list except it is immutable. It supports list and method functions.
Its notation is different () instead of []. Tuples are typically used when element
position, not just the ordering of elements, is important (e.g (x,y) coordinates).
'''

'''
A named tuple allows you to make a tuple with named attributes.
For example, [make, model, year,]. namedtuple must be imported.
Once imported, create the named tuple.

e.g.

from collections import namedtuple

Car = namedtuple('Car', ['make', 'model', 'price', 'horsepower', 'seats']) #creating the named tuple

chevy_blazer = Car('Chevrolet', 'Blazer', 32000, 275, 8)
print(chevy_blazer)

'''

from collections import namedtuple

Car = namedtuple('Carrrrr', ['make', 'model', 'price', 'horsepower', 'seats']) #creating the named tuple

chevy_blazer = Car('Chevrolet', 'Blazer', 32000, 275, 8)
print(chevy_blazer)

'''

A set is an unorderd collection of unique elements, elements do not have
a position or index, and no elements share the same value.

A set can be created using set(), which accepts sequence-type iterable objects
(list, tuple, string, etc) whose elements are inserted into the set. A set literal
can be made using { } with commas separating set elements. (An empty set can only be made using set())

nums1 = set([1, 2, 3])
nums2 = {7, 8, 9}

Sets are often used to reduce a list of items that may contain duplicates into a collection of unique values
Passing a list into set() will cause any duplicates to be omitted.

# Initial list contains some duplicate values
first_names = [ 'Harry', 'Hermione', 'Ron', 'Harry', 'Albus', 'Ron', 'Ron' ]

# Creating a set removes any duplicate values
names_set = set(first_names)

print(names_set)

Set functions:
    
    len(set)	Find the length (number of elements) of the set.
set1.update(set2)	Adds the elements in set2 to set1.
set.add(value)	Adds value into the set.
set.remove(value)	Removes value from the set. Raises KeyError if value is not found.
set.pop()	Removes a random element from the set.
set.clear()	Clears all elements from the set.

Set theory functions:
    
    set.intersection(set_a, set_b, set_c...)	Returns a new set containing only the elements in common between set and all provided sets.
set.union(set_a, set_b, set_c...)	Returns a new set containing all of the unique elements in all sets.
set.difference(set_a, set_b, set_c...)	Returns a set containing only the elements of set that are not found in any of the provided sets.
set_a.symmetric_difference(set_b)	Returns a set containing only elements that appear in exactly one of set_a or set_b

'''

'''

A dictionary key can be any immutable type (string, number, tuple)

players = {'Messi': 10, 'Ronaldo': 7}

or,

players = {
    'Lionel Messi': 10,
    'Cristiano Ronaldo': 7
}


To access a dictionary entry:
    
prices = {'apples': 1.99, 'oranges': 1.49}
print('The price of apples is', prices['apples'])


Modifying dictionary entries:

Adding new entries to a dictionary:

dict[k] = v: Adds the new key-value pair k-v, if dict[k] does not already exist.
Example: students['John'] = 'A+'

Modifying existing entries in a dictionary:

dict[k] = v: Updates the existing entry dict[k], if dict[k] already exists.
Example: students['Jessica'] = 'A+'

Removing entries from a dictionary:

del dict[k]: Deletes the entry dict[k].
Example: del students['Rachel']
'''

#Dictionary example
num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

num_dict = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
}

num = int(input())
print(num_list[num])
print(num_dict[num])


'''
format() allows a programmer to create a string with placeholders that
are replaced by values or variables. The placeholder surrounded by {} is 
called a replacement field. Values inside format() are inserted into the 
replacement fields in the string.

number = 6
amount = 32

print('{} burritos cost ${}'.format(number, amount))

'''

'''
There are three ways to format strings

Positional replacement	
'The {1} in the {0} is {2}.'.format('hat', 'cat', 'fat')
The cat in the hat is fat.

Inferred positional replacement	
'The {} in the {} is {}.'.format('cat', 'hat', 'fat')
The cat in the hat is fat.

Named replacement	
'The {animal} in the {headwear} is {shape}.'.format(animal='cat', headwear='hat', shape='fat')
The cat in the hat is fat.

It's good practice to use named replacement when formatting strings with many replacement
fields to make the code more legible.
Additionally, positional and inferred can't be combined but named and positional can.

Double braces {{}} will place an actual {} into a string
e.g.

'{0} {{Bezos}}'.format('Amazon') will print
Amazon{Bezos}

'''

'''
format specifications inside a replacement field allows you to format 
the string. A common specification is to provide a presentation type:

s	String (default presentation type - can be omitted)	
'{:s}'.format('Aiden')
Aiden

d	Decimal (integer values only)	
'{:d}'.format(4)
4

b	Binary (integer values only)	
'{:b}'.format(4)
100

x, X	Hexadecimal in lowercase (x) and uppercase (X) (integer values only)	
'{:x}'.format(15)
f

e	Exponent notation	
'{:e}'.format(44)
4.400000e+01

f	Fixed-point notation (6 places of precision)	
'{:f}'.format(4)
4.000000

.[precision]f	Fixed-point notation (programmer-defined precision)	
'{:.2f}'.format(4)
4.00

'''

'''

The : in the replacement field of the format function differentiates the 'what' on the
left and the 'how' on the right. The left side may be empty, a number, or a name, depending
on the type of replacement. Furthermore, the right side determines how to show a value, such as
a presentation type.

'''




































