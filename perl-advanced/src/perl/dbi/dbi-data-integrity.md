# Data integrity

When you are working in a place where data integrity is important you have
to use transactions when executing multiple queries that should either all
succeed or all fail.


{% embed include file="src/examples/dbi/integrity_loss.pl" %}


Try to see what happens when you enable the exit() function


{% embed include file="src/examples/dbi/show_accounts.pl" %}


