from pymongo import MongoClient
import datetime

client = MongoClient()
db = client.demo

for person in db.people.find():
    print(person)

