# Signals and the kill function


* $SIG
* %SIG
* kill

List of [signals on Linux](http://kernel.org/doc/man-pages/online/pages/man7/signal.7.html): `man -S 7 signal`

To send a signal use `kill SIG, LIST` (process IDs)

For example: `kill 9, $pid;`

{% embed include file="src/examples/signals/signal.pl" %}


