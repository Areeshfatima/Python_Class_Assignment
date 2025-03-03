# Keywords in Python
# Keywords in Python are reserved words that have special meanings and cannot be used as variable names, function names, or identifiers.
# Python has a set of built-in keywords that define the syntax and structure of the language.

# 1.False 

can_vote: bool = False

print(can_vote)
print(int(False))   #False integer version is 0

# None  represents absence of value , no value

x = None
print(type(x) , x)

logged_in = None
print(logged_in)

# True 

can_vote: bool = True

print(can_vote)
print(int(can_vote))   #True integer version is 1

print(True + True)  #output is 2

# if

x: int = 5
y: int = 6
z: int = 8

if z > y and z > x:
    print("Both conditions are True..!!")


marks = int(input("Your marks: "))


if(marks >= 90):
    print("Your grade is A+1")


# as

import math as mt
from random import randint as ra


print(mt.cos(10))
print(ra(10 , 20))


try:
    with open("nextjs.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'nextjs.txt' was not found. Please check the file path.")


# assert
# The assert keyword in Python is used for debugging and testing. 
# It checks whether a given condition is True, and if not, it raises an AssertionError. 
# This helps in catching bugs early during development.

m = 10
assert m > 5  # No error because the condition is True
print("Assertion passed!")  

n = 2
# assert n > 5, "x should be greater than 5"  #shows an AssertionError


def square(a):
    return a * a

assert square(3) == 9  # Passes
assert square(4) == 16  # Passes
assert square(5) == 25  # Passes
# assert square(6) == 35  # Fails, AssertionError

# async

import asyncio

async def learning():
    print("Learning")
    await asyncio.sleep(2)  #delay
    print("Python")

asyncio.run(learning())


# await
# The await keyword pauses the execution of an async function until the awaited task completes.

import asyncio

async def task1():
    print("Task 1: Start")
    await asyncio.sleep(2)  #wait
    print("Task 1: Done")

async def task2():
    print("Task 2: Start")
    await asyncio.sleep(1)
    print("Task 2: Done")

async def main():
    await task1()
    await task2()

asyncio.run(main())










