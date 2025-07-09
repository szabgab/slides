# find

```
> db.messages.find({ 'From.address' : 'foo@bar.com' })

> db.messages.find({ 'From.address' : 'foo@bar.com' })
         .sort({ Date : -1 })
         .skip(20)
         .limit(5)
```



