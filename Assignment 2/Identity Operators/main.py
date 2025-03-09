# Identity Operators
# Used to compare objects (not just their values).

ramadan_schedule: list[str] = ["Tahajuud", "Suhoor", "Quran Recitation", "Iftar", "Taraweeh"]
obligatory_prayers: list[str] = ["Fajar", "Zuhar", "Asar", "Magrib", "Esha"]
ramadan_vibes: list = ramadan_schedule  # ramadan_vibes refers to the same object as ramadan_schedule


# Using `is` (checks if two variables point to the same object in memory)
print("ramadan_schedule is ramadan_vibes:", ramadan_schedule is ramadan_vibes)  # True (same objects, same memory space)
print("ramadan_schedule is obligatory_prayers:", ramadan_schedule is obligatory_prayers)  # False (different objects, separate memory spaces)
print("ramadan_schedule == ramadan_vibes:", ramadan_schedule == ramadan_vibes)  # True (same values)



# Using `is not` (checks if two variables point to different objects)
print("ramadan_schedule is not obligatory_prayers:", ramadan_schedule is not obligatory_prayers)  # True (different memory spaces)


print("\n")  # Separator for better output readability

# Displaying memory addresses using id()

print("id(ramadan_schedule) =", id(ramadan_schedule))
print("id(obligatory_prayers) =", id(obligatory_prayers))
print("id(ramadan_vibes) =", id(ramadan_vibes))


