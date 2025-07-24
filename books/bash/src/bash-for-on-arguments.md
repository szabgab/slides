# Bash for loop on command-line arguments

* $@

```
If there is no list to go over (there is no "in something" part) then by default it will go over
the values on the command line as if this was written:

for a in "$@"
```
{% embed include file="src/examples/bash/for_arguments.sh" %}



