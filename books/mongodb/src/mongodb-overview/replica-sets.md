# Replica set - high availability and data duability

* They are called primary and secondaries.
* Provides automatic fail-over.
* Primary
* (Operation log, Op-log used to replicate the data to the secondaries)


If the primary goes off-line, the remaining secondary nodes elect a new primary.
When the old primary comes back online it will become another secondary.



