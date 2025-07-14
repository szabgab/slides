# /x enable white spaces and comments

```
/(X\d+).*\1/

/
 (X\d+)         # product number
 .*             # any character
 \1             # the same product number
/x
```


