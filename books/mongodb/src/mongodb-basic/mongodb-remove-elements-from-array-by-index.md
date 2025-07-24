# Remove elements of an array by index  (trick)

```
db.users.update({ name: "Foo"}, { $set: { "technologies.2": null } })
db.users.update({ name: "Foo"}, { $pull: { "technologies": null } })
```


