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

![](examples/advanced-perl/signal.pl)

```
%SIG

$SIG{INT}  = sub { print "INT received\n";};         # kill -2  or Ctrl-C
$SIG{TERM} = sub { print "TERM received\n"; exit;};  # kill -15
$SIG{TSTP} = sub { print "TSTP received\n";};        # kill -20 or Ctrl-Z

$SIG{KILL} = sub { print "KILL received\n"; exit;};  # kill -9  cannot catch it


$SIG{$name} = 'IGNORE';             # to ignore it
$SIG{$name} = 'DEFAULT';            # to reset to the default behavior
```


## Catch Ctrl-C
{id: catch-ctrl-c}
![](examples/advanced-perl/catch_ctr_c.pl)


## Catch signals
{id: catch-signals}
![](examples/advanced-perl/catch_signals.pl)


## Exercise: Catch ctrl-c and ask continue or terminate?
{id: exercise-catch-ctrl-c}


Take the `examples/advanced-perl/catch_ctr_c.pl`
and change it so when the user presses Ctrl-C the counting
stops and the user is asked if she really wants
to terminate the program. (y/n).




If yes is given then quit. If no is given continue.




If Ctrl-c is pressed again later then ask again.




Make sure you do as little as possible in the actual signal handle.




## Solution: Catch ctrl-c and ask
{id: solution-catch-ctrl-c}
![](examples/advanced-perl/catch_ctr_c_confirm.pl)

See what happens if you don't set the SIG handler to IGNORE?


See what happens if you remove the word local?



## Page Two
{id: page-two}
{i: $SIG}
{i: __WARN__}

[signal 7](http://kernel.org/doc/man-pages/online/pages/man7/signal.7.html)

Alternatively you could also insert the following in your code:
`use diagnostics;`
to get the explanations for every warning.
See also `perldoc perldiag` for a detailed explanation of each warning and error.


```
$SIG{KILL} = sub { print "KILL received\n"; exit;};  # kill -9  cannot catch it
$SIG{INT}  = sub { print "INT received\n";};         # kill -2  or Ctrl-C
$SIG{TERM} = sub { print "TERM received\n"; exit;};  # kill -15
$SIG{TSTP} = sub { print "TSTP received\n";};        # kill -20 or Ctrl-Z
```
