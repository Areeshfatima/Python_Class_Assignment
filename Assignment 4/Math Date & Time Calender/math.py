# The Date & Time
# What are Tick Intervals
# Time intervals are floating-point numbers in units of seconds.
# We called tick(on each seconds).

# What is Epoch?
# In Python, the epoch is a reference point in time from which time is measured. 
# It's the moment when time "begins" for a particular system or standard.

# How is the epoch used in Python?
# Python's time module provides functions to work with time based on the epoch:
# time.time(): Returns the current time as a floating-point number of seconds since the epoch.
# time.gmtime(seconds): Converts seconds since the epoch to a time tuple in Coordinated Universal Time (UTC).
# time.localtime(seconds): Converts seconds since the epoch to a time tuple in local time.

import time    # This is required to include time module.

ticks = time.time()
print("Number of ticks since January 1st, 1970:", ticks)

# Getting the Current Time
# To translate a time instant from seconds since the epoch floating-point value into a time-tuple, 
# pass the floating-point value to a function (e.g., localtime) that returns a time-tuple with all valid nine items.

import time

local_time = time.localtime(time.time())
print("Local current time:", local_time)

# Getting the Formatted Time
# You can format any time as per your requirement, but a simple method to get time in a readable format is asctime()

import time

local_time = time.asctime(time.localtime(time.time()))
print("Local Current Time:", local_time)

# The Calendar

# Getting the Calendar for a Month
# The calendar module gives a wide range of methods to play with yearly and monthly calendars. 
# Here, we print a calendar for a given month (Oct 2025).

import calendar

cal = calendar.month(2025, 10)
print("Here is the Calender:")
print(cal)


# The Date Time
from datetime import date

date1 = date(2017, 2, 2)
print("Date1:", date1)
date2 = date(2011, 6, 13)
print("Date2:", date2)

import datetime

x = datetime.datetime.now()   #The date contains year, month, day, hour, minute, second, and microsecond
print(x)
    
# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

import datetime

x = datetime.datetime(2025, 2, 2)

print(x.strftime("%f"))  # Display Microsecond 000000-999999
print(x.strftime("%A"))  # Display the name of the Day
print(x.strftime("%Y"))  # Display the year
print(x.strftime("%B"))  # Display the name of the month

# Python Math Module
# The math module is a built-in module in Python that is used for performing mathematical operations. 
# This module provides various built-in methods for performing different mathematical tasks.

import math

# In Python, abs() is a built-in function, which means it's a global function

# 1. abs(x) – Absolute Value
# Returns the positive version of any number.

print("abs(-6) = ", abs(-6))  # 6

# 2. pow(x, y) – Power Function
# Raises a number to the power of another.

print("pow(3, 3) =", pow(3, 3))  # 3 x 3 x 3 = 27

# 3. round(number, digits)
# Rounds a number to the nearest given decimal places.

print("round(5.4200, 2) =", round(5.4200, 2))  # 5.42

# 4(a). max() returns the largest of a set of numbers
print("max(1, 6, 4) =", max(1, 6, 4))  # 6

# 4(b). min() returns the smallest of a set of numbers
print("min(1, 6, 4) =", min(1, 6, 4))  # 1


# The math Module (Needs import math)
# This module offers advanced mathematical functions, including trigonometry, constants like π, and logarithmic/exponential tools.

# 5. math.sin(x)
# returns the sine of an angle in radians
print("math.sin(math.pi/2) =", math.sin(math.pi/2))

# 6. math.cos(x)
# returns the cosine of an angle in radians
print("math.cos(0) =", math.cos(0))

# 7. math.tan(x)
# returns the tangent of an angle in radians
print("math.tan(math.pi/4) =", math.tan(math.pi/4))

# 8. math.sqrt(x) – Square Root
#  returns the square root of a number
print("math.sqrt(8) =", math.sqrt(8))

# 9. math.factorial(x) – Factorial
# returns the factorial of a number
print("math.factorial(5) =", math.factorial(5))

# Logarithmic Functions

# 10. math.log(x) – Natural Log (base e)
# returns the natural logarithm of a number
print("math.log(10) =", math.log(10))

# 11. math.log10(x) – Base-10 Logarithm
# returns the base-10 logarithm of a number
print("math.log10(100) =", math.log10(100))

# 12. math.exp(x) – e^x (exponential)
# returns the value of e raised to a power
print("math.exp(2) =", math.exp(2))

# Rounding Up/Down

# 13. math.ceil(x) – Round UP
# returns the smallest integer greater than or equal to a number
print("math.ceil(4.7) = ", math.ceil(4.7)) 

# 14. math.floor(x) – Round DOWN
# returns the largest integer less than or equal to a number
print("math.floor(4.7) = ", math.floor(4.7)) 

# Mathematical Constants
# These are predefined values used in science, engineering, or geometry.

# 5. math.pi – π (3.14159...)
# math.pi is a constant representing the ratio of a circle's circumference to its diameter
print("math.pi = ", math.pi) 

# 16. math.e – Euler’s Number (2.718...)
# math.e is a constant representing the base of the natural logarithm
print("math.e = ", math.e) 

# 17. math.tau – Tau (2π)
# math.tau is a constant representing the ratio of a circle's circumference to its radius
print("math.tau = ", math.tau)  

# Special Constants

# 18. math.inf – Infinity
# math.inf is a constant representing infinity
print("math.inf = ", math.inf) 

# 19. math.nan – Not a Number
# math.nan is a constant representing "not a number"
print("math.nan = ", math.nan) 


# ZeroDivisionError

result = 10 / 0
print(result)  # nan

# NaN
# In Python, NaN stands for "Not a Number".It's a special floating-point value that represents an undefined or unrepresentable numerical result.
# It's a way for Python to indicate that a calculation or operation couldn't produce a valid numerical outcome.

result = float("nan")  # Explicitly creating NaN
print(result)

# Working with NaN:
# Checking for NaN: You can use the math.isnan() function to check if a value is NaN

import math

x = float("nan")
if math.isnan(x):
    print("x is NaN")

print(type(math.nan))


# NaN compares unequal to any number, including itself.
# So, NaN == NaN is False. Calculations involving NaN often result in NaN.

x = float('nan')
y = float('nan')

print( x == y) # prints False
print(x is y)  # prints False

print(id(x))
print(id(y))

# Infinity
# In Python, math.inf represents positive infinity, and it is indeed displayed as inf when you print it.

import math

positive_infinity = math.inf
print(positive_infinity)  # Output: inf
print(type(positive_infinity))  # Output: <class 'float'>


negative_infinity = -math.inf # Negative infinity
print(negative_infinity)  # Output: -inf


import math

positive_infinity_1 = math.inf
positive_infinity_2 = math.inf

print(positive_infinity_1 - positive_infinity_2)  # Output: nan
print(positive_infinity_1 * 2)  # Output: inf


import math

positive_infinity = math.inf
print(positive_infinity > 999999999999999999999999999999) #It's greater than any finite number.









