# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:11:32 2021

@author: MOSS
"""

'''

A loop executes the loop's statements (loop body) repeatedly. Each time through
a loop's body is an interation.

A while loop continually iterates as long as its loop expression remains true.

A sentinal value is one that terminates further iterations of a while loop

Loop e.g. :

import random

randint = random.randint(-1000,1000)
print(randint)

while randint != 0:
    randint = random.randint(-1000,1000)
    print(randint)

import random imports a library of random numbers. random.randit(a,b) gets a random
number between range a through b, inclusive of a and b.


A for loop interates over each element in a container (typically a list, tuple, 
or string.

e.g.

for name in ['Bill', 'Nicole', 'John']:
  print('Hi {}!'.format(name))

A for loop that iterates over a dictionary assigns the loop variable with the
keys of the dictionary

e.g.

channels = {
    'MTV': 35,
    'CNN': 28,
    'FOX': 11,
    'NBC': 4,
    'CBS': 12
}

for c in channels:
    print('{} is on channel {}'.format(c, channels[c]))


A for loop that interates over a string assigns the loop variable with all the
characters in the string from left to right.

e.g.

my_str = ''
for character in "Take me to the moon.":
    my_str += character + '_'
print(my_str)

A for loop may also iterate backwards over a sequence using the reverse() function.


The range() function allows for counting in a for loop. Range(x, y, z), where x
is the starting integer (included in the range), y is the ending integer (not
included in the range), and z is the integer step value (i.e. how large of counting
increments to take).

range(Y) generates a sequence of all non-negative integers less than Y.
Ex: range(3) creates the sequence 0, 1, 2.
range(X, Y) generates a sequence of all integers >= X and < Y.
Ex: range(-7, -3) creates the sequence -7, -6, -5, -4.
range(X, Y, Z), where Z is positive, generates a sequence of all integers >= X and < Y, incrementing by Z.
Ex: range(0, 50, 10) creates the sequence 0, 10, 20, 30, 40.
range(X, Y, Z), where Z is negative, generates a sequence of all integers <= X and > Y, incrementing by Z.
Ex: range(3, -1, -1) creates the sequence 3, 2, 1, 0.

Range creates a new 'range' type object. It's a sequence type (like strings
and tuples), but is immutable. Range type objects are typically only used in
in a for loop.

interesting thing to consider (demonstrates that range is an object):

r = range(1, 100)

for x in r:
    print(x)



A nested loop is one that appears inside of the body of another loop. The loops
are commonly called the inner and outer loops. One use of nested loops is to
generate all combinations of some items, like all two letter combinations, as in
the following program:
    
"""
Program to print all 2-letter domain names.

Note that ord() and chr() convert between text and the ASCII or Unicode encoding:
-  ord('a') yields the encoded value of 'a', the number 97.
-  ord('a')+1 adds 1 to the encoded value of 'a', giving 98.
-  chr(ord('a')+1) converts 98 back into a letter, producing 'b'
"""
print('Two-letter domain names:')

letter1 = 'a'
letter2 = '?'
while letter1 <= 'z':  # Outer loop
    letter2 = 'a'
    while letter2 <= 'z':  # Inner loop
        print('{}{}.com'.format(letter1, letter2))
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)


A break statement causes a loop to exit immediately and can possibly simplify your
program/loop. A continue statement causes a jump immediately to the loop header
statement. 


An else statement after a loop executes after the loop terminates normally, without
the use of a break statement.

Note: the editdistance function calculates how many edits are required between two
strings.

The enumerate function retrieves both the index and corresponding element at the
same time (when going through a container in a for loop).

e.g.

origins = [4, 8, 10]

for (index, value) in enumerate(origins):
    print('Element {}: {}'.format(index, value))

In the above example, enumerate() yields a new tuple each iteration of the loop,
this tuple contains the current index and corresponding element value. The for
loop unpacks the tuple yielded by each iteration of enumerate(origins) into two variables:
"index" and "value." Unpacking is the process that performs multiple assignments
at once, binding comma-separated names on the left to the elements of a sequence
on the right (e.g. num1, num2 = [350, 400], equates to num1 = 350 and num2 = 400)


'''

"""
Program to print all 2-letter domain names.

Note that ord() and chr() convert between text and the ASCII or Unicode encoding:
-  ord('a') yields the encoded value of 'a', the number 97.
-  ord('a')+1 adds 1 to the encoded value of 'a', giving 98.
-  chr(ord('a')+1) converts 98 back into a letter, producing 'b'
"""

'''
Simon Says Program:
    
user_score = 0
simon_pattern = input()
user_pattern  = input()
x = 0

for char in simon_pattern:
    if user_pattern[x] == char:
        user_score += 1
        x += 1
    else:
        break

print('User score:', user_score)

'''


'''

LABS


Count Input Length Lab

def user_string():
    string = input()
    return string

text = user_string()

def text_criteria(text):
    if (text == ',') or (text == ' ') or (text == '.'):
        return False
    else:
        return True

def scan_string(string):
    chars = 0
    for char in string:
        if text_criteria(char) ==  True:
            chars += 1
    return chars

print(scan_string(text))


Password Modifier Lab

pword_original = input()

def pword_mod(pword):
    new_pword = ''
    for char in pword:
        if char == 'i':
            new_pword += '1'
        elif char == 'a':
            new_pword += '@'
        elif char == 'm':
            new_pword += 'M'
        elif char == 'B':
            new_pword += '8'
        elif char == 's':
            new_pword += '$'
        else:
            new_pword += char
    new_pword += '!'
    return new_pword

print(pword_mod(pword_original))


Output Increments of Five Lab

n1 = int(input())
n2 = int(input())

def five_increments(x, y):
    if y >= x:
        while y >= x:
            print('{}'.format(x), end = ' ')
            x += 5
        print()
    else:
        print("Second integer can't be less than the first.")

five_increments(n1, n2)


Count Vowels Lab

string = input()

vowels = ['A',
          'a',
          'E',
          'e',
          'I',
          'i',
          'O',
          'o',
          'U',
          'u']

def text_criteria(text):
    if text in vowels:
        return True
    else:
        return False

def scan_string(string):
    n_vowels = 0
    for char in string:
        if text_criteria(char) ==  True:
            n_vowels += 1
    return n_vowels

print(scan_string(string))


'''