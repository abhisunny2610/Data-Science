## Q6. Write a Python program to connect to a MongoDB database and insert data.



import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = pymongo.MongoClient("mongodb+srv://@cluster0.v70mrv2.mongodb.net/?retryWrites=true&w=majority")

db = client["practice_database"]

data = {
    "name" : "Abhishek",
    "age": 19,
    "gender": "Male"
}

coll_practice_database = db["myrecords"]

coll_practice_database.insert_one(data)

# print(db)

## Q7. Write a Python program to update data in a MongoDB database.

coll_practice_database.update_one({"age" : 19}, {"$set": {'age': 20}})


##Q10. Write a Python program to perform a text search on a MongoDB database.

for i in coll_practice_database.find({"age": 20}):
    print(i)

for i in coll_practice_database.find():
    print(i)