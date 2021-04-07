# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 19:33:37 2021

@author: MOSS
"""

'''


A function that calls itself is a recursive function.

e.g.:


def count_down(count):
    if count == 0:            
        print('Go!')                  
    else:                        
        print(count)             
        count_down(count-1)        
            
count_down(2)


The end of the recursive function is the base case

Recursive functions can typically be done with loops. However, using
recursion may make a solution more clear, concise, and understandable.
Candidates for recursion are problems that be reduced into smaller and identical
problems.

Because recursive function are difficult to debug, it's smart to add output statements.
Specifically, you should add indent statements to show what the depth of a
recursive function.

e.g.:

def find(lst, item, low, high, indent):
    """
    Finds index of string in list of strings, else -1.
    Searches only the index range low to high
    Note: Upper/Lower case characters matter
    """
    print(indent, 'find() range', low, high)
    range_size = (high - low) + 1
    mid = (high + low) // 2

    if item == lst[mid]:  # Base case 1: Found at mid
        print(indent, 'Found person.')
        pos = mid
    elif range_size == 1:  # Base case 2: Not found
        print(indent, 'Person not found.')
        pos = -1
    else:  # Recursive search: Search lower or upper half
        if item < lst[mid]:  # Search lower half
            print(indent, 'Searching lower half.')
            pos = find(lst, item, low, mid, indent + '   ')
        else:  # Search upper half
            print(indent, 'Searching upper half.')
            pos = find(lst, item, mid+1, high, indent + '   ')

    print(indent, 'Returning pos = {}.'.format(pos))
    return pos

attendees = []

attendees.append('Adams, Mary')
attendees.append('Carver, Michael')
attendees.append('Domer, Hugo')
attendees.append('Fredericks, Carlo')
attendees.append('Li, Jie')

name = input("Enter person's name: Last, First: ")
pos = find(attendees, name, 0, len(attendees)-1, '   ')

if pos >= 0:
    print('Found at position {}.'.format(pos))
else:
    print( 'Not found.')


Creating a recursive function can be accomplished in two steps:

1. Write the base case: every recursive function must have a case that
returns a value without performing a recursive call. That case is the base case
2. Write recursive case: Then you need to add the recursive case to the function


(Note: cases for recursion are somewhat rare for Python bc natural iterative loop
structures are typically preferred. Recursion is typically useful when dealing
with data structures of unknown size and connectivity, properties most commonly
associated with tree-shaped data structures.)
 
 
Before writing a recursive function, always determine if there exists a natural
recursive solution and whether it is better than a non-recursive solution.
A common error is not covering all possible case cases or one that doesn't always
reach the base case. Both may lead to infinite recursion and fail.


The depth of recursion is how many recursive calls of a function have been made, but
have not yet returned. Every time a recursive call is made, memory is allocated for it.
This happens until all memory is used. Therefore, a recursion depth limit exists
which can be accessed with sys.getrecursionlimit(). The default is typically 1000.
You can change the limit with sys.setrecursionlimit().




'''



'''

LABS


Reverse Digits Lab

def reverseDigits(num,reverse=''):    
   
    if num < 0:
        return None
   
    reverse += str(num%10)  
    if 0 <= num <= 9:
        return reverse
   
    return reverseDigits(num//10, reverse)
       
print(reverseDigits(1234))
    


Number Pattern Lab

def print_num_pattern(num1,num2): 

    if (num1 <= 0): 
        print(num1, end = ' ') 
        return
    else:
        print(num1, end = ' ') 
        print_num_pattern(num1 - num2, num2) 

    print(num1, end = ' ')


if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print_num_pattern(num1, num2)
    


'''