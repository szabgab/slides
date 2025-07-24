# MongoDB CLI - find


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


