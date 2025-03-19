import requests, main_functions

# NASA's API url
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key="

# Read your NASA API key
my_key=main_functions.read_from_file("apiKeys/nasa_apis.json")["apiKey"]

#Build the final API url
final_url = url + my_key

#Make the API request
# response=requests.get(final_url).json() # This is the main part!

#Serialize the result to a JSON document
# main_functions.save_to_file(response,"mars_photos.json")

#Deserialize the recently create JSON document
mars_pics=main_functions.read_from_file("mars_photos.json")

#What is the type of the object deserialized?
print(type(mars_pics))

#What are its keys?
print(mars_pics.keys())

#Access some of their values and their types passing their keys
print("There are",len(mars_pics["photos"]),"photos in this dataset.")
print(f"There are {len(mars_pics['photos'])} photos in this dataset.")
print("There are " + str(len(mars_pics['photos'])) + " photos in this dataset.")

print(mars_pics["photos"][0].keys())
print(mars_pics["photos"][0]["img_src"])
print(mars_pics["photos"][0]["camera"]["full_name"])
print(mars_pics["photos"][0]["camera"]["name"])

print(mars_pics["photos"][500]["img_src"])
print(mars_pics["photos"][500]["camera"]["full_name"])
print(mars_pics["photos"][500]["camera"]["name"])

list_of_cameras=[]
#Create a set containing the names of all cameras
for i in mars_pics["photos"]:
    # i is each element in the list
    list_of_cameras.append(i["camera"]["full_name"])

print(set(list_of_cameras)) # set will convert the list of cameras into a set, hence eliminating duplicates

#Print the image source of the photos taken by the Navigation Camera
for j in mars_pics["photos"]:
    if j["camera"]["full_name"] == "Navigation Camera":
        print(j["img_src"])

#Create a function that takes in a dictionary and a camera name
# and prints the image sources of all photos taken by the camera
# passed as argument and test this function.
def get_img_src(dataset,camera_name):
    for j in dataset["photos"]:
        if j["camera"]["full_name"] == camera_name:
            print(j["img_src"])

get_img_src(mars_pics,'Navigation Camera')