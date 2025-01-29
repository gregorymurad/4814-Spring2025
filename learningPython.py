message = "Hello COP 4814"
print(message)

message2 = "Welcome to Miami"
print(message2, type(message2))

firstName = "greg"
lastName = "reis"

print(firstName + lastName)
print(firstName + " " + lastName) # concatenation
print(firstName, lastName) # printing two different values

""" 
This
is
a 
block
comment
"""

print(firstName.title())
print(firstName.upper())
print("FIU".lower())

a = 2
b = 5

print(a + b) # addition
print(a - b) # substraction
print(a * b) # multiplication
print(b / a) # division
print(a ** b) # exponentiation - a to the power of b
print(b // a) # integer division
print(b % a) # remainder of the division (modulo)

averageScore = 94.5

print(type(averageScore))
print(type(3//2))

# LISTS

professors = ["greg", "richard", "kianoosh", "mustafa", "fatima", "abdul", "patricia"]
print(professors, type(professors), len(professors))

print(professors[3])
#print(professors[7])
print(professors[-1])

print(professors[2:5]) # slicing - accessing indices 2, 3, and 4
print(professors[3:]) # starting in 3 all the way to the end
print(professors[:6]) # starting in 0 all the way to index 5

professors.sort()
print(professors)

professors.sort(reverse=True)
print(professors)

professors.append("charlyne")
print(professors)

professors.append("jason")
print(professors)

professors.extend(["leo","michael"])
print("leo and michael are added to the end of the list", professors)

# Methods so far: print, type, lower, upper, title, extend, append, len, sort

professors.remove("jason")
print("jason is removed", professors)

professors.pop(8)
print("index 8 is removed", professors)

professors.insert(4,"debra")
print("debra is added to index 4", professors)

professors[2]="kevin"
print(professors)

# For loop

for i in professors:
    print(i.title())
print("FIU")

print("greg" in professors)
print("trevor" in professors)

# Dictionaries

u = ["FIU", "Miami", 51000, 1954, True]
print(type(u), len(u))

sportsTeams = {
    "basketball" : "Miami Heat",
    "football" : "Miami Dolphins",
    "baseball" : "Miami Marlins"
}

print(sportsTeams["baseball"])

sportsTeams["soccer"] = "Inter Miami CF"

print(sportsTeams)

del sportsTeams["football"]
print(sportsTeams)

for sport,name in sportsTeams.items():
    print(sport,name)
print("FIU")

if "hockey" in sportsTeams:
    print("There is a hockey team.")
else:
    print("There is not a hockey team.")

print("Sports categories", list(sportsTeams.keys()))