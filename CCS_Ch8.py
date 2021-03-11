# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 17:18:32 2021

@author: MOSS
"""

'''


The function list() takes a single iterable object argument, such as a string,
list, or tuple, and returns a new list object. (e.g. list('abc') creates [a,b,c]

in-place modification refers to the fact that lists can be modified in size
(added or subtracted from) without having to create a new list, instead the original
list is modified.

my_list[start:end] gets a new list containing some other list's specified elements
my_list[len(my_list):] = [x] adds the elements in [x] to the end of my_list. Append(x)
may be preferred for clarity though.
del my_list[i] deletes an element from a list.

List Methods:

list.append(x) adds an item to the end of a list.
list.extend([x]) Add all items in [x] to list.
list.inert(i,x) Insert x in list before position i

list.remove(x) Remove first item from list with value x
list.pop() Remove and return last item in list.
list.pop(i) Remove and return item at position i in list.

list.sort() Sort the items of list in-place
list.reverse() Reverse the elements of list in-place

list.index(x) Return index of first item in list with value x
list.count(x) Count the number of times value x is in list.


The enumerate() function iterates over a list and provides an iteration counter.
It gives the index and its corresponding element.


all(list) True if every element in list is True (!=0), or if the list is empty
any(list) True if any element in the list is True
max(list)
min(list)
sum(list)


List nesting is when you contain lists inside another list (e.g. my_list = [[5, 13], [50, 75, 100]])
A program accesses elements of a nested list using syntax such as my_list[0][0]

List nesting allows you to create a multi-dimensional data structure

Nested for loops and the enumerate() function gives easy access to nested lists:

currency = [
   [1, 5, 10 ],  # US Dollars
   [0.75, 3.77, 7.53],  #Euros
   [0.65, 3.25, 6.50]  # British pounds
]
for row_index, row in enumerate(currency):
   for column_index, item in enumerate(row):
       print('currency[{}][{}] is {:.2f}'.format(row_index, column_index, item))



When iterating over a list in a for loop, you may remove or add values from that list
expecting the indeces to remain the same. However, as soon as you modify the elements
of the list, the indeces shift. To easily understand this, see this example:
    

nums1 = [5, 10, 15]
nums2 = [10, 15]

for val in nums1:
    if val in nums2:
        nums1.remove(val)


FIXED:
    
nums1 = [5, 10, 15]
nums2 = [10, 15]

for val in nums1[:]:
    if val in nums2:
        nums1.remove(val)


The sort() method (e.g. list.sort()) rearranges a list's elements from lowest to highest

When using sort(), you conduct an in-place modification, meaning the original list
is modified. The sorted() function, however, creates a new sorted copy of the list
(e.g. sorted(my_list)).

Both sort() and sorted() have an optional key argument. The key specifies a function
to be applied to each element prior to being compared such as, str.lower, str.upper,
or str.capitalize. (...)


names = []
prompt = 'Enter name: '

user_input = input(prompt)

while user_input != 'exit':
    names.append(user_input)
    user_input = input(prompt)

no_key_sort = sorted(names)
key_sort = sorted(names, key=str.lower)

print('Sorting without key:', no_key_sort)
print('Sorting with key: ', key_sort)


(...) In the above example, without the key, names left uncapitalized will be sorted
at the end of the list because capitals have lower ASCII decimal values. But with the
key str.lower, the key converts the elements to lower-case before comparison, thus
placing the names in the appropriate positions.


The reverse argument will sort from highest to lowest when set to True:

sorted([15, 20, 25], reverse=True)


Dictionaries can be used with the dict() function (both of the following are equal):

dict(Bobby='805-555-2232', Johnny='951-555-0055')
dict([('Bobby', '805-555-2232'), ('Johnny', '951-555-0055')])

Common dictionary operations:

my_dict[key]	Indexing operation – retrieves the value associated with key.	jose_grade = my_dict['Jose']
my_dict[key] = value	Adds an entry if the entry does not exist, else modifies the existing entry.	my_dict['Jose'] = 'B+'
del my_dict[key]	Deletes the key from a dict.	del my_dict['Jose']
key in my_dict	Tests for existence of key in my_dict.	if 'Jose' in my_dict: # ...


Dictionary methods operate on dict types (i.e. dictionaries... duh). Here are some:

my_dict.clear()	Removes all items from the dictionary.

my_dict.get(key, default)	Reads the value of the key from the dictionary. If the key does not exist in the dictionary, then returns default.

my_dict1.update(my_dict2)	Merges dictionary my_dict1 with another dictionary my_dict2. Existing entries in my_dict1 are overwritten if the same keys exist in my_dict2.

my_dict.pop(key, default)	Removes and returns the key value from the dictionary. If key does not exist, then default is returned.


Dictionaries are commonly iterated over, typically with a for loop. However, the order
in which keys are iterated over is not necessarily the order in which they were 
inserted into the dictionary. Python creates a hash for each key, which is a transformation
into a unique value that allows the interpreter to do very fast lookup. Thus,
the ordering is actually done according to hash value.

Dict types support the methods items(), keys(), and values(). These produce a view object,
which provides a read-only access to dictionary keys and values. A program can iterate over
a view object to access one key-value pair, one key, or one value at a time, depending
on method used. A view object reflects updates to the dictionary even if the dictionary
is altered after the creation of the view object.

dict.items() - returns a view object that yields (key, value) tuples.
dict.keys() - returns a view object that yields dictionary keys
dict.values() - returns a view object that yields dictionary values.

Examples:

num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda, calories in num_calories.items():
    print('{}: {}'.format(soda, calories))


num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda in num_calories.keys():
    print(soda)
    

num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda in num_calories.values():
    print(soda)
    

View objects don't support indexing as one result is generated for each iteration
as needed, rather than a list containing of values. (But, you can convert the view
object into a list using list().


A dictionary within a dictionary is called a nested dictionary. Here's an example:

students = {}
students ['Jose'] = {'Grade': 'A+', 'StudentID': 22321}

print('Jose:')
print(' Grade: {}'.format(students ['Jose']['Grade']))
print(' ID: {}'.format(students['Jose']['StudentID']))



'''




'''

LABS

Varied amount of input data lab

stats = []
user_input = input()

user_stats = user_input.split(' ')

for stat in user_stats:
    stats.append(int(stat))

avg = int(sum(stats)/len(stats))
max_stat = max(stats)

print(avg, max_stat)



Filter and sort a list lab

def user_input():
    user_input = input()
    return user_input


def store_in_list(user_input):
    stats = []
    user_input = user_input.split(' ')
    for stat in user_input:
        stats.append(int(stat))
    return stats

def output_pos(stats):
    for stat in stats[:]:
        if stat < 0:
            stats.remove(stat)
    stats.sort()
    return stats

def print_list_contents(stats):
    for stat in stats:
        print(stat, end = ' ')

user_input = user_input()
stats = store_in_list(user_input)
sorted_stats = output_pos(stats)
print_list_contents(sorted_stats)



Elements in a Range Lab

def user_input_1():
    user_input_1 = input()
    return user_input_1

def user_input_2():
    user_input_2 = input()
    return user_input_2

def store_in_list(user_input_1):
    int_list = []
    user_input_1 = user_input_1.split(' ')
    for n in user_input_1:
        int_list.append(int(n))
    return int_list

def max_bound(user_input_2):
    bounds = store_in_list(user_input_2)
    max_bound = max(bounds)
    return max_bound

def min_bound(user_input_2):
    bounds = store_in_list(user_input_2)
    min_bound = min(bounds)
    return min_bound

def real_list(int_list, max_bound, min_bound):
    for n in int_list[:]:
        if (n > max_bound) or (n < min_bound):
            int_list.remove(n)
    return int_list

def print_list_contents(int_list):
    for n in int_list:
        print(n, end = ' ')


user_input_1 = user_input_1()
user_input_2 = user_input_2()
int_list = store_in_list(user_input_1)
max_bound = max_bound(user_input_2)
min_bound = min_bound(user_input_2)
real_list = real_list(int_list, max_bound, min_bound)
print_list_contents(real_list)





'''