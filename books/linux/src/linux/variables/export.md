# Exporting variables

* export


The following command may be used to examine and remove things from the environment.
env, set, unset, export


If we set a variable using    name=foobar   this variable won't be visible in scripts
we launch because those scripts run in a subshell and the variable is local.

If we would like to make sure the variable is visible in the subshell we have to export
the variable.

```
$ name=foobar
$ echo $name
foobar
$ ./show_name.sh 

$ export name=FooBar
$ echo $name
FooBar
$ ./show_name.sh 
FooBar
```

{% embed include file="src/examples/script/show_name.sh" %}



