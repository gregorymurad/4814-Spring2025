import main_functions, requests

# NASA's API url
url = "https://api.nasa.gov/planetary/apod?api_key="

# Read your NASA API key
nasaAPIsDict = main_functions.read_from_file("apiKeys/nasa_apis.json")
nasaKey = nasaAPIsDict["apiKey"]

#Build the final API url
final_url = url + nasaKey

#Make the API request
response = requests.get(final_url).json()

#Serialize the result to a JSON document
main_functions.save_to_file(response,"jsonFiles/apod.json")

#Deserialize the recently create JSON document
apod = main_functions.read_from_file("jsonFiles/apod.json")

#What is the type of the object deserialized?
print(type(apod))

#What are its keys?
print(apod.keys())

#Access some of their values passing their keys
print("Title:",apod["title"])
print("Explanation:",apod["explanation"])
print("URL:",apod["hdurl"])