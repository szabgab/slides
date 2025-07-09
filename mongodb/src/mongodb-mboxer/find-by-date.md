# Find by date


Messages before January 1, 2005



```
db.messages.find({ Date: {$lt: new Date(2005, 0, 1) }})
         .limit(10)
```



