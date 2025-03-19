import main_functions

class Elf:
    def __init__(self,level,ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str":11, "dex":12, "con":10,
            "int":16, "wis":14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]

# A) Create an instance of Elf named Elora
elora = Elf(2)
print(elora)

# B) Create an instance of Elf named Elrond
elrond = Elf(3,{
            "str":12, "dex":13, "con":11,
            "int":17, "wis":15, "cha": 14
        })
print(elrond)

# C) Print the value of hp for Elora
print(elora.hp)

# D) Print the value of hp for Elrond
print(elrond.hp)

# E) Print the value of level for Elora
print(elora.level)

# F) Print the value of ability_scores for Elrond
print(elrond.ability_scores)

# G) Convert the elora object instantiated above into a Python dictionary
eloraD = elora.__dict__

# H) Printing its type:
print(type(eloraD))

# I) Converting elrond object instantiated above into a Python dictionary
elrondD = elrond.__dict__

# J) Printing its type:
print(type(elrondD))

# K) Printing both Elrond and Elora dictionaries
print(eloraD)
print(elrondD)

# L) Serializing both Elrond and Elora dictionaries to JSON
main_functions.save_to_file(eloraD,"elora.json")
main_functions.save_to_file(elrondD,"elrond.json")

# M) Deserializing both Elrond and Elora JSON files to Python dictionary
x = main_functions.read_from_file("elora.json")
y = main_functions.read_from_file("elrond.json")

# N) Printing their types
print(type(x),type(y))