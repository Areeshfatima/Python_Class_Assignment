# Practical Examples
#  Building a Phonebook

# create a notebook

phonebook: dict = {
    "Duaa" : "123-456-780",
    "Arsh" : "987-456-321",
    "javeriya" : "689-456-908"
}

# Add a new contact
phonebook["Samiya"] = "567-986-003"

# Search for a contact
name: str = input("Enter a name to search:")
if name in phonebook:
    print(f"{name}'s phone number is {phonebook[name]}.")
else:
    print(f"{name} is not in the phonebook.")


# Count the frequency of words in a sentence

poem: str = '''Red light, red light, what do you say?
I say stop and stop right away.
Yellow light, yellow light, what do you mean?
I mean wait till the light turns green.
Green light, green light, what do you say?
I say go, go on your way!'''

words: list = poem.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

#  Sort the word_count dictionary by value in descending order

sorted_word_count: dict = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
print(sorted_word_count)


# Practice Exercise
# Fahrenheit is F = (C * 9/5) + 32.

print("\n-----\n")

celsius_temp = {0, 10, 20, 30, 40, 50}
fahrenheit_temp = {str(c)+"c": str((c * 9/5) + 32)+"f" for c in celsius_temp}
print(fahrenheit_temp)