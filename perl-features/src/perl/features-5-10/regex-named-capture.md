# regex: Named capture buffers

* %+
* %-

{% embed include file="src/examples/feature/regex.pl" %}

```
See also the values in these two hashes:

%+  hash contains the left most match with the given name
%+{name}

%-  hash contains and array of the matches
%-{name}[0]
```


