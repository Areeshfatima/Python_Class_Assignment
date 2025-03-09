# Membership Operators
# Used to check if a value is present in a sequence.

# Using 'in'
summer_fruits: list[str] = ["Mango", "Banana", "Apple"]

print("Mango" in summer_fruits)   # True, "Mango" is in the list


multiple_of_2: list[int] = [2, 4, 6, 8, 10, 12]

print("multiple_of_2 =", multiple_of_2)      # [2, 4, 6, 8, 10, 12]
print("6 in multiple_of_2 =", 6 in multiple_of_2)    # True

# Using 'not in'

print("9 not in multiple_of_2 =", 9 not in multiple_of_2)   # True


islamic_month: str = "Ramadan Kareem"

print("islamic_month =", islamic_month)    # Ramadan Kareem
print("K in islamic_month =", "K" in islamic_month)   # True
print("Happy not in islamic_month =", "Happy" not in islamic_month)  # True
print("Ramadan not in islamic_month =", "Ramadan" not in islamic_month) # False




