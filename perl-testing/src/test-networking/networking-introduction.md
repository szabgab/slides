# Introduction - pick the right abstraction level



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






