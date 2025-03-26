import main_functions

#Exercise 1: Using the function 'read_from_file',
# read superCompHeroes.json as a dictionary in Python,
# and print its type to confirm:
heroes=main_functions.read_from_file("jsonFiles/superCompHeroes.json")
print(type(heroes))
#Exercise 2: Print the number of keys in superCompHeroes
print(len(heroes.keys()))

#Exercise 3: Print all the keys in superCompHeroes
print(heroes.keys())

#Exercise 4: Print the type of the value of 'members'
print(type(heroes["members"]))

#Exericse 5: Print its first element:
print(heroes["members"][0])

#Exercise 6: Print the name of the first element
print(heroes["members"][0]["name"])

#Exercise 7: Print the strength of the second member:
print(heroes["members"][1]["strength"])

#Notice that the structure of the data is: dict->list->dict->string

#Notice that the structure of the data is: dict->list->dict->int

#Exercise 8: Print the names and strengths of the Super Component Heroes
# Hint: use a for loop for the list!

for member in heroes["members"]:
    print(f"Superhero {member['name']} has a strength of {member['strength']}.")

#Exercise 9: To print members in order of strength:

#Exercise 10: Create a new Super Component Hero and using the function
# 'save_to_file', overwrite the existing 'superCompHeroes.json' with
# this new entry
# IMPORTANT: automatically typing into the JSON file is not accepted
