# What is a Module in Python?
# A module in Python is a file that contains Python code (functions, classes, variables, or even runnable code) and is used to organize and reuse code efficiently.
# A module is simply a .py file that can be imported and used in other Python programs.
# Modules help keep the code modular, readable, and maintainable.
# Python has built-in modules (like math, random, os) and also allows users to create custom modules.

# Types of Modules in Python

# 1.Built-in Modules (Standard Library)
# Pre-installed modules in Python.
# Example: math, random, os, sys

import math
print(math.sqrt(36))   # Output 6.0

# 2.User-Defined Modules (Custom Modules)
# Any Python file (.py) you create can be used as a module.

import my_modules
print(my_modules.multiply(4, 5))  # 20


# 3. External Modules (Third-party Libraries)
# Installed via pip (pip install module_name).
# Example: numpy, pandas, requests

import requests
response = requests.get("https://liyasthomas.github.io/books")
print(response.status_code)

# How to Import a Module in Python?

# 1.Basic Import
import math
print(math.pi)

# 2.Import with Alias (as)
import numpy as np
print(np.array([1, 2, 3, 4]))

# 3.Import Specific Functions or Variables (from ... import ...)
from math import sqrt, pi
print(math.sqrt(9))  # 3.0
print(math.pi)

from math import sqrt as s, pi as p

print(s(64))  
print(p)

# 4.Import Everything (from module import *) (Not recommended for large modules)
from math import * # wild card
print(sin(0))  # Output: 0.0

# What’s Happening in This Namespace Overlap?
from math import *
from numpy import *
print(pi)  # Which `pi` is being printed? math.pi or numpy.pi?

# Understanding Functions in Python

# This is a global function because it's defined at the top level of the module.
def my_function():
  print("Learning Python!")

# The function can be called from anywhere in the module.
my_function()

# Types of Python Functions

#  Built-in functions
print("Hello! World")


# Functions defined in built-in modules
import random
print(random.randint(1,20))


# User-defined functions
def my_function():
  print("Doing coding is also fun.")

my_function()

# Syntax to Define a Python Function

def greetings():
   "This is docstring of greetings function"
   greet = "Hello, coder! Let's build something awesome."
   return greet

message = greetings()
print(message)

# Pass by Reference vs Value

# Python uses pass by object reference. 
# Immutable objects (e.g. integers) are unchanged, while mutable objects (e.g. lists) are modified.

def modify_value(x):
    x = 10
    print("Within Function:", x)

# Immutable object (integer)
x = 5
print("Original =", x)
modify_value(x)
print("After Function:", x)

def modify_list(lst):
   lst.append(4)
   print("Within function:", lst, "ID", id(lst))

# Mutable object (list)
lst = [1, 2, 3]
print("Original:", lst, " - ID:", id(lst))
modify_list(lst)
print("After function:", lst, " - ID:", id(lst))

# Function Arguments
# Function arguments are the values or variables passed into a function when it is called.

def greetings(name):
   "This is docstring of greeting function"
   print("Hello {}".format(name))
   return

greetings("Arsh")
greetings("Manahil")
greetings("Eshal")

# Keyword Arguments

def person_info(name, age):
   "This print person info in the function"
   print("Name:", name)
   print("Age:", age)
   return

# Now you can call person info function
person_info(age= "8", name= "Hooria")
# person_info(8, "Hooria")

def add(x: int, y: int=0) -> float:
   return float(x + y)

print(float(add(5, 9)))  # 14.0
print(add(y=5.6, x=3.2)) # type hints are not enforced in Python
print(add(x=6))  # 6.0

# * unpacking iterables
def add(a, b, c):
   return a + b + c

numbers = [2, 3, 6]
result = add(*numbers)
print(result)

def my_sum(*nums):
   print(type(nums),nums)

   return sum(nums)

print("Sum =", my_sum(1, 2, 3, 4, 5, 6, 7, 8), "\n")
print("Sum *[]=", my_sum(*[1, 2, 3, 4, 5, 6, 7, 8]), "\n")  # unpacking list
print("Sum *()=", my_sum(*(1, 2, 3, 4, 5, 6, 7, 8)))  # unpacking tuple

# Default Arguments
# A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.

def student_info(name, roll= 20):
   "This print student info in the function"
   print("Name:", name)
   print("Roll:", roll)
   return

