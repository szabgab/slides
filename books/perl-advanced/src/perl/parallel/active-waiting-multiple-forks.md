# Non-blocking waiting with waitpid - multiple forks

In this example we create multiple child processes and wait for them with a non-blocking waitpid.
Each process will sleep for a random number of seconds imitating the randomness of the time it takes each one of them
to finish doing their job. They also generate a random exit code to imitate that some of them might have failed.


{% embed include file="src/examples/forks/active_waiting_loop.pl" %}

```
perl active_waiting_loop.pl 1
perl active_waiting_loop.pl 5
```


