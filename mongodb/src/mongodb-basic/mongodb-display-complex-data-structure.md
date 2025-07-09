# Display complex data structure

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
      "c": 42
    }
  }
}
Fetched 1 record(s) in 3ms
```



