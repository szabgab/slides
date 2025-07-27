from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://mongodb:27017')
db = client.demo

for person in db.people.find({ 'name' : 'Foo'}):
    print(person)

