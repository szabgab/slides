# sh-bang

* #!
* echo


A bash script is just a text file with commands in it. Command like the ones we can give on the command line.
It does not have to have any particular extension, but often people use the .sh extension.
For example foobar.sh

In order to be able to run it we need to make it executable   **chmod u+x foobar.sh**
or to make it exacutable for all the users on the system use   **chmod +x foobar.sh**.

To ensure the script always executes as a bash script, and not as the "current shell of the user"
we need to add ad a **sh-bang** line.

```
#!/bin/bash
```

{% embed include file="src/examples/script/hello_world.sh" %}

```
$ ./examples/script/hello_world.sh
Hello
World
```

{% embed include file="src/examples/script/hello_world_more.sh" %}

```
$ ./examples/script/hello_world_more.sh
Hello World
```

{% embed include file="src/examples/script/hello_world_n.sh" %}

```
$ ./examples/script/hello_world_n.sh
HelloWorld
```

{% embed include file="src/examples/script/hello_world_space.sh" %}

```
$ ./examples/script/hello_world_space.sh
Hello World
```


