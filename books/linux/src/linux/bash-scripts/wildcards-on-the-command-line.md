# Wildcards on the command line


If possible, wildcards are expanded before the script is executed:

```
$ ./examples/script/command_line.sh *
0: ./examples/script/command_line.sh
1: README
2: build
```

README and build are files in the current directory.



```
$ ./examples/script/command_line.sh *x
0: ./examples/script/command_line.sh
1: *x
2:
```

In this case the wildcard does not match anything and thus it is passed to the script as it is.




If you want to pass a parameter that contains a wildcard character, we need to quote the parameter or escape the wildcard.
If we try this on the current script, we won't be able to really see the impact:

```
$ ./examples/script/command_line.sh '*'
0: ./examples/script/command_line.sh
1: README build examples intro.xml linux.yml scripts.xml variables.xml
2:
$ ./examples/script/command_line.sh \*
0: ./examples/script/command_line.sh
1: README build examples intro.xml linux.yml scripts.xml variables.xml
2:
```

That's because echo itself expands the wildcard when it prints *.



