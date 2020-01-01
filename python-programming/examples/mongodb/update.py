from pymongo import MongoClient
import datetime

client = MongoClient()
db = client.demo

db.people.update({ 'name' : 'Zorg'}, { '$set' : { 'salary' : 1000 } })
for p in db.people.find({ 'name' : 'Zorg'}):
    print(p)

