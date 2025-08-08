# Set a variable in a subshell

{% embed include file="src/examples/script/change_term.sh" %}

```
$ echo $TERM
xterm-256color

$ ./examples/script/change_term.sh 
xterm-256color
xterm

$ echo $TERM
xterm-256color
```



