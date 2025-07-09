# Change element of array

```
db.users.update({ name: "Foo"}, { $set: { 'technologies.2': 'JS' } })

Updated 1 existing record(s) in 37ms
WriteResult({
  "nMatched": 1,
  "nUpserted": 0,
  "nModified": 1
})
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
    "JS",
    "SQL",
    "NoSQL",
    "MongoDB"
  ],
  "a": {
    "b": {
    }
  }
}
Fetched 1 record(s) in 11ms
```




