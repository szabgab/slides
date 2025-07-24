# Large messages

```
db.messages.find({ size : { $gt : 10000000 } }).count()
db.messages.find({ size : { $gt : 10000000 } })
```


