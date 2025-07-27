from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://mongodb:27017')
client.drop_database('demo')

