# NoSQL
{id: nosql}

## RDBMS - SQL
{id: rdbms-sql}

* RDBMS = Relational database management system
* SQL = Structured Query Language



## Problems with RDBMS in development
{id: problems-with-rdbms-in-development}

* Tables in database vs Objects in code
* [Object-relational Impedance Mismatch](http://en.wikipedia.org/wiki/Object-relational_impedance_mismatch)
* ORMs - [Object Relational Mappings](https://en.wikipedia.org/wiki/Object-relational_mapping)
* Representing Inheritance?




## Problems with RDBMS in production
{id: problems-with-rdbms-production}

* Changes in schema (migration and rollback)
* Data size
* Speed



## Scaling vertically
{id: scaling-verically}

* Expensive
* Limited to the biggest machine available.
* Fixed location (network latency for users)



## Scaling horizontally
{id: scaling-horizontally}

* Replicating to spread the read-load. "replication lag"
* Some kind of partitioning.
* Putting different tables on different servers.
* Splitting a table horizontally or vertically.
* ---
* Scaling horizontally means our data is not consistent any more.



## CAP Theorem of distributed data storage
{id: cap-theorem}

* Consistency
* Availability
* Partition Tolerance



<a href="http://en.wikipedia.org/wiki/CAP_theorem">CAP Theorem</a>.



* Pick any 2.
* In the face of networks split you need to decide if you prefer Availability or Consistency.




## ACID
{id: acid}

* Atomic
* Consistent
* Isolated
* Durable



RDBMS are usually ACID. We expect ACID.
With scaling it might not work at all.




## RDBMS - data is normalized
{id: rdbms-normalized}

* In a relational database everything is flat.
* We want to [normalize our data](https://en.wikipedia.org/wiki/Database_normalization).
* DRY = Don't repeat yourself




## NoSQL common characteristics
{id: nosql-common-characteristics}

* Non-relational  (or no tables)
* Cluster-friendliness  (mostly)
* open-source  (mostly)
* "web 2.0" / "web scale"
* Schema-less



## CRUD
{id: crud}

* Create = insert
* Read   = find
* Update = update
* Delete = remove



<a href="http://en.wikipedia.org/wiki/Create,_read,_update_and_delete">CRUD</a>




## Features
{id: nosql-features}

* Horizontally Scalable Architectures: Sharding and Replication.
* Some have Map-reduce.
* Full text index.
* "Stored procedures" simple JavaScript.



## Limitations
{id: nosql-limitations}

* Giving up on joins and complex transactions.



## NoSQL Data Models
{id: nosql-data-models}

* Document Store
* Key-value (tuple) store
* Wide Column Store
* Graph (GIS, Spatial)
* Object Databases
* Grid and Cloud Database
* XML Databases
* Multimodel Databases
* [List of NoSQL Databases (more than 225)](http://nosql-database.org/)



## Document Store
{id: document-store}

{aside}

Each document is usuall a JSON data structure.
Mo explicit schema, but there is implicit schema when we retrive data we know (or expect) certain fields with certain data-types to be in every document.
{/aside}

* [MongoDB](http://www.mongodb.org/) (10gen/MongoDB)
* [CouchDB](http://couchdb.apache.org/) (Apache)
* [RavenDB](http://ravendb.net/) (Hibernating Rhinos)
* [Elasticsearch](http://www.elasticsearch.org/) (Elasticsearch)
* [RethinkDB](http://www.rethinkdb.com/) (RethinkDB)



## MongoDB CLI - insert
{id: mongodb-cli-insert}

```
$ mongo
> show dbs
admin  (empty)
local  0.078GB

> use test
switched to db test

> db.people.insert({ "name" : "Foo Bar", "email" : "foo@bar.com",
  "count" : 0, "scores" : [17, 23] })
WriteResult({ "nInserted" : 1 })
> db.people.insert({ "name" : "Moon Go", "email" : "moon@go.com", "count" : 0 })
WriteResult({ "nInserted" : 1 })
```


## MongoDB CLI - find
{id: mongodb-cli-find}

```
> db.people.find()
{ "_id" : ObjectId("5948198866ad1950f69fe0ae"),
    "name" : "Foo Bar", "email" : "foo@bar.com",
    "count" : 0, "scores" : [ 17, 23 ] }
{ "_id" : ObjectId("594819be66ad1950f69fe0af"),
    "name" : "Moon Go", "email" : "moon@go.com", "count" : 0 }

> db.people.find({ "name" : "Foo Bar" })
{ "_id" : ObjectId("5948198866ad1950f69fe0ae"),
    "name" : "Foo Bar", "email" : "foo@bar.com",
    "count" : 0, "scores" : [ 17, 23 ] }
```


## MongoDB CLI - update $inc
{id: mongodb-cli-update-inc}

```
> db.people.update({ "name" : "Foo Bar" }, { $inc : { "count" : 1 } })
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })

> db.people.find({ "name" : "Foo Bar" })
{ "_id" : ObjectId("5948198866ad1950f69fe0ae"),
    "name" : "Foo Bar", "email" : "foo@bar.com",
    "count" : 1, "scores" : [ 17, 23 ] }
```


## MongoDB CLI - update $push
{id: mongodb-cli-update-push}

```
> db.people.update({ "name" : "Foo Bar" }, { $push : { "scores" : 42 } })
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })

> db.people.find({ "name" : "Foo Bar" })
{ "_id" : ObjectId("5948198866ad1950f69fe0ae"),
    "name" : "Foo Bar", "email" : "foo@bar.com",
    "count" : 1, "scores" : [ 17, 23, 42 ] }
```


## Key-value store
{id: key-value-store}

Like a persistent hash-map. The key is usually a string. The value can be 


* [MemcacheDB](http://memcachedb.org/) (not developed any more) 
* [Riak](http://basho.com/riak/) (Basho)
* [Redis](http://redis.io/)


{aside}

The line between document stores and key-value stores is blurry, Martin Fowler calls them "Aggregate-oriented" databases.
A data-store is a lot more flexible in what can we search on.
{/aside}


## Redis CLI
{id: redis-cli}

[redis-cli](https://redis.io/topics/rediscli)


```
$ redis-cli
> set name foo
> get name
> set name "foo bar"
> get name

> set a 1
> get a
> incr a
> get a

> set b 1
> keys *
> del b
```




## Wide Column Store families
{id: wide-column-store}

* [Hadoop](http://hadoop.apache.org/) (Apache)
* [HBase](https://hbase.apache.org/) (Apache)
* [Cassandra](https://cassandra.apache.org/) (Apache)
* [Hypertable](http://hypertable.org/) (Hypertable)



## Hadoop commands
{id: hadoop-cli}

* hadoop fs -put file.txt (split into 64Mb chunks replicated 3 times)
* hadoop jar some/long/path.java -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input inputdir -output outputdir
* hadoop fs -get outputdir/results.txt




## Cassandra
{id: cassandra}

* CQL = Cassandra Query Language (like SQL, but no joins, and need to have index (clustering) for each field in the WHERE clause)
* RF = Replication Factor (how many times each piece of data is replicated)
* CL = Consistency Level (ONE, QUORUM, ALL) (How many reads or writes need to happen before we consider the read or write "done")



## Graph
{id: graph-database}

* Graphs/trees/hierarchies/etc.
* [GIS Databases (geographic information systems)](https://en.wikipedia.org/wiki/Geographic_information_system)
* [Spatial database systems](https://en.wikipedia.org/wiki/Spatial_database)



* [Neo4j](http://www.neo4j.org/) (Neo Technology)
* [Onyx](https://www.onyxdevtools.com/)



## When to use NoSQL
{id: when-to-use-noqsl}

* Easier development
* Large scale data



## When not to use NoSQL
{id: when-not-to-use-nosql}

* Complex transactions (Banking, accounting etc)
* Data Warehousing
* Where you can't avoid complex joins






