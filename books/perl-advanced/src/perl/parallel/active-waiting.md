# Active non-blocking waiting with waitpid

* waitpid
* POSIX
* WNOHANG


Up till now we were usig the `wait` function to wait for a child process to terminate. It is a blocking call that will wait till any of the child processes terminates.

There are other options as well. Using the `waitpid` function you could wait for a specific child to terminate using its PID or you can have a non-blocking way to check
if there is any child-processes that has already terminated. The non-blocking wait mode allows the parent process to do other things while waiting for the child processes
to do their job.


* [waipid](https://metacpan.org/pod/distribution/perl/pod/perlfunc.pod#wait)

{% embed include file="src/examples/forks/active_waiting.pl" %}

```
perl active_waiting.pl 0 0
perl active_waiting.pl 1 0
perl active_waiting.pl 1 1
```
