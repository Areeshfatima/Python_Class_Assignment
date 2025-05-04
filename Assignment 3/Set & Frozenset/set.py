# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is:unordered, unindexed, mutable
# An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear more than once.


even_num: set = {6, 12, 18, 24}
table_of_06: set = set([6, 12, 18, 24])
unknown: set = {} # set or dictionary
empty_set: set = set()

print("even_num = ", even_num)
print("table_of_06 = ", table_of_06)
print("type(even_num) = ", type(even_num))
print("type(table_of_06) = ", type(table_of_06))
print("type(unknown) = ", type(unknown))
print("type(empty_set) = ", type(empty_set))
print("even_num == table_of_06 = ", even_num == table_of_06)

# Holds only Immutable Objects
# A set can store only immutable objects such as number (int, float, complex or bool), string or tuple.
# If you try to put a list or a dictionary in the set collection, Python raises a TypeError.

# odd_num = {[1, 3, 5, 7, 9, 11]} # TypeError: unhashable type: 'list'
# print(odd_num)

# It can hold multiple data types at once.

multi_type_set: set = {8, 9.0, False, True, "Learning! Python", (1,5,9,'say') }
print(multi_type_set)

# The set is unordered

programming_lang: set = {'Java', 'Python', 'JavaScript', 'TypeScript'}
print(programming_lang)

# The set can not be Change Directly using [ ]

# Create a set
my_num: set = {1, 2, 3, 4, 5}
print(my_num)  # Output: {1, 2, 3, 4, 5}

# Try to change an item (this will raise an error)
try:
    my_num[0] = 10  # Sets are unordered, so indexing doesn't work
except TypeError as e:
    print(e)  # Output: 'set' object does not support item assignment

name_of_days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(name_of_days)

# Remove an items
name_of_days.remove("Wednesday")
print(name_of_days)

name_of_days.add("Days of the week")
print(name_of_days) 

name_of_months = {"January", "February", "August", "September", "October"}
print(name_of_months)

# discard() only removes a single element
print(name_of_months.discard({"January", "February"}))   # return None

# To remove multiple elements, iterate and discard each one individually:
for item in {"January", "February"}:
    name_of_months.discard(item)

print("After removing multiple elements:", name_of_months)

# Use difference_update() method to remove multiple element at once.

islamic_month_name = {"Muharram", "Safar", "Rabi-ul-Awwal", "Ramadan"}
print("Before islamic_month_name:", islamic_month_name)

islamic_month_name.difference_update({"Safar", "Muharram"})
print("After islamic_month_name:", islamic_month_name)

# Add multiple items
islamic_month_name.update(["Shaban", "Dhul-Hijjah", "Shawwal"])
print(islamic_month_name)

# Using the union() method or | operator:

# Using the union() method:
my_set_1: set   = {1, 2, 3, 4, 5, 7}
my_set_2: set = {4, 5, 6, 7}

my_set_3 = my_set_1.union(my_set_2)
print(my_set_3)

# Using the | operator:
my_set1: set   = {1, 2, 3, 5, 7}
my_set2: set = {1, 5, 6, 7, 8, 9}

my_set3: set  = my_set1 | my_set2    # operator
print(my_set3)

# Unique Elements
my_set: set = {1,2,3,4,5, "Learning! Python"}
print("Before : ", my_set)

my_set.add(4)
my_set.add("Learning! Python")

print("After  : ", my_set)

# discard() and remove() methods

# Lets create an error to understand
num_set: set = {1,2,3}

# num_set.remove(4)
# print(num_set)

print("Before pop() = ", num_set)

#When you call `my_set.pop()`, it removes and returns an arbitrary element from the set.
#Since sets are unordered data structures, the element that is removed and returned is not predictable.
my_set.pop()
print("Before pop() = ", my_set)

num_set = {1,2,3}

num_set.discard(4)    # method
print(num_set)

# The Inner Working of SET (Advance Topic)
# The Hashing

# Initial set
my_odd = {1, 3, 5, 7, 9}
print(my_odd) 


# Adding an element
my_odd.add(13)
print(my_odd)  # The order might change unpredictably


# Removing an element
# my_odd.remove(15)
# print(my_odd)  # Again, the order can change

# The Hashing

x: str = "Coding Vibes!"
y: str = "Coding Vibes!"

print("id(x) = ", id(x))
print("id(y) = ", id(y))

# using hash
print("hash(x) =", hash(x))
print("hash(y) =", hash(y))
print("\n----\n")
print("hash(x)=", hash(x))
print("x.__hash__() =", x.__hash__())   # __dunder__()

