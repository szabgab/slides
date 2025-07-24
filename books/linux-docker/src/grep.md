# grep


```
grep expression filename
```

```
ll /etc/apt/sources.list
cat /etc/apt/sources.list
grep security /etc/apt/sources.list
grep -v security /etc/apt/sources.list
grep '#' /etc/apt/sources.list
grep '# ' /etc/apt/sources.list
grep '^# ' /etc/apt/sources.list


grep -v '#' /etc/apt/sources.list
grep -v '#' /etc/apt/sources.list | grep security
```


