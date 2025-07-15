# The problem with die and croak


```
In both cases the error string defines the type of the error.
If we want to change the text, then in every place where we catch those
errors we have to update some regular expression.

Cannot easily propagate the context of the error as it is just a string.
```


