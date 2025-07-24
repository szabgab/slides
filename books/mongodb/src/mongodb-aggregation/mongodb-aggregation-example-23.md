# $unwind and $group


```
db.scores.aggregate( [
    { $unwind: "$scores" },
    { $group: { _id: "$name", score: { $sum: "$scores" } } }
] )

{
  "result": [
    {
      "_id": "bar",
      "score": 18
    },
    {
      "_id": "foo",
      "score": 12
    }
  ],
  "ok": 1
}
```



