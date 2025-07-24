# Exercise 5


* Create a function that can be triggered by a URL request passing in parameters like this: ?name="Foo Bar"
* Create an object in S3 called something like "in/time.json"  (with the current time)

* Create another function that will be triggered by a newaobject  with a perfix "in/"
* Load that object and creare a new object called "out/time.json" using the same object name, but adding 3 new fields to it called

```
new_time:  the time portion of the name of the object
end_time:  the time when we read the object in the second function.
elapsed:   the difference.
```


