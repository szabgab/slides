# Servers
{id: servers}

## Net::Server
{id: net-server}
{i: Net::Server}

We are going to use the [Net::Server](https://metacpan.org/pod/Net::Server) module to create various server processes.


## Skeleton Server
{id: skeleton-network-server}

First we create a skeleton server that does not do anything.

![](examples/server/skeleton_server.pl)
![](examples/server/lib/SkeletonServer.pm)


## Simple Echo Server
{id: simple-echo-server}


The Simple Echo Server lets you telnet to it and echos back every word you type.


![](examples/server/simple_echo_server.pl)
![](examples/server/lib/SimpleEchoServer.pm)


## Echo Server
{id: echo-server}


The Echo Server lets you telnet to it and echos back every word you type just
like the Simple Echo Server but once connected you have 5 seconds between
every two line you type or it prints Timeout and closes the connection.
Prints a message both to the client and the console (STDERR) of the server.


![](examples/server/echo_server.pl)
![](examples/server/lib/EchoServer.pm)


## Complex network servers
{id: complex-net-server}


There are many other options to build a network server.
Besides providing more complex interaction with the single server one can
configure it to be able to handle multiple clients at the same time.





Just replace "use base 'Net::Server';"
by "use base 'Net::Server::PreFork';" and you have a preforking 
web server.





