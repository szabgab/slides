# Command line `$#`, `$*`, `$@`

* $#
* $*
* $@

{% embed include file="src/examples/script/command_line_params.sh" %}

```
"$*" = "$1 $2 $3 $4 ... $n"
"$@" = "$1" "$2" "$3" "$4" ... "$n"
```

```
$ ./examples/script/command_line_params.sh foo bar
2
foo bar
foo bar

$ ./examples/script/command_line_params.sh "foo bar"
1
foo bar
foo bar
```


When put in double quotes "$*" and "$@" are slightly different. (See man bash)