# TypeError: unhashable type: 'set'
# my_set: set   = {1,2,3,4,5, "Learning Programming!"}
# my_dict: dict = {my_set: "Learning Programming!"} # dictionary only accept immutable objects as a key
# print(my_dict)

# Understanding Rehashing and Changing Order

# Set Order Can Change Dynamically
# Initial set
num_of_set = {10, 3, 5, 8}
print(num_of_set)  

# Adding an element
num_of_set.add(20)
print(num_of_set)  # The order might change unpredictably

# Removing an element
num_of_set.remove(10)
print(num_of_set)  # Again, the order can change

# Frozenset
# frozenset is hashable and can be used as dictionary keys, unlike regular sets.

my_frozenset: frozenset = frozenset([1,2,3, "Hello! World"])
print("my_frozenset  = ", my_frozenset)

my_set: set = {1,2,3, "Hello! World"}
my_frozenset2: frozenset = frozenset(my_set)
print("my_frozenset2 = ",my_frozenset2)

# Set Method
visited_cities = {"Karachi", "Istanbul", "Makkah", "Toronto", "Islamabad"}
popular_cities = {"Makkah", "Istanbul", "Karachi", "Islamabad"}
popular_capitals = {"Islamabad", "Ankara", "London", "Tokyo", "Paris"}

print(visited_cities.difference(popular_cities, popular_capitals))   # Returns a set containing the difference between two or more sets
print(visited_cities.intersection(popular_cities, popular_capitals)) # Return a set that contains the items that exist in both set
print(visited_cities.union(popular_cities, popular_capitals))        # Return a set that contains all items from both sets, duplicates are excluded:
print(visited_cities.symmetric_difference(popular_capitals))         # argument only, Return a set that contains only unique items from both sets

print(visited_cities.isdisjoint(popular_cities)) # Return True if no items in set x is present in set y


popular_cities = {"Makkah", "Istanbul", "Karachi"}

print(visited_cities.issuperset(popular_cities))  # Return True if all items in set x are present in set y
print(popular_cities.issubset(visited_cities))    

# Example of frozenset()

frozen_set1: frozenset = frozenset([2, 4, 6, 8])
frozen_set2: frozenset = frozenset([1, 3, 5, 7])
frozen_set3: frozenset = frozenset([1, 2])

#  1.difference(): Returns a new frozenset with elements present in the first frozenset but not in the second.
difference_set: frozenset = frozen_set1.difference(frozen_set2)
print(f"difference(): {difference_set}") 


#  2.intersection(): Returns a new frozenset containing only elements common to both frozensets.
intersection_set: frozenset = frozen_set1.intersection(frozen_set2)
print(f"intersection(): {intersection_set}")   # empty frozenset

# 3.union(): Returns a new frozenset containing all unique elements from both frozensets.
union_set: frozenset = frozen_set1.union(frozen_set2)
print(f"union(): {union_set}") 

# 4.symmetric_difference(): Returns a new frozenset with elements that are in either of the sets but not in both.
symmetric_difference_set: frozenset = frozen_set1.symmetric_difference(frozen_set2)
print(f"symmetric_difference(): {symmetric_difference_set}") 


# 5.isdisjoint(): Returns True if the two frozensets have no elements in common; otherwise, False.
print(f"isdisjoint(): {frozen_set1.isdisjoint(frozen_set2)}")  # Output: True
print(f"isdisjoint(): {frozen_set1.isdisjoint(frozenset([4,6]))}")  # Output: False

frozen_set3 = {2, 8, 4}

# 6.issubset(): Returns True if all elements of the first frozenset are present in the second frozenset.
print(f"issubset(): {frozen_set3.issubset(frozen_set1)}")  # Output: True
print(f"issubset(): {frozen_set1.issubset(frozen_set3)}")  # Output: False


# 7.issuperset(): Returns True if all elements of the second frozenset are present in the first frozenset.
print(f"issuperset(): {frozen_set1.issuperset(frozen_set3)}")  # Output: True
print(f"issuperset(): {frozen_set3.issuperset(frozen_set1)}")  # Output: False


# 8.copy(): Returns a new frozenset that is a shallow copy of the original.
copy_set: frozenset = frozen_set3.copy()
print(f"copy(): {copy_set}")  
print(f"copy() is same object?: {copy_set is frozen_set3}") # Output: False 


# GC: Garbage Collection
# Python has a garbage collection mechanism.
# Python's garbage collector is a Memory Management System that automatically frees up memory occupied by objects that are no longer needed or referenced. 
# This helps prevent memory leaks and allows Python to manage memory efficiently.

import gc

gc.collect()
print(gc.get_count())  # prints the number of collected objects, unreachable objects, and reference cycles



