# Python MongoDB insert

* MongoClient
* insert
* insert_one

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

{% embed include file="src/examples/mongodb/insert.py" %}


