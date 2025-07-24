# Sparse index



When only some of the documents have a certain field it might be useful to set
the index to be sparse. That way only docuemnts that actually have that field will be in the index.


```
> db.collection.ensureIndex({ field : 1 }, {sparse : true})
```




