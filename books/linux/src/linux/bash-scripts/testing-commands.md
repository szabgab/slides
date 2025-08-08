# Testing commands

{% embed include file="src/examples/script/testing_command.sh" %}

```
$ ./examples/script/testing_command.sh Gate
_taskgated:*:13:13:Task Gate Daemon:/var/empty:/usr/bin/false
found Gate in /etc/passwd
```


We can check the exit value of a command directly as the command is executed.
The problem is that in many cases we are not interested in the output of the command, just if it was successful or not.
Redirection to /dev/null can solve the problem by hiding the extra output.



