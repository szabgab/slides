# WWW::Mechanize, and example using OOP

Before learning how to write our classes, let's take a look at an example of using a Perl module which was written in Object Oriented style.

We are looking at the [WWW::Mechanize](https://metacpan.org/pod/WWW::Mechanize) module that makes it easy to send HTTP requests to web servers.
I am quite sure you have encountered many similar modules, but for our purposes this would be a fine example.

This is the full code in a file called `demo.pl`.

{% embed include file="src/examples/www-mechanize/demo.pl" %}

We can use it on the command line by passing a URL as a parameter. [httpbin.org](https://httpbin.org/) is a nice web site that can help us verify if your HTTP client works correctly.

In the first example we send a request that is expected to return a JSON structure describing our request.

* The first 3 printed line are the status of the response in 3 different ways.
* Then we have some 15 line of text which is the header sent by the server to our client.
* Then we can see a JSON structure showing the content the server sent us back. In this particular request the server sends back details about our request. So for example we can see that the the **User-Agent** field was **WWW-Mechanize/2.19** the module we used.


```
$ perl demo.pl https://httpbin.org/get

200 OK
200
200 OK

Connection: close
Date: Sun, 22 Jun 2025 12:40:45 GMT
Server: gunicorn/19.9.0
Content-Length: 271
Content-Type: application/json
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
Client-Date: Sun, 22 Jun 2025 12:38:26 GMT
Client-Peer: 34.198.95.5:443
Client-Response-Num: 1
Client-SSL-Cert-Issuer: /C=US/O=Amazon/CN=Amazon RSA 2048 M02
Client-SSL-Cert-Subject: /CN=httpbin.org
Client-SSL-Cipher: ECDHE-RSA-AES128-GCM-SHA256
Client-SSL-Socket-Class: IO::Socket::SSL
Client-SSL-Version: TLSv1_2

{
  "args": {}, 
  "headers": {
    "Accept-Encoding": "gzip", 
    "Host": "httpbin.org", 
    "User-Agent": "WWW-Mechanize/2.19", 
    "X-Amzn-Trace-Id": "Root=1-6857f9cd-788661eb40c56ecd14d4d272"
  }, 
  "origin": "46.120.8.126", 
  "url": "https://httpbin.org/get"
}
```

In the second example we ask the server to pretend there was an uncaught exception in the server that resulted in a "500 Internal Server Error".


```
$ perl demo.pl https://httpbin.org/status/500

500 INTERNAL SERVER ERROR
500
500 INTERNAL SERVER ERROR

Connection: close
Date: Sun, 22 Jun 2025 12:41:15 GMT
Server: gunicorn/19.9.0
Content-Length: 0
Content-Type: text/html; charset=utf-8
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
Client-Date: Sun, 22 Jun 2025 12:38:56 GMT
Client-Peer: 18.209.97.55:443
Client-Response-Num: 1
Client-SSL-Cert-Issuer: /C=US/O=Amazon/CN=Amazon RSA 2048 M02
Client-SSL-Cert-Subject: /CN=httpbin.org
Client-SSL-Cipher: ECDHE-RSA-AES128-GCM-SHA256
Client-SSL-Socket-Class: IO::Socket::SSL
Client-SSL-Version: TLSv1_2
```

## Details of the code

Let's go over the important parts of the code:

We load the module. There is no need to list the function we would like to import as we don't import any functions.

```perl
use WWW::Mechanize;
```

In Perl the thin arrow operator is used for method calls. (In most other languages the dot `.` is used for that, but in Perl the `.` was already used by string concatenation and thus a different symbol had to be selected.

In this expression we call the `new` method of the `WWW::Mechanize` class. It is the constructor. We pass some parameters to initialize the instance. What this expression returns, what we assign to the `$mech` variable
is an instance (object) of the `WWW::Mechanize` class.

```perl
my $mech = WWW::Mechanize->new(autocheck => 0);
```

In the next line we call the `get` method on the instance (object) passing some parameter to it. It returns a different object. Specifically this call returns an instance
of the [HTTP::Response](https://metacpan.org/pod/HTTP::Response) class. I assume, that internally the `get` method does some work then calls the constructor of
the HTTP::Response class and then returns the created instance.

```perl
my $res = $mech->get($url);
```

The next 3 lines show the status of the request in 3 different ways. Normally you'd use only one of them, but here I wanted to show different ways
of using OOP.

* In the first line we use the `status_line` method of the `HTTP::Response` instance we got back from the `get` call.
* In the second line we use the `status` method of the original `WWW::Mechanize` instance. This one only shows the status number, without the text.
* Finally we see a chained call. Apparently the `res` method of the `WWW::Mechanize` instance returns the same `HTTP::Response` instance as we got from the `get` call earlier. We don't need to store it in a variable, we can immediately call its method.

```perl
say $res->status_line;
say $mech->status();
say $mech->res->status_line;
```

Reading the code further we see 3 additional method calls.

That's it for our little demonstration of OOP.

We also have a file called `Makefile.PL`. It is useful to defined the dependencies of our little project.

{% embed include file="src/examples/www-mechanize/Makefile.PL" %}


