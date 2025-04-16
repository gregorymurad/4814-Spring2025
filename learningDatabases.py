import ssl

from pymongo import MongoClient
import os
from dotenv import load_dotenv


load_dotenv()

db_user = os.getenv("DB_USER")
db_pwd = os.getenv("DB_PASSWORD")

URI = (f"mongodb+srv://{db_user}:{db_pwd}@cluster0.cp82vcs.mongodb.net/?"
       f"retryWrites=true&w=majority&appName=Cluster0")

# import certifi
# ca=certifi.where()

client = MongoClient(URI)
# print(client)

db = client["school_database"] # from client, we access a database
print(db)

students_collection = db["students"] # from a database, we access a collection

student1 = {
    "name":"Pedro",
    "grade":'A',
    "age":17
}

students_collection.insert_one(student1)