# The total size of the messages - aggregate

```
db.messages.aggregate( { $group : { _id : '', size : { $sum : '$size' } } } )

{
  "result": [
    {
      "_id": "",
      "size": NumberLong("17318623")
    }
  ],
  "ok": 1
}
```


