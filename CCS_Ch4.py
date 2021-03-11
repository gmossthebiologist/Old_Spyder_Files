# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:26:36 2021

@author: MOSS
"""

'''

You can determine whether a value is found within a container,
such as a dictionary or list, using in and not in, which are known
as membership operators. The yield Boolean values

prices = [5, 15, 20]
print(15 in prices)

yields: True


You can also use them to check is a substring is part of a 
string (e.g. abc in abcdefg). But, when identifying membership
in a dictionary, only the key is searched for, not the values
of the keys.
'''


'''

To check if two variables are the same object, use is or is not.
Identity operators do not compare object values, they compare object
identities. (Identity is usually memory address of object)
is is not the same as ==. You typically only want to use
identity operators when explicity testing if two objects are
identical. If x is y is true, id(x) == id(y) is also true.

'''

'''

Sometimes indentations in a program are continuations of the previous line.
Multiple lines in parantheses are implicitly joined into a single string.
Use these traits for very long strings or functions. When making lists or dictionaries,
entries can be placed on seperate lines for clarity.

result_of_power = math.pow(long_variable_name_left_operand,
                           long_variable_name_right_operand)

'''

declaration = ("When in the Course of human events, it becomes necessary for "
               "one people to dissolve the political bands which have connected "
               "them with another, and to assume among the powers of the earth...")
print(declaration)















'''
LABS:



Shades of Gray ZyLab:
    
    
red = int(input('Enter a value for Red: '))
green = int(input('Enter a value for Green: '))
blue = int(input('Enter a value for Blue: '))

colors = (red, green, blue)

lowest_n = min(colors)

new_red = red - lowest_n
new_green = green - lowest_n
new_blue = blue - lowest_n

new_colors =(new_red, new_green, new_blue)
print(new_colors)



Smallest Number ZyLab:
    
    
n_1 = int(input())
n_2 = int(input())
n_3 = int(input())

n_list = [n_1, n_2, n_3]

n_min = min(n_list)

print(n_min)



Interstate Highway Numbers ZyLab:
    
highway = int(input())

if 1 <= highway <= 99: #if between 1 and 99, highway is a primary highway
    if highway % 2 == 0: #even primaries go east or west
        print('I-{} is primary, going east/west.'.format(highway))
    if highway % 2 != 0: #odd primaries go north or south
        print('I-{} is primary, going north/south.'.format(highway))

if 100 <= highway <= 999:
    primary_highway = highway % 100 #primary highways serve the highway that is the rightmost two digits of auxiliary
    if highway % 2 == 0:
        print('I-{} is auxiliary, serving I-{}, going east/west.'.format(highway, primary_highway))
    if highway % 2 != 0:
        print('I-{} is auxiliary, serving I-{}, going north/south.'.format(highway, primary_highway))

if highway < 1 or highway > 999:
    print('{} is not a valid interstate highway number.'.format(highway))



Seasons ZyLab:

month = input()
day = int(input())

months = {
    'January': 32,
    'February': 29,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31.
    }


#Test if Invalid
if month in months:
    day_test = (0 < day <= months[month])
    if day_test == False:
        print('Invalid')
else:
    print('Invalid')
    day_test = False

#Winter
if day_test == True:
    if month == 'January':
        print('Winter')
    if month == 'February':
        print('Winter')
    if month == 'December' and day >= 21:
        print('Winter')
    if month == 'March' and day <= 19:
        print('Winter')
    
#Spring
if day_test == True:
    if month == 'April':
        print('Spring')
    if month == 'May':
        print('Spring')
    if month == 'March' and day >= 20:
        print('Spring')
    if month == 'June' and day <= 20:
        print('Spring')

#Summer
if day_test == True:
    if month == 'July':
        print('Summer')
    if month == 'August':
        print('Summer')
    if month == 'June' and day >= 21:
        print('Summer')
    if month == 'September' and day <= 21:
        print('Summer')

#Autumn
if day_test == True:
    if month == 'October':
        print('Autumn')
    if month == 'November':
        print('Autumn')
    if month == 'September' and day >= 22:
        print('Autumn')
    if month == 'December' and day <= 20:
        print('Autumn')


Exact change ZyLab:

coins = int(input())

if coins <= 0:
    print('No Change')

dollars = int(coins / 100)
coins -= (dollars * 100)
quarters = int(coins / 25)
coins -= (quarters * 25)
dimes = int(coins / 10)
coins -= (dimes * 10)
nickels = int(coins / 5)
coins -= (nickels * 5)
pennies = coins

if dollars == 1:
    print('1 Dollar')
if dollars > 1:
    print('{} Dollars'.format(dollars))
    
if quarters == 1:
    print('1 Quarter')
if quarters > 1:
    print('{} Quarters'.format(quarters))
    
if dimes == 1:
    print('1 Dime')
if dimes > 1:
    print('{} Dimes'.format(dimes))
    
if nickels == 1:
    print('1 Nickel')
if nickels > 1:
    print('{} Nickels'.format(nickels))
    
if pennies == 1:
    print('1 Penny')
if pennies > 1:
    print('{} Pennies'.format(pennies))

'''








