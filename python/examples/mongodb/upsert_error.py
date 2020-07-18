from pymongo import MongoClient
import datetime

import pymongo
print(pymongo.__version__)

client = MongoClient()
collection = client.demo.data

collection.drop()
collection.update_one({ '_id' : 'stats'}, { '$set': { 'total': 1 } }, upsert=True)
collection.update_one({ '_id' : 'stats'}, { '$set': { 'total': 2 } }, { "upsert": True })
