# MongoDB CLI - update $inc


```
> db.people.update({ "name" : "Foo Bar" }, { $inc : { "count" : 1 } })
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })

> db.people.find({ "name" : "Foo Bar" })
{ "_id" : ObjectId("5948198866ad1950f69fe0ae"),
    "name" : "Foo Bar", "email" : "foo@bar.com",
    "count" : 1, "scores" : [ 17, 23 ] }
```



