# $group with $push


```
db.simple.aggregate( [ { $group: { _id: "$name", total: { $push : "$cnt" } } } ])

{
  "result": [
    {
      "_id": "bar",
      "total": [
        5,
        9
      ]
    },
    {
      "_id": "foo",
      "total": [
        3,
        4,
        5
      ]
    }
  ],
  "ok": 1
}
```




