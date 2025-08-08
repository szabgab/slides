# cd in subshell


{% embed include file="src/examples/script/change_dir.sh" %}


When a shell script is executed ./foobar.sh it is executed in a subshell.
This means certain changes made in the script don't apply in the original (parent) shell. 
For example if we change the current working directory using cd, when the script ends, we are back in the
same directory where we started.

```
$ pwd
/home/gabor

$ ./examples/script/change_dir.sh 
/home/gabor
/etc

$ pwd
/home/gabor
```


