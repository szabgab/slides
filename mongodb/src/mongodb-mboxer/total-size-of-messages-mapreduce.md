# The total size of the messages - mapReduce



Create a mapping function:



```
map = function() { emit('msize', this.size); }
```



Create a reduce function:



```
red = function(k, v) {
  return Array.sum(v);
}
```



Run the mapReduce:



```
res = db.messages.mapReduce(map, red, {out: "Result"})
```



Get the result from the temporary collection called `res`.



```
res.find()

{
  "_id": "msize",
  "value": 17318623
}
```



