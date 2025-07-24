# Group by name and count


```
db.simple.aggregate( [ { $group: { _id: "$name", total: { $sum : 1 } } } ] )

{
  "result": [
    {
      "_id": "bar",
      "total": 2
    },
    {
      "_id": "foo",
      "total": 3
    }
  ],
  "ok": 1
}
```



