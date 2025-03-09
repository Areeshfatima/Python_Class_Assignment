# Logical Operators
# Used to combine conditional statements.

m: bool = True
n: bool = False

# and
print("m and n =", m and n)   # False

# or 
print("m or n =", m or n)     # True
 
# not
print("not m =", not m)   # False, reverses True to False
print("not n =", not n)   # True, reverses False to True


x: int = 15

# and
print(x > 10 and x < 20)   # True, both statements are True

# or
print(x > 20 or x < 16)   # True, if at least one statement is True

# not
print(not(x > 10 and x < 20))   # False, reverses the result