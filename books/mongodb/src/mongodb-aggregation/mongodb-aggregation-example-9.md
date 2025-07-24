# $match (filter)

* $match
* filter

```
db.simple.aggregate( [ { $match : { name: "foo" } } ] )

{
  "result": [
    {
      "_id": ObjectId("5988aeb33b04d96991d11159"),
      "name": "foo",
      "cnt": 3
    },
    {
      "_id": ObjectId("5988aeb33b04d96991d1115a"),
      "name": "foo",
      "cnt": 4
    },
    {
      "_id": ObjectId("5988aeb33b04d96991d1115b"),
      "name": "foo",
      "cnt": 5
    }
  ],
  "ok": 1
}
```



