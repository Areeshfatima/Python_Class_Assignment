# A dictionary is a collection of key-value pairs. It is:
# Ordered (since Python 3.7): Items are stored in the order they were inserted.
# Mutable: Items can be added, removed, or modified after the dictionary is created.
# Un-indexed: Items are accessed using keys, not indices.
# Without duplicates: Keys must be unique, but values can be duplicated.

# Creating a Dictionary
# Dictionaries are created using curly braces {} with key-value pairs separated by commas.

passed_class: dict = ["I", "II", "III", "IV", "V", "VI", "VII"]
print(passed_class)

student_details: dict = {
    "name" : "Fatima",
    "age" : 14,
    "passed_class" : passed_class
}

print(student_details)

# using dict() constructor

passenger: dict = dict(name = "Noor-e-Haram", age = 24, city = "Antalya")
print(type(passenger), passenger)

# Accessing values
# You can access the value associated with a key using square brackets [] or the get() method.

# Access values using keys
print(passenger["name"])
print(passenger.get("age", "40"))   # if not found it will return 40 (default value)

# Access a non-existent key
print(passenger.get("country", "default_value_key_not_found"))

# Modifying a Dictionary
# You can add new key-value pairs or modify existing ones.

# Add a new key-value pair
passenger["email"] = "haram@gmail.com"
print(passenger)

#  Modify an existing value
passenger["age"] = 25
print(passenger)

# Deleting Items
# You can remove a key-value pair using the del keyword or the pop() method.
# Note that pop() returns the value of the removed key-value pair, whereas del does not return anything.

# Remove a key-value pair using del
del passenger["city"]
print(passenger)

# Remove a key-value pair using pop
age: int = passenger.pop("age", -1)
print("Removed age:", age)

print("\n")

#Again remove a key which is already removed to check the default value
age: int = passenger.pop("age", -1)
print("Key not found! Default value is:", age)

# Dictionary Methods

# Get all keys
print("passenger.keys()=",passenger.keys())  

# Get all values
print("passenger.values()=", passenger.values())

#  Get all key-value pairs
print("pasenger.items() =", passenger.items())

# Update the dictionary
passenger.update({"country" : "Turkey", "token_num" : 45})
print("After: passenger.update =", passenger)

# Clear the dictionary
passenger.clear()
print("After: passenger.clear() =", passenger)

# Duplicate Key Not Allowed
# Dictionaries cannot have two items with the same key:

duplicate_dict: dict = {
    "clothing_brand" : "Sapphire",
    "popular" : "women's wear",
    "year" : 2014,
    "year" : 2016     # this will overwrite the previous key:vlaue
}
print("duplicate values not allowed :", duplicate_dict)

# Iterating Over a Dictionary
# You can loop through a dictionary using for loops.

for key in duplicate_dict:
    print(key)

    for key, value in duplicate_dict.items():
        print(key, " : ", value)


# Common Pitfalls
# Using a non-existent key without checking first for e.g.

print(student_details.get("name_1"))    # None
print(student_details.get("name_1", "Not found default error"))   # Not found default error
# print(student_details["name_1"])   # Raise KeyError


# generate a working example of all dictionary function

my_dict = {
  "name": "Albert",
  "age": 40,
  "city": "Norway"
}

# 1. Accessing Items
print("1. Accessing Items")
print("Name:", my_dict["name"])     # by key
print("Age =", my_dict.get("age"))  # using get
print("City =", my_dict.get("city"))

# 2. Adding Items
print("\n2. Adding Items")
my_dict["email"] = "albert321@gmail.com"
print("After adding Email:", my_dict)

# 3. Modifying Items
print("\n3. Modifying Items")
my_dict["age"] = 45
print("After modifying age =", my_dict)

# 4. Removing Items
print("\n4. Removing Items")
my_dict.pop("city")
print("Dictionary after removing city:", my_dict)

del my_dict["age"]
print("After removing age with del:", my_dict)

# 5. Dictionary Methods
print("\n5. Dictionary Methods")
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print( "Items:", my_dict.items())

# 6. Clearing the Dictionary
print("\n6. Clearing the Dictionary")
my_dict.clear()
print("Dictionary after clearing:", my_dict)

# Adding items back for further examples

my_dict2 = {
  "name": "William",
  "age": 35,
  "city": "Toronto"
}

# 7. Updating the Dictionary
print("\n7. Updating the Dictionary")
my_dict2.update({"age" : 25, "country" : "Canada"})
print("After updating:", my_dict2)

# 8. Iterating Through a Dictionary
print("\n8. Iterating Through a Dictionary")
for value in my_dict2.values():
    print(value)

print("\nIterating through items (key-value pairs):")
for key, value in my_dict2.items():
    print(f"{key} : {value}")

#9 checking if a key exist
print("\n9. checking if a key exist")
if "name" in my_dict2:
    print("Name exist")
else:
    print("Name do not exist")

# 10. Dictionary Length
print("\n10. Dictionary Length")
print("Length of the dictionary:", len(my_dict2))

# 11. Creating a dictionary from iterable
print("\n11. Creating a dictionary from iterable")
iterable = [("country1", "Pakistan"), ("country2", "Saudia Arabia"), ("country3", "Turkey")]
new_dict = dict(iterable)
print("new dictionary:", new_dict)

# 12. Copying a dictionary
print("\n12. Copying a dictionary")
copied_dict = my_dict2.copy()
print("Copied dictionary:", copied_dict)

# 13. Nested Dictionaries
print("\n13. Nested Dictionaries")
nested_dict = {
    "person1": {"name": "Ali", "age": 14},
    "person2": {"name": "Ayan", "age": 19}
}
print("Nested dictionary:", nested_dict)
print("Ali's age:", nested_dict["person1"]["age"])

# Dictionary Comprehensions
# key_expression: value_expression for item in iterable if condition}

original_dict = {"a" : 2, "b" : 4, "c" : 6, "d" : 8}
print("Original Dict =", original_dict)
double_dict = {k: v * 2 for k, v in original_dict.items()}
print("Double Dict =", double_dict)





