# Tuples in Python
# A tuple is an ordered, immutable (unchangeable) sequence of elements. Tuples are useful for fixed data collections.
# In Python, a tuple is an immutable data type. This means that once a tuple is created, its elements cannot be changed, added, or removed.
# 1. Cannot Modify Elements: Once a tuple is created, you cannot change its elements.
# 2. Cannot Add or Remove Elements: You cannot add new elements to a tuple or remove existing ones.

# Immutable: Since tuples cannot be changed, they are safer to use when you want to ensure that the data remains constant.
# Hashable: Tuples can be used as keys in dictionaries because they are immutable.
# Performance: Tuples are generally faster than lists because of their immutability.

# Creating a Tuple

stationary: tuple = tuple(["pencil", "ruler", "remover", "ink"])   # cast a list into tuple
rank: tuple = (1, 2, 3)    # tuple
result: tuple = ("Hooriya", 1, 95.6, True)  # tuple

print("Stationary:", stationary)
print("Rank:", rank)
print("Result:", result)

# Even though tuples are immutable,Python may create new instances in memory when you define identical tuples in separate assignments.

class_students: tuple = ("Hooriya", "Malaika", "Manahil", "Eshal")   # unique memory address
position_holders: tuple = ("Hooriya", "Malaika", "Manahil", "Eshal") # unique memory address

print("id(class_students):", id(class_students))
print("id(position_holders):", id(position_holders))

print("class_students == position_holders:", class_students == position_holders)  # comparing by value

roll_num: tuple = (1, 2, 3, 4, 6)
serial_num: tuple = (1, 2, 3, 4, 6)

print("id(roll_num) = ", id(roll_num))
print("id(serial_num) = ", id(serial_num))

#  Create an error
# roll_num[0] = 2   immutable(typeError)

# Tuples in Python
# A tuple is an `ordered`, `immutable` (unchangeable) sequence of elements.
# Tuples are useful for fixed data collections.

# Creating a tuple

rainbow_colors: tuple = tuple(["red", "blue", "green", "yellow", "indigo", "orange", "violet"])
table_of_4: tuple = (4, 8, 12, 16, 20, 24, 28)
mixed_tuple: tuple = ("Perfect", 69, 5.9, True)

print("rainbow_colors:", rainbow_colors)
print("table_of_04", table_of_4)
print("mixed_tuple", mixed_tuple)

# Accessing elements in a tuple
print("rainbow_colors[0] =", rainbow_colors[0])  

# Tuple slicing
print("table_of_04[3:] =", table_of_4[3:])

# Tuple length
print("Length of mixed_tuples =", len(mixed_tuple))

# Iterating through a tuple
print("Iterating through rainbow_colors:")
for item in rainbow_colors:
    print(item)

# Checking if an item exists in a tuple
print("Is 12 in table_of_04:", 12 in table_of_4)

# Concatenating tuples
tuple1: tuple = rainbow_colors + table_of_4
print("rainbow_colors + table_of_4 =", tuple1)

# Repeating tuples
tuple2: tuple = table_of_4 * 2
print("table_of_4 * 2 =", tuple2)

# Nested tuples
nested_tuple: tuple = (table_of_4, mixed_tuple)
print("Nested Tuple:", nested_tuple)

# Unpacking tuples
a, b, c, d, e, f, g = table_of_4
print("Unpacking tuple:", a, b, c, d, e, f, g)

# Using tuples as keys in dictionaries (because they are immutable)
my_dict = {rainbow_colors: "This is the tuple key", table_of_4: "This is the tuple key"}
print("Dictionary with tuple keys:", my_dict)

#Trying to modify a tuple will result in a TypeError
# mixed_tuple[2] = 6.8    # immutable can't modify

print(rainbow_colors[3])
print(rainbow_colors[-4])
print(rainbow_colors.count("red"))
print(rainbow_colors.index("red"))


# error
# rainbow_colors.sort()
# rainbow_colors.reverse()
# rainbow_colors.append("grey")
# rainbow_colors.extend(["aqua", "black"])
# rainbow_colors.remove("orange")
# deleted = rainbow_colors.pop(1)

# Get a list of all attributes and methods of a tuple
tuple_methods: list = [method for method in dir(tuple) if not method.startswith("__")]

# Print the list of methods (excluding dunder methods)
print(tuple_methods)

# Python is Type Hint Language

age: int = input("Enter you age: ")
print(age, type(age))

