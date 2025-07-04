# Connect to the device

Setting both

    Dump_log  => 'dump.log',
    Input_log => 'input.log',

in the constructor of Net::Telnet will allow us to see
what is really going on on the connection.



```
We also add a call to wait for something that likely won't show up
in the output. Depending on where the demo application (the daemon)
is running you might need to change the $hostname variable.
```
{% embed include file="src/examples/cli-perl/eg/cli_01.pl" %}

```
Running the script we notice that after printing "opened" it waits
quite a lot of time and it never prints "after wait".

This happened because waitfor was waiting for a string that never 
showed up. Hence it gave up waiting after the built-in timeout
period. Once it reached the timeout it called the default errmode()
function which is the "die" function. So the script never reached
the second print() and did not have a chance to print anything.
```



