from pymongo import MongoClient
import datetime

client = MongoClient()
db = client.demo

for person in db.people.find({ 'name' : 'Foo'}):
    print(person)

