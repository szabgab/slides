# Group by name and caluclate average $avg

* $avg

```
db.simple.aggregate( [ { $group: { _id: "$name", total: { $avg : "$cnt" } } } ] )

{
  "result": [
    {
      "_id": "bar",
      "total": 7
    },
    {
      "_id": "foo",
      "total": 4
    }
  ],
  "ok": 1
}
```



