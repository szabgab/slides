# MongoDB
{id: mongodb}

## MongoDB CRUD
{id: mongodb-crud}

* CRUD stands for Create, Read, Update, Delete

## Install MongoDB support
{id: install-mongodb-support}

* **pip install pymongo**


## Python MongoDB insert
{id: mongodb-insert}
{i: MongoClient}
{i: insert}
{i: insert_one}

{aside}
In order to interract with a MongoDB Database we first need to import the MongoClient from the pymongo module.

Then connect to the MongoDB server using the `MongoClient()` call. Using the resulting client object we can
access the database. MonogoDB does not require us to create a database schema and  just by accessing a database and
inserting data in it we create the database. So we can use any database name here. In the example the name of the database
is going to be `demo`.

Once we have an object representing the database we can access a "collection" in the database.
This too is created automatically if it did not exist earlier. In  our example we use the name "people"
for our collection.

We then calle the `insert_one` method passing it a dictionary that we prepared earlier.

This will insert the dictionary as a JSON data structure in the selected collection.
{/aside}

![](examples/mongodb/insert.py)

## MongoDB CLI
{id: mongodb-cli}

```
$ mongo
> help
...
> show dbs
admin  (empty)
demo   0.078GB
local  0.078GB

> use demo      (name of db)
switched to db demo

> show collections
people
system.indexes

> db.people.find()
{ "_id" : ObjectId("58a3e9b2962d747a9c6e676c"), "email" : "foo@example.com", "student" : true,
    "birthdate" : ISODate("2002-01-02T00:00:00Z"), "name" : "Foo" }
{ "_id" : ObjectId("58a3e9b2962d747a9c6e676d"), "email" : "bar@example.com", "name" : "Bar", "student" : true,
    "birthdate" : ISODate("1998-08-03T00:00:00Z"), "teacher" : false }
{ "_id" : ObjectId("58a3e9b2962d747a9c6e676e"), "email" : "zorg@corp.com",
    "birthdate" : ISODate("1995-12-12T00:00:00Z"), "teacher" : true, "name" : "Zorg" }

> db.people.drop()      (drop a collection)
> db.dropDatabase()     (drop a whole database)
```


## Python MongoDB find
{id: mongodb-find}

![](examples/mongodb/find.py)


## Python MongoDB find refine
{id: mongodb-find-refine}

![](examples/mongodb/find_by_name.py)


## Python MongoDB update
{id: mongodb-update}

![](examples/mongodb/update.py)


## Python MongoDB remove (delete)
{id: mongodb-remove}

![](examples/mongodb/delete.py)


## Python MongoDB replace
{id: mongodb-replace}

![](examples/mongodb/replace.py)
![](examples/mongodb/replace.out)

## Python MongoDB upsert
{id: python-mongodb-upsert}

![](examples/mongodb/replace_upsert.py)
![](examples/mongodb/replace_upsert.out)

## Python Mongodb: TypeError: upsert must be True or False
{id: python-mongodb-upsert-error}

![](examples/mongodb/upsert_error.py)
![](examples/mongodb/upsert_error.out)

