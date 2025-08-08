# . (dot command)

* source
* .


The **source** and the . command will execute the script in the current shell. Which means the above changes are now persistant even after the script finishes running.

```
$ pwd
/home/gabor
$ . examples/script/change_dir.sh 
/home/gabor
/etc
$ pwd
/etc
```


```
$ echo $TERM
xterm-256color
$ . examples/script/change_term.sh 
xterm-256color
xterm
$ echo $TERM
xterm
```



