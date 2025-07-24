# Introduction

We have a device that has a Command Line Interface (CLI).
Normally you would telnet to it and type in commands.

Let's see what can we do with Net::Telnet.

In order to do that first we need to see how the device behaves
when we access it manually.

Use the local telnet command to access the device and try 
some basic commands. (eg. type "help")

We supply an example system that shows a partially faulty system.
In order to run the daemon by yourself you need to install 
Net::Server and Class::Accessor and type
**perl examples/cli-perl/bin/cli_daemon.pl**

Then you can access it using **telnet localhost 8000**

When accessing it using a telnet client you can use the built in
**username: admin and password: nimda**.




