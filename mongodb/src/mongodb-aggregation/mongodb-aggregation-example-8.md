# All the elements - sum

We can also use an arbitrary string instead of the **null**



```
db.simple.aggregate( [ { $group: { _id: "total", total: { $sum : "$cnt" } } } ])

{
  "result": [
    {
      "_id": "total",
      "total": 26
    }
  ],
  "ok": 1
}
```



