# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:12:56 2021

@author: MOSS
"""

'''

A function is a named series of statements. A function definition consists
of the new function's name and a block of statements following 
(e.g. def pizza_area(): ). The function call is an invocation of the function's
name that executes the function.(Python has built-in functions, such as
input(), int(), len(), etc.) 

A parameter is a function input specified in the definition (e.g. pizza area
will have diameter as an input). An argument is a value provided to a function's
parameter during a function call (e.g. pizza_area(12.0)). Note that a parameter may
only be a variable, not an expression.

A function may return one value using a return statement, which 'returns' a value
produced by the function back to the variable within the call statement.

No return statement produces a None. Additionally, a function can only return one item,
though a list or tuple can be returned. Return can appear anywhere in the function, not
just at the end.

A function's statements may include function calls known as hierarchical function calls
or nested function calls. user_input = int(input()) consists of such a hierarchical
function call, where input() is called and evaluated, then int() is called and 
evaluated.

A programmer can pass any type of an object as an argument to a function. For example,
add(5, 7) or add('abc', 'def') (which will output 'abc' + 'def' = 'abcdef'). The
function's behavior of being able to add together different types of objects is known
as polymorphism (e.g. 'x' * 5 = xxxxx).

Python uses dynamic typing which constantly changes the type of an operator. And
languages (like python) w dynamic typing check if the lines of code are valid as
they execute.

Programs are typically written using incremental development, where small amounts of
code are written and tested. To assist with this, programmers will often use function
stubs, functions w/o a definition that show the roadmap and planned execution of steps
of a function.(Leads to better organization, reduced dev time, and less bugs). The
pass keyword will perform no operation and act as a placeholder for a function def'n.

In other cases you may want to simply stop the execution of a program as soon as a 
function stub is encountered. To do this, raise NotImplementedError.

An example of improving readability of code by calling functions as objects, not the
functions themselves:
    
def human_head():
    print('   ||||| ')
    print('   o   o')
    print('     >' )
    print('   ooooo')
    return

def monkey_head():
    print('   .-"-.')
    print(' _/.-.-.\\_')
    print('( ( o o ) )')
    print(' |/  "  \\|')
    print('  \\ .-. /')
    print('  /`"""`\\')
    return

def print_figure(face):
    face()  # Print the face
    print('     |')
    print('   --|--')
    print('  /  |  \\')
    print('@    |    @')
    print('     |')
    print('    /|\\')
    print('   @   @')
    return

choice = int(input('Enter "1" to draw monkey, "2" for human: '))

if choice == 1:
    print_figure(monkey_head)
elif choice == 2:
    print_figure(human_head)

Esaier to read bc you aren't calling human/monkey_head() followed by print_body()


The scope of a variable or function object is only visible to part of a program,
known as a scope. If a variable is created inside a function, its scope is limited
to the function and only after its first assignment. These are known as local variables.
A global variable can be accessed anywhere after its assignment. When operating inside
a function, to access a global variable, the global statement must be used:
    
employee_name = 'N/A'

def get_name():
    global employee_name
    name = input('Enter employee name:')
    employee_name = name

get_name()
print('Employee name:', employee_name)

Modification of a mutable global variable does not require the global statement to
modify it within a function (such as a list or dictionary).


A namespace maps names to objects. The python interpreter uses it to track objects in
a program and to access them later for use. A namespace is just a normal dictionary; it
can be accessed by the locals() and globals() functions.

When a name is referenced, the local scope is checked first, then global, then the
built-in (contains built-in names of Python like int(), str(), list(), etc.). If the
name cannot be found, a NameError is generated. This process of searching for a name
is called scope resolution.
'''

'''
LABS:

    

Tracking Laps Lab

def meters_to_laps(length):
    laps = length/50
    return laps

if __name__ == '__main__':
    meters = float(input())
    laps = meters_to_laps(meters)
    print('{:.2f}'.format(laps))


Longer String Lab

def longer_string(user_val1, user_val2):
    if len(user_val1) > len(user_val2):
        long_string = user_val1
        print(user_val1)
    if len(user_val1) < len(user_val2):
        long_string = user_val2
        print(user_val2)
    if len(user_val1) == len(user_val2):
        long_string = user_val2 #not actually longer but, need to return a value and the project wants the second string
        print('{}'.format(user_val2))
    return long_string

if __name__ == '__main__':
    user_val1 = input()
    user_val2 = input()
    longer_string(user_val1, user_val2)


Driving Costs Lab

def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    gallons = driven_miles / miles_per_gallon
    cost = gallons * dollars_per_gallon
    return cost

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    
    ten = driving_cost(10, miles_per_gallon, dollars_per_gallon)
    fifty = driving_cost(50, miles_per_gallon, dollars_per_gallon)
    fourhundred = driving_cost(400, miles_per_gallon, dollars_per_gallon)
    
    print('{:.2f}'.format(ten))
    print('{:.2f}'.format(fifty))
    print('{:.2f}'.format(fourhundred))


Customized Step Counter Lab

def steps_to_miles(user_steps, step_length):
    miles_walked  = (user_steps * step_length) / 36630
    return miles_walked

if __name__ == "__main__":
    user_steps = float(input())
    step_length = float(input())
    miles_walked = steps_to_miles(user_steps, step_length)
    print('{:.2f}'.format(miles_walked))


Leap Year Lab

def is_leap_year(user_year):
    if (float(user_year / 100)) == (float(user_year // 100)):
        if (user_year % 400) == 0:
            leap_year = True
        else:
            leap_year = False
    elif (user_year % 4) == 0:
        leap_year = True
    else: 
        leap_year = False
    return leap_year

if __name__ == '__main__':
    user_year = int(input())
    leap_year = is_leap_year(user_year)
    if leap_year == True:
        print('{} is a leap year.'.format(user_year))
    else:
        print('{} is not a leap year.'.format(user_year))


'''