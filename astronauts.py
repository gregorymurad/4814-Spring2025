import requests, main_functions

#API url
url = "http://api.open-notify.org/astros.json"

#Make the API request
response = requests.get(url).json()

#Serialize the result to a JSON document
main_functions.save_to_file(response,"jsonFiles/astronauts.json")

#Deserialize the recently create JSON document
astronautsDict = main_functions.read_from_file("jsonFiles/astronauts.json")

#What is the type of the object deserialized?
print(type(astronautsDict))

#What are its keys?
print(astronautsDict.keys())

#Access some of their values passing their keys
print(astronautsDict["number"])

#What are the names of the astronauts?
print(astronautsDict["people"][0]["name"])

#Print their names using a for loop
# for i in astronautsDict["people"]:
#     print(i["name"])

#Sort their names
for j in sorted(astronautsDict['people'],key = lambda x : x["name"]):
    print(j["name"])