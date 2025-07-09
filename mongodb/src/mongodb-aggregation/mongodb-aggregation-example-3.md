# Group by name and sum - $sum

* $group
* $sum

```
db.simple.aggregate( [ { $group: { _id: "$name", total: { $sum : "$cnt" } } } ])

{
  "result": [
    {
      "_id": "bar",
      "total": 14
    },
    {
      "_id": "foo",
      "total": 12
    }
  ],
  "ok": 1
}
```


