# $unwind and $group and $sort

```
db.scores.aggregate( [
    { $unwind: "$scores" },
    { $group: { _id: "$name", score: { $sum: "$scores" } } }, 
    { $sort: { "score" : 1 } }
] )

{
  "result": [
    {
      "_id": "foo",
      "score": 12
    },
    {
      "_id": "bar",
      "score": 18
    }
  ],
  "ok": 1
}
```



