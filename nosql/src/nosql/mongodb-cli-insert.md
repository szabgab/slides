# MongoDB CLI - insert


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




