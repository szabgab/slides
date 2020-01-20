# Overview
{id: mongodb-overview}

## MongoDB ("humongous")  (= huge; enormous.)
{id: humongous}

* Scalable, high-performance, open source NoSQL database



## 5 types of NoSQL databases
{id: types-of-nosql-databases}

* Key/value stores
* Column stores
* Graph
* Multi-model database
* Document store




## Languages
{id: languages}

{aside}
The languages officially supported by MongoDB.
{/aside}


* C/C++/C#
* Go
* Erlang
* Java
* JavaScript
* Node.js
* Perl
* PHP
* Python
* Ruby
* Scala
* ...


There are many more [languages](https://docs.mongodb.com/ecosystem/drivers/) supported by the Open Source community.



## Documentation
{id: mongodb-documentation}

* Excellent [documentation](http://docs.mongodb.com/) can be found on the MongoDB site.



## Features
{id: mongodb-features}

* Horizontally Scalable Architectures: Sharding and Replication.
* Journaling.
* Map-reduce.
* Full text index.
* "Stored procedures" simple JavaScript.



## Limitations
{id: mongodb-limitations}

* Giving up on joins and complex transactions.



## Performance
{id: performance}

* Native binary protocol between client and server.
* Insert does not (necessarily) wait for the write to the disk.



## Auto-sharding
{id: auto-sharding}


The <b>mongos</b> process knows which shard holds which part of the data.




## Sharding
{id: mongodb-sharding}

* mongos = mongo Sharding router process (in front of the mongod daemons)
* Config Server = Where data is located (the address book of the shard)
* We shard specific collections based on an existing unique index on the collection.
* Scatter-gather query.



## Picking a Shard Key
{id: mongodb-picking-a-shard-key}

* Cardinality
* Write Distribution
* Query Isolation
* Hashed shard key



## Replica set - high availability and data duability
{id: replica-sets}

* They are called primary and secondaries.
* Provides automatic fail-over.
* Primary
* (Operation log, Op-log used to replicate the data to the secondaries)


{aside}

If the primary goes off-line, the remaining secondary nodes elect a new primary.
When the old primary comes back online it will become another secondary.
{/aside}


## Write concern
{id: mongodb-write-concern}

* 0 - (Unacknoledged)
* 1 - (Acknowledged) by the primary when it has it in its own memory.
* N - Acknowledged by N servers.
* "majority" - the majority of the replicas have the information.



## Storage Engines
{id: mongodb-storage-engines}

* MMAPV1 (legacy)
* In-memory
* Encrypted
* WiredTiger



## MongoDB Data format
{id: mongodb-data-format}


Data is kept in BSON format (Binary JSON) which is JSON with some extensions.



* JSON = JavaScript Object
* PHP array
* Python Dictionary
* Perl Hash
* Ruby Hash




## Driver Responsibility
{id: mongodb-driver-responsibility}

* Authentication and Security
* Python, Perl, etc. conversion to BSON
* Error handling and recovery
* Wire Protocol
* Topology Management
* Connection Pool





