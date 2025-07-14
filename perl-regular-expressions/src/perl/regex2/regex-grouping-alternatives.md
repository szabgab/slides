# Grouping, alternatives

all the rows with either 'apple pie' or 'banana pie' in them

```
if ($row =~ /apple pie/ or $row =~ /banana pie/) {
}
```

Alternatives


```
if ($row =~ /apple pie|banana pie/) {
}
```


Move the common part in one place and limit the alternation
to the part within the parentheses.



```
if ($row =~ /(apple|banana) pie/) {
}
```


