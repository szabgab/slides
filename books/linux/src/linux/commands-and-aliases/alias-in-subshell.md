# Alias only works in the shell it has been defined in


Aliases only work in the same shell where they were defined. Not even in a subshell
we get when we run a script. (But if we sourced the script then it runs in the same shell.)

```
$ alias tweet=echo
$ tweet hello
hello
```
{% embed include file="src/examples/linux/tweet.sh" %}

```
$ ./examples/linux/tweet.sh 
./examples/linux/tweet.sh: 2: ./examples/linux/tweet.sh: tweet: not found
```



