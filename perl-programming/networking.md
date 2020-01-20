# Networking devices
{id: networking-examples}

## Introduction - pick the right abstraction level
{id: networking-introduction}


When trying to connect some network device using Perl you have a number of choices.




See the full stack of HTTP connections:



* [Socket](https://metacpan.org/pod/Socket), and the socket function.
* [IO::Socket::INET](https://metacpan.org/pod/IO::Socket::INET) using [IO::Socket](https://metacpan.org/pod/IO::Socket)
* [Net::Telnet](https://metacpan.org/pod/Net::Telnet),
* [Net::FTP](https://metacpan.org/pod/Net::FTP),
* [Net::SSH](https://metacpan.org/pod/Net::SSH) (wrapping ssh),
* [Net::SSH::Perl](https://metacpan.org/pod/Net::SSH::Perl),
* Net::*
* [LWP::Simple](https://metacpan.org/pod/LWP::Simple), LWP
* [WWW::Mechanize](https://metacpan.org/pod/WWW::Mechanize)
* [WWW::Gittip](https://metacpan.org/pod/WWW::Gittip) (scaping or talking to an API)


```
At the lowest level you can use the built in socket function.

Using the Socket library provides several extra functions
and constants that will make your code cleaner and more portable.

See also perlipc
```

**plackup examples/server.psgi**




## Socket level programming using Socket.pm
{id: socket-pm}
{i: Socket}

{aside}

Using the built in "socket" function with various helper variables
and functions from the standard Socket.pm module
{/aside}
![](examples/network/socket.pl)

```
HTTP/1.0 200 OK
Date: Sun, 03 Aug 2014 11:59:18 GMT
Server: HTTP::Server::PSGI
Content-Type: text/html
Content-Length: 2

42
```


## Newline
{id: newlines}

```
\n   is a newline on our current system (is NOT always ASCII LF)
\r   is (is NOT always ASCII CR)
use  \015\012   to say CR+LF on networking applications
```


## Socket level programming using IO::Socket
{id: io-socket}
{i: IO::Socket}

{aside}

IO::Socket is a higher level abstraction
Hides many of the ugly part we had to know in case of the socket() function.
Provides an OOP interface.
{/aside}
![](examples/network/io_socket.pl)


## Net::Telnet
{id: net-telnet}
{i: Net::Telnet}
![](examples/telnet/telnet.pl)


## Net::Telnet for HTTP
{id: net-telnet-for-http}
![](examples/telnet/telnet_http.pl)


## Net::Telnet configure VLAN
{id: net-telnet-configure-vlan}
![](examples/telnet/configure_vlan.pl)


## ftp using Net::FTP
{id: net-ftp}
{i: Net::FTP}
![](examples/network/upload.pl)


## ssh using Net::SSH
{id: net-ssh}
{i: Net::SSH}

{aside}

Wrapping the external ssh command. Therefore working only in UNIX/Linux.
See also Net::SSH::Perl.
{/aside}
![](examples/network/ssh.pl)


## LWP::Simple
{id: lwp-simple}
{i: LWP::Simple}
![](examples/network/lwp_simple.pl)

```
42
```


## LWP::UserAgent
{id: lwp}
{i: LWP::UserAgent}
![](examples/network/lwp.pl)


## WWW::Mechanize
{id: www-mechanize}
{i: WWW::Mecanize}
![](examples/network/mechanize.pl)

```
42
```


## WWW::Mechanize for Google
{id: www-mechanize-google}
![](examples/network/mechanize_google.pl)


## Exercise: Search on Financial Times
{id: exercise-search-on-financial-times}


Go to the <a href="http://www.ft.com/">Financial Times</a> and search for the word "perl".
Print out how many items match.




## Exercise: Compare exchange rates
{id: exercise-compare-exchange-rates}


Go to various sites, check the AAA/BBB exchange rate on each one of them.
Print out the current exchange rate and also send an e-mail to yourself 
with the information.
Also put a ARBITRAGE warning if there is a difference between the rates.




AAA and BBB can be any two currencies you are interested in.



```
Try the following sites:
  http://www.xe.com/
  http://www.oanda.com/
  http://www.bankofcanada.ca/en/rates/exchform.html
```


## Exercise: Telnet or SSH to Unix machines
{id: exercise-telnet-to-unix-machines}


Pick a Unix/Linux machine your are using and write a script that will telnet or ssh 
to it, execute report what network cards does it have (ifconfig on Linux)
and what is its routing table (route -n on Linux).





## Introduction
{id: cli-introduction}

{aside}

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
**perl examples/cli/bin/cli_daemon.pl**

Then you can access it using **telnet localhost 8000**

When accessing it using a telnet client you can use the built in
**username: admin and password: nimda**.
{/aside}


## Connect to the device
{id: cli-connect-to-device}


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
![](examples/cli/eg/cli_01.pl)

```
Running the script we notice that after printing "opened" it waits
quite a lot of time and it never prints "after wait".

This happened because waitfor was waiting for a string that never 
showed up. Hence it gave up waiting after the built-in timeout
period. Once it reached the timeout it called the default errmode()
function which is the "die" function. So the script never reached
the second print() and did not have a chance to print anything.
```


## Reduce timeout
{id: reduce-timeout}

```
- Reduce the timeout
- Wait for a string we know will show up
- After seeing Username: we should type in 'admin', the username
```
![](examples/cli/eg/cli_02.pl)


## Exercise: Telnet
{id: exercise-telnet}

* Manually check out what does this server do?
* Turn the two example clients scripts into test using Test::More.
* Continue and write more tests for this telnet server.



* write a test that makes sure when someone types in 'help' the system *does not* write invalid command
* make sure you can write a test that can handle cases such as the '??'



## Our test script
{id: test-telnet}
![](examples/cli/t/cli.t)




