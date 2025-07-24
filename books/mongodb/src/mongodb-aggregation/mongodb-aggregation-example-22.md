# $unwind


* $unwind

``
db.scores.aggregate( [ { $unwind: "$scores" } ] );

{
  "result": [
    {
      "_id": ObjectId("5988c63dd474ca272db3fb2e"),
      "name": "foo",
      "scores": 2
    },
    {
      "_id": ObjectId("5988c63dd474ca272db3fb2e"),
      "name": "foo",
      "scores": 4
    },
    {
      "_id": ObjectId("5988c63dd474ca272db3fb2e"),
      "name": "foo",
      "scores": 6
    },
    {
      "_id": ObjectId("5988c676d474ca272db3fb2f"),
      "name": "bar",
      "scores": 9
    },
    {
      "_id": ObjectId("5988c676d474ca272db3fb2f"),
      "name": "bar",
      "scores": 5
    },
    {
      "_id": ObjectId("5988c676d474ca272db3fb2f"),
      "name": "bar",
      "scores": 3
    },
    {
      "_id": ObjectId("5988c676d474ca272db3fb2f"),
      "name": "bar",
      "scores": 1
    }
  ],
  "ok": 1
}
```


