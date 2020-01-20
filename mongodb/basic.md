# First steps
{id: first-steps}

## SQL to MongoDB terms
{id: sql-to-mongodb-terms}

```
SQL                       MongoDB
--------                  --------
database                  database
table                     collection
row                       BSON document

index                     index
column                    not really
join                      Lookup
                          embedding
Foreign key               Reference
primary key               _id field
group by                  aggregation
Multi-table transaction   Single document transaction
```


## Embedded documents
{id: embedded-documents}

{aside}

A "document" usually refers to a simple, one-level hash.
If one of the values is itself a hash we can say "embeded document".
Though in other languages we might just talk about a large, multi-level data-structure, without this whole idea that they are somehow embedded in each other.
{/aside}



## GUI client for MongoDB
{id: gui-for-mongodb}

* [GUIs](https://docs.mongodb.com/ecosystem/tools/)
* Campus



## Atlas hosted environment
{id: atlas-for-mongodb}


## Command line tools
{id: command-line-tools}

* mongod     - the server process
* mongo      - the MongoDB shell


* mongodump    - Dump the data into BSON files (creating the dump/ subdirectory).
* mongoexport  - Export MongoDB data to CSV, TSV or JSON files.
* mongofiles   - 
* mongoimport  - Import CSV, TSV or JSON data into MongoDB.
* mongooplog   - 
* mongoperf    - 
* mongorestore - Import BSON files.
* mongos       - 
* mongosniff   - 
* mongostat    - A bit like top, showing live performance stats.
* mongotop     - Another top-like tool.




## MongoDB on the command line
{id: mongodb-command-line}

```
$ mongo
> help
  db.help()                    help on db methods
  db.mycoll.help()             help on collection methods
  sh.help()                    sharding helpers
  rs.help()                    replica set helpers
  help admin                   administrative help
  help connect                 connecting to a db help
  help keys                    key shortcuts
  help misc                    misc things to know
  help mr                      mapreduce

  show dbs                     show database names
  show collections             show collections in current database
  show users                   show users in current database
  show profile                 show most recent system.profile entries
                               with time >= 1ms
  show logs                    show the accessible logger names
  show log [name]              prints out the last segment of log in memory,
                               'global' is default
  use db_name                  set current database
  db.foo.find()                list objects in collection foo
  db.foo.find( { a : 1 } )     list objects in foo where a == 1
  it                           result of the last line evaluated;
                               use to further iterate
  DBQuery.shellBatchSize = x   set default number of items to display on shell
  exit                         quit the mongo shell
> exit
bye
$
```


## insert
{id: insert}
{i: insert}
{i: find}
![](examples/mongodb/insert.txt)


## insert more
{id: insert-more}
![](examples/mongodb/insert_more.txt)



## Pretty printing in the MongoDB shell
{id: pretty-printing-in-the-mongodb-shell}

```
db.collection.find().limit(1).pretty()
```

Or add **DBQuery.prototype._prettyShell = true** to ~/.mongorc.js



Even <a href="http://tylerbrock.github.io/mongo-hacker/">prettier shell</a>.




## find
{id: find}
{i: find}

Searching for documents

![](examples/mongodb/find.txt)



## update a document
{id: update}
{i: update}
![](examples/mongodb/update.txt)

{aside}
This will replace the entire docuent keeping only the _id.
{/aside}



## Update modifiers for fields
{id: update-operators}
{i: $set}
{i: $inc}
{i: $rename}
{i: $setOnInsert}
{i: $unset}

* $set
* $inc
* $rename
* $setOnInsert
* $unset



## update - add values using $set
{id: add-values}
{i: $set}
![](examples/mongodb/update_add_values.txt)


## update - add array using $set
{id: add-array}
{i: $set}
![](examples/mongodb/update_add_array.txt)


## remove value from document
{id: remove-value-from-document}
{i: $unset}
![](examples/mongodb/update_unset.txt)


## transaction in a document
{id: transaction-in-a-document}
![](examples/mongodb/update_transaction.txt)


## push
{id: push}
{i: $push}
![](examples/mongodb/update_push.txt)


## Update modifiers for arrays
{id: update-modifiers-for-arrays}
{i: $push}
{i: $pop}
{i: $pull}
{i: $pushAll}
{i: $pullAll}
{i: $addToSet}

* $push
* $pop
* $pull
* $pushAll
* $pullAll
* $addToSet
* $ - The single $ sign used as a placeholder



## Update array element
{id: update-array-element}
![](examples/mongodb/update_array_element.txt)


## Remove array element
{id: remove-array-element}
{i: $pull}
![](examples/mongodb/remove_array_element.txt)



## _id is unique in a collection
{id: id-is-unique}
{i: _id}
![](examples/mongodb/unique_id.txt)


## update and save
{id: update-and-save}
{i: update}
{i: save}

* save() replaces a single document (or creates a new one)
* update() updates a single document (or multiple documents)



## save()
{id: save}
{i: save}
![](examples/mongodb/save.txt)


## Remove (delete) document
{id: remove-document}

```
db.a.remove({  "_id" : ObjectId("52ef998222e9d7ee82000000") })
```


## Count documents
{id: count}

* db.collection.count()
* db.collection.find().count()



## Find deeply
{id: find-deeply}
![](examples/mongodb/find_deeply.txt)


## sort()
{id: sort}

```
find() returns a cursor instance - lazy retreival!
```


## push
{id: push-email}
{i: $push}

```
db.emails.update({ _id: msg._id },
                 {$push: {tags : "mongodb"}})
```



## Update modifiers
{id: update-modifiers}
{i: $each}
{i: $slice}
{i: $sort}

* $each
* $slice
* $sort




## Conditional Operators
{id: conditional-operators}

* $in
* $nin
* $mod
* $all
* $size
* $exists
* $type


* $ne
* $lt
* $lte
* $gt
* $gte




## Indexes
{id: mongodb-indexes}

{aside}
Indexes are per collection
{/aside}


* B-tree indexes


* _id is indexed (and unique)
* Single Field
* Compund-key indexes
* Multi-key indexes (indexing each element of an array)
* Geospatial Index
* Text Indexes (beta)


{aside}

If there is an array of values (eg. tags) then the specific document will be indexed by each one of the values
in that array. "Fake full-text indexing."
{/aside}



## Creat Indexes
{id: create-index}

```
db.users.createIndex( {"field" : 1 });
db.users.dropIndex({ "field" : 1 });
db.users.getIndexes
```


## Unique Index
{id: unique-index}


Make sure that two documents cannot contain the same value in the given field.



```
db.collection.ensureIndex({ field : 1 })
```


## Sparse index
{id: sparse-index}

{aside}

When only some of the documents have a certain field it might be useful to set
the index to be sparse. That way only docuemnts that actually have that field will be in the index.
{/aside}

```
> db.collection.ensureIndex({ field : 1 }, {sparse : true})
```


## Index embedded document (or subkey)
{id: index-embedded-document}

```
> db.messages.ensureIndex({ "From.address" : 1 })

> db.messages.find({ "From.address" : "foo@bar.com" })
```


## Insert complex data structure
{id: mongodb-insert-complex-data-structure}

```
db.users.insert({
    "name" : "Foo",
    "email" : "foo@company.com",
    "technologies" : [
        "Perl",
        "Python",
        "JavaScript",
        "SQL",
        "NoSQL",
        "MongoDB"
    ],
    "a" : {
        "b" : {
            "c" : 42
        }
    }
})
```



## Display complex data structure
{id: mongodb-display-complex-data-structure}

```
db.users.find({ name: "Foo"})

{
  "_id": ObjectId("59895a5d98392edc6c7074ca"),
  "name": "Foo",
  "email": "foo@company.com",
  "technologies": [
    "Perl",
    "Python",
    "JavaScript",
    "SQL",
    "NoSQL",
    "MongoDB"
  ],
  "a": {
    "b": {
      "c": 42
    }
  }
}
Fetched 1 record(s) in 3ms
```



## Rename embedded document
{id: mongodb-rename-embedded-document}

```
db.users.update({ name: "Foo"}, { $rename: { 'a.b.c': 'a.b.d' } })
```


```
db.users.find({ name: "Foo"})
{
  "_id": ObjectId("59895a5d98392edc6c7074ca"),
  "name": "Foo",
  "email": "foo@company.com",
  "technologies": [
    "Perl",
    "Python",
    "JavaScript",
    "SQL",
    "NoSQL",
    "MongoDB"
  ],
  "a": {
    "b": {
      "d": 42
    }
  }
}
Fetched 1 record(s) in 2ms
```



## Remove ($unset) embedded document
{id: mongodb-remove-embedded-document}

```
db.users.update({ name: "Foo"}, { $unset: { 'a.b.d' : true } })
Updated 1 existing record(s) in 2ms
WriteResult({
  "nMatched": 1,
  "nUpserted": 0,
  "nModified": 1
})
```


```
db.users.find({ name: "Foo"})
{
  "_id": ObjectId("59895a5d98392edc6c7074ca"),
  "name": "Foo",
  "email": "foo@company.com",
  "technologies": [
    "Perl",
    "Python",
    "JavaScript",
    "SQL",
    "NoSQL",
    "MongoDB"
  ],
  "a": {
    "b": {

    }
  }
}
Fetched 1 record(s) in 2ms
```


## Change element of array
{id: mongodb-change-element-of-array}

```
db.users.update({ name: "Foo"}, { $set: { 'technologies.2': 'JS' } })

Updated 1 existing record(s) in 37ms
WriteResult({
  "nMatched": 1,
  "nUpserted": 0,
  "nModified": 1
})
```


```
db.users.find({ name: "Foo"})

{
  "_id": ObjectId("59895a5d98392edc6c7074ca"),
  "name": "Foo",
  "email": "foo@company.com",
  "technologies": [
    "Perl",
    "Python",
    "JS",
    "SQL",
    "NoSQL",
    "MongoDB"
  ],
  "a": {
    "b": {
    }
  }
}
Fetched 1 record(s) in 11ms
```


## Add embedded document
{id: mongodb-add-embedded-document}

```
db.users.update({ name: "Foo"}, { $set: { 'a.b.x': 19 } })
Updated 1 existing record(s) in 7ms
WriteResult({
  "nMatched": 1,
  "nUpserted": 0,
  "nModified": 1
})
```


```
> db.users.find({ name: "Foo"})
{
  "_id": ObjectId("59895a5d98392edc6c7074ca"),
  "name": "Foo",
  "email": "foo@company.com",
  "technologies": [
    "Perl",
    "Python",
    "JS",
    "SQL",
    "NoSQL",
    "MongoDB"
  ],
  "a": {
    "b": {
      "x": 19
    }
  }
}
Fetched 1 record(s) in 3ms
```



## Remove elements of an array by value
{id: mongodb-remove-elements-from-array-by-value}

```
db.users.update({ name: "Foo"}, { $pull: { "technologies": "yy" } })
```



## Remove elements of an array by index  (trick)
{id: mongodb-remove-elements-from-array-by-index}

```
db.users.update({ name: "Foo"}, { $set: { "technologies.2": null } })
db.users.update({ name: "Foo"}, { $pull: { "technologies": null } })
```



## Append one element to an array
{id: mongodb-append-elemnt-to-array}

```
db.users.update({ name: "Foo"}, { $push: { "technologies": "yy" } })
```


## Append multiple elements to an array
{id: mongodb-append-multiple-elements-to-array}

```
db.users.update(
    { name: "Foo"},
    { $push: { "technologies": { $each: ["abc", "def"] } } })
```


## Insert multiple elements in an array
{id: mongodb-insert-multiple-elements-in-array}

```
db.users.update(
   { name: "Foo"},
   { $push: { "technologies": { $each: ["one", "two"], $position: 4} } })
```




## Drop collection
{id: drop-collection}

```
> use try
> db.users.drop()
true
```


## Drop database
{id: drop-database}

```
> use try
> db.dropDatabase()
```


## MongoDB shell tools
{id: mongodb-shell-tools}

* db.serverStatus()
* db.stats()
* db.collection.stats()
* db.printReplicationInfo()
* db.printSlaveReplicationInfo()
* db.collection.find().explain()



## Resources
{id: mongodb-resources}

* H Waldo Grunenwald  [Introduction to MongoDB](http://www.youtube.com/watch?v=xOLwqUbpxGQ)
* [Introduction to NoSQL](http://www.youtube.com/watch?v=qI_g07C_Q5I) by Martin Fowler
* [The People vs. NoSQL Databases](http://www.youtube.com/watch?v=191kCkNya5Q): Panel Discussion Round-table with people from several NoSQL databases.
* [Introduction to MongoDB](http://www.youtube.com/watch?v=w5qr4sx5Vt0) (O'Reilly Webcast) A bit old,(from 2010), but a nice introduction to MongoDB.
* [MongoDB Schema Design: How to Think NoSQL](http://www.youtube.com/watch?v=PIWVFUtBV1Q) (O'Reilly Webcast)
* [presentations](http://www.mongodb.com/presentations)
* [MongoDB for Perl Developers](http://www.slideshare.net/YnonPerek/mongodb-for-perl-developers) by Ynon Perek
* [What is NoSQL](http://www.thoughtworks.com/insights/articles/nosql-comparison)
* Book: Martin Fowler: [NoSQL distilled](http://martinfowler.com/books/nosql.html)
* Book: [Domain-Driven design](http://dddcommunity.org/) by Eric Evans
* [Getting started with MongoDB](https://resources.mongodb.com/getting-started-with-mongodb)
* [Exploring the Aggregation Framework in MongoDB](https://www.youtube.com/watch?v=PrBSuxXURYs)
* [dropping ACID with MongoDB](http://www.slideshare.net/kchodorow/dropping-acid-with-mongodb)



## Projection
{id: mongodb-projection}

```
Second {} in a find() to limit which fields are going to be returned.
.explain("executionStats").executionStats

Execution
COLLSCAN
IXSCAN
FETCH
SHARD_MERGE
```




