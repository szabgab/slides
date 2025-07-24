# Strings - Single quoted

* q

```
print 'one string';               # one string
print 'a\n';                      # a\n
print 'a $name';                  # a $name
print 'another "string"';         # another "string"
```

There are only two special characters in this kind of string the '
and the \ at the end of the string

```
print 'a'b';                      # ERROR - perl will see the string 'a'
                                  #         and something attached to it
print 'a\'b';                     # a'b

print q(His "variable" name '$name'\n);     # His "variable" name is '$name'\n
```



