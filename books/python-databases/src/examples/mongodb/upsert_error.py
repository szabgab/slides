from pymongo import MongoClient
import datetime

import pymongo
print(pymongo.__version__)

client = MongoClient('mongodb://mongodb:27017')
collection = client.demo.data

collection.drop()

print("working:")
collection.update_one({ '_id' : 'stats'}, { '$set': { 'total': 1 } }, upsert=True)


print("failing:")
collection.update_one({ '_id' : 'stats'}, { '$set': { 'total': 2 } }, { "upsert": True })
