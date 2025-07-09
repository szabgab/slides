# All the elements - sum

* null

```
db.simple.aggregate( [ { $group: { _id: null, total: { $sum : "$cnt" } } } ] )

{
  "result": [
    {
      "_id": null,
      "total": 26
    }
  ],
  "ok": 1
}
```


