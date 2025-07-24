# Remove elements of an array by value

```
db.users.update({ name: "Foo"}, { $pull: { "technologies": "yy" } })
```



