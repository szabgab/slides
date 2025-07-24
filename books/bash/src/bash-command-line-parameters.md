# Bash command line parameters


* $1

{% embed include file="src/examples/bash/hello_foo.sh" %}

```
$1 $2 $3
$*      which is $1 $2 $3 ...   but that splits up the spaces that might be inside $1 or $2 ..
"$*"    is the same
$@      is the same but
"$@"    is "$1" "$2" "$3" ...
```


