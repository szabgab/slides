# Command line parameters

* $0
* $1


The shell puts the space separated values from the command line in variables $0 .. $9 where
$0 is the name of the current script. Can handle up to 9 parameters (excluding the script itself)

$10 would be $1 followed by a 0, but we can write ${10} in our script which will be the 10th command line parameter.
{% embed include file="src/examples/script/command_line.sh" %}

```
$ ./examples/script/command_line.sh Foo Bar wins
0: ./examples/script/command_line.sh
1: Foo
2: Bar
```


```
$ ./examples/script/command_line.sh "Foo Bar" wins
0: ./examples/script/command_line.sh
1: Foo Bar
2: wins
```


```
$ ./examples/script/command_line.sh Foo 
0: ./examples/script/command_line.sh
1: Foo
2:
```


