# Add timestamp to item (back-end)

```perl
use DateTime::Tiny;
```

```perl
date => DateTime::Tiny->now,
```
{% embed include file="src/examples/snippets/10/lib/D2/Ajax.pm" %}

mongo client


```
$ mongo
test> use d2-ajax
d2-ajax> db.items.find()
{
  "_id": ObjectId("557593b5a114607aa9188b91"),
  "date": ISODate("2015-06-08T16:08:05Z"),
  "text": "new item"
}
Fetched 1 record(s) in 3ms
```



