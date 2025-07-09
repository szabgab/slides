import sys
from pymongo import Connection
from pymongo.errors import ConnectionFailure

def main():

    try:
       c = Connection(host="localhost", port=27017)
    except ConnectionFailure as e:
        sys.stderr.write("Could not connect to MongoDB: {}\n".format(e))
        exit()

    db = c["users"]

    student = {
        "name"  : "Foo Bar",
        "email" : "foo@bar.com",
    }

    db.users.insert(student, w=1)

    db.users.insert({ "name" : "other" }, w=1)

    for user in db.users.find():
        print(user)

main()

