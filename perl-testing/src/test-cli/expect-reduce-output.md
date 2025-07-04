# Reduce output - turn it into a test script


We don't want to see all the output bc generates and then try to look
for the correct responses or the error messages. We'd prefer just see ok or not ok

{% embed include file="src/examples/bc/bc4.pl" %}

* $e->log_stdout(0); - turn off the printing to the screen



