# List and kill processes by username

List the PIDs of the given user.


```
$ ps aux | awk '$1=="gabor" {print $2}'
```

```
$ ps aux | awk '$1=="gabor" {print $2}' | kill -9
```



