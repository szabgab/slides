# Simple computation - adding two values


{% embed include file="src/examples/bc/bc1.pl" %}

* raw_pty turns off echo
* spawn starts the external program
* expect(timeout, regex) return undef if failed
* timeout is in seconds, 0 means check once, undef means wait forever
* send - as if the user was typing at the keyboard


