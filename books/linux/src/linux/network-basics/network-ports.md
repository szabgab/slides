# Network ports

How to identify used and free ports?


```
$ sudo lsof -i         list all the processes using some port

/proc/PID/exe          is a symlink to the real executable
/proc/PID/cmdline      is the content of the command line
/proc/PID/cwd          current working directory of the process
```


