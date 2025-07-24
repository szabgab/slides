# $match

* $match

```
db.scores.aggregate( [ { $match: { name: "bar" } } ] )

{
  "result": [
    {
      "_id": ObjectId("5988c676d474ca272db3fb2f"),
      "name": "bar",
      "scores": [
        9,
        5,
        3,
        1
      ]
    }
  ],
  "ok": 1
}
```


