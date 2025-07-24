# $match (filter) and the total


```
db.simple.aggregate( [
    { $match : { name: "foo" } },
    { $group: { _id: "total", total: { $sum : "$cnt" } } }
] )

{
  "result": [
    {
      "_id": "total",
      "total": 12
    }
  ],
  "ok": 1
}
```



