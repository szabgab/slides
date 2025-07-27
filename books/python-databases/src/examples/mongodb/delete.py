from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://mongodb:27017')
db = client.demo

print("before")
for p in db.people.find():
    print(p)

db.people.delete_one({ 'name' : 'Zorg'})

print("after")
for p in db.people.find():
    print(p)

