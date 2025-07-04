# Complex network servers

There are many other options to build a network server.
Besides providing more complex interaction with the single server one can
configure it to be able to handle multiple clients at the same time.

Just replace "use base 'Net::Server';"
by "use base 'Net::Server::PreFork';" and you have a preforking web server.