student_info(roll="6", name = "Arisha")
student_info(name= "Fatima")

# Positional-only arguments
# Those arguments that can only be specified by their position in the function call is called as Positional-only arguments.
# They are defined by placing a "/" in the function's parameter list after all positional-only parameters.

def pos_func(x, y, /, z):
   print(x + y + z)

print("Evaluating positional-only arguments: ")
pos_func(2, 2, z=3)

#  uncomment to see error
# pos_func(x=2, y=2, z=3)

# Keyword-only arguments
# Those arguments that must be specified by their name while calling the function is known as Keyword-only arguments.
# They are defined by placing an asterisk ("*") in the function's parameter list before any keyword-only parameters.
# This type of argument can only be passed to a function as a keyword argument, not a positional argument.

def post_fun(*, num1, num2, num3):
   print(num1 * num2 * num3)

print("Evaluating keyword-only arguments: ")
post_fun(num1=4, num2=6, num3=3)

# TypeError: posFun() takes 0 positional arguments but 3 were given
# post_fun(4, 6, 3)


# Arbitrary or Variable-length Arguments
# You may need to process a function for more arguments than you specified while defining the function.
# These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.

# 1. Non-keyword arguments: *args
def my_func(*args):
    print("Non-keyword arguments: *args")
    for value in args:
        print(value)

my_func(10, 20, 30)

