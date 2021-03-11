# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 12:46:53 2021

@author: MOSS
"""

'''

list[:] creates a copy of the orginal list without modifying it.
ARguments t functions are passed by object reference, something in python called
pass-by-assignment. When the function is called, new local variables are created
in the function's local namespace.

When a function modifies a parameter, whether that change is seen outside the 
function's scope depends on the argument object's mutability:
    if immutable, like a string or integer, the modification is limited to
    inside the function. Modification to an immutable object results in the 
    creation of a new object in the function's local scope, leaving the original
    unchanged
    if mutable, the modification will be seen outside the function's scope.

Sometimes a function may require many arguments and will cause clunkiness. Python
lets you use keyword arguments to map parameters by name, not by position in the
argument list and thus does not require specific ordering:

    
def print_book_description(title, author, publisher, year, version, num_chapters, num_pages):
    # Format and print description of a book...

print_book_description(title='The Lord of the Rings', publisher='George Allen & Unwin',
                       year=1954, author='J. R. R. Tolkien', version=1.0,
                       num_pages=456, num_chapters=22)


(Generally use for when a function requires >4 arguments.) Also, you may combine
positional arguments with keyword arguments, given that positional arguments are all
used first:

    
def split_check(amount, num_people, tax_percentage, tip_percentage):
    # ...

split_check(125.00, tip_percentage=0.15, num_people=2, tax_percentage=0.095)


Function parameters may be optional, meaning an argument can omit that parameter
instead for a default value:


def print_date(day, month = 0, year = 2000, style = 0)
...


A possible error is using a muttable object as a default value. The object is created
only once, not after every function call:

def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

numbers = append_to_list(50)  # default list appended with 50
print(numbers)
numbers = append_to_list(100)  # default list appended with 100
print(numbers)

VERSUS

def append_to_list(value, my_list=None):  # Use default parameter value of None
    if my_list == None:  # Create a new list if a list was not provided
        my_list = []

    my_list.append(value)
    return my_list

numbers = append_to_list(50)  # default list appended with 50
print(numbers)
numbers = append_to_list(100)  # default list appended with 100
print(numbers)


If you don't know how many arguments a function requires, including *args parameter
collects optional positional parameters in an arbitrary argument list tuple.
Adding **kwargs creates a dictionary with extra arguments (kwargs short for
keyword arguments). The keys of the dictionary are the parameter names specified
in the function call.
(NOTE: * and ** are the important symbols here. args and kwargs are just standard
 practice. But any valid identifier (like *condiments) is fine).
Also, one or both *  ** may be used. They must come in last and in the order used.


Because a function can't return multiple output values, you can instead package them
inside a tuple or list (or other container).


Strings may be read using an index (e.g. my_strin[5]). To read more than one
character at one time, use slice notation my_str[start:end] (which yields indices
from start to (end-1). Other sequence types like ists and tuples support slice notation.
Also, because slice notation yields (end - 1), you can use (end + 1) to yield the
last element in the last sequence.


When sliced, Python creates a new object for it. So, if you create a slice of
my_str, and then change the value of my_str, you won't change the value of the slice.

You can also leave out slice notation parameters (e.g. my_str[:5] or my_str5:],
whose output is self-evident, or my_str[x:y]).


Field width defines the minimum number of characters that must be inserted into
a string. If the replacement value is smaller in size than the given width, then
th string's left side is padded with space characters. A field width is specified
in a format specification by including an integer after a colon, like in {name:16}
to specify a width of 16 characters. Numbers will be right-aligned within the width
by default, whereas most other types like strings will be left-aligned.

print('{:10}{:6}'.format('Hi', 'Greg'))

versus

print('{:10}{:6}'.format(1, 'Greg'))
                                                  
'''




'''
LABS


Exact Change Lab

def exact_change(coins):

    num_dollars = int(coins / 100)
    coins -= (num_dollars * 100)
    num_quarters = int(coins / 25)
    coins -= (num_quarters * 25)
    num_dimes = int(coins / 10)
    coins -= (num_dimes * 10)
    num_nickels = int(coins / 5)
    coins -= (num_nickels * 5)
    num_pennies = coins
    
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies
    

if __name__ == '__main__': 
    coins = int(input())    
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(coins)
        
    if coins <= 0:
        print('no change')
    if num_dollars == 1:
        print('1 dollar')
    if num_dollars > 1:
        print('{} dollars'.format(num_dollars))
        
    if num_quarters == 1:
        print('1 quarter')
    if num_quarters > 1:
        print('{} quarters'.format(num_quarters))
        
    if num_dimes == 1:
        print('1 dime')
    if num_dimes > 1:
        print('{} dimes'.format(num_dimes))
        
    if num_nickels == 1:
        print('1 nickel')
    if num_nickels > 1:
        print('{} nickels'.format(num_nickels))
        
    if num_pennies == 1:
        print('1 penny')
    if num_pennies > 1:
        print('{} pennies'.format(num_pennies))



Character in Word Lab

def charInWord(character, word):
    for char in word:
        if character == char:
            return True
            break
    if (type(character) != str) or (type(word) != str) or (len(character) >= 2):
        return None
    else:
        return False

if __name__ == '__main__': 
    character = (input())  
    word = input()
    result = charInWord(character, word)

    if result == True:
        print('{} is in {}'.format(character, word))
    elif result == False:
        print('{} is not in {}'.format(character, word))
    else:
        print('wrong types passed in')


Last N Characters Lab

def test_passed(word, num_chars):
    if (num_chars == '0') or (int(num_chars) <= 0):
        input_type = False
    elif (word.isalpha()):
        input_type = True
    else:
        input_type = False
    return input_type


def last_chars(word, num_chars):
    if test_passed(word,num_chars) == True:
        result = word[-(int(num_chars)):]
        return result
        

if __name__ == '__main__': 
    input_str = input()
    num = int(input())
    result = last_chars(input_str, num)

    if test_passed(input_str, num) == False:
        print('Invalid input')
    else:
        print('The last {} characters of \'{}\' are \'{}\'.'.format(num, input_str, result))

NOTE: This was truly a poorly designed lab...




'''