# Insert multiple elements in an array


```
db.users.update(
   { name: "Foo"},
   { $push: { "technologies": { $each: ["one", "two"], $position: 4} } })
```


