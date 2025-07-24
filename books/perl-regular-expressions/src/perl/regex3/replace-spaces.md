# Replace spaces

```
s/^\s+//        leading
s/\s+$//        trailing
```


both ends:



```
s/^\s*(.*)\s*$/$1/   " abc " =>  "abc "  because of the greediness
```


```
s/^\s*(.*?)\s*$/$1/   " abc " =>  "abc"  minimal match
```


