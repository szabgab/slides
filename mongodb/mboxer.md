# Mailbox analyzing
{id: mongodb-mboxer}

## Email messages
{id: email-messages}

```
> use mboxer
> db.messages.count()
> db.messages.find().limit(1)
```


## find
{id: find-emails}

```
> db.messages.find({ 'From.address' : 'foo@bar.com' })

> db.messages.find({ 'From.address' : 'foo@bar.com' })
         .sort({ Date : -1 })
         .skip(20)
         .limit(5)
```


## Find by date
{id: find-by-date}


Messages before January 1, 2005



```
db.messages.find({ Date: {$lt: new Date(2005, 0, 1) }})
         .limit(10)
```



## Messages that have CC field
{id: messages-that-have-cc-field}

```
db.messages.find( { 'CC' : { $exists : true } } ).count()
```


## Large messages
{id: find-large-messages}

```
db.messages.find({ size : { $gt : 10000000 } }).count()
db.messages.find({ size : { $gt : 10000000 } })
```


## List the 10 biggest messages
{id: list-10-biggest-messages}

```
db.messages.find( ).sort( { size : -1 } ).limit(10)
```


## The total size of the messages - aggregate
{id: total-size-of-messages-aggregate}

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


## The total size of the messages - mapReduce
{id: total-size-of-messages-mapreduce}

{aside}
Create a mapping function:
{/aside}


```
map = function() { emit('msize', this.size); }
```


{aside}
Create a reduce function:
{/aside}


```
red = function(k, v) {
  return Array.sum(v);
}
```


{aside}
Run the mapReduce:
{/aside}


```
res = db.messages.mapReduce(map, red, {out: "Result"})
```


{aside}
Get the result from the temporary collection called <b>res</b>
{/aside}


```
res.find()

{
  "_id": "msize",
  "value": 17318623
}
```



