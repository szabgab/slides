# Non-blocking waiting, rerun on failure

In this example we have a list of tasks we need to do. The user can supply the number of child processes that will deal with the tasks.
Each child process generates a random number to wait to imitatet the work time and a random number as the exit code.

The parent monitors the child processes. If one of them exits with a non-zero error code the parent re-runs that job with another
child process until all the tasks are done.


{% embed include file="src/examples/forks/active_waiting_tasks.pl" %}
{% embed include file="src/examples/forks/active_waiting_tasks.out" %}


