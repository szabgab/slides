# Processes and signals
{id: process-and-signals}

## Signals and the kill function
{id: signal-handlers}
{i: $SIG}
{i: %SIG}
{i: kill}

List of [signals on Linux](http://kernel.org/doc/man-pages/online/pages/man7/signal.7.html): `man -S 7 signal`

To send a signal use `kill SIG, LIST` (process IDs)

For example: `kill 9, $pid;`

![](examples/signals/signal.pl)

## Catch signals
{id: catch-signals}

![](examples/signals/catch_signals.pl)

```
$SIG{$name} = sub {};     # do something when signal received
$SIG{$name} = 'IGNORE';   # ignore it
$SIG{$name} = 'DEFAULT';  # reset to the default behavior
```


## Catch Ctrl-C
{id: catch-ctrl-c}

![](examples/signals/catch_ctr_c.pl)



## Exercise: Catch ctrl-c and ask continue or terminate?
{id: exercise-catch-ctrl-c}


Take the `examples/signals/catch_ctr_c.pl`
and change it so when the user presses Ctrl-C the counting
stops and the user is asked if she really wants
to terminate the program. (y/n).

If yes is given then quit. If no is given continue.

If Ctrl-c is pressed again later then ask again.

Make sure you do as little as possible in the actual signal handle.


## Solution: Catch ctrl-c and ask
{id: solution-catch-ctrl-c}

![](examples/signals/catch_ctr_c_confirm.pl)

See what happens if you don't set the SIG handler to IGNORE?


See what happens if you remove the word local?

## Graceful termination of process
{id: graceful-termination-of-process}

{aside}
This process will catch both the INT and the TERM signals and in both cases it will flip a flag and based on that flag it will
stop he program. INT is received when the user presses Ctrl-C or if using a another terminal the user sends the `kill -2` signal.
TERM is `kill -15`.

When we run the program it will print out its process ID and instructions how to stop it.

kill -15 810344    or press Ctrl-C    to stop

So Ctrl-C instead of just killing the process in mid-operation it will tell the process to "please stop" and the loop will finish whatever it was doing and exit the program.
{/aside}

![](examples/signals/graceful_termination.pl)
