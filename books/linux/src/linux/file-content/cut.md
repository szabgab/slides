# cut

Extract fields or charcters from strings.

```
cut -c 3,2,10    files (characters)
cut -f 1,3       files (fields separated by tab)
cut -f 1,3 -d' ' files (fields separated by space)
cut -f 1,3 -d':' files (fields separated by :)

cut -b   files   (bytes)
```

* -c N      charcter
* -f N      field
* -d ':'    delimeter (defaults to TAB)


```
$ who
foo      console  Apr  8 18:57
bar      ttys000  Apr  9 07:42
moose    ttys001  Apr  8 18:57
```


```
$ who | cut -f1 -d' '
foo
bar
moose
```

