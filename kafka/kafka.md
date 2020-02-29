- ordering
- horizontal scaling
- push or pull?    (what is backpressure system  in reactive programming?)

Kafka
  redundant distributed ledger system
  distributed commit log

  linear scaling
  near network scale

  vocabulary is similar to Messaging System Semantics
  in production you'd never use a single node

What is Kafka used for
* Modern ETL/CDC  (Change Data Capture)
* Data Pipelines
* Big Data Ingest


* Key, Value, Timestamp
* Immutable Records
* Append Only
* Persisted (to disk)

Broker = Node in a cluster
Producer writers records to a broker
Consumer reads records from a broker
Leader / Follower for cluster distribution

Topic = Logical name with one or more partitions.
Ordering is guaranteed for a partition
Offset = Unique sequential ID (per partition)
Consumers track offsets

Write to the leader of a partition
Followers will replicate the data
Partition can be done manually or based on a key
Replication factor is Topic-based
Auto-Rebalancing

(leaders are elected)

Consumer groups

https://www.youtube.com/watch?v=UEg40Te8pnE  23:00


