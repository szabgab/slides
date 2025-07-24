# Graceful termination of process


This process will catch both the INT and the TERM signals and in both cases it will flip a flag and based on that flag it will
stop he program. INT is received when the user presses Ctrl-C or if using a another terminal the user sends the `kill -2` signal.
TERM is `kill -15`.

When we run the program it will print out its process ID and instructions how to stop it.

kill -15 810344    or press Ctrl-C    to stop

So Ctrl-C instead of just killing the process in mid-operation it will tell the process to "please stop" and the loop will finish whatever it was doing and exit the program.


{% embed include file="src/examples/signals/graceful_termination.pl" %}


