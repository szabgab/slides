# Rename embedded document


```
db.users.update({ name: "Foo"}, { $rename: { 'a.b.c': 'a.b.d' } })
```


```
db.users.find({ name: "Foo"})
{
  "_id": ObjectId("59895a5d98392edc6c7074ca"),
  "name": "Foo",
  "email": "foo@company.com",
  "technologies": [
    "Perl",
    "Python",
    "JavaScript",
    "SQL",
    "NoSQL",
    "MongoDB"
  ],
  "a": {
    "b": {
      "d": 42
    }
  }
}
Fetched 1 record(s) in 2ms
```




