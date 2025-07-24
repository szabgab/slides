# Echo Server

The Echo Server lets you telnet to it and echos back every word you type just
like the Simple Echo Server but once connected you have 5 seconds between
every two line you type or it prints Timeout and closes the connection.
Prints a message both to the client and the console (STDERR) of the server.


{% embed include file="src/examples/server/echo_server.pl" %}
{% embed include file="src/examples/server/lib/EchoServer.pm" %}



