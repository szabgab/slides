# $match with $gt

```
db.simple.aggregate( [
    { $match : { cnt: { $gt: 4 } } },
    { $group: { _id: "total", total: { $sum : "$cnt" } } }
] )

{
  "result": [
    {
      "_id": "total",
      "total": 19
    }
  ],
  "ok": 1
}
```



