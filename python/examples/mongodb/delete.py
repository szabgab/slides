from pymongo import MongoClient
import datetime

client = MongoClient()
db = client.demo

db.people.remove({ 'name' : 'Zorg'})
for p in db.people.find():
    print(p)

