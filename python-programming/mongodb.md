# MongoDB
{id: mongodb}

## MongoDB CRUD
{id: mongodb-crud}

* Create, Read, Update, Delete




## Install MongoDB support
{id: install-mongodb-support}

* Otherwise: **pip install pymongo**



## Python MongoDB insert
{id: mongodb-insert}
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

