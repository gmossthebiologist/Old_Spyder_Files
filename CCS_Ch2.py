# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 22:55:45 2021

@author: MOSS
"""

'''The floored division operator // rounds down (DOWN) the float 
resulting from division (/) to the nearest whole number. If
both numbers are int then the result is int. Not true
if either is float'''
'''
print(20 // 2) 
print(20. // 2)

# Q: When is modulo ever really used?

hours = int(input('Enter hours:\n\n')) #You can't do: int(input('Enter hours:\n', '\n')) because input can only do one argument. To add multiple lines, \n\n...\n
minutes = int(input('Enter minutes:\n\n'))

new_minutes = (hours * 60) + minutes

print('Total minutes: ', new_minutes)


# Modulo can, for example, identify individual digits of a number
user_val = 927
ones_digit     = user_val % 10    # Ex: 927 % 10 is 7. 
tmp_val        = user_val // 10

tens_digit     = tmp_val % 10     # Ex: tmp_val = 927 // 10 is 92. Then 92 % 10 is 2.
tmp_val        = tmp_val // 10

hundreds_digit = tmp_val % 10     # Ex: tmp_val = 92 // 10 = 9. Then 9 % 10 is 9.


#Dictionaries are a mutable data type (i.e. can be changed)

english_to_spanish = {
    "cat" : "gato",
    "one" : "uno",
    "two" : "dos",
    }
'''

x = -4

y = x%(-10)
z = (x%10)

print(y, z)

'''
# The baby_names.py module

print ('Initializing baby variables...')
baby_name1 = 'Ryder'
baby_name2 = 'Jess'
baby_weight1 = 5.1
baby_weight2 = 8.5

# Executes only if file run as a script (e.g., python baby_names.py)
if __name__ == '__main__':
    print('Baby 1:', baby_name1, 'was born', baby_weight1, 'lbs')
    print('Baby 2:', baby_name2, 'was born', baby_weight2, 'lbs')
 '''
# A script favorite_child.py that imports and uses the baby_names module.

import baby_names  # Importing the module executes the module contents  

print('My favorite child is', baby_names.baby_name1, '-')
print('I remember when he weighed only', baby_names.baby_weight1, 'pounds.')
print('I love', baby_names.baby_name2, 'too, of course.')


#raw string r'xxx' ignores escape sequences

my_string = 'This is a \n \'normal\' string\n'
my_raw_string = r'This is a \n \'raw\' string'

print(my_string)
print(my_raw_string)
































