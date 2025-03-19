import requests, main_functions

# NASA's API url
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key="

# Read your NASA API key
dict_keys=main_functions.read_from_file("api_keys.json")
nasa_key = dict_keys["nasa_key"]

#Build the final API url

final_url = url + nasa_key

#Make the request
# response = requests.get(final_url).json()

#Serialize the result to a JSON document
# main_functions.save_to_file(response,"mars_photos.json")

#Deserialize the recently create JSON document
mars_pictures = main_functions.read_from_file("mars_photos.json")

#What is the type of the object deserialized?
print(type(mars_pictures))

#What are its keys?
print(mars_pictures.keys())

#Access some of their values and their types passing their keys
print(type(mars_pictures["photos"]))
print(mars_pictures["photos"][0])
print(mars_pictures["photos"][0].keys())
print(mars_pictures["photos"][0]["camera"])
print(mars_pictures["photos"][0]["camera"]["full_name"])


#Create a set containing the names of all cameras
camera_names=[]
for i in mars_pictures["photos"]:
    camera_names.append(i["camera"]["full_name"])

print(set(camera_names))


#Print the image source of the photos taken by the Navigation Camera
for j in mars_pictures["photos"]:
    print(j["img_src"])

#Create a function that takes in a dictionary and a camera name
# and prints the image sources of all photos taken by the camera
# passed as argument and test this function.
# def get_img_src(dataset,camera_name):
#     #TODO: implement the get_img_src function
#
# get_img_src(mars_pics,'Navigation Camera')