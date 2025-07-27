from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://mongodb:27017')
db = client.demo

foo = {
    'name'      : 'Foo',
    'email'     : 'foo@example.com',
    'birthdate' : datetime.datetime.strptime('2002-01-02', '%Y-%m-%d'),
    'student'   : True,
}

bar = {
    'name'      : 'Bar',
    'email'     : 'bar@example.com',
    'birthdate' : datetime.datetime.strptime('1998-08-03', '%Y-%m-%d'),
    'student'   : True,
    'teacher'   : False,
}

zorg = {
    'name'      : 'Zorg',
    'email'     : 'zorg@corp.com',
    'birthdate' : datetime.datetime.strptime('1995-12-12', '%Y-%m-%d'),
    'teacher'   : True,
}


db.people.insert_one(foo)
db.people.insert_one(bar)
db.people.insert_one(zorg)

