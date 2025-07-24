# $match and $unwind and $group



```
db.scores.aggregate( [
    { $match: { name: "bar" } },
    { $unwind: "$scores" },
    { $group: { _id: "$name", score: { $sum: "$scores" } } }
] )

{
  "result": [
    {
      "_id": "bar",
      "score": 18
    }
  ],
  "ok": 1
}
```




