from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://mongodb:27017')
db = client.demo

db.people.update_one({ 'name' : 'Zorg'}, { '$set' : { 'salary' : 1000 } })
for p in db.people.find({ 'name' : 'Zorg'}):
    print(p)

# db.people.update_many({ 'name' : 'Zorg'}, { '$set' : { 'salary' : 1000 } })
