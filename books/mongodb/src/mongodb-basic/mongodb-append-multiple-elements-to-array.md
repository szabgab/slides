# Append multiple elements to an array


```
db.users.update(
    { name: "Foo"},
    { $push: { "technologies": { $each: ["abc", "def"] } } })
```


