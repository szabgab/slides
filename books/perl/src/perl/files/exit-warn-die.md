# die, warn, exit

* die
* warn
* exit
* STDERR

**exit()** -                      exits from the program


**warn()** - writes to STDERR


**die()**  - writes to STDERR and exits from the program (raising exception)



```
warn "This is a warning";
```

```
This is a warning at script.pl line 132.

If no \n at the end of the string both warn and die add the
name of file and line number and possibly the chunk of the input.
```


