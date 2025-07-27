from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://mongodb:27017')
collection = client.demo.cache

data1 = {
    'total': 10,
    'current': 5,
}

data2 = {
    'total': 13,
    'current': 3,
}


def show():
    print(collection.count_documents({}))
    for entry in collection.find({}):
        print(entry)
    print()

collection.drop()
print(collection.count_documents({}))

collection.insert_one({ '_id' : 'stats', **data1})
show()

collection.replace_one({ '_id' : 'stats'}, data2)
show()
