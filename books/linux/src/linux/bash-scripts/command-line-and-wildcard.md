# Command line and wildcard


A little script to show that escaping matters.
{% embed include file="src/examples/script/command_line_wild.sh" %}

```
$ ./examples/script/command_line_wild.sh 
0: ./examples/script/command_line_wild.sh
1:

$ ./examples/script/command_line_wild.sh *
0: ./examples/script/command_line_wild.sh
1: README

$ ./examples/script/command_line_wild.sh '*'
0: ./examples/script/command_line_wild.sh
1: README build examples intro.xml linux.yml scripts.xml variables.xml
star

$ ./examples/script/command_line_wild.sh "*"
0: ./examples/script/command_line_wild.sh
1: README build examples intro.xml linux.yml scripts.xml variables.xml
star

$ ./examples/script/command_line_wild.sh \*
0: ./examples/script/command_line_wild.sh
1: README build examples intro.xml linux.yml scripts.xml variables.xml
star
```



