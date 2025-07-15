# Exercise: Catch ctrl-c and ask continue or terminate?


Take the `examples/signals/catch_ctr_c.pl`
and change it so when the user presses Ctrl-C the counting
stops and the user is asked if she really wants
to terminate the program. (y/n).

If yes is given then quit. If no is given continue.

If Ctrl-c is pressed again later then ask again.

Make sure you do as little as possible in the actual signal handle.


