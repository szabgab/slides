# Exercise: Counter in JSON


Write a script that will provide several counters. The user can provide an argument on the command
line and the script will increment and display that counter.
Keep the current values of the counters in a single JSON file.
The script should behave like this:


```
$ python counter.py foo
1

$ python counter.py foo
2

$ python counter.py bar
1

$ python counter.py foo
3
```

* Extend the exercise so if the user provides the `--list` flag then all the indexes are listed (and no counting is done).
* Extend the exercise so if the user provides the `--delete foo` parameter then the counter `foo` is removed.



