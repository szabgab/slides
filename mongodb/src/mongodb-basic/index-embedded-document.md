# Index embedded document (or subkey)


```
> db.messages.ensureIndex({ "From.address" : 1 })

> db.messages.find({ "From.address" : "foo@bar.com" })
```


