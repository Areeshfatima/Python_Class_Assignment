# Lists in Python
# Ordered: Lists are ordered, meaning that the items in the list have a specific order and can be accessed by their index.
# Mutable: Lists are mutable, meaning that they can be modified after they are created.
# Indexed: Lists are indexed, meaning that each item in the list has a specific index that can be used to access it.
# Dynamic size: Lists can grow or shrink dynamically as elements are added or removed.
# Heterogeneous: Lists can contain elements of different data types, such as integers, strings, floats, and other lists.
# Supports duplicate values: Lists can contain duplicate values.

# Creating a list with different data types

fav_subjects: list[str] = ["Math's", "Accounting", "Islamiat", "English"]
roll_numbers: list[int] = [1, 2, 3, 6, 9]
all_in_one: list = ["Math's", 6, True]

print("fav_subjects =", fav_subjects)
print("roll_numbers =", roll_numbers)
print("all_in_one =", all_in_one)

# Accessing List Element
# access elements using indexing(starting from 0) and negative indexing (starting from -1)

baskets: list[str] = ["fruits", "vegetables", "drinks", "cake"]
print(baskets[0])
print(baskets[-2])

# Modifying lists

baskets_items: list[str] = ["fruits", "vegetables", "drinks", "cake"]
baskets_items[-3] = "chips"      # replacing vegetables with chips
print(baskets_items)

# Lists Slicing
# Extract multiple elements using slicing.

print(baskets_items[0:3])    # 0, 1 and 2

# Common Lists method
# Appending and Expending Lists

baskets_items.append("biscuits")   # add single  element at the end 
print(baskets_items)

baskets_items.extend(["pastries", "eggs"])   # add multiple elements
print(baskets_items)

# Removing elements
# In Python, remove() and pop() are two distinct methods used to manipulate lists.
#  While they may seem similar, they have different purposes and behaviors.

# Remove() Method:
# Key aspects of remove():
# Value-based: remove() searches for a specific value in the list.
# Returns None: The remove() method does not return any value.
# Raises ValueError: If the value is not found in the list, a ValueError exception is raised.

baskets_items.remove("chips")  
print(baskets_items)    


# baskets_items.remove("vegetables")  
# print(baskets_items)     # raise an error "value error"

# Pop() method
# The pop() method is used to delete an item at a specified index from a list. If no index is provided, it removes and returns the last item in the list.
# Key aspects of pop():
# Index-based: pop() searches for an item at a specific index in the list.
# Returns the removed item: The pop() method returns the item that was removed from the list.
# Raises IndexError: If the index is out of range, an IndexError exception is raised.

deleted_element = baskets_items.pop(2)   # remove and return an element at index 2
print("deleted_element: ", deleted_element)
print(baskets_items)

# Sorting a list

# Default sorting(Ascending order)
numbers: list[int] = [4, 5, 8, 9, 10, 1]      # unsorted list
numbers.sort()
print(numbers)

# Sorting in descending order(reverse= True)

numbers: list[int] = [4, 5, 7, 8, 1]
numbers.sort(reverse = True)
print(numbers)

#  Sorting by string length(key= len).

good_name: list[str] = ["Arisha", "Ali", "Ayan", "Hooriya"]
good_name.sort(key=len)
print(good_name)

# sorting by last character(key=lambda word:word[-1]

good_name: list[str] = ["Arisha", "Ali", "Ayan", "Hooriya"]
good_name.sort(key= lambda word:word[-2])
print(good_name)


# Reverse sorting

class_name: list[int] = [2, 4, 6, 7, 8]
class_name.reverse()
print(class_name)

# Iterating over list
# Use loops to process elements in a list.
# Using a for-loop

quote: list[str] = ["Consistency", "is", "the", "key"]
print(quote)
for words in quote:
    print(words)


# Using List Comprehension

# Without using if condition

squared: list = [x ** 2 for x in [1,  2, 3, 4, 5]]

print(squared, ":", type(squared))


# With using if statement

squared: list = [x ** 2 for x in [6, 8, 10, 12, 14] if x > 10]

print(squared, ":", type(squared))














   