# 2. Keyword arguments: **kwargs
def my_func(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

my_func(name="Areesha", age=21, city="Karachi")

def passenger_info(name, *visitedCities):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print(name)
   for city in visitedCities:
      print("*", city)
   return


# Now you can call passenger_info funct
passenger_info("Ayesha")
passenger_info("Minhal","Lahore", "Islamabad", "Quetta")

# Python Function with Return Value
def add(a,b):
   c= a + b
   return c

x=10
y=20
result = add(x,y)

print ("x = {} y = {} x + y = {}".format(x, y, result))

# The Anonymous Functions
# The functions are called anonymous when they are not declared in the standard manner by using the def keyword. 
# Instead, they are defined using the lambda keyword.

def add_two(x, y):
  return x + y

my_lambda = lambda x, y:  x + y;

print(my_lambda(1,2))

fruits_dict = {"apples" : 6, "water-melon" : 5, "mangoes" : 4, "cherry" : 8, "dates" : 10}
sorted_fruits = dict(sorted(fruits_dict.items(), key= lambda item: item[1]))
print(sorted_fruits)

# Function definition is here
add = lambda arg1, arg2: arg1 + arg2;

# Now you can call add as a function
print("Sum of total numbers:", add(2, 8))
print("Sum of total numbers:", add(80, 40))

# Scope of Variables
#  Global Variables
#  Local Variables

left_amount = 0;     # This is global variable.

# Function definition is here

def sub(para1, para2):
   # Subtract both the parameters and return them."
   left_amount = para1 - para2   # Here left amount is local variable.
   print("Inside the function local total : ", left_amount)
   return left_amount;

#  Now you can call the sub func
sub(50, 25)
print ("Outside the function global total : ", left_amount)


# Arbitrary Keyword Arguments, **kwargs

def my_function(**kwargs):
   # kwargs is now dictionary
    print(kwargs)

my_function(name="Arshi", age=22, City="Islamabad")

def greet(**info):
    for key, value in info.items():
        print(f"{key} is {value}")

greet(name="Arisha", age=22, city="Makkah")

def my_function(**student):
   print("\n His last name is" + " " + student["last_name"])
   for key, value in student.items():
      print(key, value)
   print(student)

my_function(first_name = "Hooria", last_name = "Fatima")
my_function(first_name = "Hooria", last_name = "Fatima", course = "Python - 101", day="Monday", time="14:00 - 17:00")
my_dict = {"first_name": "Arisha", "last_name": "Fatima", "course":"101 - 201", "day":"Saturday | Monday", "role":"Student"}

# my_function(my_dict)    # TypeError
my_function(**my_dict)    # use ** to unpack the dictionary


# Generator Function

def my_generator():
    yield 3
    yield 2
    yield 1
    yield 0

# Create a generator object
gen = my_generator()

print(gen, ":" , type(gen))
# print(next(gen)) 
# print(next(gen)) 
# print(next(gen))  

#  Iterate over the generator
for value in gen:
    print(value, " : ", type(value))

# Lets produce an error:
# print(next(gen))      # error: StopIteration

print("\n---------------\n")

# Example 2: Infinite Sequence

def infinite_sequence():
   num = 0
   while True:
      yield num    # Since yield pauses execution, it remembers the state and resumes from there when next() is called.
      num += 1

# create a generator object
gen = infinite_sequence()    # initializes the generator.

# Print the first 5 numbers, _ is a throw away variable
for _ in range(6):
   print(next(gen))   # The next time we call next(gen), execution resumes from where it left off.

print("\n ------- \n")

def infinite_loop():
   num = 0
   while True:
      num += 1
      print("Infinite Loop:", num)

# infinite_loop()

# Generator Expressions

gen = (x * x for x in range(5))
print( type(gen))

# Iterate over the generator
for value in gen:
   print(value, type(value))

# Recursive Function in Python

# Example: Factorial of a Number

def factorial(n):
   # Base case
   if n == 0:
      return 1
   # Recursive case
   else:
      return n * factorial(n - 1)

print(factorial(6))  #  6! = 6 * 5 * 4 * 3 * 2 * 1 = 720 factorial(0) returns 1


# Example: Fibonacci Sequence

def fibonacci(n):
   # Base case
   if n == 0:
      return 0
   elif n == 1:
      return 1
   # Recursive case
   else:
      return fibonacci(n - 1) + fibonacci(n - 2)
   
print(fibonacci(8))   # 0, 1, 1, 2, 3, 5, 8, 13, 21

def factorial(n):
   if n == 0:
      return 1
   else:
      return n * factorial(n - 1) 

number = 6
result = factorial(number)
print(f"The factorial of {number} is {result}")

# Multi Type Return in Function

def get_user_info():
   name = "Areesha"
   hobbies = ["coding", "reading", "writing"]
   stats = {"age" : 22, "level" : "beginner"}
   return name, hobbies, stats   # return in tuple

info = get_user_info()
print(info, type(info))

# Type Annotations ( for more readable code)
from typing import Tuple, List, Dict

def get_data() -> Tuple[int, List[str], Dict[str, int]]:
   return 200, ["done", "successful"], {"code" : 6}
data = get_data()
print(data, type(data))

def example_function(a: int, b: int=0, *args: float, **kwargs: str) -> Tuple[int, List[float], Dict[str, str]]:
   sum = a + b
   args_list = list(args)  # Convert tuple into list
   return sum, args_list, kwargs

result = example_function(1, 2, 6.2, 4.5, 2.2, name = "Robert", city = "Karachi", country = "Pakistan")
print(result)

result = example_function(20, *[2.0, 3.0, 5.0], **{"language" :"Arabic", "Country" : "Saudia Arabia"})
print(result)

# Python’s Precedence Rules for Name Resolution

# This is based on something called the LEGB rule,it defines the order in which Python looks for names (variables, functions, etc.).
#  L → Local
# Inside the current function or method.
#  E → Enclosing
# Functions inside other functions (closures).
#  G → Global
# Top-level of the script/module.
#  B → Built-in
# Python’s built-in names like len, sum, etc.

# Full LEGB Precedence Example in One Go:

from math import *

print("Math: pi =", pi )

pi = 1
print("Global pi =", pi)

class MyClass:
   pi = 2
   print("MyClass pi =", pi)

def my_function():
   pi = 3
   print("my_function pi =", pi)

   def inner_function():
      pi = 4
      print("inner_function pi =", pi)

   inner_function()
my_function()

print("\n --- \n")

# This is a GLOBAL variable
total_clicks = 0

def web_page():
   # This is an ENCLOSING variable
    page_views = 100

    def click_button():
       # Let Python know we want to use and change the global variable
       global total_clicks

       # Let Python know we want to change the 'page_views' in the outer function
       nonlocal page_views

       # Now we modify both
       total_clicks += 1
       page_views += 1

       print("Inside Click Button()")
       print("Total clicks(global):", total_clicks)
       print("page views(enclosing):", page_views )

    # Call the inner function
    click_button()

    # Check the value of page_views after inner function ran
    print("After click_button(), page_views:", page_views)

# Call the outer function
web_page()

# Check the global total_clicks value
print("After webpage(), total_clicks:", total_clicks)





























