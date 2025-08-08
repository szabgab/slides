# Iterate over commend line arguments

By omitting the list of values the for-loop needs to go over, it will default to the
list of values supplied on the command line.

{% embed include file="src/examples/script/for_argv.sh" %}

```
$ ./examples/script/for_argv.sh 
$ ./examples/script/for_argv.sh one two
one
two
```



